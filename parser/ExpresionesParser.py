# Generated from Expresiones.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,42,8,1,
        1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,61,8,4,1,4,1,4,3,4,65,8,4,1,5,1,5,4,5,69,8,5,11,5,12,5,70,
        1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,86,8,7,1,
        7,1,7,1,7,1,7,1,7,1,7,5,7,94,8,7,10,7,12,7,97,9,7,1,7,0,1,14,8,0,
        2,4,6,8,10,12,14,0,3,1,0,14,19,1,0,20,21,1,0,22,23,101,0,16,1,0,
        0,0,2,41,1,0,0,0,4,43,1,0,0,0,6,46,1,0,0,0,8,50,1,0,0,0,10,66,1,
        0,0,0,12,74,1,0,0,0,14,85,1,0,0,0,16,17,5,1,0,0,17,18,5,2,0,0,18,
        19,5,3,0,0,19,21,5,4,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,
        0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,5,0,0,26,27,
        5,6,0,0,27,28,5,2,0,0,28,29,5,3,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,
        32,3,4,2,0,32,33,5,7,0,0,33,42,1,0,0,0,34,35,3,6,3,0,35,36,5,7,0,
        0,36,42,1,0,0,0,37,42,3,8,4,0,38,39,3,14,7,0,39,40,5,7,0,0,40,42,
        1,0,0,0,41,31,1,0,0,0,41,34,1,0,0,0,41,37,1,0,0,0,41,38,1,0,0,0,
        42,3,1,0,0,0,43,44,5,8,0,0,44,45,5,24,0,0,45,5,1,0,0,0,46,47,5,24,
        0,0,47,48,5,9,0,0,48,49,3,14,7,0,49,7,1,0,0,0,50,51,5,10,0,0,51,
        52,5,4,0,0,52,53,5,11,0,0,53,54,3,12,6,0,54,55,5,5,0,0,55,60,3,10,
        5,0,56,57,5,12,0,0,57,58,5,4,0,0,58,59,5,5,0,0,59,61,3,10,5,0,60,
        56,1,0,0,0,60,61,1,0,0,0,61,64,1,0,0,0,62,63,5,13,0,0,63,65,3,10,
        5,0,64,62,1,0,0,0,64,65,1,0,0,0,65,9,1,0,0,0,66,68,5,4,0,0,67,69,
        3,2,1,0,68,67,1,0,0,0,69,70,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,
        71,72,1,0,0,0,72,73,5,5,0,0,73,11,1,0,0,0,74,75,3,14,7,0,75,76,7,
        0,0,0,76,77,3,14,7,0,77,13,1,0,0,0,78,79,6,7,-1,0,79,86,5,25,0,0,
        80,86,5,24,0,0,81,82,5,2,0,0,82,83,3,14,7,0,83,84,5,3,0,0,84,86,
        1,0,0,0,85,78,1,0,0,0,85,80,1,0,0,0,85,81,1,0,0,0,86,95,1,0,0,0,
        87,88,10,5,0,0,88,89,7,1,0,0,89,94,3,14,7,6,90,91,10,4,0,0,91,92,
        7,2,0,0,92,94,3,14,7,5,93,87,1,0,0,0,93,90,1,0,0,0,94,97,1,0,0,0,
        95,93,1,0,0,0,95,96,1,0,0,0,96,15,1,0,0,0,97,95,1,0,0,0,8,23,41,
        60,64,70,85,93,95
    ]

