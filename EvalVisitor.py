from parser.ExpresionesVisitor import ExpresionesVisitor

class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        # Tabla de símbolos (Memoria del compilador)
        self.memoria = {}

    def __init__(self):
        self.memoria = {}

    # --- ROOT ---
    def visitRoot(self, ctx):
        return self.visitChildren(ctx)

    # --- DECLARACION ---
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        if nombre not in self.memoria:
            self.memoria[nombre] = 0
        return 0

    # --- ASIGNACION ---
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        self.memoria[nombre] = valor
        return valor

    # --- CONDICIONAL ---
    def visitCondicional(self, ctx):
        cumple = self.visit(ctx.condicion())  # 🔥 CORRECTO

        if cumple:
            return self.visit(ctx.bloqueInstrucciones(0))

        # TONCES (else)
        if len(ctx.bloqueInstrucciones()) > 1:
            return self.visit(ctx.bloqueInstrucciones(1))

        # CHI_NO (else alternativo)
        if len(ctx.bloqueInstrucciones()) > 2:
            return self.visit(ctx.bloqueInstrucciones(2))

        return 0

    # --- COMPARACION ---
    def visitComparacion(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.op.text

        if op == '>': return izq > der
        if op == '<': return izq < der
        if op == '==': return izq == der
        if op == '!=': return izq != der
        if op == '>=': return izq >= der
        if op == '<=': return izq <= der

        return False

    # --- ARITMETICA ---
    def visitAritmetica(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == '+': return izq + der
        if op == '-': return izq - der
        if op == '*': return izq * der
        if op == '/': return izq / der if der != 0 else 0

        return 0

    # --- NUMERO ---
    def visitNumero(self, ctx):
        return int(ctx.NUM().getText())

    # --- VARIABLE ---
    def visitVariable(self, ctx):
        nombre = ctx.ID().getText()
        return self.memoria.get(nombre, 0)

    # --- PARENTESIS ---
    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())

    # --- BLOQUES ---
    def visitBloqueInstrucciones(self, ctx):
        return self.visitChildren(ctx)