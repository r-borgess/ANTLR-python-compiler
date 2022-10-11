from antlr4 import *
from gen.RaimundoLexer import RaimundoLexer as RaimundoLexerLib
from gen.RaimundoParser import RaimundoParser as RaimundoParserLib
from CustomListener import CustomListener
import os, sys

if __name__ == '__main__':
    filename = "input"
    content = FileStream(f"{filename}.py")
    lexerlib = RaimundoLexerLib(content)
    streamlib = CommonTokenStream(lexerlib)
    parserlib = RaimundoParserLib(streamlib)
    tree = parserlib.program()
    listenerlib = CustomListener(filename)
    treewalker = ParseTreeWalker()
    treewalker.walk(listenerlib, tree)
    finalfilename = filename + '.j'
    os.system(f'java -jar jasmin.jar {finalfilename}')
    os.system(f'java {finalfilename}')
