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
    | expr SEMI
    ;

// =========================
// DECLARACION / ASIGNACION
// =========================
declaracion
    : SONTAY ID
    ;

asignacion
    : ID ASSIGN expr
    ;


cicloWhile
    : MIENTRAS '[' 'CON' condicion ']' bloqueInstrucciones
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
    ;

comparacion
    : expr relop expr
    ;

// =========================
// EXPRESIONES ARITMÉTICAS
// =========================
expr
    : expr (MUL | DIV) expr   #aritmetica
    | expr (SUM | RES) expr   #aritmetica
    | NUM                     #numero
    | ID                      #variable
    | LPAREN expr RPAREN      #parentesis
    ;

// =========================
// RELOP
// =========================
relop
    : GT
    | LT
    | EQ
    | NEQ
    | GTE
    | LTE
    ;

// =========================
// TOKENS KEYWORDS
// =========================
PROGRAMA_INICIO : 'EZEQUIELAQUIINICIA' ;
PROGRAMA_FIN    : 'EZEQUIELAQUIFINALIZA' ;

SONTAY          : 'SONTAY' ;
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
// LEXER
// =========================
MIENTRAS : 'MIENTRAS' ;
ID  : [a-zA-ZáéíóúÁÉÍÓÚ_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;

WS  : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\n\r]* -> skip ;