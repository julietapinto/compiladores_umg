from ExpresionesVisitor import ExpresionesVisitor

class EvalVisitor(ExpresionesVisitor):

    def visitProg(self, ctx):
        return self.visitChildren(ctx)