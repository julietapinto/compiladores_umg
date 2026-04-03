import sys
from parser.ExpresionesVisitor import ExpresionesVisitor
from symbol_table import SymbolTable

class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        super().__init__()
        # Gestión de ámbitos mediante Pila de Tablas Hash
        self.memoria = SymbolTable()

    def visitRoot(self, ctx):
        print("--- Ejecutando Lenguaje EZEQUIEL ---")
        return self.visitChildren(ctx)

    def visitDeclaracion(self, ctx):
        nombre_var = ctx.ID().getText()
        self.memoria.declare(nombre_var, 0)
        return 0

    def visitAsignacion(self, ctx):
        nombre_var = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        self.memoria.update(nombre_var, valor)
        return valor

    def visitBloqueInstrucciones(self, ctx):
        texto = ctx.getText()
        tiene_corchetes = texto.startswith('[')
        if tiene_corchetes:
            self.memoria.push_scope()
        
        resultado = self.visitChildren(ctx)
        
        if tiene_corchetes:
            self.memoria.pop_scope()
        return resultado

    def visitCondicional(self, ctx):
        # Evaluamos la condición (que ahora es una sola expr)
        cumple = self.visit(ctx.condicion())
        
        if cumple:
            return self.visit(ctx.bloqueInstrucciones(0))
        elif ctx.CHI_NO():
            # El bloque CHI_NO es el tercer hijo en la regla (opcional)
            return self.visit(ctx.instrucciones(len(ctx.instrucciones())-1))
        return None

    # --- NUEVA REGLA PARA LA CONDICIÓN ---
    def visitCondicion(self, ctx):
        # Simplemente visita la expresión que tiene adentro
        return self.visit(ctx.expr())

    # --- LÓGICA DE COMPARACIÓN (Etiqueta #comparacion) ---
    def visitComparacion(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.op.text
        
        if op == '>':  return izq > der
        if op == '<':  return izq < der
        if op == '==': return izq == der
        if op == '!=': return izq != der
        if op == '>=': return izq >= der
        if op == '<=': return izq <= der
        return False

    def visitLogicaNot(self, ctx):
        return not self.visit(ctx.expr())

    def visitLogicaAnd(self, ctx):
        return bool(self.visit(ctx.expr(0)) and self.visit(ctx.expr(1)))

    def visitLogicaOr(self, ctx):
        return bool(self.visit(ctx.expr(0)) or self.visit(ctx.expr(1)))

    def visitAritmetica(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        operador = ctx.op.text
        
        if operador == '+': return izq + der
        if operador == '-': return izq - der
        if operador == '*': return izq * der
        if operador == '/': 
            if der == 0: raise Exception("Error: División por cero")
            return izq // der
        return 0

    def visitNumero(self, ctx):
        return int(ctx.NUM().getText())

    def visitVariable(self, ctx):
        nombre_var = ctx.ID().getText()
        return self.memoria.lookup(nombre_var)

    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())