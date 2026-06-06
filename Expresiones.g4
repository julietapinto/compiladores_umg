grammar Expresiones;

root
    : PROGRAMA_INICIO LPAREN RPAREN LBRACKET instrucciones+ RBRACKET PROGRAMA_FIN LPAREN RPAREN EOF
    ;

instrucciones
    : declaracion SEMI
    | asignacion SEMI
    | condicional
    | decFuncion
    | retorna SEMI
    | imprimir SEMI
    | llamadaFuncion SEMI
    | importStmt
    | cicloWhile
    | cicloFor
    | switchStmt
    | BREAK SEMI
    | CONTINUE SEMI
    | expr SEMI
    ;

declaracion
    : tipo ID (ASSIGN expr)?
    | tipo ID LBRACKET NUM RBRACKET
    ;

asignacion
    : ID ASSIGN expr
    | ID LBRACKET expr RBRACKET ASSIGN expr
    ;

cicloWhile
    : MIENTRAS LBRACKET CON condicion RBRACKET bloqueInstrucciones
    ;

cicloFor
    : PARA LBRACKET asignacion SEMI CON condicion SEMI asignacion RBRACKET bloqueInstrucciones
    ;

condicional
    : CHI_LO_HACE LPAREN CON condicion RPAREN bloqueInstrucciones
      (TONCES bloqueInstrucciones)?
      (CHI_NO bloqueInstrucciones)?
    ;

switchStmt
    : SEGUN LPAREN expr RPAREN LBRACKET caseStmt* defaultStmt? RBRACKET
    ;

caseStmt
    : CASO NUM LBRACKET instrucciones+ RBRACKET
    ;

defaultStmt
    : DEFECTO LBRACKET instrucciones+ RBRACKET
    ;

bloqueInstrucciones
    : LBRACKET instrucciones+ RBRACKET
    ;

decFuncion
    : FUNCION tipo ID LPAREN parametros? RPAREN LBRACKET instrucciones+ RBRACKET
    | FUNCION VACIO ID LPAREN parametros? RPAREN LBRACKET instrucciones+ RBRACKET
    ;

parametros
    : tipo ID (COMMA tipo ID)*
    ;

tipo
    : INT_TYPE
    | FLOAT_TYPE
    | STRING_TYPE
    ;

retorna
    : RETORNA expr
    ;

imprimir
    : IMPRIMIR LPAREN expr RPAREN
    ;

importStmt
    : IMPORT STRING SEMI
    ;

llamadaFuncion
    : ID LPAREN argumentos? RPAREN
    ;

argumentos
    : expr (COMMA expr)*
    ;

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

expr : term ((SUM | RES) term)* ;
term : factor ((MUL | DIV | MOD) factor)* ;
factor
    : NUM
    | FLOAT_NUM
    | STRING
    | ID
    | ID LPAREN argumentos? RPAREN
    | ID LBRACKET expr RBRACKET
    | LPAREN expr RPAREN
    ;

relop
    : GT | LT | EQ | NEQ | GTE | LTE
    ;

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
SEGUN           : 'SEGUN' ;
CASO            : 'CASO' ;
DEFECTO         : 'DEFECTO' ;
LPAREN   : '(' ;
RPAREN   : ')' ;
LBRACKET : '[' ;
RBRACKET : ']' ;
SEMI     : ';' ;
ASSIGN   : '=' ;
COMMA    : ',' ;
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
ID       : [a-zA-ZáéíóúÁÉÍÓÚ_][a-zA-Z0-9_]* ;
NUM      : [0-9]+ ;
FLOAT_NUM: [0-9]+ '.' [0-9]+ ;
STRING   : '"' (~["\r\n])* '"' ;
WS       : [ \t\r\n]+ -> skip ;
COMMENT  : '//' ~[\n\r]* -> skip ;
ERROR_CHAR : . { print(f"[ERROR LÉXICO] símbolo inválido: {self.text}") } -> skip ;
