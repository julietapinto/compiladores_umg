# Generated from Expresiones.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpresionesParser import ExpresionesParser
else:
    from ExpresionesParser import ExpresionesParser

# This class defines a complete listener for a parse tree produced by ExpresionesParser.
class ExpresionesListener(ParseTreeListener):

    # Enter a parse tree produced by ExpresionesParser#root.
    def enterRoot(self, ctx:ExpresionesParser.RootContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#root.
    def exitRoot(self, ctx:ExpresionesParser.RootContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#instrucciones.
    def enterInstrucciones(self, ctx:ExpresionesParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#instrucciones.
    def exitInstrucciones(self, ctx:ExpresionesParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#declaracion.
    def enterDeclaracion(self, ctx:ExpresionesParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#declaracion.
    def exitDeclaracion(self, ctx:ExpresionesParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#asignacion.
    def enterAsignacion(self, ctx:ExpresionesParser.AsignacionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#asignacion.
    def exitAsignacion(self, ctx:ExpresionesParser.AsignacionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#cicloWhile.
    def enterCicloWhile(self, ctx:ExpresionesParser.CicloWhileContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#cicloWhile.
    def exitCicloWhile(self, ctx:ExpresionesParser.CicloWhileContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#cicloFor.
    def enterCicloFor(self, ctx:ExpresionesParser.CicloForContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#cicloFor.
    def exitCicloFor(self, ctx:ExpresionesParser.CicloForContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#condicional.
    def enterCondicional(self, ctx:ExpresionesParser.CondicionalContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#condicional.
    def exitCondicional(self, ctx:ExpresionesParser.CondicionalContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#bloqueInstrucciones.
    def enterBloqueInstrucciones(self, ctx:ExpresionesParser.BloqueInstruccionesContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#bloqueInstrucciones.
    def exitBloqueInstrucciones(self, ctx:ExpresionesParser.BloqueInstruccionesContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#decFuncion.
    def enterDecFuncion(self, ctx:ExpresionesParser.DecFuncionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#decFuncion.
    def exitDecFuncion(self, ctx:ExpresionesParser.DecFuncionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#parametros.
    def enterParametros(self, ctx:ExpresionesParser.ParametrosContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#parametros.
    def exitParametros(self, ctx:ExpresionesParser.ParametrosContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#tipo.
    def enterTipo(self, ctx:ExpresionesParser.TipoContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#tipo.
    def exitTipo(self, ctx:ExpresionesParser.TipoContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#retorna.
    def enterRetorna(self, ctx:ExpresionesParser.RetornaContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#retorna.
    def exitRetorna(self, ctx:ExpresionesParser.RetornaContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#imprimir.
    def enterImprimir(self, ctx:ExpresionesParser.ImprimirContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#imprimir.
    def exitImprimir(self, ctx:ExpresionesParser.ImprimirContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:ExpresionesParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:ExpresionesParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#argumentos.
    def enterArgumentos(self, ctx:ExpresionesParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#argumentos.
    def exitArgumentos(self, ctx:ExpresionesParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#condicion.
    def enterCondicion(self, ctx:ExpresionesParser.CondicionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#condicion.
    def exitCondicion(self, ctx:ExpresionesParser.CondicionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#orExpr.
    def enterOrExpr(self, ctx:ExpresionesParser.OrExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#orExpr.
    def exitOrExpr(self, ctx:ExpresionesParser.OrExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#andExpr.
    def enterAndExpr(self, ctx:ExpresionesParser.AndExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#andExpr.
    def exitAndExpr(self, ctx:ExpresionesParser.AndExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#notExpr.
    def enterNotExpr(self, ctx:ExpresionesParser.NotExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#notExpr.
    def exitNotExpr(self, ctx:ExpresionesParser.NotExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#comparacion.
    def enterComparacion(self, ctx:ExpresionesParser.ComparacionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#comparacion.
    def exitComparacion(self, ctx:ExpresionesParser.ComparacionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#expr.
    def enterExpr(self, ctx:ExpresionesParser.ExprContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#expr.
    def exitExpr(self, ctx:ExpresionesParser.ExprContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#term.
    def enterTerm(self, ctx:ExpresionesParser.TermContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#term.
    def exitTerm(self, ctx:ExpresionesParser.TermContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#factor.
    def enterFactor(self, ctx:ExpresionesParser.FactorContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#factor.
    def exitFactor(self, ctx:ExpresionesParser.FactorContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#relop.
    def enterRelop(self, ctx:ExpresionesParser.RelopContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#relop.
    def exitRelop(self, ctx:ExpresionesParser.RelopContext):
        pass



del ExpresionesParser