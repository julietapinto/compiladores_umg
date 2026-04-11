from parser.ExpresionesVisitor import ExpresionesVisitor


class SemanticVisitor(ExpresionesVisitor):
    def __init__(self):
        self.pila = [{}]  # tabla de símbolos (solo nombres)
        self.funciones = {}

    # =========================
    # ÁMBITOS
    # =========================
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

    # =========================
    # ROOT
    # =========================
    def visitRoot(self, ctx):
        return self.visitChildren(ctx)

    # =========================
    # DECLARACION
    # =========================
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        self.declarar(nombre)

        if ctx.expr():
            self.visit(ctx.expr())

    # =========================
    # ASIGNACION
    # =========================
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()

        if not self.existe(nombre):
            raise Exception(f"[ERROR SEMÁNTICO] Variable '{nombre}' no declarada")

        self.visit(ctx.expr())

    # =========================
    # USO DE VARIABLES
    # =========================
    def visitFactor(self, ctx):
        if ctx.ID() and ctx.getChildCount() == 1:
            nombre = ctx.ID().getText()

            if not self.existe(nombre):
                raise Exception(f"[ERROR SEMÁNTICO] Variable '{nombre}' no definida")

        return self.visitChildren(ctx)

    # =========================
    # FUNCIONES
    # =========================
    def visitDecFuncion(self, ctx):
        nombre = ctx.ID().getText()

        if nombre in self.funciones:
            raise Exception(f"[ERROR SEMÁNTICO] Función '{nombre}' ya existe")

        self.funciones[nombre] = ctx

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()

        if nombre not in self.funciones:
            raise Exception(f"[ERROR SEMÁNTICO] Función '{nombre}' no existe")

        # validar argumentos
        if ctx.argumentos():
            for expr in ctx.argumentos().expr():
                self.visit(expr)

    # =========================
    # BLOQUES
    # =========================
    def visitBloqueInstrucciones(self, ctx):
        self.push_scope()

        for ins in ctx.instrucciones():
            self.visit(ins)

        self.pop_scope()

    # =========================
    # CICLOS
    # =========================
    def visitCicloWhile(self, ctx):
        self.visit(ctx.condicion())
        self.visit(ctx.bloqueInstrucciones())

    def visitCicloFor(self, ctx):
        self.visit(ctx.asignacion(0))
        self.visit(ctx.condicion())
        self.visit(ctx.bloqueInstrucciones())
        self.visit(ctx.asignacion(1))