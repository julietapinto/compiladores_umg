# Generated from gramatica_v4.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramatica_v4Parser import gramatica_v4Parser
else:
    from gramatica_v4Parser import gramatica_v4Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v4Parser.

class gramatica_v4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v4Parser#root.
    def visitRoot(self, ctx:gramatica_v4Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#instrucciones.
    def visitInstrucciones(self, ctx:gramatica_v4Parser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#declaracion.
    def visitDeclaracion(self, ctx:gramatica_v4Parser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#asignacion.
    def visitAsignacion(self, ctx:gramatica_v4Parser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#cicloWhile.
    def visitCicloWhile(self, ctx:gramatica_v4Parser.CicloWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#cicloFor.
    def visitCicloFor(self, ctx:gramatica_v4Parser.CicloForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#condicional.
    def visitCondicional(self, ctx:gramatica_v4Parser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#bloqueInstrucciones.
    def visitBloqueInstrucciones(self, ctx:gramatica_v4Parser.BloqueInstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#switchStmt.
    def visitSwitchStmt(self, ctx:gramatica_v4Parser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#caseStmt.
    def visitCaseStmt(self, ctx:gramatica_v4Parser.CaseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#defaultStmt.
    def visitDefaultStmt(self, ctx:gramatica_v4Parser.DefaultStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#decStruct.
    def visitDecStruct(self, ctx:gramatica_v4Parser.DecStructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#campoStruct.
    def visitCampoStruct(self, ctx:gramatica_v4Parser.CampoStructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#decFuncion.
    def visitDecFuncion(self, ctx:gramatica_v4Parser.DecFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#parametros.
    def visitParametros(self, ctx:gramatica_v4Parser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#tipo.
    def visitTipo(self, ctx:gramatica_v4Parser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#retorna.
    def visitRetorna(self, ctx:gramatica_v4Parser.RetornaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#imprimir.
    def visitImprimir(self, ctx:gramatica_v4Parser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#importStmt.
    def visitImportStmt(self, ctx:gramatica_v4Parser.ImportStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:gramatica_v4Parser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#argumentos.
    def visitArgumentos(self, ctx:gramatica_v4Parser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#condicion.
    def visitCondicion(self, ctx:gramatica_v4Parser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#orExpr.
    def visitOrExpr(self, ctx:gramatica_v4Parser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#andExpr.
    def visitAndExpr(self, ctx:gramatica_v4Parser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#notExpr.
    def visitNotExpr(self, ctx:gramatica_v4Parser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#comparacion.
    def visitComparacion(self, ctx:gramatica_v4Parser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ternario.
    def visitTernario(self, ctx:gramatica_v4Parser.TernarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#expr.
    def visitExpr(self, ctx:gramatica_v4Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#term.
    def visitTerm(self, ctx:gramatica_v4Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#castExpr.
    def visitCastExpr(self, ctx:gramatica_v4Parser.CastExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#factor.
    def visitFactor(self, ctx:gramatica_v4Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#relop.
    def visitRelop(self, ctx:gramatica_v4Parser.RelopContext):
        return self.visitChildren(ctx)



del gramatica_v4Parser