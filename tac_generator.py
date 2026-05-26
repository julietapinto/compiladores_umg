from parser.ExpresionesVisitor import ExpresionesVisitor

class TACGenerator(ExpresionesVisitor):
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

    # =========================
    # EXPRESIONES ARITMÉTICAS
    # =========================
    def visitExpr(self, ctx):
        if ctx.getChildCount() == 3:
            izq = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            der = self.visit(ctx.getChild(2))
            temp = self.new_temp()
            self.agregar(f"{temp} = {izq} {op} {der}")
            return temp
        return self.visit(ctx.getChild(0))

    def visitTerm(self, ctx):
        if ctx.getChildCount() == 3:
            izq = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            der = self.visit(ctx.getChild(2))
            temp = self.new_temp()
            self.agregar(f"{temp} = {izq} {op} {der}")
            return temp
        return self.visit(ctx.getChild(0))

    # =========================
    # ACCESO A ARRAYS 1D
    # =========================
    def visitFactor(self, ctx):
        if ctx.ID() and ctx.LBRACKET():
            nombre = ctx.ID().getText()
            indice = self.visit(ctx.expr())
            temp = self.new_temp()
            self.agregar(f"{temp} = {nombre}[{indice}]")
            return temp
        
        if ctx.ID(): return ctx.ID().getText()
        if ctx.NUM(): return ctx.NUM().getText()
        if ctx.FLOAT_NUM(): return ctx.FLOAT_NUM().getText()
        if ctx.STRING(): return ctx.STRING().getText()
        return self.visitChildren(ctx)

    # =========================
    # ASIGNACIONES
    # =========================
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        if ctx.LBRACKET():
            indice = self.visit(ctx.expr(0))
            valor = self.visit(ctx.expr(1))
            self.agregar(f"{nombre}[{indice}] = {valor}")
        else:
            valor = self.visit(ctx.expr(0))
            self.agregar(f"{nombre} = {valor}")

    # =========================
    # CONTROL DE FLUJO
    # =========================
    def visitCicloWhile(self, ctx):
        l_inicio = self.new_label()
        l_cuerpo = self.new_label()
        l_fin = self.new_label()

        self.agregar(f"{l_inicio}:")
        cond = self.visit(ctx.condicion())
        self.agregar(f"if {cond} goto {l_cuerpo}")
        self.agregar(f"goto {l_fin}")
        self.agregar(f"{l_cuerpo}:")
        self.visit(ctx.bloqueInstrucciones())
        self.agregar(f"goto {l_inicio}")
        self.agregar(f"{l_fin}:")

    def visitCondicional(self, ctx):
        l_true = self.new_label()
        l_false = self.new_label()
        
        cond = self.visit(ctx.condicion())
        self.agregar(f"if {cond} goto {l_true}")
        self.agregar(f"goto {l_false}")
        
        self.agregar(f"{l_true}:")
        self.visit(ctx.bloqueInstrucciones(0))
        
        if ctx.TONCES() or ctx.CHI_NO():
            l_fin = self.new_label()
            self.agregar(f"goto {l_fin}")
            self.agregar(f"{l_false}:")
            self.visit(ctx.bloqueInstrucciones(1))
            self.agregar(f"{l_fin}:")
        else:
            self.agregar(f"{l_false}:")

    # =========================
    # FUNCIONES
    # =========================
    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        if ctx.argumentos():
            for arg in ctx.argumentos().expr():
                val = self.visit(arg)
                self.agregar(f"param {val}")
        
        temp = self.new_temp()
        self.agregar(f"{temp} = call {nombre}")
        return temp

    def visitRetorna(self, ctx):
        val = self.visit(ctx.expr())
        self.agregar(f"return {val}")

    def visitComparacion(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.relop().getText()
        temp = self.new_temp()
        self.agregar(f"{temp} = {izq} {op} {der}")
        return temp
if __name__ == "__main__":
    # Prueba rápida 
    gen = TACGenerator()
    
    # Simulamos una operación aritmética y un IF
    gen.agregar("// --- Ejemplo de Aritmética ---")
    gen.agregar("t1 = 5 * 2")
    gen.agregar("x = 10 + t1")
    
    gen.agregar("\n// --- Ejemplo de Condicional ---")
    gen.agregar("if x > 10 goto L1")
    gen.agregar("goto L2")
    gen.agregar("L1:")
    gen.agregar("   IMPRIMIR(x)")
    gen.agregar("L2:")
    
    print(gen.obtener_codigo())