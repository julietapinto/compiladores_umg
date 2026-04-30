from parser.ExpresionesVisitor import ExpresionesVisitor
from Simbolo import Simbolo

class SemanticVisitor(ExpresionesVisitor):
    def __init__(self):
        self.pila = [{}]
        self.funciones = {}
        self.current_function = None
        self.in_loop = 0
        self.errores = []

    def push_scope(self):
        self.pila.append({})

    def pop_scope(self):
        self.pila.pop()

    def declarar(self, nombre, tipo, valor=None):
        scope = self.pila[-1]

        if nombre in scope:
            self.errores.append(f"[ERROR SEMÁNTICO] Variable '{nombre}' ya declarada")
            return

        # Detectar arrays
        if "[]" in tipo:
            tipo_base = tipo.replace("[]", "")
            tipo = {"tipo": "array", "subtipo": tipo_base}

        scope[nombre] = Simbolo(nombre, tipo, valor)

    def tipos_compatibles(self, t1, t2):
        return t1 == t2

    def visitArrayAccess(self, ctx):
        nombre = ctx.ID().getText()
        simbolo = self.buscar(nombre)

        if not simbolo:
            raise Exception("[ERROR] Array no declarado")

        if simbolo.tipo != "array":
            raise Exception("[ERROR] No es un array")

        index_tipo = self.visit(ctx.expr())

        if index_tipo != "int":
            raise Exception("[ERROR] Índice debe ser int")

        return "int"
    
    def imprimir_tabla(self):
        print("\n===== TABLA DE SÍMBOLOS =====")

        nivel = 0
        for scope in self.pila:
            print(f"\nScope {nivel}:")
            if not scope:
                print("  (vacío)")
            for nombre, simbolo in scope.items():
                tipo = simbolo.tipo
                if isinstance(tipo, dict):
                    tipo = f"array[{tipo.get('subtipo')}]"
                valor = simbolo.valor if simbolo.valor is not None else "(sin valor)"
                print(f"  {nombre} -> {tipo} | valor: {valor}")
            nivel += 1
    # def declarar(self, nombre):
    #     scope = self.pila[-1]
    #     if nombre in scope:
    #         raise Exception(f"[ERROR SEMÁNTICO] Variable '{nombre}' ya declarada")
    #     scope[nombre] = True
    def buscar(self, nombre):
        for scope in reversed(self.pila):
            if nombre in scope:
                return scope[nombre]
        return None

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
        tipo = ctx.tipo().getText()

        if ctx.LBRACKET():
            self.declarar(nombre, f"{tipo}[]")
            return

        self.declarar(nombre, tipo)

        if ctx.expr():
            expr_tipo = self.visit(ctx.expr())
            if expr_tipo is None:
                expr_tipo = tipo

            if expr_tipo != tipo:
                self.errores.append(f"[ERROR SEMÁNTICO] Tipo incompatible en '{nombre}'")
   
   
    # def visitDeclaracion(self, ctx):
    #     nombre = ctx.ID().getText()
    #     self.declarar(nombre)
    #     if ctx.expr():
    #         self.visit(ctx.expr())

    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        exprs = ctx.expr()

        simbolo = self.buscar(nombre)
        if not simbolo:
            self.errores.append(f"[ERROR SEMÁNTICO] Variable '{nombre}' no declarada")
            return None

        if ctx.LBRACKET():
            index_tipo = self.visit(exprs[0]) if len(exprs) > 0 else None
            valor_tipo = self.visit(exprs[1]) if len(exprs) > 1 else None

            if not isinstance(simbolo.tipo, dict) or simbolo.tipo.get("tipo") != "array":
                self.errores.append(f"[ERROR SEMÁNTICO] '{nombre}' no es un array")
                return None

            if index_tipo != "int":
                self.errores.append("[ERROR SEMÁNTICO] Índice debe ser int")

            if valor_tipo != simbolo.tipo.get("subtipo"):
                self.errores.append(f"[ERROR SEMÁNTICO] Asignación con tipo incorrecto en '{nombre}'")
            return valor_tipo

        expr_tipo = self.visit(exprs[-1]) if exprs else None
        if expr_tipo is None:
            return None

        if simbolo.tipo != expr_tipo:
            self.errores.append("[ERROR SEMÁNTICO] Asignación con tipo incorrecto")
        return expr_tipo
    
    def visitFactor(self, ctx):

        if ctx.NUM():
            return "int"

        if ctx.FLOAT_NUM():
            return "float"

        if ctx.STRING():
            return "string"

        if ctx.ID() and ctx.LBRACKET():
            nombre = ctx.ID().getText()

            simbolo = self.buscar(nombre)
            if not simbolo:
                self.errores.append(f"[ERROR SEMÁNTICO] Array '{nombre}' no declarado")
                return None

            if not isinstance(simbolo.tipo, dict) or simbolo.tipo.get("tipo") != "array":
                self.errores.append(f"[ERROR SEMÁNTICO] '{nombre}' no es un array")
                return None

            index_tipo = self.visit(ctx.expr())
            if index_tipo != "int":
                self.errores.append("[ERROR SEMÁNTICO] Índice debe ser int")

            return simbolo.tipo.get("subtipo")

        if ctx.ID() and ctx.getChildCount() == 1:
            nombre = ctx.ID().getText()
            simbolo = self.buscar(nombre)
            if not simbolo:
                self.errores.append(f"[ERROR SEMÁNTICO] Variable '{nombre}' no definida")
                return None
            return simbolo.tipo

        if ctx.expr():
            return self.visit(ctx.expr())

        return None

    def visitTerm(self, ctx):
        result_type = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            right = self.visit(ctx.factor(i))
            if result_type is None or right is None:
                result_type = None
                continue

            if ctx.MUL(i - 1):
                if result_type in ["int", "float"] and right in ["int", "float"]:
                    result_type = "float" if "float" in [result_type, right] else "int"
                else:
                    self.errores.append("[ERROR SEMÁNTICO] Operación '*' sólo válida para numéricos")
                    result_type = None
            elif ctx.DIV(i - 1):
                if result_type in ["int", "float"] and right in ["int", "float"]:
                    result_type = "float"
                else:
                    self.errores.append("[ERROR SEMÁNTICO] Operación '/' sólo válida para numéricos")
                    result_type = None
            elif ctx.MOD(i - 1):
                if result_type == "int" and right == "int":
                    result_type = "int"
                else:
                    self.errores.append("[ERROR SEMÁNTICO] Operación '%' sólo válida para int")
                    result_type = None
        return result_type

    def visitExpr(self, ctx):
        result_type = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            right = self.visit(ctx.term(i))
            if result_type is None or right is None:
                result_type = None
                continue

            if ctx.SUM(i - 1):
                if result_type == "string" and right == "string":
                    result_type = "string"
                elif result_type in ["int", "float"] and right in ["int", "float"]:
                    result_type = "float" if "float" in [result_type, right] else "int"
                else:
                    self.errores.append("[ERROR SEMÁNTICO] Operación '+' inválida para estos tipos")
                    result_type = None
            elif ctx.SUB(i - 1):
                if result_type in ["int", "float"] and right in ["int", "float"]:
                    result_type = "float" if "float" in [result_type, right] else "int"
                else:
                    self.errores.append("[ERROR SEMÁNTICO] Operación '-' sólo válida para numéricos")
                    result_type = None
        return result_type

    # def visitFactor(self, ctx):
    #     if ctx.ID() and ctx.getChildCount() == 1:
    #         nombre = ctx.ID().getText()
    #         if not self.existe(nombre):
    #             raise Exception(f"[ERROR SEMÁNTICO] Variable '{nombre}' no definida")
    #     return self.visitChildren(ctx)

    def visitDecFuncion(self, ctx):
        nombre = ctx.ID().getText()
        tipo_retorno = ctx.tipo().getText()

        if nombre in self.funciones:
            raise Exception(f"[ERROR SEMÁNTICO] Función '{nombre}' ya existe")

        self.funciones[nombre] = {
            "tipo": tipo_retorno,
            "ctx": ctx
        }

        self.current_function = tipo_retorno

        self.push_scope()

        # parámetros si existen
        # for param in ctx.parametros(): ...

        self.visit(ctx.bloqueInstrucciones())

        self.pop_scope()

        self.current_function = None

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
        self.in_loop += 1
        self.visit(ctx.condicion())
        self.visit(ctx.bloqueInstrucciones())
        self.in_loop -= 1

    def visitCicloFor(self, ctx):
        if ctx.asignacion(0):
            self.visit(ctx.asignacion(0))
        if ctx.condicion():
            self.visit(ctx.condicion())
        if ctx.bloqueInstrucciones():
            self.visit(ctx.bloqueInstrucciones())
        if ctx.asignacion(1):
            self.visit(ctx.asignacion(1))

    def visitBreak(self, ctx):
        if self.in_loop == 0:
            raise Exception("[ERROR SEMÁNTICO] break fuera de ciclo")
    
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
        if self.current_function is None:
            raise Exception("[ERROR SEMÁNTICO] return fuera de función")

        expr_tipo = self.visit(ctx.expr())

        if expr_tipo != self.current_function:
            raise Exception("[ERROR SEMÁNTICO] Tipo de retorno incorrecto")