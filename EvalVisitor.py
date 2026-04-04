from parser.ExpresionesVisitor import ExpresionesVisitor

class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        # Memoria (tabla de símbolos para ejecución)
        self.memoria = {}

    # =========================
    # ROOT
    # =========================
    def visitRoot(self, ctx):
        return self.visitChildren(ctx)

    # =========================
    # INSTRUCCIONES
    # =========================
    def visitInstrucciones(self, ctx):
        return self.visitChildren(ctx)

    # =========================
    # DECLARACIÓN (MODIFICADO PARA TIPOS DE DATOS EXPLICITOS)
    # =========================
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        valor = 0 # Valor por defecto
        
        # Si tiene una asignación inmediata (ej: int x = 10;)
        if ctx.expr():
            valor = self.visit(ctx.expr())
        
        self.memoria[nombre] = valor
        return valor

    # =========================
    # ASIGNACIÓN
    # =========================
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        self.memoria[nombre] = valor
        return valor

    # =========================
    # CONDICIONAL
    # =========================
    def visitCondicional(self, ctx):
        condicion = self.visit(ctx.condicion())
        bloques = ctx.bloqueInstrucciones()

        # IF
        if condicion:
            return self.visit(bloques[0])

        # CHI_NO (else if exists as second block)
        if len(bloques) == 2:
            return self.visit(bloques[1])

        # TONCES (si lo usan como segundo bloque separado)
        if len(bloques) > 2:
            return self.visit(bloques[2])

        return 0

    # =========================
    # BLOQUE
    # =========================
    def visitBloqueInstrucciones(self, ctx):
        return self.visitChildren(ctx)

    # =========================
    # CONDICIONES LÓGICAS 
    # =========================
    def visitOrExpr(self, ctx):
        left = self.visit(ctx.andExpr(0))
        for i in range(1, len(ctx.andExpr())):
            if left: return True
            left = left or self.visit(ctx.andExpr(i))
        return left

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.notExpr(0))
        for i in range(1, len(ctx.notExpr())):
            if not left: return False
            left = left and self.visit(ctx.notExpr(i))
        return left

    def visitNotExpr(self, ctx):
        if ctx.NOT():
            return not self.visit(ctx.notExpr())
        if ctx.comparacion():
            return self.visit(ctx.comparacion())
        if ctx.condicion():
            return self.visit(ctx.condicion())
        return False

    # =========================
    # COMPARACIÓN
    # =========================
    def visitComparacion(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.relop().getText()

        if op == '>': return izq > der
        if op == '<': return izq < der
        if op == '==': return izq == der
        if op == '!=': return izq != der
        if op == '>=': return izq >= der
        if op == '<=': return izq <= der
        return False

    # =========================
    # EXPRESIONES ARITMÉTICAS
    # =========================
    def visitAritmetica(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == '+': return izq + der
        if op == '-': return izq - der
        if op == '*': return izq * der
        if op == '/': return izq / der if der != 0 else 0
        return 0

    # =========================
    # PUNTO 1: NUEVOS TIPOS DE DATOS EXPLICITOS
    # =========================
    def visitNumero(self, ctx):
        return int(ctx.NUM().getText())

    def visitDecimal(self, ctx):
        return float(ctx.DECIMAL().getText())

    def visitTexto(self, ctx):
        return ctx.STRING().getText().replace('"', '')

    def visitLogico(self, ctx):
        return ctx.BOOLEAN().getText() == 'true'

    # =========================
    # VARIABLE / PARENTESIS
    # =========================
    def visitVariable(self, ctx):
        nombre = ctx.ID().getText()
        return self.memoria.get(nombre, 0)

    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())