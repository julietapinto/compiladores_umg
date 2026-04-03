# Generated from Expresiones.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by ExpresionesParser#comparacion.
    def enterComparacion(self, ctx:ExpresionesParser.ComparacionContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#comparacion.
    def exitComparacion(self, ctx:ExpresionesParser.ComparacionContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#parentesis.
    def enterParentesis(self, ctx:ExpresionesParser.ParentesisContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#parentesis.
    def exitParentesis(self, ctx:ExpresionesParser.ParentesisContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#numero.
    def enterNumero(self, ctx:ExpresionesParser.NumeroContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#numero.
    def exitNumero(self, ctx:ExpresionesParser.NumeroContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#aritmetica.
    def enterAritmetica(self, ctx:ExpresionesParser.AritmeticaContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#aritmetica.
    def exitAritmetica(self, ctx:ExpresionesParser.AritmeticaContext):
        pass


    # Enter a parse tree produced by ExpresionesParser#variable.
    def enterVariable(self, ctx:ExpresionesParser.VariableContext):
        pass

    # Exit a parse tree produced by ExpresionesParser#variable.
    def exitVariable(self, ctx:ExpresionesParser.VariableContext):
        pass



del ExpresionesParser