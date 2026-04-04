from parser.ExpresionesVisitor import ExpresionesVisitor


class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        # Memoria (tabla de símbolos)
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
    # DECLARACIÓN
    # =========================
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        if nombre not in self.memoria:
            self.memoria[nombre] = 0
        return 0

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

        # TONCES (si lo usas como segundo bloque separado)
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
            if left:
                return True
            left = left or self.visit(ctx.andExpr(i))

        return left

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.notExpr(0))

        for i in range(1, len(ctx.notExpr())):
            if not left:
                return False
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

        if op == '>':
            return izq > der
        if op == '<':
            return izq < der
        if op == '==':
            return izq == der
        if op == '!=':
            return izq != der
        if op == '>=':
            return izq >= der
        if op == '<=':
            return izq <= der

        return False

    # =========================
    # EXPRESIONES ARITMÉTICAS
    # =========================
    def visitAritmetica(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if op == '+':
            return izq + der
        if op == '-':
            return izq - der
        if op == '*':
            return izq * der
        if op == '/':
            return izq / der if der != 0 else 0

        return 0

    # =========================
    # NUMERO
    # =========================
    def visitNumero(self, ctx):
        return int(ctx.NUM().getText())

    # =========================
    # VARIABLE
    # =========================
    def visitVariable(self, ctx):
        nombre = ctx.ID().getText()
        return self.memoria.get(nombre, 0)

    # =========================
    # PARENTESIS
    # =========================
    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())

    def visitCicloWhile(self, ctx):
        while True:
            condicion = self.visit(ctx.condicion())

            #print("Evaluando condición:", condicion, "a =", self.memoria.get("a"))

            if not condicion:
                break

            for instr in ctx.bloqueInstrucciones().instrucciones():
                self.visit(instr)

        return 0
    
    def visitCicloFor(self, ctx):
    # inicialización
        print("Ejecutando inicialización...")
        self.visit(ctx.asignacion(0))

        while self.visit(ctx.condicion()):
            
            # ejecutar bloque
            for instr in ctx.bloqueInstrucciones().instrucciones():
                self.visit(instr)

            # incremento
            # print("Ejecutando incremento...")
            self.visit(ctx.asignacion(1))

        return 0