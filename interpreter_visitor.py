from parser.ExpresionesVisitor import ExpresionesVisitor
from symbol_table import SymbolTable


class ReturnException(Exception):
    def __init__(self, valor):
        self.valor = valor


class BreakException(Exception):
    pass


class ContinueException(Exception):
    pass


class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        self.symbols = SymbolTable()
        self.funciones = {}

    def visitRoot(self, ctx):
        for ins in ctx.instrucciones():
            self.visit(ins)

    def visitDeclaracion(self, ctx):
        nombre = ctx.ID().getText()
        # Array: int arr[5]
        if ctx.NUM():
            tamano = int(ctx.NUM().getText())
            self.symbols.declarar(nombre, [0] * tamano)
            return
        # Variable normal
        valor = self.visit(ctx.expr()) if ctx.expr() else 0
        self.symbols.declarar(nombre, valor)
        return valor

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        exprs = ctx.expr()
        # Asignación a array: arr[i] = valor
        if len(exprs) == 2:
            indice = self.visit(exprs[0])
            valor = self.visit(exprs[1])
            arr = self.symbols.obtener(nombre)
            arr[indice] = valor
            return valor
        # Asignación normal
        valor = self.visit(exprs[-1])
        self.symbols.asignar(nombre, valor)
        return valor

    def visitImprimir(self, ctx):
        valor = self.visit(ctx.expr())
        print(valor)
        return valor

    def visitRetorna(self, ctx):
        valor = self.visit(ctx.expr())
        raise ReturnException(valor)

    def visitImportStmt(self, ctx):
        archivo = ctx.STRING().getText().strip('"')
        try:
            with open(f"input/{archivo}", "r", encoding="utf-8") as f:
                contenido = f.read()
            print(f"[IMPORT] Archivo '{archivo}' cargado.")
        except FileNotFoundError:
            print(f"[IMPORT ERROR] Archivo '{archivo}' no encontrado.")
        return None

    def visitInstrucciones(self, ctx):
        if ctx.BREAK():
            raise BreakException()
        if ctx.CONTINUE():
            raise ContinueException()
        return self.visitChildren(ctx)

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
        return False

    def visitComparacion(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.relop().getText()
        if op == ">":  return izq > der
        if op == "<":  return izq < der
        if op == "==": return izq == der
        if op == "!=": return izq != der
        if op == ">=": return izq >= der
        if op == "<=": return izq <= der
        return False

    def visitExpr(self, ctx):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            if ctx.SUM(i - 1):
                next_val = self.visit(ctx.term(i))
                if isinstance(result, str) or isinstance(next_val, str):
                    result = str(result) + str(next_val)
                else:
                    result += next_val
            else:
                result -= self.visit(ctx.term(i))
        return result

    def visitTerm(self, ctx):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            if ctx.MUL(i - 1):
                result *= self.visit(ctx.factor(i))
            elif ctx.DIV(i - 1):
                divisor = self.visit(ctx.factor(i))
                result /= divisor if divisor != 0 else 1
            elif ctx.MOD(i - 1):
                result %= self.visit(ctx.factor(i))
        return result

    def visitFactor(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())
        if ctx.FLOAT_NUM():
            return float(ctx.FLOAT_NUM().getText())
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        if ctx.ID() and ctx.LPAREN():
            nombre = ctx.ID().getText()
            args = []
            if ctx.argumentos():
                for e in ctx.argumentos().expr():
                    args.append(self.visit(e))
            return self._ejecutarFuncion(nombre, args)
        if ctx.ID() and ctx.LBRACKET():
            nombre = ctx.ID().getText()
            indice = self.visit(ctx.expr())
            arr = self.symbols.obtener(nombre)
            return arr[indice]
        if ctx.ID():
            return self.symbols.obtener(ctx.ID().getText())
        if ctx.expr():
            return self.visit(ctx.expr())
        return 0

    def visitCicloWhile(self, ctx):
        while self.visit(ctx.condicion()):
            try:
                self.visit(ctx.bloqueInstrucciones())
            except BreakException:
                break
            except ContinueException:
                continue

    def visitCicloFor(self, ctx):
        self.visit(ctx.asignacion(0))
        while self.visit(ctx.condicion()):
            try:
                self.visit(ctx.bloqueInstrucciones())
            except BreakException:
                break
            except ContinueException:
                pass
            self.visit(ctx.asignacion(1))

    def visitBloqueInstrucciones(self, ctx):
        self.symbols.push_scope()
        for ins in ctx.instrucciones():
            self.visit(ins)
        self.symbols.pop_scope()

    def visitCondicional(self, ctx):
        condicion = self.visit(ctx.condicion())
        bloques = ctx.bloqueInstrucciones()
        if condicion:
            self.visit(bloques[0])
        elif len(bloques) > 1:
            self.visit(bloques[1])

    def visitDecFuncion(self, ctx):
        nombre = ctx.ID().getText()
        self.funciones[nombre] = ctx

    def visitLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        args = []
        if ctx.argumentos():
            for e in ctx.argumentos().expr():
                args.append(self.visit(e))
        return self._ejecutarFuncion(nombre, args)

    def _ejecutarFuncion(self, nombre, args):
        if nombre not in self.funciones:
            raise Exception(f"Funcion '{nombre}' no existe")
        func = self.funciones[nombre]
        params = []
        if func.parametros():
            for p in func.parametros().ID():
                params.append(p.getText())
        self.symbols.push_scope()
        for i, p in enumerate(params):
            valor = args[i] if i < len(args) else 0
            self.symbols.declarar(p, valor)
        resultado = None
        try:
            for ins in func.instrucciones():
                self.visit(ins)
        except ReturnException as r:
            resultado = r.valor
        self.symbols.pop_scope()
        return resultado