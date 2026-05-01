import sys
import traceback
import symbol_table
from antlr4 import *
from parser.ExpresionesLexer import ExpresionesLexer
from parser.ExpresionesParser import ExpresionesParser
from interpreter_visitor import EvalVisitor
from custom_errors import MyErrorListener
from semantic_visitor import SemanticVisitor
from tac_generator import TACGenerator

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
        if len(semantic.errores) == 0:
            print("No hay errores semánticos.")
        else:
            for error in semantic.errores:
                print(error)

        # Mostrar tabla de símbolos
        semantic.imprimir_tabla()
        if len(semantic.errores) > 0:
            print("\nSe encontraron errores semánticos. No se ejecuta el programa.")
            return

        print("Análisis semántico exitoso.")

        # 7. Generar TAC
        print("\nGenerando código TAC...")
        tac = TACGenerator()
        tac.visit(tree)

        codigo_tac = tac.obtener_codigo()

        print("\n===== TAC =====")
        print(codigo_tac)

        with open("output/programa.tac", "w") as f:
            f.write(codigo_tac)

        print("Archivo TAC generado en output/programa.tac")
        
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

    # 9. Mostrar tabla de símbolos de ejecución
    visitor.symbols.imprimir_tabla()
    
    
if __name__ == '__main__':
    main()