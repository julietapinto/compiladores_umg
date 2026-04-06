from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if offendingSymbol.type == -1:
            print(f"[ERROR LÉXICO] Línea {line}:{column} símbolo inválido")
        else:
            print(f"[ERROR SINTÁCTICO] Línea {line}:{column} -> {msg}")