from parser.ExpresionesVisitor import ExpresionesVisitor

class SemanticVisitor(ExpresionesVisitor):
    def __init__(self):
        self.pila = [{}]
        self.funciones = {}

    def push_scope(self):
        self.pila.append({})

    def pop_scope(self):
        self.pila.pop()

    def declarar(self, nombre):
        scope = self.pila[-1]
        if nombre in scope:
            raise Exception(f"[ERROR SEMÁNTICO] Variable '{nombre}' ya declarada")
        scope[nombre] = True

    def existe(self, nombre):
        for scope in reversed(self.pila):
            if nombre in scope:
                return True
        return False

    def visitRoot(self, ctx):
        for ins in ctx.instrucciones():
            self.visit(ins)

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        self.declarar(nombre)
        if ctx.expr():
            self.visit(ctx.expr())

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        if not self.existe(nombre):
            raise Exception(f"[ERROR SEMÁNTICO] Variable '{nombre}' no declarada")
        exprs = ctx.expr()
        self.visit(exprs[-1])

    def visitFactor(self, ctx):
        if ctx.ID() and ctx.getChildCount() == 1:
            nombre = ctx.ID().getText()
            if not self.existe(nombre):
                raise Exception(f"[ERROR SEMÁNTICO] Variable '{nombre}' no definida")
        return self.visitChildren(ctx)

    def visitDecFuncion(self, ctx):
        nombre = ctx.ID().getText()
        if nombre in self.funciones:
            raise Exception(f"[ERROR SEMÁNTICO] Función '{nombre}' ya existe")
        self.funciones[nombre] = ctx

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        if nombre not in self.funciones:
            raise Exception(f"[ERROR SEMÁNTICO] Función '{nombre}' no existe")
        if ctx.argumentos():
            for expr in ctx.argumentos().expr():
                self.visit(expr)

    def visitBloqueInstrucciones(self, ctx):
        self.push_scope()
        for ins in ctx.instrucciones():
            if ins is not None:
                self.visit(ins)
        self.pop_scope()

    def visitCicloWhile(self, ctx):
        self.visit(ctx.condicion())
        self.visit(ctx.bloqueInstrucciones())

    def visitCicloFor(self, ctx):
        if ctx.asignacion(0):
            self.visit(ctx.asignacion(0))
        if ctx.condicion():
            self.visit(ctx.condicion())
        if ctx.bloqueInstrucciones():
            self.visit(ctx.bloqueInstrucciones())
        if ctx.asignacion(1):
            self.visit(ctx.asignacion(1))

    def visitCondicion(self, ctx):
        return self.visitChildren(ctx)

    def visitOrExpr(self, ctx):
        return self.visitChildren(ctx)

    def visitAndExpr(self, ctx):
        return self.visitChildren(ctx)

    def visitNotExpr(self, ctx):
        return self.visitChildren(ctx)

    def visitComparacion(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))

    def visitImprimir(self, ctx):
        self.visit(ctx.expr())

    def visitRetorna(self, ctx):
        self.visit(ctx.expr())