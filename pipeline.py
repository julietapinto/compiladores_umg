import sys
import traceback
from antlr4 import *
from parser.ExpresionesLexer import ExpresionesLexer
from parser.ExpresionesParser import ExpresionesParser
from interpreter_visitor import EvalVisitor
from custom_errors import MyErrorListener
from semantic_visitor import SemanticVisitor

def main():
    # 1. Leer archivo
    try:
        input_stream = FileStream("input/programa.txt", encoding='utf-8')
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'programa.txt'")
        return

    # 2. Lexer y tokens
    lexer = ExpresionesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # 3. Parser
    parser = ExpresionesParser(token_stream)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())
    parser.addErrorListener(MyErrorListener())

    # 4. Árbol
    tree = parser.root()

    # 5. Validar errores sintácticos
    if parser.getNumberOfSyntaxErrors() > 0:
        print("El programa tiene errores de sintaxis. Deteniendo pipeline.")
        return

    print("Análisis sintáctico exitoso.")

    # 6. Análisis semántico
    semantic = SemanticVisitor()
    try:
        semantic.visit(tree)
        print("Análisis semántico exitoso.")
    except Exception as e:
        print(e)
        return

    # 7. Ejecutar visitor intérprete
    print("Ejecutando programa...")
    visitor = EvalVisitor()
    try:
        visitor.visit(tree)
    except Exception as e:
        traceback.print_exc()
        return

    # 8. Resultados
    print("\n--- Resultados del Programa ---")
    for var, val in visitor.symbols.pila[0].items():
        if isinstance(val, bool):
            val = "true" if val else "false"
        print(var, "=", val)

if __name__ == '__main__':
    main()