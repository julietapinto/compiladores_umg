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
        4,1,29,109,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,0,4,0,24,8,0,11,0,12,0,25,1,
        0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,45,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,3,4,64,8,4,1,4,1,4,3,4,68,8,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,4,6,79,8,6,11,6,12,6,80,1,6,1,6,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,96,8,8,1,8,1,8,1,8,1,8,1,8,1,8,
        5,8,104,8,8,10,8,12,8,107,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,
        0,3,1,0,13,18,1,0,19,20,1,0,21,22,111,0,18,1,0,0,0,2,44,1,0,0,0,
        4,46,1,0,0,0,6,49,1,0,0,0,8,53,1,0,0,0,10,69,1,0,0,0,12,76,1,0,0,
        0,14,84,1,0,0,0,16,95,1,0,0,0,18,19,5,1,0,0,19,20,5,2,0,0,20,21,
        5,3,0,0,21,23,5,4,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,
        25,23,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,5,0,0,28,29,5,
        6,0,0,29,30,5,2,0,0,30,31,5,3,0,0,31,32,5,0,0,1,32,1,1,0,0,0,33,
        34,3,4,2,0,34,35,5,7,0,0,35,45,1,0,0,0,36,37,3,6,3,0,37,38,5,7,0,
        0,38,45,1,0,0,0,39,45,3,8,4,0,40,45,3,10,5,0,41,42,3,16,8,0,42,43,
        5,7,0,0,43,45,1,0,0,0,44,33,1,0,0,0,44,36,1,0,0,0,44,39,1,0,0,0,
        44,40,1,0,0,0,44,41,1,0,0,0,45,3,1,0,0,0,46,47,5,8,0,0,47,48,5,26,
        0,0,48,5,1,0,0,0,49,50,5,26,0,0,50,51,5,9,0,0,51,52,3,16,8,0,52,
        7,1,0,0,0,53,54,5,10,0,0,54,55,5,4,0,0,55,56,5,25,0,0,56,57,3,14,
        7,0,57,58,5,5,0,0,58,63,3,12,6,0,59,60,5,11,0,0,60,61,5,4,0,0,61,
        62,5,5,0,0,62,64,3,12,6,0,63,59,1,0,0,0,63,64,1,0,0,0,64,67,1,0,
        0,0,65,66,5,12,0,0,66,68,3,12,6,0,67,65,1,0,0,0,67,68,1,0,0,0,68,
        9,1,0,0,0,69,70,5,23,0,0,70,71,5,4,0,0,71,72,5,25,0,0,72,73,3,14,
        7,0,73,74,5,5,0,0,74,75,3,12,6,0,75,11,1,0,0,0,76,78,5,4,0,0,77,
        79,3,2,1,0,78,77,1,0,0,0,79,80,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,
        0,81,82,1,0,0,0,82,83,5,5,0,0,83,13,1,0,0,0,84,85,3,16,8,0,85,86,
        7,0,0,0,86,87,3,16,8,0,87,15,1,0,0,0,88,89,6,8,-1,0,89,96,5,27,0,
        0,90,96,5,26,0,0,91,92,5,2,0,0,92,93,3,16,8,0,93,94,5,3,0,0,94,96,
        1,0,0,0,95,88,1,0,0,0,95,90,1,0,0,0,95,91,1,0,0,0,96,105,1,0,0,0,
        97,98,10,5,0,0,98,99,7,1,0,0,99,104,3,16,8,6,100,101,10,4,0,0,101,
        102,7,2,0,0,102,104,3,16,8,5,103,97,1,0,0,0,103,100,1,0,0,0,104,
        107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,17,1,0,0,0,107,105,
        1,0,0,0,8,25,44,63,67,80,95,103,105
    ]

