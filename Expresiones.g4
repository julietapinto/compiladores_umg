grammar Expresiones;

// --- REGLAS SINTÁCTICAS ---
ezequiel : 'EZEQUIELAQUIINICIA' '(' ')' '[' contenido ']' 'EZEQUIELAQUIFINALIZA' '(' ')' ;

contenido : (instruccion)* ;

instruccion 
    : declaracion ';'   # DoDeclaracion
    | asignacion ';'    # DoAssign
    | condicional       # DoCondicional
    ;

declaracion : 'SONTAY' ID ;

asignacion : ID '=' expr ;

condicional : 'CHI_LO_HACE' '[' 'CON' condicion ']' 
              bloque 
              ('TONCES' '[' ']' bloque)? 
              ('CHI_NO' bloque)? ;

bloque : '[' contenido ']' ;

condicion : expr '>' expr   # MayorQue
          | expr '<' expr   # MenorQue
          | expr '==' expr  # Igualdad
          ;

expr : expr (MUL|DIV) expr  # MulDiv
     | expr (ADD|SUB) expr  # AddSub
     | INT                  # Int
     | ID                   # Id
     | '(' expr ')'         # Parens
     ;

// --- REGLAS LÉXICAS ---
SONTAY : 'SONTAY' ;
CHI_LO_HACE : 'CHI_LO_HACE' ;
TONCES : 'TONCES' ;
CHI_NO : 'CHI_NO' ;
CON : 'CON' ;

ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;

ID  : [a-zA-Z]+ ;
INT : [0-9]+ ;

WS : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;