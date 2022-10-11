grammar pyGram;

program: global_variables_declaration functions_declaration main_function_declaration;

global_variables_declaration: variable_declaration_statement*;
functions_declaration: function_declaration*;

main_function_declaration: KW_DEF KW_MAIN KW_PARENTHESIS_OPEN KW_PARENTHESIS_CLOSE KW_BRACKETS_OPEN function_body_statements KW_BRACKETS_CLOSE
;

function_body_statements: forloop_statement function_body_statements
| break_statement function_body_statements
| while_statement function_body_statements
| if_statement else_statement? function_body_statements
| print_statement function_body_statements
| assigment_statement function_body_statements
| variable_declaration_statement function_body_statements
| function_call_statement KW_SEMICOLON function_body_statements
| return_statement function_body_statements
|
;

function_declaration: KW_DEF ID KW_PARENTHESIS_OPEN (TYPE ID (KW_COMMA TYPE ID)*)? KW_PARENTHESIS_CLOSE TYPE KW_BRACKETS_OPEN function_body_statements KW_BRACKETS_CLOSE #l_type
| KW_DEF ID KW_PARENTHESIS_OPEN (TYPE ID (KW_COMMA TYPE ID)*)? KW_PARENTHESIS_CLOSE (KW_VOID)? KW_BRACKETS_OPEN function_body_statements KW_BRACKETS_CLOSE #l_void
;

return_statement : KW_RETURN expr? KW_SEMICOLON;

function_call_statement returns [type]: ID KW_PARENTHESIS_OPEN (expr (KW_COMMA expr)*)? KW_PARENTHESIS_CLOSE;

// For each
forloop_statement returns [idx] : KW_FOR ID KW_IN RANGE KW_PARENTHESIS_OPEN (expr KW_COMMA)? expr KW_PARENTHESIS_CLOSE KW_COLON function_body_statements KW_BRACKETS_CLOSE;

//while
while_statement: KW_WHILE KW_PARENTHESIS_OPEN expr KW_PARENTHESIS_CLOSE KW_BRACKETS_OPEN function_body_statements KW_BRACKETS_CLOSE;
break_statement : KW_BREAK KW_SEMICOLON;

// if
if_statement: KW_IF KW_PARENTHESIS_OPEN expr KW_PARENTHESIS_CLOSE KW_BRACKETS_OPEN function_body_statements KW_BRACKETS_CLOSE;

else_statement: KW_ELSE KW_BRACKETS_OPEN function_body_statements KW_BRACKETS_CLOSE;

// print
print_statement: PRINT KW_PARENTHESIS_OPEN (expr (KW_COMMA expr)*)? KW_PARENTHESIS_CLOSE KW_SEMICOLON;

variable_declaration_statement: single_variable_declaration | multiple_variable_declaration;
single_variable_declaration: TYPE ID (KW_ASSIGNMENT expr)? KW_SEMICOLON;
multiple_variable_declaration: TYPE ID (KW_COMMA ID)* (KW_ASSIGNMENT expr (KW_COMMA expr)*)? KW_SEMICOLON;

assigment_statement: ID KW_ASSIGNMENT expr KW_SEMICOLON #e_assigment
| ID KW_ASSIGNMENT r_input KW_SEMICOLON #input
;


expr returns [type, inh_type]
    : expr KW_OR term #or_logic
    | term #e_term
    ;

term returns [type]
    : term KW_AND term2 #and_logic
    | term2 #e_term2
    ;

term2   returns [type]
        : term2 op=(KW_GREATERTHAN | KW_LESSERTHAN | KW_LESSEREQUALTHAN | KW_GREATERQUALTHAN) term3 #comp_logic
        | term3 #e_term3
        ;

term3   returns [type]
        : term3 op=(KW_EQUAL | KW_NOTEQUAL) term4 #eq_logic
        | term4 #e_term4
        ;

term4   returns [type]
        : term4 op=(KW_PLUS | KW_MINUS) term5 #sum_minus
        | term5 #e_term5
        ;

term5   returns [type]
        : term5 op=(KW_MULT | KW_DIV) term6 #time_div
        | term6 #e_term6
        ;

term6 returns [type]
        : op=(KW_MINUS | KW_NOT) term6 #minus_not
        | factor #e_factor
        ;

factor  returns [type]
        : KW_PARENTHESIS_OPEN expr KW_PARENTHESIS_CLOSE #l_expr// expr.type
        | function_call_statement #l_function_call//function_call.type
        | ID #l_id//symbol_table
        | INT_VALUE #l_int_value //integer
        | FLOAT_VALUE #l_float_value//float
        | STR_VALUE #l_str_value//string
        | BOOL_VALUE #l_bool_value// boolean
        ;

r_input: INPUT KW_PARENTHESIS_OPEN KW_PARENTHESIS_CLOSE
;

//Funções
PRINT: 'print';
INPUT: 'input';
RANGE: 'range';

//Valores
INT_VALUE: [0-9]+;
FLOAT_VALUE: [0-9]+[.][0-9]+;
STR_VALUE: '"' .*? '"';
BOOL_VALUE: KW_TRUE | KW_FALSE;

// Símbolo
//Operadores de atribuição
KW_ASSIGNMENT: '=';

//Operadores relacionais
KW_GREATERTHAN: '>';
KW_LESSERTHAN: '<';
KW_GREATERQUALTHAN: '>=';
KW_LESSEREQUALTHAN: '<=';

KW_EQUAL: '==';
KW_NOTEQUAL: '!=';

KW_PLUS: '+';
KW_MINUS: '-';
KW_MULT: '*';
KW_DIV: '/';

KW_COMMA: ',';
KW_COLON: ':';
KW_SEMICOLON: ';';
KW_PARENTHESIS_OPEN: '(';
KW_PARENTHESIS_CLOSE: ')';
KW_BRACKETS_OPEN: '{';
KW_BRACKETS_CLOSE: '}';

KW_OR: '||';
KW_AND: '&&';
KW_NOT: '!';

KW_FOR: 'for';
KW_BREAK: 'break';
KW_IF: 'if';
KW_ELSE: 'else';
KW_WHILE: 'while';
KW_IN: 'in';
KW_DEF: 'def';
KW_MAIN: 'main';
KW_RETURN: 'return';

TYPE: KW_INT | KW_FLOAT | KW_STRING | KW_BOOL;
KW_INT: 'int';
KW_FLOAT: 'real';
KW_STRING: 'string';
KW_BOOL: 'bool';
KW_VOID: 'void';

KW_TRUE: 'true';
KW_FALSE: 'false';
ID: [a-zA-Z][a-zA-Z0-9_]*;
WS: [ \t\r\n] -> skip;