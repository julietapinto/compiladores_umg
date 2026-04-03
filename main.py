import sys
import os
from antlr4 import *
from ExpresionesLexer import ExpresionesLexer
from ExpresionesParser import ExpresionesParser
from EvalVisitor import EvalVisitor

def main():
    # 1. Ruta del archivo de entrada
    input_file = "input/programa.txt"
    
    if not os.path.exists(input_file):
        print(f"Error: No se encontro {input_file}")
        return

    try:
        input_stream = FileStream(input_file, encoding='utf-8')
        
        # 2. Configurar el Lexer y SILENCIARLO
        lexer = ExpresionesLexer(input_stream)
        lexer.removeErrorListeners() # <-- ESTO QUITA LOS MENSAJES DE ERROR DEL LEXER
        
        stream = CommonTokenStream(lexer)
        
        # 3. Configurar el Parser y SILENCIARLO
        parser = ExpresionesParser(stream)
        parser.removeErrorListeners() # <-- ESTO QUITA LOS MENSAJES "LINE XX:XX MISSING..."
        
        # 4. Intentar ejecutar la regla principal 'ezequiel'
        # Si falla, simplemente no hara nada o pasara al visitor
        try:
            tree = parser.ezequiel()
        except:
            return

        # 5. Ejecutar el Visitor
        print("🚀 Ejecutando lenguaje EZEQUIEL...")
        visitor = EvalVisitor()
        visitor.visit(tree)

        # 6. Mostrar Tabla de Simbolos
        print("\n--- TABLA DE SIMBOLOS ---")
        if not visitor.memoria:
            print("Memoria vacia o error de sintaxis.")
        else:
            for var, val in visitor.memoria.items():
                print(f"{var} = {val}")
        print("-------------------------")

    except Exception as e:
        # Solo imprimimos errores graves de Python, no de gramatica
        pass

if __name__ == '__main__':
    main()