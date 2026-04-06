# Generated from Expresiones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionesParser import ExpresionesParser
else:
    from ExpresionesParser import ExpresionesParser

# This class defines a complete generic visitor for a parse tree produced by ExpresionesParser.

class ExpresionesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpresionesParser#root.
    def visitRoot(self, ctx:ExpresionesParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#instrucciones.
    def visitInstrucciones(self, ctx:ExpresionesParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#declaracion.
    def visitDeclaracion(self, ctx:ExpresionesParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#asignacion.
    def visitAsignacion(self, ctx:ExpresionesParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#cicloWhile.
    def visitCicloWhile(self, ctx:ExpresionesParser.CicloWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#cicloFor.
    def visitCicloFor(self, ctx:ExpresionesParser.CicloForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#condicional.
    def visitCondicional(self, ctx:ExpresionesParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#bloqueInstrucciones.
    def visitBloqueInstrucciones(self, ctx:ExpresionesParser.BloqueInstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#decFuncion.
    def visitDecFuncion(self, ctx:ExpresionesParser.DecFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#parametros.
    def visitParametros(self, ctx:ExpresionesParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#tipo.
    def visitTipo(self, ctx:ExpresionesParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#retorna.
    def visitRetorna(self, ctx:ExpresionesParser.RetornaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#imprimir.
    def visitImprimir(self, ctx:ExpresionesParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:ExpresionesParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#argumentos.
    def visitArgumentos(self, ctx:ExpresionesParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#condicion.
    def visitCondicion(self, ctx:ExpresionesParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#orExpr.
    def visitOrExpr(self, ctx:ExpresionesParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#andExpr.
    def visitAndExpr(self, ctx:ExpresionesParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#notExpr.
    def visitNotExpr(self, ctx:ExpresionesParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#comparacion.
    def visitComparacion(self, ctx:ExpresionesParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#expr.
    def visitExpr(self, ctx:ExpresionesParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#term.
    def visitTerm(self, ctx:ExpresionesParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#factor.
    def visitFactor(self, ctx:ExpresionesParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#relop.
    def visitRelop(self, ctx:ExpresionesParser.RelopContext):
        return self.visitChildren(ctx)



del ExpresionesParser