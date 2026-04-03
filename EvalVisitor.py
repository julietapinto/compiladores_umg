from ExpresionesParser import ExpresionesParser
from ExpresionesVisitor import ExpresionesVisitor

class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        self.memoria = {}

    # Regla principal
    def visitEzequiel(self, ctx):
        return self.visitChildren(ctx)

    # Manejo de la etiqueta # DoDeclaracion
    def visitDoDeclaracion(self, ctx):
        return None  # Solo pasamos por aquí para reconocer la sintaxis

    # Manejo de la etiqueta # DoAssign (x = 10;)
    def visitDoAssign(self, ctx):
        # Buscamos el nodo de la asignación real
        asignacion_node = ctx.asignacion()
        nombre = asignacion_node.ID().getText()
        valor = self.visit(asignacion_node.expr())
        self.memoria[nombre] = valor
        return valor

    # Manejo de la etiqueta # DoCondicional
    def visitDoCondicional(self, ctx):
        return self.visitChildren(ctx)

    # Manejo de números e identificadores
    def visitInt(self, ctx): 
        return int(ctx.getText())
    
    def visitId(self, ctx):
        nombre = ctx.getText()
        return self.memoria.get(nombre, 0)

    # Operaciones aritméticas
    def visitAddSub(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        return izq + der if "+" in ctx.getText() else izq - der

    def visitMulDiv(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        if "*" in ctx.getText(): 
            return izq * der
        return izq / der if der != 0 else 0

    def visitParens(self, ctx): 
        return self.visit(ctx.expr())