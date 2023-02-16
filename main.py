import os

from antlr4 import *

from MyListener import CustomListener
from gen.PythonSLexer import PythonSLexer
from gen.PythonSParser import PythonSParser

if __name__ == '__main__':
    filename = "input"
    content = FileStream(f"{filename}.py")
    lexerlib = PythonSLexer(content)
    streamlib = CommonTokenStream(lexerlib)
    parserlib = PythonSParser(streamlib)
    tree = parserlib.program()
    listenerlib = CustomListener(filename)
    treewalker = ParseTreeWalker()
    treewalker.walk(listenerlib, tree)
    jasminFile = filename + '.j'
    os.system(f'java -jar jasmin.jar {jasminFile}')
    execFile = jasminFile.removesuffix('.class')
    print(execFile)
    os.system(f'java {jasminFile}')
