# symbol_table.py

class SymbolTable:
    def __init__(self):
        self.pila = [{}]  # índice 0 = ámbito global

    # =====================
    # DECLARAR VARIABLE
    # =====================
    def declarar(self, nombre, valor):
        if nombre in self.pila[-1]:
            raise Exception(f"Variable '{nombre}' ya declarada en este ámbito")
        self.pila[-1][nombre] = valor

    # =====================
    # OBTENER VALOR
    # =====================
    def obtener(self, nombre):
        for scope in reversed(self.pila):
            if nombre in scope:
                return scope[nombre]
        raise Exception(f"Variable '{nombre}' no definida")

    # =====================
    # ASIGNAR VALOR
    # =====================
    def asignar(self, nombre, valor):
        for scope in reversed(self.pila):
            if nombre in scope:
                scope[nombre] = valor
                return
        raise Exception(f"Variable '{nombre}' no declarada")

    # =====================
    # CONTROL DE AMBITO
    # =====================
    def push_scope(self):
        self.pila.append({})

    def pop_scope(self):
        if len(self.pila) == 1:
            raise Exception("No se puede eliminar el ámbito global")
        self.pila.pop()

    # =====================
    # GLOBAL
    # =====================
    def global_scope(self):
        return self.pila[0]