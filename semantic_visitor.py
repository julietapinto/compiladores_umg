from parser.gramatica_v4Visitor import gramatica_v4Visitor
from Simbolo import Simbolo
from symbol_table import SymbolTable


class SemanticVisitor(gramatica_v4Visitor):
    def __init__(self):
        self.tabla = SymbolTable()
        self.funciones = {}
        self.current_function = None
        self.in_loop = 0
        self.in_switch = 0
        self.errores = []

    # ------------------------
    # UTILIDADES
    # ------------------------
    def get_text(self, node):
        if node is None:
            return ""

        if isinstance(node, list):
            if len(node) == 0:
                return ""
            return node[0].getText()

        if hasattr(node, "getText"):
            return node.getText()

        return str(node)

    def push_scope(self):
        self.tabla.push_scope()

    def pop_scope(self):
        self.tabla.pop_scope()

    def buscar(self, nombre):
        for scope in reversed(self.tabla.pila):
            if nombre in scope:
                return scope[nombre]
        return None

    def existe(self, nombre):
        return self.buscar(nombre) is not None

    def declarar(self, nombre, tipo, valor=None):
        if nombre in self.tabla.pila[-1]:
            self.errores.append(f"[ERROR SEMÁNTICO] Variable '{nombre}' ya declarada")
            return

        if "[]" in tipo:
            tipo_base = tipo.replace("[]", "")
            tipo = {"tipo": "array", "subtipo": tipo_base}

        self.tabla.pila[-1][nombre] = Simbolo(nombre, tipo, valor)

    # ------------------------
    # ROOT
    # ------------------------
    def visitRoot(self, ctx):
        for ins in ctx.instrucciones():
            self.visit(ins)

    # ------------------------
    # DECLARACIÓN
    # ------------------------
    def visitDeclaracion(self, ctx):
        nombre = self.get_text(ctx.ID(0))
        tipo = self.get_text(ctx.tipo()) if ctx.tipo() else "int"

        if ctx.LBRACKET():
            self.declarar(nombre, f"{tipo}[]")
        else:
            self.declarar(nombre, tipo)

        if ctx.ternario():
            expr_tipo = self.visit(ctx.ternario())
            if expr_tipo and expr_tipo != tipo:
                self.errores.append(
                    f"[ERROR SEMÁNTICO] Tipo incompatible en '{nombre}'"
                )

    # ------------------------
    # ASIGNACIÓN
    # ------------------------
    def visitAsignacion(self, ctx):
        nombre = self.get_text(ctx.ID())

        simbolo = self.buscar(nombre)
        if not simbolo:
            self.errores.append(f"[ERROR SEMÁNTICO] Variable '{nombre}' no declarada")
            return None

        # ARRAY
        if ctx.LBRACKET():
            index_tipo = self.visit(ctx.expr()) if ctx.expr() else None
            valor_tipo = self.visit(ctx.ternario())

            if not isinstance(simbolo.tipo, dict):
                self.errores.append(f"[ERROR SEMÁNTICO] '{nombre}' no es un array")
                return None

            if index_tipo != "int":
                self.errores.append("[ERROR SEMÁNTICO] Índice debe ser int")

            if valor_tipo != simbolo.tipo.get("subtipo"):
                self.errores.append(
                    f"[ERROR SEMÁNTICO] Tipo incorrecto en asignación de '{nombre}'"
                )

            return valor_tipo

        # NORMAL
        valor_tipo = self.visit(ctx.ternario())

        if simbolo.tipo != valor_tipo:
            self.errores.append("[ERROR SEMÁNTICO] Asignación con tipo incorrecto")

        return valor_tipo

    # ------------------------
    # FACTOR
    # ------------------------
    def visitFactor(self, ctx):
        if ctx.NUM():
            return "int"

        if ctx.FLOAT_NUM():
            return "float"

        if ctx.STRING():
            return "string"

        # ARRAY ACCESS
        if ctx.ID() and ctx.LBRACKET():
            nombre = self.get_text(ctx.ID())
            simbolo = self.buscar(nombre)

            if not simbolo:
                self.errores.append(f"[ERROR] Array '{nombre}' no declarado")
                return None

            index_tipo = self.visit(ctx.expr())
            if index_tipo != "int":
                self.errores.append("[ERROR] Índice debe ser int")

            if isinstance(simbolo.tipo, dict):
                return simbolo.tipo.get("subtipo")

            return None

        # VARIABLE
        if ctx.ID():
            nombre = self.get_text(ctx.ID())
            simbolo = self.buscar(nombre)

            if not simbolo:
                self.errores.append(f"[ERROR] Variable '{nombre}' no definida")
                return None

            return simbolo.tipo

        # EXPRESIÓN
        if ctx.expr():
            return self.visit(ctx.expr())

        return None

    # ------------------------
    # EXPRESSIONS
    # ------------------------
    def visitTerm(self, ctx):
        elementos = ctx.castExpr()
        result = self.visit(elementos[0])

        for i in range(1, len(elementos)):
            right = self.visit(elementos[i])

            if result is None or right is None:
                result = None
                continue

            if ctx.MUL(i - 1):
                if result in ["int", "float"] and right in ["int", "float"]:
                    result = "float" if "float" in [result, right] else "int"
                else:
                    self.errores.append("Error en *")
                    result = None

        return result

    def visitExpr(self, ctx):
        return self.visit(ctx.comparacionExpr())

    # ------------------------
    # IMPRIMIR (CORREGIDO)
    # ------------------------
    def visitImprimir(self, ctx):
        if ctx.ternario():
            return self.visit(ctx.ternario())
        return None

    # ------------------------
    # RETURN
    # ------------------------
    def visitRetorna(self, ctx):
        if self.current_function is None:
            raise Exception("return fuera de función")

        expr_tipo = self.visit(ctx.ternario())

        if expr_tipo != self.current_function:
            raise Exception("tipo de retorno incorrecto")

    # ------------------------
    # TABLA DE SÍMBOLOS
    # ------------------------
    def imprimir_tabla(self):
        print("\n===== TABLA DE SÍMBOLOS =====")

        for i, scope in enumerate(self.tabla.pila):
            print(f"\nScope {i}:")
            if not scope:
                print("  (vacío)")
            for nombre, simbolo in scope.items():
                tipo = simbolo.tipo
                if isinstance(tipo, dict):
                    tipo = f"array[{tipo.get('subtipo')}]"
                print(f"  {nombre} -> {tipo}")
