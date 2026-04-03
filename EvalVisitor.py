from parser.ExpresionesVisitor import ExpresionesVisitor

class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        # Tabla de símbolos (Memoria del compilador)
        self.memoria = {}

    # --- ENTRADAS AL PROGRAMA ---
    def visitRoot(self, ctx):
        return self.visitChildren(ctx)

    # --- DECLARACIONES Y ASIGNACIONES ---
    def visitDeclaracion(self, ctx):
        nombre_var = ctx.ID().getText()
        if nombre_var not in self.memoria:
            self.memoria[nombre_var] = 0
        return 0

    def visitAsignacion(self, ctx):
        nombre_var = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        self.memoria[nombre_var] = valor
        return valor

    # --- LÓGICA DE CONDICIONALES ---
    # Nota: Ahora 'condicional' usa 'expr' directamente en lugar de 'condicion'
    def visitCondicional(self, ctx):
        # Evaluamos la expresión dentro de [CON ...]
        cumple = self.visit(ctx.expr()) 
        
        if cumple:
            return self.visit(ctx.bloqueInstrucciones())
        # Si tiene el bloque CHI_NO (el else)
        elif ctx.instructions(): # Verifica si hay instrucciones en el bloque opcional
             # Como el CHI_NO es opcional en tu g4: ( 'CHI_NO' '[' instrucciones* ']' )?
             # Buscamos ejecutar ese bloque si el if falló.
             return self.visitChildren(ctx) 
        return 0

    # --- NUEVOS OPERADORES (Basados en las etiquetas # de la g4) ---

    def visitComparacion(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        if op == '>':  return izq > der
        if op == '<':  return izq < der
        if op == '==': return izq == der
        if op == '!=': return izq != der
        if op == '>=': return izq >= der
        if op == '<=': return izq <= der
        return False

    def visitLogicaAnd(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        return bool(izq) and bool(der)

    def visitLogicaOr(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        return bool(izq) or bool(der)

    def visitLogicaNot(self, ctx):
        valor = self.visit(ctx.expr())
        return not bool(valor)

    def visitPotencia(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        return izq ** der

    # --- OPERACIONES MATEMÁTICAS ---
    def visitAritmetica(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText() 

        if op == '+': return izq + der
        if op == '-': return izq - der
        if op == '*': return izq * der
        if op == '/': return izq / der if der != 0 else 0
        return 0

    def visitNumero(self, ctx):
        return int(ctx.NUM().getText())

    def visitVariable(self, ctx):
        nombre_var = ctx.ID().getText()
        return self.memoria.get(nombre_var, 0)

    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())

    def visitBloqueInstrucciones(self, ctx):
        return self.visitChildren(ctx)