import sys
import os
from antlr4 import *

# 1. Configuración de Carpeta 'parser'
try:
    from parser.ExpresionesLexer import ExpresionesLexer
    from parser.ExpresionesParser import ExpresionesParser
except ImportError:
    print("\n[!] Error: No se encontraron los archivos en la carpeta 'parser'.")
    print("    Asegúrate de ejecutar ANTLR y tener el archivo __init__.py")
    sys.exit(1)

# 2. Importar tu lógica de ejecución
from EvalVisitor import EvalVisitor 

def main():
    # Ruta del archivo de entrada en la carpeta input
    ruta_archivo = os.path.join("input", "programa.txt")

    try:
        input_stream = FileStream(ruta_archivo, encoding='utf-8')
    except FileNotFoundError:
        print(f"\n[!] Error: No se encontró '{ruta_archivo}'")
        print("    Verifica que el archivo esté en la carpeta 'input'.")
        return

    # 3. Proceso de ANTLR
    lexer = ExpresionesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExpresionesParser(token_stream)
    
    # 4. Construcción del Árbol Sintáctico (Regla raíz: root)
    tree = parser.root()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("\n[X] Error de sintaxis detectado en el código EZEQUIEL.")
    else:
        print(f"\n[✓] Archivo cargado: {ruta_archivo}")
        print("[✓] Análisis sintáctico exitoso.")
        print("-" * 45)
        
        # 5. Ejecución del Visitor con Scopes (Punto 4)
        visitor = EvalVisitor()
        try:
            visitor.visit(tree)
            
            # --- SALIDA ESTILIZADA DE LA TABLA DE SÍMBOLOS ---
            print("\n" + "="*45)
            print("   ESTADO FINAL DE LA MEMORIA (SCOPES)   ")
            print("="*45)
            
            # Mostramos la pila de Scopes (del más interno al global)
            # reversed ayuda a visualizar el tope de la pila arriba
            stack_view = list(reversed(visitor.memoria.stack))
            
            for i, scope in enumerate(stack_view):
                nivel_real = len(stack_view) - 1 - i
                label = "ÁMBITO GLOBAL" if nivel_real == 0 else f"📍 ÁMBITO LOCAL {nivel_real}"
                
                print(f"\n {label}:")
                if not scope:
                    print("    (No hay variables declaradas)")
                else:
                    for var, val in scope.items():
                        # Mostramos el nombre de la variable y su valor actual
                        print(f"    ├── {var.ljust(10)} : {val}")
                print("    " + "─"*35)
                
            print("\n" + "="*45)
            print("Ejecución finalizada correctamente.")

        except Exception as e:
            print(f"\n[!] Error en tiempo de ejecución: {e}")

if __name__ == '__main__':
    main()
    
       