import sys
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

    # Validación semántica
    semantic = SemanticVisitor()

    try:
        semantic.visit(tree)
    except Exception as e:
        print(e)
        return

    # 5. Validar errores
    if parser.getNumberOfSyntaxErrors() > 0:
        print("El programa tiene errores de sintaxis.")
    else:
        print("Análisis sintáctico exitoso. Ejecutando programa...")

        # 6. Ejecutar visitor
        visitor = EvalVisitor()
        visitor.visit(tree)

        # 7. Resultados
        print("\n--- Resultados del Programa ---")
        for var, val in visitor.symbols.pila[0].items():
            if isinstance(val, bool):
                val = "true" if val else "false"
            print(var, "=", val)


if __name__ == '__main__':
    main()