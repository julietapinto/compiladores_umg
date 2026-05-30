from parser.gramatica_v4Visitor import gramatica_v4Visitor


class TACGenerator(gramatica_v4Visitor):

    def __init__(self):
        self.count_t = 0
        self.count_l = 0
        self.instrucciones = []

    def new_temp(self):
        self.count_t += 1
        return f"t{self.count_t}"

    def new_label(self):
        self.count_l += 1
        return f"L{self.count_l}"

    def agregar(self, linea):
        self.instrucciones.append(linea)

    def obtener_codigo(self):
        return "\n".join(self.instrucciones)

    # =====================================
    # EXPRESIONES
    # =====================================

    def visitExpr(self, ctx):

        if ctx.getChildCount() == 3:
            izq = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            der = self.visit(ctx.getChild(2))

            temp = self.new_temp()
            self.agregar(f"{temp} = {izq} {op} {der}")

            return temp

        return self.visitChildren(ctx)

    def visitTerm(self, ctx):

        if ctx.getChildCount() == 3:
            izq = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            der = self.visit(ctx.getChild(2))

            temp = self.new_temp()
            self.agregar(f"{temp} = {izq} {op} {der}")

            return temp

        return self.visitChildren(ctx)

    def visitTernario(self, ctx):

        if ctx.QUESTION():
            cond = self.visit(ctx.expr(0))
            verdadero = self.visit(ctx.expr(1))
            falso = self.visit(ctx.expr(2))

            temp = self.new_temp()

            self.agregar(
                f"{temp} = {cond} ? {verdadero} : {falso}"
            )

            return temp

        return self.visit(ctx.expr(0))

    # =====================================
    # FACTOR
    # =====================================

    def visitFactor(self, ctx):

        if ctx.NUM():
            return ctx.NUM().getText()

        if ctx.FLOAT_NUM():
            return ctx.FLOAT_NUM().getText()

        if ctx.STRING():
            return ctx.STRING().getText()

        # arreglo
        if ctx.LBRACKET():
            nombre = ctx.ID(0).getText()
            indice = self.visit(ctx.expr())

            temp = self.new_temp()
            self.agregar(f"{temp} = {nombre}[{indice}]")

            return temp

        # acceso struct
        if ctx.DOT():
            return f"{ctx.ID(0).getText()}.{ctx.ID(1).getText()}"

        # llamada función
        if ctx.LPAREN() and ctx.ID():
            return self.visitChildren(ctx)

        # variable simple
        if ctx.ID():
            return ctx.ID(0).getText()

        if ctx.expr():
            return self.visit(ctx.expr())

        return self.visitChildren(ctx)

    # =====================================
    # ASIGNACION
    # =====================================

    def visitAsignacion(self, ctx):

        ids = ctx.ID()

        # arreglo
        if ctx.LBRACKET():

            nombre = ids[0].getText()
            indice = self.visit(ctx.expr())
            valor = self.visit(ctx.ternario())

            self.agregar(
                f"{nombre}[{indice}] = {valor}"
            )

        # struct
        elif len(ids) == 2:

            nombre = ids[0].getText()
            campo = ids[1].getText()

            valor = self.visit(ctx.ternario())

            self.agregar(
                f"{nombre}.{campo} = {valor}"
            )

        # variable normal
        else:

            nombre = ids[0].getText()
            valor = self.visit(ctx.ternario())

            self.agregar(
                f"{nombre} = {valor}"
            )

    # =====================================
    # COMPARACIONES
    # =====================================

    def visitComparacion(self, ctx):

        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))

        op = ctx.relop().getText()

        temp = self.new_temp()

        self.agregar(
            f"{temp} = {izq} {op} {der}"
        )

        return temp

    # =====================================
    # WHILE
    # =====================================

    def visitCicloWhile(self, ctx):

        l_inicio = self.new_label()
        l_true = self.new_label()
        l_fin = self.new_label()

        self.agregar(f"{l_inicio}:")

        cond = self.visit(ctx.condicion())

        self.agregar(f"if {cond} goto {l_true}")
        self.agregar(f"goto {l_fin}")

        self.agregar(f"{l_true}:")

        self.visit(ctx.bloqueInstrucciones())

        self.agregar(f"goto {l_inicio}")
        self.agregar(f"{l_fin}:")

    # =====================================
    # IF
    # =====================================

    def visitCondicional(self, ctx):

        l_true = self.new_label()
        l_false = self.new_label()
        l_fin = self.new_label()

        cond = self.visit(ctx.condicion())

        self.agregar(f"if {cond} goto {l_true}")
        self.agregar(f"goto {l_false}")

        self.agregar(f"{l_true}:")

        self.visit(ctx.bloqueInstrucciones(0))

        self.agregar(f"goto {l_fin}")

        self.agregar(f"{l_false}:")

        if len(ctx.bloqueInstrucciones()) > 1:
            self.visit(ctx.bloqueInstrucciones(1))

        self.agregar(f"{l_fin}:")

    # =====================================
    # LLAMADA FUNCION
    # =====================================

    def visitLlamadaFuncion(self, ctx):

        nombre = ctx.ID().getText()

        if ctx.argumentos():

            for arg in ctx.argumentos().ternario():

                valor = self.visit(arg)

                self.agregar(
                    f"param {valor}"
                )

        temp = self.new_temp()

        self.agregar(
            f"{temp} = call {nombre}"
        )

        return temp

    # =====================================
    # RETURN
    # =====================================

    def visitRetorna(self, ctx):

        valor = self.visit(ctx.ternario())

        self.agregar(
            f"return {valor}"
        )


if __name__ == "__main__":

    gen = TACGenerator()

    gen.agregar("// TAC generado")

    print(gen.obtener_codigo())