class ExpresionesParser ( Parser ):

    grammarFileName = "Expresiones.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'EZEQUIELAQUIINICIA'", "'('", "')'", 
                     "'['", "']'", "'EZEQUIELAQUIFINALIZA'", "';'", "'SONTAY'", 
                     "'='", "'CHI_LO_HACE'", "'TONCES'", "'CHI_NO'", "'>'", 
                     "'<'", "'=='", "'!='", "'>='", "'<='", "'*'", "'/'", 
                     "'+'", "'-'", "'MIENTRAS'", "'PARA'", "'CON'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "SUM", "RES", "MIENTRAS", "PARA", "CON", "ID", "NUM", 
                      "WS", "COMMENT" ]

    RULE_root = 0
    RULE_instrucciones = 1
    RULE_declaracion = 2
    RULE_asignacion = 3
    RULE_condicional = 4
    RULE_cicloWhile = 5
    RULE_bloqueInstrucciones = 6
    RULE_condicion = 7
    RULE_expr = 8

    ruleNames =  [ "root", "instrucciones", "declaracion", "asignacion", 
                   "condicional", "cicloWhile", "bloqueInstrucciones", "condicion", 
                   "expr" ]

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
    MUL=19
    DIV=20
    SUM=21
    RES=22
    MIENTRAS=23
    PARA=24
    CON=25
    ID=26
    NUM=27
    WS=28
    COMMENT=29

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




    def root(self):

        localctx = ExpresionesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(ExpresionesParser.T__0)
            self.state = 19
            self.match(ExpresionesParser.T__1)
            self.state = 20
            self.match(ExpresionesParser.T__2)
            self.state = 21
            self.match(ExpresionesParser.T__3)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.instrucciones()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 209716484) != 0)):
                    break

            self.state = 27
            self.match(ExpresionesParser.T__4)
            self.state = 28
            self.match(ExpresionesParser.T__5)
            self.state = 29
            self.match(ExpresionesParser.T__1)
            self.state = 30
            self.match(ExpresionesParser.T__2)
            self.state = 31
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


        def cicloWhile(self):
            return self.getTypedRuleContext(ExpresionesParser.CicloWhileContext,0)


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




    def instrucciones(self):

        localctx = ExpresionesParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.declaracion()
                self.state = 34
                self.match(ExpresionesParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.asignacion()
                self.state = 37
                self.match(ExpresionesParser.T__6)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.condicional()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.cicloWhile()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.expr(0)
                self.state = 42
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




    def declaracion(self):

        localctx = ExpresionesParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ExpresionesParser.T__7)
            self.state = 47
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




    def asignacion(self):

        localctx = ExpresionesParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(ExpresionesParser.ID)
            self.state = 50
            self.match(ExpresionesParser.T__8)
            self.state = 51
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

        def CON(self):
            return self.getToken(ExpresionesParser.CON, 0)

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




    def condicional(self):

        localctx = ExpresionesParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ExpresionesParser.T__9)
            self.state = 54
            self.match(ExpresionesParser.T__3)
            self.state = 55
            self.match(ExpresionesParser.CON)
            self.state = 56
            self.condicion()
            self.state = 57
            self.match(ExpresionesParser.T__4)
            self.state = 58
            self.bloqueInstrucciones()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 59
                self.match(ExpresionesParser.T__10)
                self.state = 60
                self.match(ExpresionesParser.T__3)
                self.state = 61
                self.match(ExpresionesParser.T__4)
                self.state = 62
                self.bloqueInstrucciones()


            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 65
                self.match(ExpresionesParser.T__11)
                self.state = 66
                self.bloqueInstrucciones()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloWhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(ExpresionesParser.MIENTRAS, 0)

        def CON(self):
            return self.getToken(ExpresionesParser.CON, 0)

        def condicion(self):
            return self.getTypedRuleContext(ExpresionesParser.CondicionContext,0)


        def bloqueInstrucciones(self):
            return self.getTypedRuleContext(ExpresionesParser.BloqueInstruccionesContext,0)


        def getRuleIndex(self):
            return ExpresionesParser.RULE_cicloWhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCicloWhile" ):
                listener.enterCicloWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCicloWhile" ):
                listener.exitCicloWhile(self)




    def cicloWhile(self):

        localctx = ExpresionesParser.CicloWhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cicloWhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ExpresionesParser.MIENTRAS)
            self.state = 70
            self.match(ExpresionesParser.T__3)
            self.state = 71
            self.match(ExpresionesParser.CON)
            self.state = 72
            self.condicion()
            self.state = 73
            self.match(ExpresionesParser.T__4)
            self.state = 74
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




    def bloqueInstrucciones(self):

        localctx = ExpresionesParser.BloqueInstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bloqueInstrucciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(ExpresionesParser.T__3)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.instrucciones()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 209716484) != 0)):
                    break

            self.state = 82
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



    def condicion(self):

        localctx = ExpresionesParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            localctx = ExpresionesParser.ComparacionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.expr(0)
            self.state = 85
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 86
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpresionesParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = ExpresionesParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 89
                self.match(ExpresionesParser.NUM)
                pass
            elif token in [26]:
                localctx = ExpresionesParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.match(ExpresionesParser.ID)
                pass
            elif token in [2]:
                localctx = ExpresionesParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.match(ExpresionesParser.T__1)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(ExpresionesParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 103
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ExpresionesParser.AritmeticaContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 98
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 99
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExpresionesParser.AritmeticaContext(self, ExpresionesParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 101
                        _la = self._input.LA(1)
                        if not(_la==21 or _la==22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        self.expr(5)
                        pass

             
                self.state = 107
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
        self._predicates[8] = self.expr_sempred
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
         




