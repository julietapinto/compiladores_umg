grammar gramatica_v4;

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
    | switchStmt
    | decFuncion
    | decStruct
    | retorna SEMI
    | imprimir SEMI
    | llamadaFuncion SEMI
    | importStmt
    | cicloWhile
    | cicloFor
    | BREAK SEMI
    | CONTINUE SEMI
    | expr SEMI
    ;

// =========================
// DECLARACION / ASIGNACION
// =========================
declaracion
    : tipo ID (ASSIGN ternario)?
    | tipo ID LBRACKET NUM RBRACKET
    | ID ID (ASSIGN ternario)?
    ;

asignacion
    : ID ASSIGN ternario
    | ID LBRACKET expr RBRACKET ASSIGN ternario
    | ID DOT ID ASSIGN ternario
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
// SWITCH / CASE / DEFAULT
// =========================
switchStmt
    : SWITCH LPAREN expr RPAREN LBRACKET caseStmt* defaultStmt? RBRACKET
    ;

caseStmt
    : CASE expr COLON instrucciones*
    ;

defaultStmt
    : DEFAULT COLON instrucciones*
    ;

// =========================
// STRUCTS
// =========================
decStruct
    : STRUCT ID LBRACKET campoStruct+ RBRACKET SEMI
    ;

campoStruct
    : tipo ID SEMI
    ;

// =========================
// FUNCIONES
// =========================
decFuncion
    : FUNCION tipo ID LPAREN parametros? RPAREN LBRACKET instrucciones+ RBRACKET
    | FUNCION VACIO ID LPAREN parametros? RPAREN LBRACKET instrucciones+ RBRACKET
    ;

parametros
    : tipo ID (COMMA tipo ID)*
    ;

// =========================
// TIPOS
// =========================
tipo
    : INT_TYPE
    | FLOAT_TYPE
    | STRING_TYPE
    ;

// =========================
// RETURN / PRINT
// =========================
retorna
    : RETORNA ternario
    ;

imprimir
    : IMPRIMIR LPAREN ternario RPAREN
    ;

// =========================
// IMPORT / FUNCIONES
// =========================
importStmt
    : IMPORT STRING SEMI
    ;

llamadaFuncion
    : ID LPAREN argumentos? RPAREN
    ;

argumentos
    : ternario (COMMA ternario)*
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

// =========================
// COMPARACIONES (FIX IMPORTANTE)
// =========================
comparacion
    : expr relop expr
    ;

// =========================
// EXPRESIONES (CORREGIDAS)
// =========================
ternario
    : expr QUESTION expr COLON expr
    | expr
    ;

// 🔥 FIX PRINCIPAL: comparación separada
expr
    : comparacionExpr
    ;

comparacionExpr
    : sumaExpr (relop sumaExpr)?
    ;

sumaExpr
    : term ((SUM | RES) term)*
    ;

term
    : castExpr ((MUL | DIV | MOD) castExpr)*
    ;

// 🔥 FIX UNARIO (-x)
castExpr
    : RES castExpr
    | LPAREN tipo RPAREN castExpr
    | factor
    ;

// =========================
// FACTOR
// =========================
factor
    : NUM
    | FLOAT_NUM
    | STRING
    | ID LPAREN argumentos? RPAREN
    | ID LBRACKET expr RBRACKET
    | ID DOT ID
    | ID
    | LPAREN expr RPAREN
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

INT_TYPE        : 'int' ;
FLOAT_TYPE      : 'float' ;
STRING_TYPE     : 'string' ;

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

BREAK           : 'BREAK' ;
CONTINUE        : 'CONTINUE' ;

IMPORT          : 'IMPORT' ;
SWITCH          : 'SWITCH' ;
CASE            : 'CASE' ;
DEFAULT         : 'DEFAULT' ;

STRUCT          : 'STRUCT' ;

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
DOT      : '.' ;
COLON    : ':' ;
QUESTION : '?' ;

// =========================
// OPERADORES
// =========================
MUL : '*' ;
DIV : '/' ;
MOD : '%' ;
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

WS       : [ \t\r\n]+ -> skip ;
COMMENT  : '//' ~[\n\r]* -> skip ;

ERROR_CHAR
    : . { print(f"[ERROR LÉXICO] símbolo inválido: {self.text}") } -> skip
    ;