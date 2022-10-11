# Generated from /home/jpedro/workspace/jpedrodsp/novo_compilador/pyGram.g4 by ANTLR 4.10.1
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
        4,1,47,367,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,1,0,1,1,5,1,60,8,1,10,1,12,1,63,9,1,1,2,5,2,66,8,2,10,
        2,12,2,69,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,90,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,111,8,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,121,8,5,10,5,12,5,124,9,5,3,5,126,
        8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,
        142,8,5,10,5,12,5,145,9,5,3,5,147,8,5,1,5,1,5,3,5,151,8,5,1,5,1,
        5,1,5,1,5,3,5,157,8,5,1,6,1,6,3,6,161,8,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,5,7,170,8,7,10,7,12,7,173,9,7,3,7,175,8,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,187,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,
        13,5,13,224,8,13,10,13,12,13,227,9,13,3,13,229,8,13,1,13,1,13,1,
        13,1,14,1,14,3,14,236,8,14,1,15,1,15,1,15,1,15,3,15,242,8,15,1,15,
        1,15,1,16,1,16,1,16,1,16,5,16,250,8,16,10,16,12,16,253,9,16,1,16,
        1,16,1,16,1,16,5,16,259,8,16,10,16,12,16,262,9,16,3,16,264,8,16,
        1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,
        278,8,17,1,18,1,18,1,18,1,18,1,18,1,18,5,18,286,8,18,10,18,12,18,
        289,9,18,1,19,1,19,1,19,1,19,1,19,1,19,5,19,297,8,19,10,19,12,19,
        300,9,19,1,20,1,20,1,20,1,20,1,20,1,20,5,20,308,8,20,10,20,12,20,
        311,9,20,1,21,1,21,1,21,1,21,1,21,1,21,5,21,319,8,21,10,21,12,21,
        322,9,21,1,22,1,22,1,22,1,22,1,22,1,22,5,22,330,8,22,10,22,12,22,
        333,9,22,1,23,1,23,1,23,1,23,1,23,1,23,5,23,341,8,23,10,23,12,23,
        344,9,23,1,24,1,24,1,24,3,24,349,8,24,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,1,25,1,25,3,25,361,8,25,1,26,1,26,1,26,1,26,1,26,0,
        6,36,38,40,42,44,46,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,0,5,1,0,9,12,1,0,13,14,1,0,15,16,
        1,0,17,18,2,0,16,16,28,28,382,0,54,1,0,0,0,2,61,1,0,0,0,4,67,1,0,
        0,0,6,70,1,0,0,0,8,110,1,0,0,0,10,156,1,0,0,0,12,158,1,0,0,0,14,
        164,1,0,0,0,16,178,1,0,0,0,18,194,1,0,0,0,20,202,1,0,0,0,22,205,
        1,0,0,0,24,213,1,0,0,0,26,218,1,0,0,0,28,235,1,0,0,0,30,237,1,0,
        0,0,32,245,1,0,0,0,34,277,1,0,0,0,36,279,1,0,0,0,38,290,1,0,0,0,
        40,301,1,0,0,0,42,312,1,0,0,0,44,323,1,0,0,0,46,334,1,0,0,0,48,348,
        1,0,0,0,50,360,1,0,0,0,52,362,1,0,0,0,54,55,3,2,1,0,55,56,3,4,2,
        0,56,57,3,6,3,0,57,1,1,0,0,0,58,60,3,28,14,0,59,58,1,0,0,0,60,63,
        1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,3,1,0,0,0,63,61,1,0,0,0,64,
        66,3,10,5,0,65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,
        0,0,68,5,1,0,0,0,69,67,1,0,0,0,70,71,5,35,0,0,71,72,5,36,0,0,72,
        73,5,22,0,0,73,74,5,23,0,0,74,75,5,24,0,0,75,76,3,8,4,0,76,77,5,
        25,0,0,77,7,1,0,0,0,78,79,3,16,8,0,79,80,3,8,4,0,80,111,1,0,0,0,
        81,82,3,20,10,0,82,83,3,8,4,0,83,111,1,0,0,0,84,85,3,18,9,0,85,86,
        3,8,4,0,86,111,1,0,0,0,87,89,3,22,11,0,88,90,3,24,12,0,89,88,1,0,
        0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,3,8,4,0,92,111,1,0,0,0,93,
        94,3,26,13,0,94,95,3,8,4,0,95,111,1,0,0,0,96,97,3,34,17,0,97,98,
        3,8,4,0,98,111,1,0,0,0,99,100,3,28,14,0,100,101,3,8,4,0,101,111,
        1,0,0,0,102,103,3,14,7,0,103,104,5,21,0,0,104,105,3,8,4,0,105,111,
        1,0,0,0,106,107,3,12,6,0,107,108,3,8,4,0,108,111,1,0,0,0,109,111,
        1,0,0,0,110,78,1,0,0,0,110,81,1,0,0,0,110,84,1,0,0,0,110,87,1,0,
        0,0,110,93,1,0,0,0,110,96,1,0,0,0,110,99,1,0,0,0,110,102,1,0,0,0,
        110,106,1,0,0,0,110,109,1,0,0,0,111,9,1,0,0,0,112,113,5,35,0,0,113,
        114,5,46,0,0,114,125,5,22,0,0,115,116,5,38,0,0,116,122,5,46,0,0,
        117,118,5,19,0,0,118,119,5,38,0,0,119,121,5,46,0,0,120,117,1,0,0,
        0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,126,1,0,0,
        0,124,122,1,0,0,0,125,115,1,0,0,0,125,126,1,0,0,0,126,127,1,0,0,
        0,127,128,5,23,0,0,128,129,5,38,0,0,129,130,5,24,0,0,130,131,3,8,
        4,0,131,132,5,25,0,0,132,157,1,0,0,0,133,134,5,35,0,0,134,135,5,
        46,0,0,135,146,5,22,0,0,136,137,5,38,0,0,137,143,5,46,0,0,138,139,
        5,19,0,0,139,140,5,38,0,0,140,142,5,46,0,0,141,138,1,0,0,0,142,145,
        1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,147,1,0,0,0,145,143,
        1,0,0,0,146,136,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,150,
        5,23,0,0,149,151,5,43,0,0,150,149,1,0,0,0,150,151,1,0,0,0,151,152,
        1,0,0,0,152,153,5,24,0,0,153,154,3,8,4,0,154,155,5,25,0,0,155,157,
        1,0,0,0,156,112,1,0,0,0,156,133,1,0,0,0,157,11,1,0,0,0,158,160,5,
        37,0,0,159,161,3,36,18,0,160,159,1,0,0,0,160,161,1,0,0,0,161,162,
        1,0,0,0,162,163,5,21,0,0,163,13,1,0,0,0,164,165,5,46,0,0,165,174,
        5,22,0,0,166,171,3,36,18,0,167,168,5,19,0,0,168,170,3,36,18,0,169,
        167,1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,
        175,1,0,0,0,173,171,1,0,0,0,174,166,1,0,0,0,174,175,1,0,0,0,175,
        176,1,0,0,0,176,177,5,23,0,0,177,15,1,0,0,0,178,179,5,29,0,0,179,
        180,5,46,0,0,180,181,5,34,0,0,181,182,5,3,0,0,182,186,5,22,0,0,183,
        184,3,36,18,0,184,185,5,19,0,0,185,187,1,0,0,0,186,183,1,0,0,0,186,
        187,1,0,0,0,187,188,1,0,0,0,188,189,3,36,18,0,189,190,5,23,0,0,190,
        191,5,20,0,0,191,192,3,8,4,0,192,193,5,25,0,0,193,17,1,0,0,0,194,
        195,5,33,0,0,195,196,5,22,0,0,196,197,3,36,18,0,197,198,5,23,0,0,
        198,199,5,24,0,0,199,200,3,8,4,0,200,201,5,25,0,0,201,19,1,0,0,0,
        202,203,5,30,0,0,203,204,5,21,0,0,204,21,1,0,0,0,205,206,5,31,0,
        0,206,207,5,22,0,0,207,208,3,36,18,0,208,209,5,23,0,0,209,210,5,
        24,0,0,210,211,3,8,4,0,211,212,5,25,0,0,212,23,1,0,0,0,213,214,5,
        32,0,0,214,215,5,24,0,0,215,216,3,8,4,0,216,217,5,25,0,0,217,25,
        1,0,0,0,218,219,5,1,0,0,219,228,5,22,0,0,220,225,3,36,18,0,221,222,
        5,19,0,0,222,224,3,36,18,0,223,221,1,0,0,0,224,227,1,0,0,0,225,223,
        1,0,0,0,225,226,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,228,220,
        1,0,0,0,228,229,1,0,0,0,229,230,1,0,0,0,230,231,5,23,0,0,231,232,
        5,21,0,0,232,27,1,0,0,0,233,236,3,30,15,0,234,236,3,32,16,0,235,
        233,1,0,0,0,235,234,1,0,0,0,236,29,1,0,0,0,237,238,5,38,0,0,238,
        241,5,46,0,0,239,240,5,8,0,0,240,242,3,36,18,0,241,239,1,0,0,0,241,
        242,1,0,0,0,242,243,1,0,0,0,243,244,5,21,0,0,244,31,1,0,0,0,245,
        246,5,38,0,0,246,251,5,46,0,0,247,248,5,19,0,0,248,250,5,46,0,0,
        249,247,1,0,0,0,250,253,1,0,0,0,251,249,1,0,0,0,251,252,1,0,0,0,
        252,263,1,0,0,0,253,251,1,0,0,0,254,255,5,8,0,0,255,260,3,36,18,
        0,256,257,5,19,0,0,257,259,3,36,18,0,258,256,1,0,0,0,259,262,1,0,
        0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,264,1,0,0,0,262,260,1,0,
        0,0,263,254,1,0,0,0,263,264,1,0,0,0,264,265,1,0,0,0,265,266,5,21,
        0,0,266,33,1,0,0,0,267,268,5,46,0,0,268,269,5,8,0,0,269,270,3,36,
        18,0,270,271,5,21,0,0,271,278,1,0,0,0,272,273,5,46,0,0,273,274,5,
        8,0,0,274,275,3,52,26,0,275,276,5,21,0,0,276,278,1,0,0,0,277,267,
        1,0,0,0,277,272,1,0,0,0,278,35,1,0,0,0,279,280,6,18,-1,0,280,281,
        3,38,19,0,281,287,1,0,0,0,282,283,10,2,0,0,283,284,5,26,0,0,284,
        286,3,38,19,0,285,282,1,0,0,0,286,289,1,0,0,0,287,285,1,0,0,0,287,
        288,1,0,0,0,288,37,1,0,0,0,289,287,1,0,0,0,290,291,6,19,-1,0,291,
        292,3,40,20,0,292,298,1,0,0,0,293,294,10,2,0,0,294,295,5,27,0,0,
        295,297,3,40,20,0,296,293,1,0,0,0,297,300,1,0,0,0,298,296,1,0,0,
        0,298,299,1,0,0,0,299,39,1,0,0,0,300,298,1,0,0,0,301,302,6,20,-1,
        0,302,303,3,42,21,0,303,309,1,0,0,0,304,305,10,2,0,0,305,306,7,0,
        0,0,306,308,3,42,21,0,307,304,1,0,0,0,308,311,1,0,0,0,309,307,1,
        0,0,0,309,310,1,0,0,0,310,41,1,0,0,0,311,309,1,0,0,0,312,313,6,21,
        -1,0,313,314,3,44,22,0,314,320,1,0,0,0,315,316,10,2,0,0,316,317,
        7,1,0,0,317,319,3,44,22,0,318,315,1,0,0,0,319,322,1,0,0,0,320,318,
        1,0,0,0,320,321,1,0,0,0,321,43,1,0,0,0,322,320,1,0,0,0,323,324,6,
        22,-1,0,324,325,3,46,23,0,325,331,1,0,0,0,326,327,10,2,0,0,327,328,
        7,2,0,0,328,330,3,46,23,0,329,326,1,0,0,0,330,333,1,0,0,0,331,329,
        1,0,0,0,331,332,1,0,0,0,332,45,1,0,0,0,333,331,1,0,0,0,334,335,6,
        23,-1,0,335,336,3,48,24,0,336,342,1,0,0,0,337,338,10,2,0,0,338,339,
        7,3,0,0,339,341,3,48,24,0,340,337,1,0,0,0,341,344,1,0,0,0,342,340,
        1,0,0,0,342,343,1,0,0,0,343,47,1,0,0,0,344,342,1,0,0,0,345,346,7,
        4,0,0,346,349,3,48,24,0,347,349,3,50,25,0,348,345,1,0,0,0,348,347,
        1,0,0,0,349,49,1,0,0,0,350,351,5,22,0,0,351,352,3,36,18,0,352,353,
        5,23,0,0,353,361,1,0,0,0,354,361,3,14,7,0,355,361,5,46,0,0,356,361,
        5,4,0,0,357,361,5,5,0,0,358,361,5,6,0,0,359,361,5,7,0,0,360,350,
        1,0,0,0,360,354,1,0,0,0,360,355,1,0,0,0,360,356,1,0,0,0,360,357,
        1,0,0,0,360,358,1,0,0,0,360,359,1,0,0,0,361,51,1,0,0,0,362,363,5,
        2,0,0,363,364,5,22,0,0,364,365,5,23,0,0,365,53,1,0,0,0,30,61,67,
        89,110,122,125,143,146,150,156,160,171,174,186,225,228,235,241,251,
        260,263,277,287,298,309,320,331,342,348,360
    ]

