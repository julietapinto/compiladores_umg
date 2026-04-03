grammar Expresiones;

// --- REGLA RAÍZ ---
root : 'EZEQUIELAQUIINICIA' '(' ')' '[' instrucciones+ ']' 'EZEQUIELAQUIFINALIZA' '(' ')' EOF ;

// --- INSTRUCCIONES ---
instrucciones : declaracion ';'
              | asignacion ';'
              | condicional
              | expr ';' ;

// --- DECLARACIÓN (SONTAY x;) ---
declaracion : 'SONTAY' ID ;

// --- ASIGNACIÓN (x = 10;) ---
asignacion : ID '=' expr ;

// --- LÓGICA DE CONTROL (CHI_LO_HACE) ---
// Se simplificó 'condicion' para que acepte cualquier expresión lógica o aritmética
condicional : 'CHI_LO_HACE' '[' 'CON' condicion ']' bloqueInstrucciones
              ( 'TONCES' '[' ']' bloqueInstrucciones )?
              ( 'CHI_NO' '[' instrucciones* ']' )? ;

bloqueInstrucciones : instrucciones 
                   | '[' instrucciones+ ']' ;

// Ahora 'condicion' es un alias de 'expr' para permitir AND/OR/NOT dentro de los corchetes
condicion : expr ;

// --- EXPRESIONES (Jerarquía de Operadores) ---
expr : 'NOT' expr                                 #logicaNot
     | expr 'AND' expr                            #logicaAnd
     | expr 'OR' expr                             #logicaOr
     | expr op=( '>' | '<' | '==' | '!=' | '>=' | '<=' ) expr #comparacion
     | expr op=( '*' | '/' ) expr                 #aritmetica
     | expr op=( '+' | '-' ) expr                 #aritmetica
     | NUM                                        #numero
     | ID                                         #variable
     | '(' expr ')'                               #parentesis ;

// --- TOKENS (LEXER) ---
MUL : '*' ;
DIV : '/' ;
SUM : '+' ;
RES : '-' ;

// Soporte para tildes y caracteres en español para los IDs
ID  : [a-zA-ZáéíóúÁÉÍÓÚ_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ;

// Ignorar espacios, tabulaciones y saltos de línea
WS  : [ \t\r\n]+ -> skip ;

// Ignorar comentarios de una sola línea
COMMENT : '//' ~[\n\r]* -> skip ;