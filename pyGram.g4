grammar pyGram;

global: declaration* function* main;

main: MAIN OPEN CLOSE COLON local BRACKET
;

local   : r_for local
        | r_break local
        | r_while local
        | r_if r_else? local
        | r_print local
        | assigment local
        | function_call SEMI_COLON local
        | r_return local
        |
;

function: DEF type ID OPEN (type ID (COMMA type ID)*)? CLOSE COLON local BRACKET
        | DEF VOID ID OPEN (type ID (COMMA type ID)*)? CLOSE COLON local BRACKET
        ;

r_return : RETURN expr? SEMI_COLON
;

function_call: ID OPEN (expr (COMMA expr)*)? CLOSE
;

// For each
r_for: FOR ID IN RANGE OPEN (expr COMMA)? expr CLOSE COLON local BRACKET
;

//while
r_while: WHILE expr COLON local BRACKET
;

r_break : BREAK SEMI_COLON
;

// if
r_if: IF expr COLON local BRACKET
;

r_else: ELSE COLON local BRACKET
;

// print
r_print: PRINT (expr (COMMA expr)*)? SEMI_COLON
;

declaration: type ID (ASSIGNMENT expr)? (COMMA ID (ASSIGNMENT expr)?)* SEMI_COLON
;

assigment: ID ASSIGNMENT expr SEMI_COLON
;

expr: expr OR term
    | term
    ;

term: term AND term2
    | term2
    ;

term2   : term2 GT term3
        | term2 LT term3
        | term2 GE term3
        | term2 LE term3
        | term3
        ;

term3   : term3 EQ term4
        | term3 NE term4
        | term4
        ;

term4   : term4 PLUS_MINUS term5
        | term5
        ;

term5   : term5 TIMES_DIVIDES term6
        | term6
        ;

term6   : MINUS term6
        | term7
        ;

term7   : NOT factor
        | factor
        ;

factor  : OPEN expr CLOSE
        | ID
        | INT_VALUE
        | FLOAT_VALUE
        | STR_VALUE
        | BOOL_VALUE
        | r_input
        | function_call
        ;

r_input: INPUT OPEN CLOSE
;

type: INT | FLOAT | STRING | BOOLEAN;

// Símbolo
//Operadores de atribuição
ASSIGNMENT: '=';

//Operadores relacionais
EQ: '==';
NE: '!=';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';

//Operadores aritméticos
PLUS_MINUS : '+' | '-';
TIMES_DIVIDES : '*' | '/';

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIVIDES: '/';

//Pontuação
COMMA: ',';
COLON: ':';
SEMI_COLON: ';';
OPEN: '(';
CLOSE: ')';
BRACKET: '}';

// P.R.
//Operadores lógicos
OR: 'or';
AND: 'and';
NOT: 'not';

//Comandos
FOR: 'for';
BREAK: 'break';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
IN: 'in';
DEF: 'def';
MAIN: 'main';
RETURN: 'return';

//tipos
VOID: 'void';
INT: 'int';
FLOAT: 'float';
STRING: 'string';
BOOLEAN: 'boolean';

//Funções
PRINT: 'print';
INPUT: 'input';
RANGE: 'range';

//ID
ID: [a-zA-Z][a-zA-Z0-9]*;

//Valores
INT_VALEU: [0-9]+;
FLOAT_VALUE: [0-9]+[.][0-9]+;
STR_VALUE: ["]~["]*["];
BOOL_VALUE: 'True' | 'False';

WS: [ \t\r\n] -> skip;