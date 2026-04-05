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
    | cicloWhile
    | cicloFor
    | expr SEMI
    ;
// =========================
// DECLARACION / ASIGNACION
// =========================
declaracion
    : (SONTAY | tipo) ID (ASSIGN expr)?
    ;
asignacion
    : ID ASSIGN expr
    ;
// =========================
// CICLOS
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
    : INT_TYPE
    | FLOAT_TYPE
    | STRING_TYPE
    | BOOL_TYPE
    | ENTERO
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
    | BOOLEAN
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
    | FLOAT_NUM                    #decimal
    | STRING                       #texto
    | BOOLEAN                      #logico
    | ID                           #variable
    | LPAREN expr RPAREN           #parentesis
    ;
// =========================
// RELOP
// =========================
relop
    : GT | LT | EQ | NEQ | GTE | LTE
    ;
// =========================
// TOKENS KEYWORDS
// =========================
PROGRAMA_INICIO : 'EZEQUIELAQUIINICIA' ;
PROGRAMA_FIN    : 'EZEQUIELAQUIFINALIZA' ;
SONTAY          : 'SONTAY' ;
INT_TYPE        : 'int' ;
FLOAT_TYPE      : 'float' ;
STRING_TYPE     : 'string' ;
BOOL_TYPE       : 'bool' ;
PARA            : 'PARA' ;
MIENTRAS        : 'MIENTRAS' ;
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
LPAREN   : '(' ;
RPAREN   : ')' ;
LBRACKET : '[' ;
RBRACKET : ']' ;
SEMI     : ';' ;
ASSIGN   : '=' ;
COMMA    : ',' ;
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
ID       : [a-zA-ZáéíóúÁÉÍÓÚ_][a-zA-Z0-9_]* ;
NUM      : [0-9]+ ;
FLOAT_NUM: [0-9]+ '.' [0-9]+ ;
STRING   : '"' (~["\r\n])* '"' ;
BOOLEAN  : 'true' | 'false' ;
WS       : [ \t\r\n]+ -> skip ;
COMMENT  : '//' ~[\n\r]* -> skip ;