from parser.ExpresionesVisitor import ExpresionesVisitor


class ReturnException(Exception):
    def __init__(self, valor):
        self.valor = valor


class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        self.memoria = {}
        self.funciones = {}

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
    # DECLARACION
    # =========================
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr()) if ctx.expr() else 0
        self.memoria[nombre] = valor
        return valor

    # =========================
    # ASIGNACION
    # =========================
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        self.memoria[nombre] = valor
        return valor

    # =========================
    # IMPRIMIR
    # =========================
    def visitImprimir(self, ctx):
        valor = self.visit(ctx.expr())
        print(valor)
        return valor

    # =========================
    # RETORNA
    # =========================
    def visitRetorna(self, ctx):
        valor = self.visit(ctx.expr())
        raise ReturnException(valor)

    # =========================
    # CONDICION
    # =========================
    def visitCondicion(self, ctx):
        return self.visit(ctx.orExpr())

    def visitOrExpr(self, ctx):
        result = self.visit(ctx.andExpr(0))
        for i in range(1, len(ctx.andExpr())):
            result = result or self.visit(ctx.andExpr(i))
        return result

    def visitAndExpr(self, ctx):
        result = self.visit(ctx.notExpr(0))
        for i in range(1, len(ctx.notExpr())):
            result = result and self.visit(ctx.notExpr(i))
        return result

    def visitNotExpr(self, ctx):
        if ctx.NOT():
            return not self.visit(ctx.notExpr())
        if ctx.comparacion():
            return self.visit(ctx.comparacion())
        if ctx.condicion():
            return self.visit(ctx.condicion())
        if ctx.BOOLEAN():
            return ctx.BOOLEAN().getText() == "true"

    # =========================
    # COMPARACION
    # =========================
    def visitComparacion(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.relop().getText()

        if op == ">":
            return izq > der
        if op == "<":
            return izq < der
        if op == "==":
            return izq == der
        if op == "!=":
            return izq != der
        if op == ">=":
            return izq >= der
        if op == "<=":
            return izq <= der

    # =========================
    # EXPRESIONES ARITMETICAS
    # =========================
    def visitExpr(self, ctx):
        result = self.visit(ctx.term(0))

        for i in range(1, len(ctx.term())):
            if ctx.SUM(i - 1):
                result += self.visit(ctx.term(i))
            else:
                result -= self.visit(ctx.term(i))

        return result

    def visitTerm(self, ctx):
        result = self.visit(ctx.factor(0))

        for i in range(1, len(ctx.factor())):
            if ctx.MUL(i - 1):
                result *= self.visit(ctx.factor(i))
            else:
                result /= self.visit(ctx.factor(i))

        return result

    # =========================
    # FACTORES
    # =========================
    def visitFactor(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())

        if ctx.FLOAT_NUM():
            return float(ctx.FLOAT_NUM().getText())

        if ctx.STRING():
            return ctx.STRING().getText().strip('"')

        if ctx.BOOLEAN():
            return ctx.BOOLEAN().getText() == "true"

        if ctx.ID() and ctx.getChildCount() == 1:
            return self.memoria.get(ctx.ID().getText(), 0)

        if ctx.expr():
            return self.visit(ctx.expr())

        if ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())

    # =========================
    # VARIABLES / DEFAULT
    # =========================
    def visitVariable(self, ctx):
        return self.memoria.get(ctx.ID().getText(), 0)

    # =========================
    # CICLO WHILE
    # =========================
    def visitCicloWhile(self, ctx):
        while self.visit(ctx.condicion()):
            self.visit(ctx.bloqueInstrucciones())

    # =========================
    # CICLO FOR
    # =========================
    def visitCicloFor(self, ctx):
        self.visit(ctx.asignacion(0))
        while self.visit(ctx.condicion()):
            self.visit(ctx.bloqueInstrucciones())
            self.visit(ctx.asignacion(1))

    # =========================
    # BLOQUE
    # =========================
    def visitBloqueInstrucciones(self, ctx):
        for ins in ctx.instrucciones():
            self.visit(ins)

    # =========================
    # FUNCIONES (BÁSICO)
    # =========================
    def visitDecFuncion(self, ctx):
        nombre = ctx.ID().getText()
        self.funciones[nombre] = ctx

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()

        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no existe")

        func = self.funciones[nombre]

        args = []
        if ctx.argumentos():
            for e in ctx.argumentos().expr():
                args.append(self.visit(e))

        params = []
        if func.parametros():
            for p in func.parametros().ID():
                params.append(p.getText())

        backup = self.memoria.copy()

        for i, p in enumerate(params):
            self.memoria[p] = args[i] if i < len(args) else 0

        try:
            for ins in func.instrucciones():
                self.visit(ins)
        except ReturnException as r:
            self.memoria = backup
            return r.valor

        self.memoria = backup
        return None