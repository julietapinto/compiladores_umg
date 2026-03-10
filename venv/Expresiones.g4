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
