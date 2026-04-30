class SymbolTable:
    def __init__(self):
        self.pila = [{}]

    def push_scope(self):
        self.pila.append({})

    def pop_scope(self):
        if len(self.pila) > 1:
            self.pila.pop()

    def declarar(self, nombre, valor=0):
        self.pila[-1][nombre] = valor

    def asignar(self, nombre, valor):
        for scope in reversed(self.pila):
            if nombre in scope:
                scope[nombre] = valor
                return
        raise Exception(f"[ERROR] Variable '{nombre}' no declarada")

    def obtener(self, nombre):
        for scope in reversed(self.pila):
            if nombre in scope:
                return scope[nombre]
        raise Exception(f"[ERROR] Variable '{nombre}' no existe")

    def imprimir_tabla(self):
        print("\n===== TABLA DE SÍMBOLOS (EJECUCIÓN) =====")
        for nivel, scope in enumerate(self.pila):
            print(f"\nScope {nivel}:")
            if not scope:
                print("  (vacío)")
            for nombre, valor in scope.items():
                if isinstance(valor, bool):
                    valor = "true" if valor else "false"
                print(f"  {nombre} -> {repr(valor)}")