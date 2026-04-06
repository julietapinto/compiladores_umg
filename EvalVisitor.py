from parser.ExpresionesVisitor import ExpresionesVisitor


class ReturnException(Exception):
    def __init__(self, valor):
        self.valor = valor


class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        self.pila = [{}]  # scope global
        self.funciones = {}

    # =========================
    # MANEJO DE ÁMBITOS
    # =========================
    def push_scope(self):
        self.pila.append({})

    def pop_scope(self):
        self.pila.pop()

    def declarar(self, nombre, valor):
        scope_actual = self.pila[-1]

        if nombre in scope_actual:
            raise Exception(f"Variable '{nombre}' ya declarada en este ámbito")

        scope_actual[nombre] = valor

    def asignar(self, nombre, valor):
        for scope in reversed(self.pila):
            if nombre in scope:
                scope[nombre] = valor
                return

        raise Exception(f"Variable '{nombre}' no declarada")

    def obtener(self, nombre):
        for scope in reversed(self.pila):
            if nombre in scope:
                return scope[nombre]

        raise Exception(f"Variable '{nombre}' no definida")

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

        self.declarar(nombre, valor)
        return valor

    # =========================
    # ASIGNACION
    # =========================
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr())

        self.asignar(nombre, valor)
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

        if ctx.ID() and ctx.getChildCount() == 1:
            return self.obtener(ctx.ID().getText())

        if ctx.expr():
            return self.visit(ctx.expr())

        if ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())

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
    # FUNCIONES
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

        self.push_scope()

        for i, p in enumerate(params):
            valor = args[i] if i < len(args) else 0
            self.declarar(p, valor)

        try:
            for ins in func.instrucciones():
                self.visit(ins)
        except ReturnException as r:
            self.pop_scope()
            return r.valor

        self.pop_scope()
        return None