class ExpresionesParser ( Parser ):

    grammarFileName = "Expresiones.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'EZEQUIELAQUIINICIA'", "'('", "')'", 
                     "'['", "']'", "'EZEQUIELAQUIFINALIZA'", "';'", "'SONTAY'", 
                     "'='", "'CHI_LO_HACE'", "'CON'", "'TONCES'", "'CHI_NO'", 
                     "'>'", "'<'", "'=='", "'!='", "'>='", "'<='", "'*'", 
                     "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "MUL", "DIV", "SUM", "RES", "ID", "NUM", "WS", "COMMENT" ]

    RULE_root = 0
    RULE_instrucciones = 1
    RULE_declaracion = 2
    RULE_asignacion = 3
    RULE_condicional = 4
    RULE_bloqueInstrucciones = 5
    RULE_condicion = 6
    RULE_expr = 7

    ruleNames =  [ "root", "instrucciones", "declaracion", "asignacion", 
                   "condicional", "bloqueInstrucciones", "condicion", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    MUL=20
    DIV=21
    SUM=22
    RES=23
    ID=24
    NUM=25
    WS=26
    COMMENT=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExpresionesParser.EOF, 0)

        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.InstruccionesContext,i)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExpresionesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(ExpresionesParser.T__0)
            self.state = 17
            self.match(ExpresionesParser.T__1)
            self.state = 18
            self.match(ExpresionesParser.T__2)
            self.state = 19
            self.match(ExpresionesParser.T__3)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.instrucciones()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 50332932) != 0)):
                    break

            self.state = 25
            self.match(ExpresionesParser.T__4)
            self.state = 26
            self.match(ExpresionesParser.T__5)
            self.state = 27
            self.match(ExpresionesParser.T__1)
            self.state = 28
            self.match(ExpresionesParser.T__2)
            self.state = 29
            self.match(ExpresionesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(ExpresionesParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(ExpresionesParser.AsignacionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(ExpresionesParser.CondicionalContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = ExpresionesParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.declaracion()
                self.state = 32
                self.match(ExpresionesParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.asignacion()
                self.state = 35
                self.match(ExpresionesParser.T__6)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.condicional()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.expr(0)
                self.state = 39
                self.match(ExpresionesParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExpresionesParser.ID, 0)

        def getRuleIndex(self):
            return ExpresionesParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = ExpresionesParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ExpresionesParser.T__7)
            self.state = 44
            self.match(ExpresionesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExpresionesParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = ExpresionesParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ExpresionesParser.ID)
            self.state = 47
            self.match(ExpresionesParser.T__8)
            self.state = 48
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicion(self):
            return self.getTypedRuleContext(ExpresionesParser.CondicionContext,0)


        def bloqueInstrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.BloqueInstruccionesContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.BloqueInstruccionesContext,i)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = ExpresionesParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ExpresionesParser.T__9)
            self.state = 51
            self.match(ExpresionesParser.T__3)
            self.state = 52
            self.match(ExpresionesParser.T__10)
            self.state = 53
            self.condicion()
            self.state = 54
            self.match(ExpresionesParser.T__4)
            self.state = 55
            self.bloqueInstrucciones()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 56
                self.match(ExpresionesParser.T__11)
                self.state = 57
                self.match(ExpresionesParser.T__3)
                self.state = 58
                self.match(ExpresionesParser.T__4)
                self.state = 59
                self.bloqueInstrucciones()


            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 62
                self.match(ExpresionesParser.T__12)
                self.state = 63
                self.bloqueInstrucciones()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueInstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.InstruccionesContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.InstruccionesContext,i)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_bloqueInstrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloqueInstrucciones" ):
                listener.enterBloqueInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloqueInstrucciones" ):
                listener.exitBloqueInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloqueInstrucciones" ):
                return visitor.visitBloqueInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def bloqueInstrucciones(self):

        localctx = ExpresionesParser.BloqueInstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bloqueInstrucciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ExpresionesParser.T__3)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.instrucciones()
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 50332932) != 0)):
                    break

            self.state = 72
            self.match(ExpresionesParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpresionesParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComparacionContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.CondicionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparacion" ):
                listener.enterComparacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparacion" ):
                listener.exitComparacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparacion" ):
                return visitor.visitComparacion(self)
            else:
                return visitor.visitChildren(self)



    def condicion(self):

        localctx = ExpresionesParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            localctx = ExpresionesParser.ComparacionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.expr(0)
            self.state = 75
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1032192) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 76
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpresionesParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParentesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExpresionesParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class NumeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExpresionesParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumero" ):
                return visitor.visitNumero(self)
            else:
                return visitor.visitChildren(self)


    class AritmeticaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpresionesParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExpresionesParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ExpresionesParser.MUL, 0)
        def DIV(self):
            return self.getToken(ExpresionesParser.DIV, 0)
        def SUM(self):
            return self.getToken(ExpresionesParser.SUM, 0)
        def RES(self):
            return self.getToken(ExpresionesParser.RES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAritmetica" ):
                listener.enterAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAritmetica" ):
                listener.exitAritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAritmetica" ):
                return visitor.visitAritmetica(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpresionesParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExpresionesParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpresionesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = ExpresionesParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 79
                self.match(ExpresionesParser.NUM)
                pass
            elif token in [24]:
                localctx = ExpresionesParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(ExpresionesParser.ID)
                pass
            elif token in [2]:
                localctx = ExpresionesParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(ExpresionesParser.T__1)
                self.state = 82
                self.expr(0)
                self.state = 83
                self.match(ExpresionesParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 93
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ExpresionesParser.AritmeticaContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 87
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 88
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExpresionesParser.AritmeticaContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 91
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 92
                        self.expr(5)
                        pass

             
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




