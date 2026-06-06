from parser.ExpresionesVisitor import ExpresionesVisitor


class TACGenerator(ExpresionesVisitor):

    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.label_count = 0
        self.break_targets = []
        self.continue_targets = []

    def new_temp(self):
        t = f"t{self.temp_count}"
        self.temp_count += 1
        return t

    def new_label(self):
        l = f"L{self.label_count}"
        self.label_count += 1
        return l

    def emit(self, instruction):
        self.code.append(instruction)

    def obtener_codigo(self):
        return "\n".join(self.code)

    def visitRoot(self, ctx):
        for ins in ctx.instrucciones():
            self.visit(ins)

    def visitDeclaracion(self, ctx):
        if ctx.ternario():
            valor = self.visit(ctx.ternario())
            ids = ctx.ID()
            nombre = ids[-1].getText() if isinstance(ids, list) else ids.getText()
            self.emit(f"{nombre} = {valor}")

    def visitAsignacion(self, ctx):
        if ctx.DOT():
            nombre = f"{ctx.ID(0).getText()}.{ctx.ID(1).getText()}"
        else:
            nombre = ctx.ID(0).getText()
        if ctx.LBRACKET():
            index = self.visit(ctx.expr())
            valor = self.visit(ctx.ternario())
            self.emit(f"{nombre}[{index}] = {valor}")
            return nombre
        valor = self.visit(ctx.ternario())
        self.emit(f"{nombre} = {valor}")
        return nombre

    def visitImprimir(self, ctx):
        valor = self.visit(ctx.ternario())
        self.emit(f"print {valor}")
        return valor

    def visitRetorna(self, ctx):
        valor = self.visit(ctx.ternario())
        self.emit(f"return {valor}")
        return valor

    def visitImportStmt(self, ctx):
        archivo = ctx.STRING().getText()
        self.emit(f"import {archivo}")

    def visitInstrucciones(self, ctx):
        if ctx.BREAK():
            if not self.break_targets:
                raise Exception("break fuera de un bloque válido")
            self.emit(f"goto {self.break_targets[-1]}")
            return
        if ctx.CONTINUE():
            if not self.continue_targets:
                raise Exception("continue fuera de un bloque válido")
            self.emit(f"goto {self.continue_targets[-1]}")
            return
        return self.visitChildren(ctx)

    def visitCondicional(self, ctx):
        condicion = self.visit(ctx.condicion())
        then_label = self.new_label()
        end_label = self.new_label()
        else_label = self.new_label() if ctx.CHI_NO() else end_label

        self.emit(f"if {condicion} goto {then_label}")
        self.emit(f"goto {else_label}")
        self.emit(f"{then_label}:")
        self.visit(ctx.bloqueInstrucciones(0))
        if ctx.CHI_NO():
            self.emit(f"goto {end_label}")
            self.emit(f"{else_label}:")
            self.visit(ctx.bloqueInstrucciones(1))
        self.emit(f"{end_label}:")

    def visitCicloWhile(self, ctx):
        start_label = self.new_label()
        body_label = self.new_label()
        end_label = self.new_label()

        self.emit(f"{start_label}:")
        condicion = self.visit(ctx.condicion())
        self.emit(f"if {condicion} goto {body_label}")
        self.emit(f"goto {end_label}")
        self.emit(f"{body_label}:")

        self.break_targets.append(end_label)
        self.continue_targets.append(start_label)
        self.visit(ctx.bloqueInstrucciones())
        self.break_targets.pop()
        self.continue_targets.pop()

        self.emit(f"goto {start_label}")
        self.emit(f"{end_label}:")

    def visitCicloFor(self, ctx):
        self.visit(ctx.asignacion(0))

        start_label = self.new_label()
        body_label = self.new_label()
        increment_label = self.new_label()
        end_label = self.new_label()

        self.emit(f"{start_label}:")
        condicion = self.visit(ctx.condicion())
        self.emit(f"if {condicion} goto {body_label}")
        self.emit(f"goto {end_label}")
        self.emit(f"{body_label}:")

        self.break_targets.append(end_label)
        self.continue_targets.append(increment_label)
        self.visit(ctx.bloqueInstrucciones())
        self.break_targets.pop()
        self.continue_targets.pop()

        self.emit(f"{increment_label}:")
        self.visit(ctx.asignacion(1))
        self.emit(f"goto {start_label}")
        self.emit(f"{end_label}:")

    def visitBloqueInstrucciones(self, ctx):
        for ins in ctx.instrucciones():
            self.visit(ins)

    def visitDecFuncion(self, ctx):
        self.emit(f"func {ctx.ID().getText()}:")
        self.visit(ctx.bloqueInstrucciones())
        self.emit("endfunc")

    def visitLlamadaFuncion(self, ctx):
        args = []
        if ctx.argumentos():
            for expr in ctx.argumentos().expr():
                args.append(self.visit(expr))
        resultado = self.new_temp()
        self.emit(f"{resultado} = call {ctx.ID().getText()}({', '.join(args)})")
        return resultado

    def visitSwitchStmt(self, ctx):
        expr = self.visit(ctx.expr())
        case_labels = [self.new_label() for _ in ctx.caseStmt()]
        default_label = self.new_label()
        end_label = self.new_label()

        for i, case_ctx in enumerate(ctx.caseStmt()):
            case_value = self.visit(case_ctx.expr())
            self.emit(f"if {expr} == {case_value} goto {case_labels[i]}")

        self.emit(f"goto {default_label}")

        for i, case_ctx in enumerate(ctx.caseStmt()):
            self.emit(f"{case_labels[i]}:")
            self.break_targets.append(end_label)
            self.continue_targets.append(end_label)
            self.visit(case_ctx)
            self.break_targets.pop()
            self.continue_targets.pop()

        self.emit(f"{default_label}:")
        if ctx.defaultStmt():
            self.break_targets.append(end_label)
            self.continue_targets.append(end_label)
            self.visit(ctx.defaultStmt())
            self.break_targets.pop()
            self.continue_targets.pop()

        self.emit(f"{end_label}:")

    def visitCaseStmt(self, ctx):
        for ins in ctx.instrucciones():
            self.visit(ins)

    def visitDefaultStmt(self, ctx):
        for ins in ctx.instrucciones():
            self.visit(ins)

    def visitCondicion(self, ctx):
        return self.visit(ctx.orExpr())

    def visitOrExpr(self, ctx):
        left = self.visit(ctx.andExpr(0))
        for i in range(1, len(ctx.andExpr())):
            right = self.visit(ctx.andExpr(i))
            temp = self.new_temp()
            self.emit(f"{temp} = {left} || {right}")
            left = temp
        return left

    def visitAndExpr(self, ctx):
        left = self.visit(ctx.notExpr(0))
        for i in range(1, len(ctx.notExpr())):
            right = self.visit(ctx.notExpr(i))
            temp = self.new_temp()
            self.emit(f"{temp} = {left} && {right}")
            left = temp
        return left

    def visitNotExpr(self, ctx):
        if ctx.NOT():
            operand = self.visit(ctx.notExpr())
            temp = self.new_temp()
            self.emit(f"{temp} = ! {operand}")
            return temp
        if ctx.comparacion():
            return self.visit(ctx.comparacion())
        if ctx.condicion():
            return self.visit(ctx.condicion())
        return "false"

    def visitComparacion(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.relop().getText()
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op} {right}")
        return temp

    def visitExpr(self, ctx):
        return self.visit(ctx.comparacionExpr())

    def visitComparacionExpr(self, ctx):
        left = self.visit(ctx.sumaExpr(0))
        if ctx.relop():
            right = self.visit(ctx.sumaExpr(1))
            op = ctx.relop().getText()
            temp = self.new_temp()
            self.emit(f"{temp} = {left} {op} {right}")
            return temp
        return left

    def visitSumaExpr(self, ctx):
        left = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            right = self.visit(ctx.term(i))
            temp = self.new_temp()
            if ctx.SUM(i - 1):
                self.emit(f"{temp} = {left} + {right}")
            else:
                self.emit(f"{temp} = {left} - {right}")
            left = temp
        return left

    def visitTerm(self, ctx):
        left = self.visit(ctx.castExpr(0))
        for i in range(1, len(ctx.castExpr())):
            right = self.visit(ctx.castExpr(i))
            temp = self.new_temp()
            if ctx.MUL(i - 1):
                self.emit(f"{temp} = {left} * {right}")
            elif ctx.DIV(i - 1):
                self.emit(f"{temp} = {left} / {right}")
            else:
                self.emit(f"{temp} = {left} % {right}")
            left = temp
        return left

    def visitCastExpr(self, ctx):
        if ctx.RES():
            operand = self.visit(ctx.castExpr())
            temp = self.new_temp()
            self.emit(f"{temp} = - {operand}")
            return temp
        if ctx.LPAREN() and ctx.tipo() and ctx.castExpr():
            return self.visit(ctx.castExpr())
        if ctx.factor():
            return self.visit(ctx.factor())
        return "0"

    def visitFactor(self, ctx):
        if ctx.NUM():
            return ctx.NUM().getText()
        if ctx.FLOAT_NUM():
            return ctx.FLOAT_NUM().getText()
        if ctx.STRING():
            return ctx.STRING().getText()
        if ctx.ID() and ctx.LPAREN():
            args = []
            if ctx.argumentos():
                for expr in ctx.argumentos().expr():
                    args.append(self.visit(expr))
            temp = self.new_temp()
            self.emit(f"{temp} = call {ctx.ID(0).getText()}({', '.join(args)})")
            return temp
        if ctx.ID() and ctx.LBRACKET():
            index = self.visit(ctx.expr())
            temp = self.new_temp()
            self.emit(f"{temp} = {ctx.ID(0).getText()}[{index}]")
            return temp
        if ctx.ID() and ctx.DOT():
            left = ctx.ID(0).getText()
            right = ctx.ID(1).getText()
            return f"{left}.{right}"
        if ctx.ID():
            return ctx.ID(0).getText()
        if ctx.expr():
            return self.visit(ctx.expr())
        return "0"