class pyGramParser ( Parser ):

    grammarFileName = "pyGram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'input'", "'range'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "'+'", "'-'", 
                     "'*'", "'/'", "','", "':'", "';'", "'('", "')'", "'{'", 
                     "'}'", "'||'", "'&&'", "'!'", "'for'", "'break'", "'if'", 
                     "'else'", "'while'", "'in'", "'def'", "'main'", "'return'", 
                     "<INVALID>", "'int'", "'real'", "'string'", "'bool'", 
                     "'void'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "INPUT", "RANGE", "INT_VALUE", 
                      "FLOAT_VALUE", "STR_VALUE", "BOOL_VALUE", "KW_ASSIGNMENT", 
                      "KW_GREATERTHAN", "KW_LESSERTHAN", "KW_GREATERQUALTHAN", 
                      "KW_LESSEREQUALTHAN", "KW_EQUAL", "KW_NOTEQUAL", "KW_PLUS", 
                      "KW_MINUS", "KW_MULT", "KW_DIV", "KW_COMMA", "KW_COLON", 
                      "KW_SEMICOLON", "KW_PARENTHESIS_OPEN", "KW_PARENTHESIS_CLOSE", 
                      "KW_BRACKETS_OPEN", "KW_BRACKETS_CLOSE", "KW_OR", 
                      "KW_AND", "KW_NOT", "KW_FOR", "KW_BREAK", "KW_IF", 
                      "KW_ELSE", "KW_WHILE", "KW_IN", "KW_DEF", "KW_MAIN", 
                      "KW_RETURN", "TYPE", "KW_INT", "KW_FLOAT", "KW_STRING", 
                      "KW_BOOL", "KW_VOID", "KW_TRUE", "KW_FALSE", "ID", 
                      "WS" ]

    RULE_program = 0
    RULE_global_variables_declaration = 1
    RULE_functions_declaration = 2
    RULE_main_function_declaration = 3
    RULE_function_body_statements = 4
    RULE_function_declaration = 5
    RULE_return_statement = 6
    RULE_function_call_statement = 7
    RULE_forloop_statement = 8
    RULE_while_statement = 9
    RULE_break_statement = 10
    RULE_if_statement = 11
    RULE_else_statement = 12
    RULE_print_statement = 13
    RULE_variable_declaration_statement = 14
    RULE_single_variable_declaration = 15
    RULE_multiple_variable_declaration = 16
    RULE_assigment_statement = 17
    RULE_expr = 18
    RULE_term = 19
    RULE_term2 = 20
    RULE_term3 = 21
    RULE_term4 = 22
    RULE_term5 = 23
    RULE_term6 = 24
    RULE_factor = 25
    RULE_r_input = 26

    ruleNames =  [ "program", "global_variables_declaration", "functions_declaration", 
                   "main_function_declaration", "function_body_statements", 
                   "function_declaration", "return_statement", "function_call_statement", 
                   "forloop_statement", "while_statement", "break_statement", 
                   "if_statement", "else_statement", "print_statement", 
                   "variable_declaration_statement", "single_variable_declaration", 
                   "multiple_variable_declaration", "assigment_statement", 
                   "expr", "term", "term2", "term3", "term4", "term5", "term6", 
                   "factor", "r_input" ]

    EOF = Token.EOF
    PRINT=1
    INPUT=2
    RANGE=3
    INT_VALUE=4
    FLOAT_VALUE=5
    STR_VALUE=6
    BOOL_VALUE=7
    KW_ASSIGNMENT=8
    KW_GREATERTHAN=9
    KW_LESSERTHAN=10
    KW_GREATERQUALTHAN=11
    KW_LESSEREQUALTHAN=12
    KW_EQUAL=13
    KW_NOTEQUAL=14
    KW_PLUS=15
    KW_MINUS=16
    KW_MULT=17
    KW_DIV=18
    KW_COMMA=19
    KW_COLON=20
    KW_SEMICOLON=21
    KW_PARENTHESIS_OPEN=22
    KW_PARENTHESIS_CLOSE=23
    KW_BRACKETS_OPEN=24
    KW_BRACKETS_CLOSE=25
    KW_OR=26
    KW_AND=27
    KW_NOT=28
    KW_FOR=29
    KW_BREAK=30
    KW_IF=31
    KW_ELSE=32
    KW_WHILE=33
    KW_IN=34
    KW_DEF=35
    KW_MAIN=36
    KW_RETURN=37
    TYPE=38
    KW_INT=39
    KW_FLOAT=40
    KW_STRING=41
    KW_BOOL=42
    KW_VOID=43
    KW_TRUE=44
    KW_FALSE=45
    ID=46
    WS=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def global_variables_declaration(self):
            return self.getTypedRuleContext(pyGramParser.Global_variables_declarationContext,0)


        def functions_declaration(self):
            return self.getTypedRuleContext(pyGramParser.Functions_declarationContext,0)


        def main_function_declaration(self):
            return self.getTypedRuleContext(pyGramParser.Main_function_declarationContext,0)


        def getRuleIndex(self):
            return pyGramParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = pyGramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.global_variables_declaration()
            self.state = 55
            self.functions_declaration()
            self.state = 56
            self.main_function_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_variables_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyGramParser.Variable_declaration_statementContext)
            else:
                return self.getTypedRuleContext(pyGramParser.Variable_declaration_statementContext,i)


        def getRuleIndex(self):
            return pyGramParser.RULE_global_variables_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_variables_declaration" ):
                listener.enterGlobal_variables_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_variables_declaration" ):
                listener.exitGlobal_variables_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobal_variables_declaration" ):
                return visitor.visitGlobal_variables_declaration(self)
            else:
                return visitor.visitChildren(self)




    def global_variables_declaration(self):

        localctx = pyGramParser.Global_variables_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_global_variables_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pyGramParser.TYPE:
                self.state = 58
                self.variable_declaration_statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Functions_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyGramParser.Function_declarationContext)
            else:
                return self.getTypedRuleContext(pyGramParser.Function_declarationContext,i)


        def getRuleIndex(self):
            return pyGramParser.RULE_functions_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions_declaration" ):
                listener.enterFunctions_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions_declaration" ):
                listener.exitFunctions_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions_declaration" ):
                return visitor.visitFunctions_declaration(self)
            else:
                return visitor.visitChildren(self)




    def functions_declaration(self):

        localctx = pyGramParser.Functions_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functions_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 64
                    self.function_declaration() 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DEF(self):
            return self.getToken(pyGramParser.KW_DEF, 0)

        def KW_MAIN(self):
            return self.getToken(pyGramParser.KW_MAIN, 0)

        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)

        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)

        def KW_BRACKETS_OPEN(self):
            return self.getToken(pyGramParser.KW_BRACKETS_OPEN, 0)

        def function_body_statements(self):
            return self.getTypedRuleContext(pyGramParser.Function_body_statementsContext,0)


        def KW_BRACKETS_CLOSE(self):
            return self.getToken(pyGramParser.KW_BRACKETS_CLOSE, 0)

        def getRuleIndex(self):
            return pyGramParser.RULE_main_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_function_declaration" ):
                listener.enterMain_function_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_function_declaration" ):
                listener.exitMain_function_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_function_declaration" ):
                return visitor.visitMain_function_declaration(self)
            else:
                return visitor.visitChildren(self)




    def main_function_declaration(self):

        localctx = pyGramParser.Main_function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_main_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(pyGramParser.KW_DEF)
            self.state = 71
            self.match(pyGramParser.KW_MAIN)
            self.state = 72
            self.match(pyGramParser.KW_PARENTHESIS_OPEN)
            self.state = 73
            self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
            self.state = 74
            self.match(pyGramParser.KW_BRACKETS_OPEN)
            self.state = 75
            self.function_body_statements()
            self.state = 76
            self.match(pyGramParser.KW_BRACKETS_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_body_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forloop_statement(self):
            return self.getTypedRuleContext(pyGramParser.Forloop_statementContext,0)


        def function_body_statements(self):
            return self.getTypedRuleContext(pyGramParser.Function_body_statementsContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(pyGramParser.Break_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(pyGramParser.While_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(pyGramParser.If_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(pyGramParser.Else_statementContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(pyGramParser.Print_statementContext,0)


        def assigment_statement(self):
            return self.getTypedRuleContext(pyGramParser.Assigment_statementContext,0)


        def variable_declaration_statement(self):
            return self.getTypedRuleContext(pyGramParser.Variable_declaration_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(pyGramParser.Function_call_statementContext,0)


        def KW_SEMICOLON(self):
            return self.getToken(pyGramParser.KW_SEMICOLON, 0)

        def return_statement(self):
            return self.getTypedRuleContext(pyGramParser.Return_statementContext,0)


        def getRuleIndex(self):
            return pyGramParser.RULE_function_body_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_body_statements" ):
                listener.enterFunction_body_statements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_body_statements" ):
                listener.exitFunction_body_statements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body_statements" ):
                return visitor.visitFunction_body_statements(self)
            else:
                return visitor.visitChildren(self)




    def function_body_statements(self):

        localctx = pyGramParser.Function_body_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function_body_statements)
        self._la = 0 # Token type
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.forloop_statement()
                self.state = 79
                self.function_body_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.break_statement()
                self.state = 82
                self.function_body_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.while_statement()
                self.state = 85
                self.function_body_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 87
                self.if_statement()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pyGramParser.KW_ELSE:
                    self.state = 88
                    self.else_statement()


                self.state = 91
                self.function_body_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.print_statement()
                self.state = 94
                self.function_body_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.assigment_statement()
                self.state = 97
                self.function_body_statements()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 99
                self.variable_declaration_statement()
                self.state = 100
                self.function_body_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 102
                self.function_call_statement()
                self.state = 103
                self.match(pyGramParser.KW_SEMICOLON)
                self.state = 104
                self.function_body_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 106
                self.return_statement()
                self.state = 107
                self.function_body_statements()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pyGramParser.RULE_function_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class L_typeContext(Function_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Function_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_DEF(self):
            return self.getToken(pyGramParser.KW_DEF, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.ID)
            else:
                return self.getToken(pyGramParser.ID, i)
        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)
        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.TYPE)
            else:
                return self.getToken(pyGramParser.TYPE, i)
        def KW_BRACKETS_OPEN(self):
            return self.getToken(pyGramParser.KW_BRACKETS_OPEN, 0)
        def function_body_statements(self):
            return self.getTypedRuleContext(pyGramParser.Function_body_statementsContext,0)

        def KW_BRACKETS_CLOSE(self):
            return self.getToken(pyGramParser.KW_BRACKETS_CLOSE, 0)
        def KW_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.KW_COMMA)
            else:
                return self.getToken(pyGramParser.KW_COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_type" ):
                listener.enterL_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_type" ):
                listener.exitL_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_type" ):
                return visitor.visitL_type(self)
            else:
                return visitor.visitChildren(self)


    class L_voidContext(Function_declarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Function_declarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_DEF(self):
            return self.getToken(pyGramParser.KW_DEF, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.ID)
            else:
                return self.getToken(pyGramParser.ID, i)
        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)
        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)
        def KW_BRACKETS_OPEN(self):
            return self.getToken(pyGramParser.KW_BRACKETS_OPEN, 0)
        def function_body_statements(self):
            return self.getTypedRuleContext(pyGramParser.Function_body_statementsContext,0)

        def KW_BRACKETS_CLOSE(self):
            return self.getToken(pyGramParser.KW_BRACKETS_CLOSE, 0)
        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.TYPE)
            else:
                return self.getToken(pyGramParser.TYPE, i)
        def KW_VOID(self):
            return self.getToken(pyGramParser.KW_VOID, 0)
        def KW_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.KW_COMMA)
            else:
                return self.getToken(pyGramParser.KW_COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_void" ):
                listener.enterL_void(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_void" ):
                listener.exitL_void(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_void" ):
                return visitor.visitL_void(self)
            else:
                return visitor.visitChildren(self)



    def function_declaration(self):

        localctx = pyGramParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = pyGramParser.L_typeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(pyGramParser.KW_DEF)
                self.state = 113
                self.match(pyGramParser.ID)
                self.state = 114
                self.match(pyGramParser.KW_PARENTHESIS_OPEN)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pyGramParser.TYPE:
                    self.state = 115
                    self.match(pyGramParser.TYPE)
                    self.state = 116
                    self.match(pyGramParser.ID)
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==pyGramParser.KW_COMMA:
                        self.state = 117
                        self.match(pyGramParser.KW_COMMA)
                        self.state = 118
                        self.match(pyGramParser.TYPE)
                        self.state = 119
                        self.match(pyGramParser.ID)
                        self.state = 124
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 127
                self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
                self.state = 128
                self.match(pyGramParser.TYPE)
                self.state = 129
                self.match(pyGramParser.KW_BRACKETS_OPEN)
                self.state = 130
                self.function_body_statements()
                self.state = 131
                self.match(pyGramParser.KW_BRACKETS_CLOSE)
                pass

            elif la_ == 2:
                localctx = pyGramParser.L_voidContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(pyGramParser.KW_DEF)
                self.state = 134
                self.match(pyGramParser.ID)
                self.state = 135
                self.match(pyGramParser.KW_PARENTHESIS_OPEN)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pyGramParser.TYPE:
                    self.state = 136
                    self.match(pyGramParser.TYPE)
                    self.state = 137
                    self.match(pyGramParser.ID)
                    self.state = 143
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==pyGramParser.KW_COMMA:
                        self.state = 138
                        self.match(pyGramParser.KW_COMMA)
                        self.state = 139
                        self.match(pyGramParser.TYPE)
                        self.state = 140
                        self.match(pyGramParser.ID)
                        self.state = 145
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 148
                self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==pyGramParser.KW_VOID:
                    self.state = 149
                    self.match(pyGramParser.KW_VOID)


                self.state = 152
                self.match(pyGramParser.KW_BRACKETS_OPEN)
                self.state = 153
                self.function_body_statements()
                self.state = 154
                self.match(pyGramParser.KW_BRACKETS_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_RETURN(self):
            return self.getToken(pyGramParser.KW_RETURN, 0)

        def KW_SEMICOLON(self):
            return self.getToken(pyGramParser.KW_SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(pyGramParser.ExprContext,0)


        def getRuleIndex(self):
            return pyGramParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = pyGramParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(pyGramParser.KW_RETURN)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pyGramParser.INT_VALUE) | (1 << pyGramParser.FLOAT_VALUE) | (1 << pyGramParser.STR_VALUE) | (1 << pyGramParser.BOOL_VALUE) | (1 << pyGramParser.KW_MINUS) | (1 << pyGramParser.KW_PARENTHESIS_OPEN) | (1 << pyGramParser.KW_NOT) | (1 << pyGramParser.ID))) != 0):
                self.state = 159
                self.expr(0)


            self.state = 162
            self.match(pyGramParser.KW_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None

        def ID(self):
            return self.getToken(pyGramParser.ID, 0)

        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)

        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyGramParser.ExprContext)
            else:
                return self.getTypedRuleContext(pyGramParser.ExprContext,i)


        def KW_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.KW_COMMA)
            else:
                return self.getToken(pyGramParser.KW_COMMA, i)

        def getRuleIndex(self):
            return pyGramParser.RULE_function_call_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_statement" ):
                listener.enterFunction_call_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_statement" ):
                listener.exitFunction_call_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_statement" ):
                return visitor.visitFunction_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_call_statement(self):

        localctx = pyGramParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(pyGramParser.ID)
            self.state = 165
            self.match(pyGramParser.KW_PARENTHESIS_OPEN)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pyGramParser.INT_VALUE) | (1 << pyGramParser.FLOAT_VALUE) | (1 << pyGramParser.STR_VALUE) | (1 << pyGramParser.BOOL_VALUE) | (1 << pyGramParser.KW_MINUS) | (1 << pyGramParser.KW_PARENTHESIS_OPEN) | (1 << pyGramParser.KW_NOT) | (1 << pyGramParser.ID))) != 0):
                self.state = 166
                self.expr(0)
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==pyGramParser.KW_COMMA:
                    self.state = 167
                    self.match(pyGramParser.KW_COMMA)
                    self.state = 168
                    self.expr(0)
                    self.state = 173
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 176
            self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forloop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.idx = None

        def KW_FOR(self):
            return self.getToken(pyGramParser.KW_FOR, 0)

        def ID(self):
            return self.getToken(pyGramParser.ID, 0)

        def KW_IN(self):
            return self.getToken(pyGramParser.KW_IN, 0)

        def RANGE(self):
            return self.getToken(pyGramParser.RANGE, 0)

        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyGramParser.ExprContext)
            else:
                return self.getTypedRuleContext(pyGramParser.ExprContext,i)


        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)

        def KW_COLON(self):
            return self.getToken(pyGramParser.KW_COLON, 0)

        def function_body_statements(self):
            return self.getTypedRuleContext(pyGramParser.Function_body_statementsContext,0)


        def KW_BRACKETS_CLOSE(self):
            return self.getToken(pyGramParser.KW_BRACKETS_CLOSE, 0)

        def KW_COMMA(self):
            return self.getToken(pyGramParser.KW_COMMA, 0)

        def getRuleIndex(self):
            return pyGramParser.RULE_forloop_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForloop_statement" ):
                listener.enterForloop_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForloop_statement" ):
                listener.exitForloop_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForloop_statement" ):
                return visitor.visitForloop_statement(self)
            else:
                return visitor.visitChildren(self)




    def forloop_statement(self):

        localctx = pyGramParser.Forloop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forloop_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(pyGramParser.KW_FOR)
            self.state = 179
            self.match(pyGramParser.ID)
            self.state = 180
            self.match(pyGramParser.KW_IN)
            self.state = 181
            self.match(pyGramParser.RANGE)
            self.state = 182
            self.match(pyGramParser.KW_PARENTHESIS_OPEN)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 183
                self.expr(0)
                self.state = 184
                self.match(pyGramParser.KW_COMMA)


            self.state = 188
            self.expr(0)
            self.state = 189
            self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
            self.state = 190
            self.match(pyGramParser.KW_COLON)
            self.state = 191
            self.function_body_statements()
            self.state = 192
            self.match(pyGramParser.KW_BRACKETS_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_WHILE(self):
            return self.getToken(pyGramParser.KW_WHILE, 0)

        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(pyGramParser.ExprContext,0)


        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)

        def KW_BRACKETS_OPEN(self):
            return self.getToken(pyGramParser.KW_BRACKETS_OPEN, 0)

        def function_body_statements(self):
            return self.getTypedRuleContext(pyGramParser.Function_body_statementsContext,0)


        def KW_BRACKETS_CLOSE(self):
            return self.getToken(pyGramParser.KW_BRACKETS_CLOSE, 0)

        def getRuleIndex(self):
            return pyGramParser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = pyGramParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(pyGramParser.KW_WHILE)
            self.state = 195
            self.match(pyGramParser.KW_PARENTHESIS_OPEN)
            self.state = 196
            self.expr(0)
            self.state = 197
            self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
            self.state = 198
            self.match(pyGramParser.KW_BRACKETS_OPEN)
            self.state = 199
            self.function_body_statements()
            self.state = 200
            self.match(pyGramParser.KW_BRACKETS_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BREAK(self):
            return self.getToken(pyGramParser.KW_BREAK, 0)

        def KW_SEMICOLON(self):
            return self.getToken(pyGramParser.KW_SEMICOLON, 0)

        def getRuleIndex(self):
            return pyGramParser.RULE_break_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_statement" ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_statement" ):
                listener.exitBreak_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = pyGramParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(pyGramParser.KW_BREAK)
            self.state = 203
            self.match(pyGramParser.KW_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(pyGramParser.KW_IF, 0)

        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)

        def expr(self):
            return self.getTypedRuleContext(pyGramParser.ExprContext,0)


        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)

        def KW_BRACKETS_OPEN(self):
            return self.getToken(pyGramParser.KW_BRACKETS_OPEN, 0)

        def function_body_statements(self):
            return self.getTypedRuleContext(pyGramParser.Function_body_statementsContext,0)


        def KW_BRACKETS_CLOSE(self):
            return self.getToken(pyGramParser.KW_BRACKETS_CLOSE, 0)

        def getRuleIndex(self):
            return pyGramParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = pyGramParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(pyGramParser.KW_IF)
            self.state = 206
            self.match(pyGramParser.KW_PARENTHESIS_OPEN)
            self.state = 207
            self.expr(0)
            self.state = 208
            self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
            self.state = 209
            self.match(pyGramParser.KW_BRACKETS_OPEN)
            self.state = 210
            self.function_body_statements()
            self.state = 211
            self.match(pyGramParser.KW_BRACKETS_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELSE(self):
            return self.getToken(pyGramParser.KW_ELSE, 0)

        def KW_BRACKETS_OPEN(self):
            return self.getToken(pyGramParser.KW_BRACKETS_OPEN, 0)

        def function_body_statements(self):
            return self.getTypedRuleContext(pyGramParser.Function_body_statementsContext,0)


        def KW_BRACKETS_CLOSE(self):
            return self.getToken(pyGramParser.KW_BRACKETS_CLOSE, 0)

        def getRuleIndex(self):
            return pyGramParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = pyGramParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(pyGramParser.KW_ELSE)
            self.state = 214
            self.match(pyGramParser.KW_BRACKETS_OPEN)
            self.state = 215
            self.function_body_statements()
            self.state = 216
            self.match(pyGramParser.KW_BRACKETS_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(pyGramParser.PRINT, 0)

        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)

        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)

        def KW_SEMICOLON(self):
            return self.getToken(pyGramParser.KW_SEMICOLON, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyGramParser.ExprContext)
            else:
                return self.getTypedRuleContext(pyGramParser.ExprContext,i)


        def KW_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.KW_COMMA)
            else:
                return self.getToken(pyGramParser.KW_COMMA, i)

        def getRuleIndex(self):
            return pyGramParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_statement" ):
                return visitor.visitPrint_statement(self)
            else:
                return visitor.visitChildren(self)




    def print_statement(self):

        localctx = pyGramParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_print_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(pyGramParser.PRINT)
            self.state = 219
            self.match(pyGramParser.KW_PARENTHESIS_OPEN)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pyGramParser.INT_VALUE) | (1 << pyGramParser.FLOAT_VALUE) | (1 << pyGramParser.STR_VALUE) | (1 << pyGramParser.BOOL_VALUE) | (1 << pyGramParser.KW_MINUS) | (1 << pyGramParser.KW_PARENTHESIS_OPEN) | (1 << pyGramParser.KW_NOT) | (1 << pyGramParser.ID))) != 0):
                self.state = 220
                self.expr(0)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==pyGramParser.KW_COMMA:
                    self.state = 221
                    self.match(pyGramParser.KW_COMMA)
                    self.state = 222
                    self.expr(0)
                    self.state = 227
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 230
            self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
            self.state = 231
            self.match(pyGramParser.KW_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_variable_declaration(self):
            return self.getTypedRuleContext(pyGramParser.Single_variable_declarationContext,0)


        def multiple_variable_declaration(self):
            return self.getTypedRuleContext(pyGramParser.Multiple_variable_declarationContext,0)


        def getRuleIndex(self):
            return pyGramParser.RULE_variable_declaration_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration_statement" ):
                listener.enterVariable_declaration_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration_statement" ):
                listener.exitVariable_declaration_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration_statement" ):
                return visitor.visitVariable_declaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration_statement(self):

        localctx = pyGramParser.Variable_declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variable_declaration_statement)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.single_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.multiple_variable_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(pyGramParser.TYPE, 0)

        def ID(self):
            return self.getToken(pyGramParser.ID, 0)

        def KW_SEMICOLON(self):
            return self.getToken(pyGramParser.KW_SEMICOLON, 0)

        def KW_ASSIGNMENT(self):
            return self.getToken(pyGramParser.KW_ASSIGNMENT, 0)

        def expr(self):
            return self.getTypedRuleContext(pyGramParser.ExprContext,0)


        def getRuleIndex(self):
            return pyGramParser.RULE_single_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_variable_declaration" ):
                listener.enterSingle_variable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_variable_declaration" ):
                listener.exitSingle_variable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_variable_declaration" ):
                return visitor.visitSingle_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def single_variable_declaration(self):

        localctx = pyGramParser.Single_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_single_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(pyGramParser.TYPE)
            self.state = 238
            self.match(pyGramParser.ID)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pyGramParser.KW_ASSIGNMENT:
                self.state = 239
                self.match(pyGramParser.KW_ASSIGNMENT)
                self.state = 240
                self.expr(0)


            self.state = 243
            self.match(pyGramParser.KW_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(pyGramParser.TYPE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.ID)
            else:
                return self.getToken(pyGramParser.ID, i)

        def KW_SEMICOLON(self):
            return self.getToken(pyGramParser.KW_SEMICOLON, 0)

        def KW_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(pyGramParser.KW_COMMA)
            else:
                return self.getToken(pyGramParser.KW_COMMA, i)

        def KW_ASSIGNMENT(self):
            return self.getToken(pyGramParser.KW_ASSIGNMENT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pyGramParser.ExprContext)
            else:
                return self.getTypedRuleContext(pyGramParser.ExprContext,i)


        def getRuleIndex(self):
            return pyGramParser.RULE_multiple_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiple_variable_declaration" ):
                listener.enterMultiple_variable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiple_variable_declaration" ):
                listener.exitMultiple_variable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_variable_declaration" ):
                return visitor.visitMultiple_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def multiple_variable_declaration(self):

        localctx = pyGramParser.Multiple_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_multiple_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(pyGramParser.TYPE)
            self.state = 246
            self.match(pyGramParser.ID)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pyGramParser.KW_COMMA:
                self.state = 247
                self.match(pyGramParser.KW_COMMA)
                self.state = 248
                self.match(pyGramParser.ID)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==pyGramParser.KW_ASSIGNMENT:
                self.state = 254
                self.match(pyGramParser.KW_ASSIGNMENT)
                self.state = 255
                self.expr(0)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==pyGramParser.KW_COMMA:
                    self.state = 256
                    self.match(pyGramParser.KW_COMMA)
                    self.state = 257
                    self.expr(0)
                    self.state = 262
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 265
            self.match(pyGramParser.KW_SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assigment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pyGramParser.RULE_assigment_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InputContext(Assigment_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Assigment_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pyGramParser.ID, 0)
        def KW_ASSIGNMENT(self):
            return self.getToken(pyGramParser.KW_ASSIGNMENT, 0)
        def r_input(self):
            return self.getTypedRuleContext(pyGramParser.R_inputContext,0)

        def KW_SEMICOLON(self):
            return self.getToken(pyGramParser.KW_SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput" ):
                return visitor.visitInput(self)
            else:
                return visitor.visitChildren(self)


    class E_assigmentContext(Assigment_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Assigment_statementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pyGramParser.ID, 0)
        def KW_ASSIGNMENT(self):
            return self.getToken(pyGramParser.KW_ASSIGNMENT, 0)
        def expr(self):
            return self.getTypedRuleContext(pyGramParser.ExprContext,0)

        def KW_SEMICOLON(self):
            return self.getToken(pyGramParser.KW_SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_assigment" ):
                listener.enterE_assigment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_assigment" ):
                listener.exitE_assigment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_assigment" ):
                return visitor.visitE_assigment(self)
            else:
                return visitor.visitChildren(self)



    def assigment_statement(self):

        localctx = pyGramParser.Assigment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assigment_statement)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = pyGramParser.E_assigmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(pyGramParser.ID)
                self.state = 268
                self.match(pyGramParser.KW_ASSIGNMENT)
                self.state = 269
                self.expr(0)
                self.state = 270
                self.match(pyGramParser.KW_SEMICOLON)
                pass

            elif la_ == 2:
                localctx = pyGramParser.InputContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(pyGramParser.ID)
                self.state = 273
                self.match(pyGramParser.KW_ASSIGNMENT)
                self.state = 274
                self.r_input()
                self.state = 275
                self.match(pyGramParser.KW_SEMICOLON)
                pass


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
            self.type_ = None
            self.inh_type = None


        def getRuleIndex(self):
            return pyGramParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_
            self.inh_type = ctx.inh_type


    class Or_logicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(pyGramParser.ExprContext,0)

        def KW_OR(self):
            return self.getToken(pyGramParser.KW_OR, 0)
        def term(self):
            return self.getTypedRuleContext(pyGramParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_logic" ):
                listener.enterOr_logic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_logic" ):
                listener.exitOr_logic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_logic" ):
                return visitor.visitOr_logic(self)
            else:
                return visitor.visitChildren(self)


    class E_termContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(pyGramParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_term" ):
                listener.enterE_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_term" ):
                listener.exitE_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_term" ):
                return visitor.visitE_term(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pyGramParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = pyGramParser.E_termContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 280
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 287
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pyGramParser.Or_logicContext(self, pyGramParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 282
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 283
                    self.match(pyGramParser.KW_OR)
                    self.state = 284
                    self.term(0) 
                self.state = 289
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return pyGramParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class And_logicContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(pyGramParser.TermContext,0)

        def KW_AND(self):
            return self.getToken(pyGramParser.KW_AND, 0)
        def term2(self):
            return self.getTypedRuleContext(pyGramParser.Term2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_logic" ):
                listener.enterAnd_logic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_logic" ):
                listener.exitAnd_logic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd_logic" ):
                return visitor.visitAnd_logic(self)
            else:
                return visitor.visitChildren(self)


    class E_term2Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term2(self):
            return self.getTypedRuleContext(pyGramParser.Term2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_term2" ):
                listener.enterE_term2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_term2" ):
                listener.exitE_term2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_term2" ):
                return visitor.visitE_term2(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pyGramParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = pyGramParser.E_term2Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 291
            self.term2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pyGramParser.And_logicContext(self, pyGramParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 293
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 294
                    self.match(pyGramParser.KW_AND)
                    self.state = 295
                    self.term2(0) 
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return pyGramParser.RULE_term2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Comp_logicContext(Term2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term2Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term2(self):
            return self.getTypedRuleContext(pyGramParser.Term2Context,0)

        def term3(self):
            return self.getTypedRuleContext(pyGramParser.Term3Context,0)

        def KW_GREATERTHAN(self):
            return self.getToken(pyGramParser.KW_GREATERTHAN, 0)
        def KW_LESSERTHAN(self):
            return self.getToken(pyGramParser.KW_LESSERTHAN, 0)
        def KW_LESSEREQUALTHAN(self):
            return self.getToken(pyGramParser.KW_LESSEREQUALTHAN, 0)
        def KW_GREATERQUALTHAN(self):
            return self.getToken(pyGramParser.KW_GREATERQUALTHAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp_logic" ):
                listener.enterComp_logic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp_logic" ):
                listener.exitComp_logic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_logic" ):
                return visitor.visitComp_logic(self)
            else:
                return visitor.visitChildren(self)


    class E_term3Context(Term2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term3(self):
            return self.getTypedRuleContext(pyGramParser.Term3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_term3" ):
                listener.enterE_term3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_term3" ):
                listener.exitE_term3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_term3" ):
                return visitor.visitE_term3(self)
            else:
                return visitor.visitChildren(self)



    def term2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pyGramParser.Term2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_term2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = pyGramParser.E_term3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 302
            self.term3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 309
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pyGramParser.Comp_logicContext(self, pyGramParser.Term2Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term2)
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 305
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pyGramParser.KW_GREATERTHAN) | (1 << pyGramParser.KW_LESSERTHAN) | (1 << pyGramParser.KW_GREATERQUALTHAN) | (1 << pyGramParser.KW_LESSEREQUALTHAN))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 306
                    self.term3(0) 
                self.state = 311
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return pyGramParser.RULE_term3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Eq_logicContext(Term3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term3Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term3(self):
            return self.getTypedRuleContext(pyGramParser.Term3Context,0)

        def term4(self):
            return self.getTypedRuleContext(pyGramParser.Term4Context,0)

        def KW_EQUAL(self):
            return self.getToken(pyGramParser.KW_EQUAL, 0)
        def KW_NOTEQUAL(self):
            return self.getToken(pyGramParser.KW_NOTEQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEq_logic" ):
                listener.enterEq_logic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEq_logic" ):
                listener.exitEq_logic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEq_logic" ):
                return visitor.visitEq_logic(self)
            else:
                return visitor.visitChildren(self)


    class E_term4Context(Term3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term4(self):
            return self.getTypedRuleContext(pyGramParser.Term4Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_term4" ):
                listener.enterE_term4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_term4" ):
                listener.exitE_term4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_term4" ):
                return visitor.visitE_term4(self)
            else:
                return visitor.visitChildren(self)



    def term3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pyGramParser.Term3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_term3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = pyGramParser.E_term4Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 313
            self.term4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pyGramParser.Eq_logicContext(self, pyGramParser.Term3Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term3)
                    self.state = 315
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 316
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==pyGramParser.KW_EQUAL or _la==pyGramParser.KW_NOTEQUAL):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 317
                    self.term4(0) 
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return pyGramParser.RULE_term4

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Sum_minusContext(Term4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term4Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term4(self):
            return self.getTypedRuleContext(pyGramParser.Term4Context,0)

        def term5(self):
            return self.getTypedRuleContext(pyGramParser.Term5Context,0)

        def KW_PLUS(self):
            return self.getToken(pyGramParser.KW_PLUS, 0)
        def KW_MINUS(self):
            return self.getToken(pyGramParser.KW_MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum_minus" ):
                listener.enterSum_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum_minus" ):
                listener.exitSum_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSum_minus" ):
                return visitor.visitSum_minus(self)
            else:
                return visitor.visitChildren(self)


    class E_term5Context(Term4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term5(self):
            return self.getTypedRuleContext(pyGramParser.Term5Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_term5" ):
                listener.enterE_term5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_term5" ):
                listener.exitE_term5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_term5" ):
                return visitor.visitE_term5(self)
            else:
                return visitor.visitChildren(self)



    def term4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pyGramParser.Term4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_term4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = pyGramParser.E_term5Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 324
            self.term5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pyGramParser.Sum_minusContext(self, pyGramParser.Term4Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term4)
                    self.state = 326
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 327
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==pyGramParser.KW_PLUS or _la==pyGramParser.KW_MINUS):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 328
                    self.term5(0) 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return pyGramParser.RULE_term5

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class E_term6Context(Term5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term5Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def term6(self):
            return self.getTypedRuleContext(pyGramParser.Term6Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_term6" ):
                listener.enterE_term6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_term6" ):
                listener.exitE_term6(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_term6" ):
                return visitor.visitE_term6(self)
            else:
                return visitor.visitChildren(self)


    class Time_divContext(Term5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term5Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term5(self):
            return self.getTypedRuleContext(pyGramParser.Term5Context,0)

        def term6(self):
            return self.getTypedRuleContext(pyGramParser.Term6Context,0)

        def KW_MULT(self):
            return self.getToken(pyGramParser.KW_MULT, 0)
        def KW_DIV(self):
            return self.getToken(pyGramParser.KW_DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_div" ):
                listener.enterTime_div(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_div" ):
                listener.exitTime_div(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime_div" ):
                return visitor.visitTime_div(self)
            else:
                return visitor.visitChildren(self)



    def term5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pyGramParser.Term5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_term5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = pyGramParser.E_term6Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 335
            self.term6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = pyGramParser.Time_divContext(self, pyGramParser.Term5Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term5)
                    self.state = 337
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 338
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==pyGramParser.KW_MULT or _la==pyGramParser.KW_DIV):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 339
                    self.term6() 
                self.state = 344
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Term6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return pyGramParser.RULE_term6

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_



    class Minus_notContext(Term6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term6Context
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term6(self):
            return self.getTypedRuleContext(pyGramParser.Term6Context,0)

        def KW_MINUS(self):
            return self.getToken(pyGramParser.KW_MINUS, 0)
        def KW_NOT(self):
            return self.getToken(pyGramParser.KW_NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinus_not" ):
                listener.enterMinus_not(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinus_not" ):
                listener.exitMinus_not(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus_not" ):
                return visitor.visitMinus_not(self)
            else:
                return visitor.visitChildren(self)


    class E_factorContext(Term6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.Term6Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(pyGramParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE_factor" ):
                listener.enterE_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE_factor" ):
                listener.exitE_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_factor" ):
                return visitor.visitE_factor(self)
            else:
                return visitor.visitChildren(self)



    def term6(self):

        localctx = pyGramParser.Term6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_term6)
        self._la = 0 # Token type
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pyGramParser.KW_MINUS, pyGramParser.KW_NOT]:
                localctx = pyGramParser.Minus_notContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==pyGramParser.KW_MINUS or _la==pyGramParser.KW_NOT):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 346
                self.term6()
                pass
            elif token in [pyGramParser.INT_VALUE, pyGramParser.FLOAT_VALUE, pyGramParser.STR_VALUE, pyGramParser.BOOL_VALUE, pyGramParser.KW_PARENTHESIS_OPEN, pyGramParser.ID]:
                localctx = pyGramParser.E_factorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.factor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None


        def getRuleIndex(self):
            return pyGramParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_



    class L_str_valueContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR_VALUE(self):
            return self.getToken(pyGramParser.STR_VALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_str_value" ):
                listener.enterL_str_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_str_value" ):
                listener.exitL_str_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_str_value" ):
                return visitor.visitL_str_value(self)
            else:
                return visitor.visitChildren(self)


    class L_int_valueContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT_VALUE(self):
            return self.getToken(pyGramParser.INT_VALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_int_value" ):
                listener.enterL_int_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_int_value" ):
                listener.exitL_int_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_int_value" ):
                return visitor.visitL_int_value(self)
            else:
                return visitor.visitChildren(self)


    class L_bool_valueContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL_VALUE(self):
            return self.getToken(pyGramParser.BOOL_VALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_bool_value" ):
                listener.enterL_bool_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_bool_value" ):
                listener.exitL_bool_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_bool_value" ):
                return visitor.visitL_bool_value(self)
            else:
                return visitor.visitChildren(self)


    class L_idContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pyGramParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_id" ):
                listener.enterL_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_id" ):
                listener.exitL_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_id" ):
                return visitor.visitL_id(self)
            else:
                return visitor.visitChildren(self)


    class L_float_valueContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_VALUE(self):
            return self.getToken(pyGramParser.FLOAT_VALUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_float_value" ):
                listener.enterL_float_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_float_value" ):
                listener.exitL_float_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_float_value" ):
                return visitor.visitL_float_value(self)
            else:
                return visitor.visitChildren(self)


    class L_exprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)
        def expr(self):
            return self.getTypedRuleContext(pyGramParser.ExprContext,0)

        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_expr" ):
                listener.enterL_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_expr" ):
                listener.exitL_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_expr" ):
                return visitor.visitL_expr(self)
            else:
                return visitor.visitChildren(self)


    class L_function_callContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pyGramParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_call_statement(self):
            return self.getTypedRuleContext(pyGramParser.Function_call_statementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL_function_call" ):
                listener.enterL_function_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL_function_call" ):
                listener.exitL_function_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL_function_call" ):
                return visitor.visitL_function_call(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = pyGramParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                localctx = pyGramParser.L_exprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.match(pyGramParser.KW_PARENTHESIS_OPEN)
                self.state = 351
                self.expr(0)
                self.state = 352
                self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
                pass

            elif la_ == 2:
                localctx = pyGramParser.L_function_callContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.function_call_statement()
                pass

            elif la_ == 3:
                localctx = pyGramParser.L_idContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.match(pyGramParser.ID)
                pass

            elif la_ == 4:
                localctx = pyGramParser.L_int_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 356
                self.match(pyGramParser.INT_VALUE)
                pass

            elif la_ == 5:
                localctx = pyGramParser.L_float_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 357
                self.match(pyGramParser.FLOAT_VALUE)
                pass

            elif la_ == 6:
                localctx = pyGramParser.L_str_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 358
                self.match(pyGramParser.STR_VALUE)
                pass

            elif la_ == 7:
                localctx = pyGramParser.L_bool_valueContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 359
                self.match(pyGramParser.BOOL_VALUE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(pyGramParser.INPUT, 0)

        def KW_PARENTHESIS_OPEN(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_OPEN, 0)

        def KW_PARENTHESIS_CLOSE(self):
            return self.getToken(pyGramParser.KW_PARENTHESIS_CLOSE, 0)

        def getRuleIndex(self):
            return pyGramParser.RULE_r_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_input" ):
                listener.enterR_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_input" ):
                listener.exitR_input(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_input" ):
                return visitor.visitR_input(self)
            else:
                return visitor.visitChildren(self)




    def r_input(self):

        localctx = pyGramParser.R_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_r_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(pyGramParser.INPUT)
            self.state = 363
            self.match(pyGramParser.KW_PARENTHESIS_OPEN)
            self.state = 364
            self.match(pyGramParser.KW_PARENTHESIS_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[18] = self.expr_sempred
        self._predicates[19] = self.term_sempred
        self._predicates[20] = self.term2_sempred
        self._predicates[21] = self.term3_sempred
        self._predicates[22] = self.term4_sempred
        self._predicates[23] = self.term5_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term2_sempred(self, localctx:Term2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term3_sempred(self, localctx:Term3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def term4_sempred(self, localctx:Term4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def term5_sempred(self, localctx:Term5Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




