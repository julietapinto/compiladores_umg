from antlr4 import *
from ExpresionesLexer import ExpresionesLexer

lexer = ExpresionesLexer(InputStream("3+5*21"))

for t in lexer.getAllTokens():
    print(t)