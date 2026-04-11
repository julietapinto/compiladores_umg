class SymbolTable:
    def __init__(self):
        self.pila = [{}]  # scope global

    # =========================
    # ÁMBITOS
    # =========================
    def push_scope(self):
        self.pila.append({})

    def pop_scope(self):
        if len(self.pila) > 1:
            self.pila.pop()

    # =========================
    # DECLARAR VARIABLE
    # =========================
    def declarar(self, nombre, valor):
        scope_actual = self.pila[-1]

        if nombre in scope_actual:
            raise Exception(f"Variable '{nombre}' ya declarada en este ámbito")

        scope_actual[nombre] = valor

    # =========================
    # ASIGNAR VARIABLE
    # =========================
    def asignar(self, nombre, valor):
        for scope in reversed(self.pila):
            if nombre in scope:
                scope[nombre] = valor
                return

        raise Exception(f"Variable '{nombre}' no declarada")

    # =========================
    # OBTENER VARIABLE
    # =========================
    def obtener(self, nombre):
        for scope in reversed(self.pila):
            if nombre in scope:
                return scope[nombre]

        print(f"[ERROR SEMÁNTICO] Variable '{nombre}' no definida")
        return 0

    # =========================
    # DEBUG (opcional)
    # =========================
    def imprimir(self):
        print("Tabla de símbolos:")
        for i, scope in enumerate(self.pila):
            print(f"Scope {i}: {scope}")