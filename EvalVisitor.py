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
    # DECLARACIÓN
    # =========================
    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr()) if ctx.expr() else 0
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
        if condicion:
            return self.visit(bloques[0])
        if len(bloques) == 2:
            return self.visit(bloques[1])
        if len(bloques) == 3:
            return self.visit(bloques[2])
        return 0

    # =========================
    # BLOQUE
    # =========================
    def visitBloqueInstrucciones(self, ctx):
        for instr in ctx.instrucciones():
            self.visit(instr)
        return 0

    # =========================
    # DECLARACIÓN DE FUNCIÓN
    # =========================
    def visitDecFuncion(self, ctx):
        nombre = ctx.ID().getText()
        self.funciones[nombre] = ctx
        return None

    # =========================
    # LLAMADA A FUNCIÓN (como instrucción)
    # =========================
    def visitLlamadaFuncion(self, ctx):
        return self._ejecutarFuncion(ctx)

    # =========================
    # LLAMADA A FUNCIÓN (dentro de expr)
    # =========================
    def visitLlamadaExpr(self, ctx):
        return self._ejecutarFuncion(ctx)

    def _ejecutarFuncion(self, ctx):
        nombre = ctx.ID().getText()

        if nombre not in self.funciones:
            raise Exception(f"Error: función '{nombre}' no declarada.")

        func_ctx = self.funciones[nombre]

        # Evaluar argumentos
        args = []
        if ctx.argumentos():
            for arg in ctx.argumentos().expr():
                args.append(self.visit(arg))

        # Obtener parámetros
        params = []
        if func_ctx.parametros():
            for param_id in func_ctx.parametros().ID():
                params.append(param_id.getText())

        # Crear ámbito local
        ambito_anterior = self.memoria.copy()
        for i, param in enumerate(params):
            self.memoria[param] = args[i] if i < len(args) else 0

        # Ejecutar cuerpo
        resultado = None
        try:
            for inst in func_ctx.instrucciones():
                self.visit(inst)
        except ReturnException as r:
            resultado = r.valor

        # Restaurar ámbito anterior
        self.memoria = ambito_anterior
        return resultado

    # =========================
    # RETORNA
    # =========================
    def visitRetorna(self, ctx):
        valor = self.visit(ctx.expr())
        raise ReturnException(valor)

    # =========================
    # IMPRIMIR
    # =========================
    def visitImprimir(self, ctx):
        valor = self.visit(ctx.expr())
        print(valor)
        return valor

    # =========================
    # CONDICIONES LÓGICAS
    # =========================
    def visitCondicion(self, ctx):
        return self.visit(ctx.orExpr())

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
        if op == '>':  return izq > der
        if op == '<':  return izq < der
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
    # TIPOS DE DATOS
    # =========================
    def visitNumero(self, ctx):
        return int(ctx.NUM().getText())

    def visitDecimal(self, ctx):
        return float(ctx.FLOAT_NUM().getText())

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

    # =========================
    # CICLOS
    # =========================
    def visitCicloWhile(self, ctx):
        while True:
            condicion = self.visit(ctx.condicion())
            if not condicion:
                break
            for instr in ctx.bloqueInstrucciones().instrucciones():
                self.visit(instr)
        return 0

    def visitCicloFor(self, ctx):
        self.visit(ctx.asignacion(0))
        while self.visit(ctx.condicion()):
            for instr in ctx.bloqueInstrucciones().instrucciones():
                self.visit(instr)
            self.visit(ctx.asignacion(1))
        return 0