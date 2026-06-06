import sys
import traceback
import os
import time

from antlr4 import *
from parser.gramatica_v4Lexer import gramatica_v4Lexer
from parser.gramatica_v4Parser import gramatica_v4Parser

from interpreter_visitor import EvalVisitor
from custom_errors import MyErrorListener
from semantic_visitor import SemanticVisitor
from tac_geerator import TACGenerator

try:
    from ir_generator import IRGenerator
except ImportError:
    IRGenerator = None

def main():

    inicio = time.time()

    # ========================================================
    # FASE 1 - LECTURA DE ARCHIVO
    # ========================================================

    try:
        input_stream = FileStream(
            "input/Entrada_valida1.src",
            encoding="utf-8"
        )

    except FileNotFoundError:

        print(
            "Error: No se encontró el archivo 'Entrada_valida1.src'"
        )

        return

    # ========================================================
    # FASE 2 - LEXER
    # ========================================================

    lexer = gramatica_v4Lexer(input_stream)

    token_stream = CommonTokenStream(
        lexer
    )

    # ========================================================
    # FASE 3 - PARSER
    # ========================================================

    parser = gramatica_v4Parser(
        token_stream
    )

    lexer.removeErrorListeners()
    parser.removeErrorListeners()

    lexer.addErrorListener(
        MyErrorListener()
    )

    parser.addErrorListener(
        MyErrorListener()
    )

    tree = parser.root()

    print(
        "\n===== FASE 1: ANÁLISIS SINTÁCTICO ====="
    )

    if parser.getNumberOfSyntaxErrors() > 0:

        print(
            "El programa tiene errores de sintaxis. Deteniendo pipeline."
        )

        return

    print(
        "Análisis sintáctico exitoso."
    )

    # ========================================================
    # FASE 2 - SEMÁNTICA
    # ========================================================

    print(
        "\n===== FASE 2: ANÁLISIS SEMÁNTICO ====="
    )

    semantic = SemanticVisitor()

    try:

        semantic.visit(tree)

        if len(semantic.errores) > 0:

            for error in semantic.errores:
                print(error)

            print(
                "\nSe encontraron errores semánticos. Deteniendo pipeline."
            )

            return

        print("No hay errores semánticos.")

        semantic.imprimir_tabla()

        print(
            "Análisis semántico exitoso."
        )

    except Exception as e:

        print(e)

        return

    # ========================================================
    # FASE 3 - TAC
    # ========================================================

    print(
        "\n===== FASE 3: GENERACIÓN TAC ====="
    )

    print(
        "\nGenerando código TAC..."
    )

    tac = TACGenerator()

    tac.visit(tree)

    codigo_tac = tac.obtener_codigo()

    print(
        "\n===== TAC ====="
    )

    print(codigo_tac)

    os.makedirs(
        "output",
        exist_ok=True
    )

    with open(
        "output/programa.tac",
        "w"
    ) as f:

        f.write(codigo_tac)

    print(
        "Archivo TAC generado en output/programa.tac"
    )

    # ========================================================
    # FASE 4 - LLVM IR
    # ========================================================

    if IRGenerator is None:
        print(
            "\n===== FASE 4: GENERACIÓN LLVM IR ====="
        )
        print(
            "No se puede generar LLVM IR porque no está disponible la dependencia llvmlite."
        )
    else:
        print(
            "\n===== FASE 4: GENERACIÓN LLVM IR ====="
        )

        print(
            "\nGenerando código LLVM IR..."
        )

        ir_gen = IRGenerator()

        ir_gen.generate_from_tac(
            codigo_tac
        )

        ir_gen.save(
            "output/programa.ll"
        )

        print(
            "Archivo LLVM IR generado en output/programa.ll"
        )

    # ========================================================
    # FASE 5 - EJECUCIÓN
    # ========================================================

    print(
        "\n===== FASE 5: EJECUCIÓN ====="
    )

    print(
        "\nEjecutando programa..."
    )

    visitor = EvalVisitor()

    try:

        visitor.visit(tree)

    except Exception:

        traceback.print_exc()

        return

    # ========================================================
    # RESULTADOS
    # ========================================================

    print(
        "\n--- Resultados del Programa ---"
    )

    for var, val in visitor.symbols.pila[0].items():

        if isinstance(val, bool):

            val = (
                "true"
                if val
                else "false"
            )

        print(
            var,
            "=",
            val
        )

    visitor.symbols.imprimir_tabla()
    
    
if __name__ == '__main__':
    main()
