grammar Expresiones;

// Regla raíz
root
    : PROGRAMA_INICIO '(' ')' '[' instrucciones+ ']' PROGRAMA_FIN '(' ')' EOF
    ;

instrucciones : declaracion ';'
              | asignacion ';'
              | condicional
              | expr ';' ;

declaracion : 'SONTAY' ID ;

asignacion : ID '=' expr ;

// ---------------------
// CONDICIONALES
// ---------------------
condicional 
    : 'CHI_LO_HACE' '[' 'CON' condicion ']' bloqueInstrucciones
      ( 'TONCES' '[' ']' bloqueInstrucciones )?
      ( 'CHI_NO' bloqueInstrucciones )?
    ;

bloqueInstrucciones 
    : '[' instrucciones+ ']'
    ;

// ---------------------
// CONDICIONES LÓGICAS
// ---------------------
condicion
    : condicion OR condicion              #orExpr
    | condicion AND condicion            #andExpr
    | NOT condicion                      #notExpr
    | expr relop expr                    #comparacion 
    | '(' condicion ')'                 #parenCondicion
    ;

// ---------------------
// EXPRESIONES ARITMÉTICAS
// ---------------------
expr : expr (MUL | DIV) expr   #aritmetica
     | expr (SUM | RES) expr   #aritmetica
     | NUM                     #numero
     | ID                      #variable
     | '(' expr ')'            #parentesis ;

// ---------------------
// REGLA OPERADORES
// ---------------------
relop
    : GT
    | LT
    | EQ
    | NEQ
    | GTE
    | LTE
    ;

// ---------------------
// TOKENS
// ---------------------

PROGRAMA_INICIO : 'EZEQUIELAQUIINICIA' ;
PROGRAMA_FIN    : 'EZEQUIELAQUIFINALIZA' ;

SONTAY          : 'SONTAY' ;
CHI_LO_HACE     : 'CHI_LO_HACE' ;
TONCES          : 'TONCES' ;
CHI_NO          : 'CHI_NO' ;
CON             : 'CON' ;

MUL : '*' ;
DIV : '/' ;
SUM : '+' ;
RES : '-' ;

GT  : '>' ;
LT  : '<' ;
EQ  : '==' ;
NEQ : '!=' ;
GTE : '>=' ;
LTE : '<=' ;

AND : '&&' ;
OR  : '||' ;
NOT : '!' ;

ID  : [a-zA-ZáéíóúÁÉÍÓÚ_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;

WS  : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\n\r]* -> skip ;