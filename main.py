import os

from antlr4 import *

from gen.pyGramLexer import pyGramLexer
from gen.pyGramParser import pyGramParser
from CustomListener import CustomListener

if __name__ == '__main__':
    # TODO : receber arquivo por argumento
    fileName = 'input'
    data = FileStream(fileName + ".py")

    # Lexer
    lexer = pyGramLexer(data)
    stream = CommonTokenStream(lexer)

    # Parser
    parser = pyGramParser(stream)
    tree = parser.program()

    # Walker using listener
    l = CustomListener(fileName)
    walker = ParseTreeWalker()
    walker.walk(l, tree)

    # Autoexecute
    os.system('java -jar jasmin.jar {}'.format(fileName + '.j'))
    os.system('java {}'.format(fileName))
