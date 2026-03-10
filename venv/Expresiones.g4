grammar Expresiones;

// Regla raíz
root : 'EZEQUIELAQUIINICIA' '(' ')' '[' instrucciones+ ']' 'EZEQUIELAQUIFINALIZA' '(' ')' EOF ;

// Tipos de instrucciones
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


