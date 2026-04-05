grammar Expresiones;

// =========================
// ROOT
// =========================
root
    : PROGRAMA_INICIO LPAREN RPAREN LBRACKET instrucciones+ RBRACKET PROGRAMA_FIN LPAREN RPAREN EOF
    ;

// =========================
// INSTRUCCIONES
// =========================
instrucciones
    : declaracion SEMI
    | asignacion SEMI
    | condicional
    | cicloWhile
    | cicloFor
    | expr SEMI
    ;

// =========================
// DECLARACION / ASIGNACION (MODIFICADO PARA TIPOS DE DATOS EXPLICITOS)
// =========================
// Ahora soporta: SONTAY x; O int x = 10;
declaracion
    : (SONTAY | tipo) ID (ASSIGN expr)? 
    ;

// Regla nueva para tipos explícitos
tipo
    : INT_TYPE 
    | FLOAT_TYPE 
    | STRING_TYPE 
    | BOOL_TYPE
    ;

asignacion
    : ID ASSIGN expr
    ;


// =========================
// Ciclos 
// =========================
cicloWhile
    : MIENTRAS LBRACKET CON condicion RBRACKET bloqueInstrucciones
    ;
    
cicloFor
    : PARA LBRACKET asignacion SEMI CON condicion SEMI asignacion RBRACKET bloqueInstrucciones
    ;

// =========================
// CONDICIONAL
// =========================
condicional
    : CHI_LO_HACE LPAREN CON condicion RPAREN bloqueInstrucciones
      (TONCES bloqueInstrucciones)?
      (CHI_NO bloqueInstrucciones)?
    ;

bloqueInstrucciones
    : LBRACKET instrucciones+ RBRACKET
    ;

// =========================
// CONDICIONES (CORREGIDAS)
// =========================
condicion
    : orExpr
    ;

orExpr
    : andExpr (OR andExpr)*
    ;

andExpr
    : notExpr (AND notExpr)*
    ;

notExpr
    : NOT notExpr
    | comparacion
    | LPAREN condicion RPAREN
    | BOOLEAN  // Soporte para true/false directo en condiciones
    ;

comparacion
    : expr relop expr
    ;

// =========================
// EXPRESIONES ARITMÉTICAS (MODIFICADO PARA TIPOS DE DATOS EXLICITOS)
// =========================
expr
    : expr (MUL | DIV) expr   #aritmetica
    | expr (SUM | RES) expr   #aritmetica
    | NUM                     #numero
    | DECIMAL                 #decimal
    | STRING                  #texto
    | BOOLEAN                 #logico
    | ID                      #variable
    | LPAREN expr RPAREN      #parentesis
    ;

// =========================
// RELOP
// =========================
relop
    : GT | LT | EQ | NEQ | GTE | LTE
    ;

// =========================
// TOKENS KEYWORDS / TYPES
// =========================
PROGRAMA_INICIO : 'EZEQUIELAQUIINICIA' ;
PROGRAMA_FIN    : 'EZEQUIELAQUIFINALIZA' ;

SONTAY          : 'SONTAY' ;

// Nuevos tipos de datos explicitos
INT_TYPE    : 'int' ;
FLOAT_TYPE  : 'float' ;
STRING_TYPE : 'string' ;
BOOL_TYPE   : 'bool' ;
PARA : 'PARA';
MIENTRAS : 'MIENTRAS';
CHI_LO_HACE     : 'CHI_LO_HACE' ;
TONCES          : 'TONCES' ;
CHI_NO          : 'CHI_NO' ;
CON             : 'CON' ;

// =========================
// SYMBOLS
// =========================
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACKET: '[' ;
RBRACKET: ']' ;
SEMI    : ';' ;
ASSIGN  : '=' ;

// =========================
// OPERADORES
// =========================
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

// =========================
// LEXER (MODIFICADO PARA TIPOS DE DATOS EXPLICITOS)
// =========================

ID      : [a-zA-ZáéíóúÁÉÍÓÚ_][a-zA-Z0-9_]* ;
NUM     : [0-9]+ ;
DECIMAL : [0-9]+ '.' [0-9]+ ;
STRING  : '"' (~["\r\n])* '"' ;
BOOLEAN : 'true' | 'false' ;


WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\n\r]* -> skip ;