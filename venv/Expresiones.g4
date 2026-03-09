grammar Expresiones;

// Regla principal
root : 'program' '{' instrucciones+ '}' EOF ;

// Tipos de instrucciones
instrucciones : asignacion ';' 
              | condicional    
              | expr ';' ;

// Condicional compacto
condicional : 'if' '(' condicion ')' '{' instrucciones+ '}' ( 'else' '{' instrucciones+ '}' )? ;

// Condición que usa la regla comparador
condicion : expr comparador expr ;

// Agrupación de operadores para no repetir código
comparador : IGUAL | DIFERENTE1 | DIFERENTE2 | MENOR | MAYOR | MENORIGUAL | MAYORIGUAL ;

// Asignación
asignacion : ID '=' expr ;

// Expresiones matemáticas
expr : expr (MUL | DIV) expr #aritmetica
     | expr (SUM | RES) expr #aritmetica
     | NUM                   #numero
     | ID                    #variable
     | '(' expr ')'          #parentesis ;

// Tokens de Operadores Aritméticos
MUL : '*' ;
DIV : '/' ;
SUM : '+' ;
RES : '-' ;

// Tokens de Operadores Relacionales (Compactos)
IGUAL       : '==' ;
DIFERENTE1  : '!=' ;
DIFERENTE2  : '<>' ;
MENOR       : '<'  ;
MAYOR       : '>'  ;
MENORIGUAL  : '<=' ;
MAYORIGUAL  : '>=' ;

// Identificadores y Números
ID  : [a-zA-Z]+ ;
NUM : [0-9]+ ;

// Salto de espacios
WS  : [ \t\r\n]+ -> skip ;
