import sys
from antlr4 import *
from antlr4.Token import CommonToken

from myListener import myListener
from gen.pyGramLexer import pyGramLexer
from gen.pyGramParser import pyGramParser

if __name__ == '__main__':
    fileName = 'input'
    data = FileStream(fileName+".py")

    #Lexer
    lexer = pyGramLexer(data)
    stream = CommonTokenStream(lexer)

    #Parser
    parser = pyGramParser(stream)
    tree = parser.prog()

    #Walker using listener
    l = myListener(fileName)
    walker = ParseTreeWalker()
    walker.walk(l, tree)