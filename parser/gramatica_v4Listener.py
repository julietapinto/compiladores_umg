# Generated from gramatica_v4.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatica_v4Parser import gramatica_v4Parser
else:
    from gramatica_v4Parser import gramatica_v4Parser

# This class defines a complete listener for a parse tree produced by gramatica_v4Parser.
class gramatica_v4Listener(ParseTreeListener):

    # Enter a parse tree produced by gramatica_v4Parser#root.
    def enterRoot(self, ctx:gramatica_v4Parser.RootContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#root.
    def exitRoot(self, ctx:gramatica_v4Parser.RootContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#instrucciones.
    def enterInstrucciones(self, ctx:gramatica_v4Parser.InstruccionesContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#instrucciones.
    def exitInstrucciones(self, ctx:gramatica_v4Parser.InstruccionesContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#declaracion.
    def enterDeclaracion(self, ctx:gramatica_v4Parser.DeclaracionContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#declaracion.
    def exitDeclaracion(self, ctx:gramatica_v4Parser.DeclaracionContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#asignacion.
    def enterAsignacion(self, ctx:gramatica_v4Parser.AsignacionContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#asignacion.
    def exitAsignacion(self, ctx:gramatica_v4Parser.AsignacionContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#cicloWhile.
    def enterCicloWhile(self, ctx:gramatica_v4Parser.CicloWhileContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#cicloWhile.
    def exitCicloWhile(self, ctx:gramatica_v4Parser.CicloWhileContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#cicloFor.
    def enterCicloFor(self, ctx:gramatica_v4Parser.CicloForContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#cicloFor.
    def exitCicloFor(self, ctx:gramatica_v4Parser.CicloForContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#condicional.
    def enterCondicional(self, ctx:gramatica_v4Parser.CondicionalContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#condicional.
    def exitCondicional(self, ctx:gramatica_v4Parser.CondicionalContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#bloqueInstrucciones.
    def enterBloqueInstrucciones(self, ctx:gramatica_v4Parser.BloqueInstruccionesContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#bloqueInstrucciones.
    def exitBloqueInstrucciones(self, ctx:gramatica_v4Parser.BloqueInstruccionesContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#switchStmt.
    def enterSwitchStmt(self, ctx:gramatica_v4Parser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#switchStmt.
    def exitSwitchStmt(self, ctx:gramatica_v4Parser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#caseStmt.
    def enterCaseStmt(self, ctx:gramatica_v4Parser.CaseStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#caseStmt.
    def exitCaseStmt(self, ctx:gramatica_v4Parser.CaseStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#defaultStmt.
    def enterDefaultStmt(self, ctx:gramatica_v4Parser.DefaultStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#defaultStmt.
    def exitDefaultStmt(self, ctx:gramatica_v4Parser.DefaultStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#decStruct.
    def enterDecStruct(self, ctx:gramatica_v4Parser.DecStructContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#decStruct.
    def exitDecStruct(self, ctx:gramatica_v4Parser.DecStructContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#campoStruct.
    def enterCampoStruct(self, ctx:gramatica_v4Parser.CampoStructContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#campoStruct.
    def exitCampoStruct(self, ctx:gramatica_v4Parser.CampoStructContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#decFuncion.
    def enterDecFuncion(self, ctx:gramatica_v4Parser.DecFuncionContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#decFuncion.
    def exitDecFuncion(self, ctx:gramatica_v4Parser.DecFuncionContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#parametros.
    def enterParametros(self, ctx:gramatica_v4Parser.ParametrosContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#parametros.
    def exitParametros(self, ctx:gramatica_v4Parser.ParametrosContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#tipo.
    def enterTipo(self, ctx:gramatica_v4Parser.TipoContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#tipo.
    def exitTipo(self, ctx:gramatica_v4Parser.TipoContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#retorna.
    def enterRetorna(self, ctx:gramatica_v4Parser.RetornaContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#retorna.
    def exitRetorna(self, ctx:gramatica_v4Parser.RetornaContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#imprimir.
    def enterImprimir(self, ctx:gramatica_v4Parser.ImprimirContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#imprimir.
    def exitImprimir(self, ctx:gramatica_v4Parser.ImprimirContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#importStmt.
    def enterImportStmt(self, ctx:gramatica_v4Parser.ImportStmtContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#importStmt.
    def exitImportStmt(self, ctx:gramatica_v4Parser.ImportStmtContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:gramatica_v4Parser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:gramatica_v4Parser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#argumentos.
    def enterArgumentos(self, ctx:gramatica_v4Parser.ArgumentosContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#argumentos.
    def exitArgumentos(self, ctx:gramatica_v4Parser.ArgumentosContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#condicion.
    def enterCondicion(self, ctx:gramatica_v4Parser.CondicionContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#condicion.
    def exitCondicion(self, ctx:gramatica_v4Parser.CondicionContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#orExpr.
    def enterOrExpr(self, ctx:gramatica_v4Parser.OrExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#orExpr.
    def exitOrExpr(self, ctx:gramatica_v4Parser.OrExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#andExpr.
    def enterAndExpr(self, ctx:gramatica_v4Parser.AndExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#andExpr.
    def exitAndExpr(self, ctx:gramatica_v4Parser.AndExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#notExpr.
    def enterNotExpr(self, ctx:gramatica_v4Parser.NotExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#notExpr.
    def exitNotExpr(self, ctx:gramatica_v4Parser.NotExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#comparacion.
    def enterComparacion(self, ctx:gramatica_v4Parser.ComparacionContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#comparacion.
    def exitComparacion(self, ctx:gramatica_v4Parser.ComparacionContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#ternario.
    def enterTernario(self, ctx:gramatica_v4Parser.TernarioContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#ternario.
    def exitTernario(self, ctx:gramatica_v4Parser.TernarioContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#expr.
    def enterExpr(self, ctx:gramatica_v4Parser.ExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#expr.
    def exitExpr(self, ctx:gramatica_v4Parser.ExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#comparacionExpr.
    def enterComparacionExpr(self, ctx:gramatica_v4Parser.ComparacionExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#comparacionExpr.
    def exitComparacionExpr(self, ctx:gramatica_v4Parser.ComparacionExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#sumaExpr.
    def enterSumaExpr(self, ctx:gramatica_v4Parser.SumaExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#sumaExpr.
    def exitSumaExpr(self, ctx:gramatica_v4Parser.SumaExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#term.
    def enterTerm(self, ctx:gramatica_v4Parser.TermContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#term.
    def exitTerm(self, ctx:gramatica_v4Parser.TermContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#castExpr.
    def enterCastExpr(self, ctx:gramatica_v4Parser.CastExprContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#castExpr.
    def exitCastExpr(self, ctx:gramatica_v4Parser.CastExprContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#factor.
    def enterFactor(self, ctx:gramatica_v4Parser.FactorContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#factor.
    def exitFactor(self, ctx:gramatica_v4Parser.FactorContext):
        pass


    # Enter a parse tree produced by gramatica_v4Parser#relop.
    def enterRelop(self, ctx:gramatica_v4Parser.RelopContext):
        pass

    # Exit a parse tree produced by gramatica_v4Parser#relop.
    def exitRelop(self, ctx:gramatica_v4Parser.RelopContext):
        pass



del gramatica_v4Parser