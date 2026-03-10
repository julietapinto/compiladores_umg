grammar Expresiones;

// Regla raíz
root : 'EZEQUIELAQUIINICIA' '(' ')' '[' instrucciones+ ']' 'EZEQUIELAQUIFINALIZA' '(' ')' EOF ;

instrucciones : declaracion ';'
              | asignacion ';'
              | condicional
              | expr ';' ;

declaracion : 'SONTAY' ID ;

asignacion : ID '=' expr ;

condicional : 'CHI_LO_HACE' '[' 'CON' condicion ']' bloqueInstrucciones
              ( 'TONCES' '[' ']' bloqueInstrucciones )?
              ( 'CHI_NO' '[' instrucciones* ']' )? ;

bloqueInstrucciones : instrucciones 
                   | '[' instrucciones+ ']' ;

condicion : expr op=( '>' | '<' | '==' | '!=' | '>=' | '<=' ) expr ;

expr : expr (MUL | DIV) expr   #aritmetica
     | expr (SUM | RES) expr   #aritmetica
     | NUM                     #numero
     | ID                      #variable
     | '(' expr ')'            #parentesis ;

MUL : '*' ;    // Simbolos de para datos
DIV : '/' ;
SUM : '+' ;
RES : '-' ;
ID  : [a-zA-ZáéíóúÁÉÍÓÚ_][a-zA-Z0-9_]* ; //  Todo el teclado alphanumerico incluyendo lestras con Tilde
NUM : [0-9]+ ;   // numeros enteros 
WS  : [ \t\r\n]+ -> skip ;    

COMMENT : '//' ~[\n\r]* -> skip ;

