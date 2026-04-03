import sys
from antlr4 import *
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser
from EvalVisitor import EvalVisitor

def main():
    # 1. Ruta del archivo de entrada (Asegúrate que exista en la Asus)
    input_file = "input/programa.txt"
    
    try:
        input_stream = FileStream(input_file, encoding='utf-8')
    except FileNotFoundError:
        # Intento B: Por si el archivo está en la raíz
        try:
            input_stream = FileStream("programa.txt", encoding='utf-8')
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{input_file}' o 'programa.txt'")
            return

    # 2. Análisis Léxico y Sintáctico
    lexer = ExpresionesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExpresionesParser(stream)
    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Error: Se detectaron errores sintácticos.")
        return

    print("Análisis sintáctico exitoso. Ejecutando programa...\n")

    # 3. Ejecución con el Visitor
    visitor = EvalVisitor()
    visitor.visit(tree)

    # 4. Mostrar Resultados de la Tabla Hash (Memoria)
    print("--- Resultados del Programa (Memoria) ---")
    if not visitor.memoria:
        print("La memoria está vacía (no hubo asignaciones).")
    else:
        for var, val in visitor.memoria.items():
            print(f"{var}: {val}")
    print("-----------------------------------------")

if __name__ == '__main__':
    main()