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
    | decFuncion
    | retorna SEMI
    | imprimir SEMI
    | llamadaFuncion SEMI
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
// FUNCIONES Y PROCEDIMIENTOS
// =========================
decFuncion
    : tipo ID LPAREN parametros? RPAREN LBRACKET instrucciones+ RBRACKET
    | VACIO ID LPAREN parametros? RPAREN LBRACKET instrucciones+ RBRACKET
    ;
parametros
    : tipo ID (COMMA tipo ID)*
    ;
tipo
    : ENTERO
    | DECIMAL
    | TEXTO
    | BOOLEANO
    ;
retorna
    : RETORNA expr
    ;
imprimir
    : IMPRIMIR LPAREN expr RPAREN
    ;
llamadaFuncion
    : ID LPAREN argumentos? RPAREN
    ;
argumentos
    : expr (COMMA expr)*
    ;
// =========================
// CONDICIONES
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
    : expr (MUL | DIV) expr        #aritmetica
    | expr (SUM | RES) expr        #aritmetica
    | ID LPAREN argumentos? RPAREN #llamadaExpr
    | NUM                          #numero
    | ID                           #variable
    | LPAREN expr RPAREN           #parentesis
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
FUNCION         : 'FUNCION' ;
VACIO           : 'VACIO' ;
RETORNA         : 'RETORNA' ;
IMPRIMIR        : 'IMPRIMIR' ;
ENTERO          : 'ENTERO' ;
DECIMAL         : 'DECIMAL' ;
TEXTO           : 'TEXTO' ;
BOOLEANO        : 'BOOLEANO' ;
// =========================
// SYMBOLS
// =========================
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACKET: '[' ;
RBRACKET: ']' ;
SEMI    : ';' ;
ASSIGN  : '=' ;
COMMA   : ',' ;
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
ID  : [a-zA-ZáéíóúÁÉÍÓÚ_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\n\r]* -> skip ;