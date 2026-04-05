# Generated from Expresiones.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by ExpresionesParser#tipo.
    def visitTipo(self, ctx:ExpresionesParser.TipoContext):
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


    # Visit a parse tree produced by ExpresionesParser#texto.
    def visitTexto(self, ctx:ExpresionesParser.TextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#parentesis.
    def visitParentesis(self, ctx:ExpresionesParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#numero.
    def visitNumero(self, ctx:ExpresionesParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#logico.
    def visitLogico(self, ctx:ExpresionesParser.LogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#aritmetica.
    def visitAritmetica(self, ctx:ExpresionesParser.AritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#variable.
    def visitVariable(self, ctx:ExpresionesParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#decimal.
    def visitDecimal(self, ctx:ExpresionesParser.DecimalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpresionesParser#relop.
    def visitRelop(self, ctx:ExpresionesParser.RelopContext):
        return self.visitChildren(ctx)



del ExpresionesParser