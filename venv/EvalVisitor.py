from ExpresionesVisitor import ExpresionesVisitor

class EvalVisitor(ExpresionesVisitor):
    def __init__(self):
        # Diccionario para guardar las variables SONTAY
        self.memoria = {}

    # Inicia el programa: EZEQUIELAQUIINICIA ... EZEQUIELAQUIFINALIZA
    def visitRoot(self, ctx):
        return self.visitChildren(ctx)

    # Declaración de variables: SONTAY x;
    def visitDeclaracion(self, ctx):
        nombre_var = ctx.ID().getText()
        if nombre_var not in self.memoria:
            self.memoria[nombre_var] = 0 # Valor inicial por defecto
        return 0

    # Asignación: x = 10;
    def visitAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expr())
        self.memoria[nombre] = valor
        return valor

    # Condicional: CHI_LO_HACE [CON ...] TONCES [] CHI_NO []
    def visitCondicional(self, ctx):
        # 1. Evaluar la condición del CHI_LO_HACE
        if self.visit(ctx.condicion()):
            return self.visit(ctx.bloqueInstrucciones(0))
        
        # 2. Evaluar el TONCES (funciona como un elif)
        elif ctx.TONCES():
            # El TONCES en tu entrada tiene [] vacío, pero se puede evaluar
            return self.visit(ctx.bloqueInstrucciones(1))
            
        # 3. Evaluar el CHI_NO (funciona como un else)
        elif ctx.CHI_NO():
            # Buscamos las instrucciones dentro del bloque CHI_NO
            for inst in ctx.instrucciones():
                self.visit(inst)
        return None

    # Condición lógica: [CON x > 3]
    def visitCondicion(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.op.text # Obtiene el operador >, <, ==, etc.
        
        if op == '>':  return izq > der
        if op == '<':  return izq < der
        if op == '==': return izq == der
        if op == '!=': return izq != der
        if op == '>=': return izq >= der
        if op == '<=': return izq <= der
        return False

    # Manejo de bloques (instrucciones simples o entre corchetes)
    def visitBloqueInstrucciones(self, ctx):
        return self.visitChildren(ctx)

    # Operaciones matemáticas (reutilizamos la lógica anterior)
    def visitAritmetica(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == '*': return izq * der
        if op == '/': return int(izq / der) if der != 0 else 0
        if op == '+': return izq + der
        if op == '-': return izq - der
        return 0

    def visitNumero(self, ctx):
        return int(ctx.NUM().getText())

    def visitVariable(self, ctx):
        nombre = ctx.ID().getText()
        if nombre in self.memoria:
            return self.memoria[nombre]
        print(f"Error: La variable '{nombre}' no ha sido declarada con SONTAY.")
        return 0