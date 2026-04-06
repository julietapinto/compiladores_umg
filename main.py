import sys
from antlr4 import *
from parser.ExpresionesLexer import ExpresionesLexer
from parser.ExpresionesParser import ExpresionesParser
from EvalVisitor import EvalVisitor
from error_listener import MyErrorListener

def main():
    # 1. Leer el archivo de entrada 
    try:
        input_stream = FileStream("input/programa.txt", encoding='utf-8')
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'programa.txt'")
        return

    # 2. Crear el Lexer y el flujo de Tokens
    lexer = ExpresionesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # 3. Crear el Parser
    parser = ExpresionesParser(token_stream)
    #  Manejo de errores personalizado
    lexer.removeErrorListeners()
    parser.removeErrorListeners()

    lexer.addErrorListener(MyErrorListener())
    parser.addErrorListener(MyErrorListener())
    
    # 4. Generar el árbol sintáctico empezando desde la regla 'root'
    tree = parser.root()

    # 5. Verificar si hubo errores de sintaxis antes de seguir
    if parser.getNumberOfSyntaxErrors() > 0:
        print("El programa tiene errores de sintaxis. Revisa tu programa.txt")
    else:
        print("Análisis sintáctico exitoso. Ejecutando programa...")
        
        # 6. INSTANCIAR Y EJECUTAR EL VISITOR 
        visitor = EvalVisitor()
        visitor.visit(tree)

        # 7. Mostrar resultados 
        print("\n--- Resultados del Programa ---")
        for var, val in visitor.pila[0].items():
            if isinstance(val, bool):
                val = "true" if val else "false"
            print(var, "=", val)

if __name__ == '__main__':
    main()