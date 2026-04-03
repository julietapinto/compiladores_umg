class SymbolTable:
    def __init__(self):
        # Pila de Tablas Hash
        self.stack = [{}]

    def push_scope(self):
        self.stack.append({})

    def pop_scope(self):
        if len(self.stack) > 1:
            self.stack.pop()

    def declare(self, name, value=0):
        current_scope = self.stack[-1]
        if name in current_scope:
            raise Exception(f"Error Semántico: La variable '{name}' ya fue declarada en este ámbito.")
        current_scope[name] = value

    def update(self, name, value):
        for scope in reversed(self.stack):
            if name in scope:
                scope[name] = value
                return
        raise Exception(f"Error Semántico: La variable '{name}' no ha sido declarada.")

    def lookup(self, name):
        for scope in reversed(self.stack):
            if name in scope:
                return scope[name]
        raise Exception(f"Error Semántico: La variable '{name}' no existe.")