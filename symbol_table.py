class SymbolTable:
    def __init__(self):
        # La PILA: Una lista de diccionarios (Hash Tables)
        # Iniciamos con el Ámbito Global en el índice 0
        self.stack = [{}]

    def push_scope(self):
        """Crea un nuevo nivel de memoria (Scope) al entrar a un bloque []"""
        self.stack.append({})
        print("DEBUG: [PUSH] Nuevo ámbito creado.")

    def pop_scope(self):
        """Elimina el nivel de memoria actual al salir de un bloque []"""
        if len(self.stack) > 1:
            self.stack.pop()
            print("DEBUG: [POP] Ámbito cerrado. Variables locales eliminadas.")

    def declare(self, name, value=0):
        """Para SONTAY: Registra la variable solo en el nivel actual."""
        current_scope = self.stack[-1]
        if name in current_scope:
            raise Exception(f"Error Semántico: La variable '{name}' ya fue declarada en este ámbito.")
        current_scope[name] = value

    def update(self, name, value):
        """Para '=': Busca la variable en la pila y cambia su valor."""
        for scope in reversed(self.stack):
            if name in scope:
                scope[name] = value
                return
        raise Exception(f"Error Semántico: La variable '{name}' no ha sido declarada (Usa SONTAY).")

    def lookup(self, name):
        """Para usar variables: Busca de adentro hacia afuera."""
        for scope in reversed(self.stack):
            if name in scope:
                return scope[name]
        raise Exception(f"Error Semántico: La variable '{name}' no existe.")