from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        # ERROR LÉXICO
        if offendingSymbol is None:
            print(f"[ERROR LÉXICO] Línea {line}:{column} -> símbolo no válido")

        # ERROR SINTÁCTICO
        else:
            print(f"[ERROR SINTÁCTICO] Línea {line}:{column} -> {msg}")