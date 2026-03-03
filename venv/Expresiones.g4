grammar Expresiones;

root: expr+ EOF;

//escritura de una gramatica
expr : expr (SUM | RES) expr 
        | expr (MUL | DIV) expr 
        | NUM
        
        ;

SUM : '+';
RES : '-';
MUL : '*';
DIV : '/';
NUM : [0-9]+;