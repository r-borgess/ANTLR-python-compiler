from gen.RaimundoParser import RaimundoParser as RaimundoParserLib
from JasminGenerator import JasminCodeGenerator, CustomListener
from gen.RaimundoListener import RaimundoListener as RaimundoListenerLib
from CustomExceptions import *


class CustomListener(RaimundoListenerLib):
    symbol_table = {}
    functions_args = {}
    stack_block = []

    def __init__(self, filename):
        self.jasmin = JasminCodeGenerator(filename, self.symbol_table)
        self.label_id = 0

    def __is_numeric(self, type):
        return (type == 'real') or (type == 'int') or (type == 'integer')

    def __is_inside_function(self):
        return 'function' in self.stack_block

    def enterMain_function_declaration(self, ctx: RaimundoParserLib.Main_function_declarationContext):
        self.jasmin.write_main_function_declaration()

    def enterL_type(self, ctx: RaimundoParserLib.L_typeContext):
        self.stack_block.append('function')
        function_id = ctx.ID(0).getText()
        if function_id in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, function_id)

        self.symbol_table[function_id] = CustomListener(type=ctx.TYPE(0).getText())

        args = []
        args_names = []
        content = list(zip(ctx.ID()[1:], ctx.TYPE()[1:]))
        for arg_id, arg_type in content:
            if arg_id.getText() in self.symbol_table:
                raise AlreadyDeclaredError(ctx.start.line, arg_id.getText())
            self.symbol_table[arg_id.getText()] = CustomListener(type=arg_type.getText(), local=True)
            args.append(arg_type.getText())
            args_names.append(arg_id.getText())

        self.functions_args[function_id] = args
        self.jasmin.write_function_declaration(function_id, args_names)

    def enterL_void(self, ctx: RaimundoParserLib.L_voidContext):
        self.stack_block.append('function')
        function_id = ctx.ID(0).getText()
        if function_id in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, function_id)

        self.symbol_table[function_id] = CustomListener(type="NoneType")

        args = []
        args_names = []
        for arg_id, arg_type in list(zip(ctx.ID()[1:], ctx.TYPE()[0:])):
            if arg_id.getText() in self.symbol_table:
                raise AlreadyDeclaredError(ctx.start.line, arg_id.getText())
            self.symbol_table[arg_id.getText()] = CustomListener(type=arg_type.getText(), local=True)
            args.append(arg_type.getText())
            args_names.append(arg_id.getText())

        self.functions_args[function_id] = args
        self.jasmin.write_function_declaration(function_id, args_names)

    def enterReturn_statement(self, ctx: RaimundoParserLib.Return_statementContext):
        if not self.__is_inside_function():
            raise ReturnException(ctx.start.line)

    def exitReturn_statement(self, ctx: RaimundoParserLib.Return_statementContext):
        self.jasmin.write_function_return(ctx.expr().val, ctx.expr().type)

    def enterFunction_call_statement(self, ctx: RaimundoParserLib.Function_call_statementContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_id)

    def enterIf_statement(self, ctx:RaimundoParserLib.If_statementContext):
        ctx.expr().inh_type = 'if'

    def enterForloop_statement(self, ctx: RaimundoParserLib.Forloop_statementContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_id)

        if not self.__is_numeric(self.symbol_table[ctx_id].type):
            raise UnexpectedTypeError(ctx.start.line, 'int', self.symbol_table[ctx_id].type)

        if len(ctx.expr()) == 1:
            ctx.expr()[0].inh_type = 'right_range'
            ctx.expr()[0].inh = self.jasmin.write_forenter_code(len(self.stack_block), True, ctx_id)
        else:
            ctx.expr()[0].inh_type = 'left_range'
            ctx.expr()[1].inh_type = 'right_range'
            ctx.expr()[0].inh = ctx_id
            ctx.expr()[1].inh = self.jasmin.write_forenter_code(len(self.stack_block), False, ctx_id)
        ctx.stack_idx = len(self.stack_block)

        self.stack_block.append('loop')

    def enterWhile_statement(self, ctx: RaimundoParserLib.While_statementContext):
        ctx.expr().inh_type = 'while'
        ctx.expr().inh = self.jasmin.write_dowhileenter_code(len(self.stack_block))
        self.stack_block.append('loop')

    def enterBreak_statement(self, ctx: RaimundoParserLib.Break_statementContext):
        if 'loop' not in self.stack_block:
            raise BreakException(ctx.start.line)

    def exitMain_function_declaration(self, ctx: RaimundoParserLib.Main_function_declarationContext):
        self.jasmin.write_main_function_end()

    def exitIf_statement(self, ctx: RaimundoParserLib.If_statementContext):
        if ctx.expr().type != 'boolean':
            raise UnexpectedTypeError(ctx.start.line, 'boolean', ctx.expr().type)
        self.jasmin.write_labelname('if_' + str(ctx.expr().end_label))

    def exitL_type(self, ctx: RaimundoParserLib.L_typeContext):
        self.jasmin.write_function_end()
        self.stack_block.pop()

    def exitL_void(self, ctx: RaimundoParserLib.L_voidContext):
        self.jasmin.write_function_return(None, 'NoneType')
        self.jasmin.write_function_end()
        self.stack_block.pop()


    def exitFunction_call_statement(self, ctx: RaimundoParserLib.Function_call_statementContext):
        function_id = ctx.ID().getText()

        if len(self.functions_args[function_id]) != len(ctx.expr()):
            raise MissingArgument(ctx.start.line, len(self.functions_args[function_id]), len(ctx.expr()))

        for expected, received in list(zip(self.functions_args[function_id], ctx.expr())):
            if expected != received.type:
                raise UnexpectedTypeError(ctx.start.line, expected, received.type)

        ctx.type = self.symbol_table[ctx.ID().getText()].type

    def exitForloop_statement(self, ctx: RaimundoParserLib.Forloop_statementContext):
        self.stack_block.pop()

        ctx_id = ctx.ID().getText()
        if len(ctx.expr()) == 1:
            self.jasmin.write_forexit_code(ctx_id, ctx.expr()[0].val, ctx.stack_idx)
        else:
            self.jasmin.write_forexit_code(ctx_id, ctx.expr()[1].val, ctx.stack_idx)

    def exitWhile_statement(self, ctx:RaimundoParserLib.While_statementContext):
        if ctx.expr().type != 'boolean':
            raise UnexpectedTypeError(ctx.start.line, 'boolean', ctx.expr().type)
        self.stack_block.pop()
        self.jasmin.write_dowhileexit_code(len(self.stack_block))


    def exitGlobal_single_variable_declaration_statement(self, ctx:RaimundoParserLib.Global_single_variable_declaration_statementContext):
        token = ctx.ID()
        if token.getText() in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, token.getText())
        self.symbol_table[token.getText()] = CustomListener(type=ctx.TYPE().getText())
        self.jasmin.create_global(token.getText(), ctx.TYPE().getText())

    def exitGlobal_multiple_variable_declaration_statement(self, ctx:RaimundoParserLib.Global_multiple_variable_declaration_statementContext):
        for token in ctx.ID():
            if token.getText() in self.symbol_table:
                raise AlreadyDeclaredError(ctx.start.line, token.getText())
            self.symbol_table[token.getText()] = CustomListener(type=ctx.TYPE().getText())
            self.jasmin.create_global(token.getText(), ctx.TYPE().getText())

    def exitLocal_single_variable_declaration_statement(self, ctx:RaimundoParserLib.Local_single_variable_declaration_statementContext):
        token = ctx.ID()
        if token.getText() in self.symbol_table:
            raise AlreadyDeclaredError(ctx.start.line, token.getText())
        self.symbol_table[token.getText()] = CustomListener(address=0, type=ctx.TYPE().getText(), local=True)
        self.jasmin.create_local(token.getText(), ctx.TYPE().getText())

    def exitLocal_multiple_variable_declaration_statement(self, ctx:RaimundoParserLib.Local_multiple_variable_declaration_statementContext):
        for token in ctx.ID():
            if token.getText() in self.symbol_table:
                raise AlreadyDeclaredError(ctx.start.line, token.getText())
            self.symbol_table[token.getText()] = CustomListener(address=0, type=ctx.TYPE().getText(), local=True)
            self.jasmin.create_local(token.getText(), ctx.TYPE().getText())

    def exitE_assigment(self, ctx: RaimundoParserLib.E_assigmentContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_id)

        expected = self.symbol_table[ctx_id].type
        received = ctx.expr().type
        if expected != received:
            raise UnexpectedTypeError(ctx.start.line, expected, received)

        self.jasmin.write_variable_store(ctx_id, ctx.expr().val)

    def exitE_plus_assigment(self, ctx:RaimundoParserLib.E_plus_assigmentContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_id)

        expected = self.symbol_table[ctx_id].type
        received = ctx.expr().type
        if expected != received:
            raise UnexpectedTypeError(ctx.start.line, expected, received)

        new_value = self.symbol_table[ctx_id].val + ctx.expr().val
        self.jasmin.write_variable_store(ctx_id, new_value)

    def exitE_mult_assigment(self, ctx:RaimundoParserLib.E_mult_assigmentContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_id)

        expected = self.symbol_table[ctx_id].type
        received = ctx.expr().type
        if expected != received:
            raise UnexpectedTypeError(ctx.start.line, expected, received)

        new_value = self.symbol_table[ctx_id].val * ctx.expr().val
        self.jasmin.write_variable_store(ctx_id, new_value)

    
    def exitInput(self, ctx: RaimundoParserLib.InputContext):
        ctx_id = ctx.ID().getText()
        if ctx_id not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_id)

        self.jasmin.write_inputfunction_code(ctx_id)

    def exitPrint_statement(self, ctx:RaimundoParserLib.Print_statementContext):
        type_val = []
        for expr in ctx.expr():
            type_val.append((expr.type, expr.val))
        self.jasmin.print(type_val)

    def exitOr_logic(self, ctx: RaimundoParserLib.Or_logicContext):
        if ctx.expr().type != 'boolean':
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.expr().type)
        elif ctx.term().type != 'boolean':
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term().type)
        else:
            ctx.type = 'boolean'

        ctx.val = self.jasmin.write_oroperator_code(ctx.expr().val, ctx.term().val)

        if ctx.inh_type == 'while':
            self.jasmin.write_inh(ctx.inh.format(ctx.val))

    def exitE_term(self, ctx: RaimundoParserLib.E_termContext):
        ctx.type = ctx.term().type
        ctx.val = ctx.term().val

        if ctx.inh_type == 'left_range':
            self.jasmin.write_variable_store(ctx.inh, ctx.val)
        elif ctx.inh_type == 'right_range':
            self.jasmin.write_inh(ctx.inh)
        elif ctx.inh_type == 'while':
            self.jasmin.write_inh(ctx.inh.format(ctx.val))
        elif ctx.inh_type == 'if':
            ctx.end_label = self.jasmin.write_ifenter_code(ctx.val)

    def exitAnd_logic(self, ctx: RaimundoParserLib.Or_logicContext):
        if ctx.term().type != 'boolean':
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term().type)
        elif ctx.term2().type != 'boolean':
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term2().type)
        else:
            ctx.type = 'boolean'

        ctx.val = self.jasmin.write_andoperator_code(ctx.term().val, ctx.term2().val)

    def exitE_term2(self, ctx: RaimundoParserLib.E_termContext):
        ctx.type = ctx.term2().type
        ctx.val = ctx.term2().val

    def exitComp_logic(self, ctx: RaimundoParserLib.Comp_logicContext):
        if ctx.term2().type != ctx.term3().type:
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term2().type, ctx.term3().type)
        ctx.type = 'boolean'
        ctx.val = self.jasmin.write_equaloperator_code(ctx.term2().type, ctx.term2().val, ctx.term3().val, self.label_id, ctx.op.text)
        self.label_id += 1

    def exitE_term3(self, ctx: RaimundoParserLib.E_termContext):
        ctx.type = ctx.term3().type
        ctx.val = ctx.term3().val

    def exitEq_logic(self, ctx: RaimundoParserLib.Eq_logicContext):
        if ctx.term3().type != ctx.term4().type:
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term3().type, ctx.term4().type)
        ctx.type = 'boolean'
        ctx.val = self.jasmin.write_equaloperator_code(ctx.term3().type, ctx.term3().val, ctx.term4().val, self.label_id, ctx.op.text)
        self.label_id += 1

    def exitE_term4(self, ctx: RaimundoParserLib.E_termContext):
        ctx.type = ctx.term4().type
        ctx.val = ctx.term4().val

    def exitSum_minus(self, ctx: RaimundoParserLib.Sum_minusContext):
        if not self.__is_numeric(ctx.term4().type):
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term4().type)
        elif not self.__is_numeric(ctx.term5().type):
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term5().type)
        elif ctx.term4().type == 'real' and ctx.term5().type == 'real':
            ctx.type = 'real'
            val1, val2 = ctx.term4().val, ctx.term5().val
        elif ctx.term4().type == 'real':
            ctx.type = 'real'
            val1, val2 = ctx.term4().val, self.jasmin.write_integertofloat_code(ctx.term5().val)
        elif ctx.term5().type == 'real':
            ctx.type = 'real'
            val1, val2 = self.jasmin.write_integertofloat_code(ctx.term4().val), ctx.term5().val
        else:
            ctx.type = 'int'
            val1, val2 = ctx.term4().val, ctx.term5().val

        if ctx.op.text == '+':
            ctx.val = self.jasmin.write_addoperator_code(ctx.type, val1, val2)
        else:
            ctx.val = self.jasmin.write_suboperator_code(ctx.type, val1, val2)

    def exitE_term5(self, ctx: RaimundoParserLib.E_termContext):
        ctx.type = ctx.term5().type
        ctx.val = ctx.term5().val

    def exitTime_div(self, ctx: RaimundoParserLib.Time_divContext):
        if not self.__is_numeric(ctx.term5().type):
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term5().type)
        if not self.__is_numeric(ctx.term6().type):
            raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term6().type)
        elif ctx.term5().type == 'real' and ctx.term6().type == 'real':
            ctx.type = 'real'
            val1, val2 = ctx.term5().val, ctx.term6().val
        elif ctx.term5().type == 'real':
            ctx.type = 'real'
            val1, val2 = ctx.term5().val, self.jasmin.write_integertofloat_code(ctx.term6().val)
        elif ctx.term6().type == 'real':
            ctx.type = 'real'
            val1, val2 = self.jasmin.write_integertofloat_code(ctx.term5().val), ctx.term6().val
        else:
            ctx.type = 'int'
            val1, val2 = ctx.term5().val, ctx.term6().val

        if ctx.op.text == '*':
            ctx.val = self.jasmin.write_multiplication_code(ctx.type, val1, val2)
        else:
            ctx.val = self.jasmin.write_division_code(ctx.type, val1, val2)

    def exitE_term6(self, ctx: RaimundoParserLib.E_termContext):
        ctx.type = ctx.term6().type
        ctx.val = ctx.term6().val

    def exitMinus_not(self, ctx: RaimundoParserLib.Minus_notContext):
        if ctx.op.text == '-':
            if self.__is_numeric(ctx.term6().type):
                ctx.type = ctx.term6().type
            else:
                raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term6().type)
        elif ctx.op.text == '!':
            if ctx.term6().type == 'boolean':
                ctx.type = 'boolean'
            else:
                raise ExpressionTypeError(ctx.start.line, ctx.op.text, ctx.term6().type)

            ctx.val = self.jasmin.write_notoperator_code(ctx.term6().val)

    def exitE_factor(self, ctx: RaimundoParserLib.E_factorContext):
        ctx.type = ctx.factor().type
        ctx.val = ctx.factor().val

    def exitL_expr(self, ctx: RaimundoParserLib.L_exprContext):
        ctx.type = ctx.expr().type
        ctx.val = ctx.expr().val

    def exitL_id(self, ctx: RaimundoParserLib.L_idContext):
        ctx_id = ctx.ID().getText()

        if ctx_id not in self.symbol_table:
            raise NonDeclaredVariableError(ctx.start.line, ctx_id)
        ctx.type = self.symbol_table[ctx_id].type
        ctx.val = self.jasmin.write_variable_load(ctx_id)

    def exitL_int_value(self, ctx: RaimundoParserLib.L_int_valueContext):
        ctx.type = 'int'
        ctx.val = self.jasmin.write_store_code(ctx.getText(), ctx.type)

    def exitL_float_value(self, ctx: RaimundoParserLib.L_float_valueContext):
        ctx.type = 'real'
        ctx.val = self.jasmin.write_store_code(ctx.getText(), ctx.type)

    def exitL_str_value(self, ctx: RaimundoParserLib.L_str_valueContext):
        ctx.type = 'string'
        ctx.val = self.jasmin.write_store_code(ctx.getText(), ctx.type)

    def exitL_bool_value(self, ctx: RaimundoParserLib.L_bool_valueContext):
        ctx.type = 'boolean'
        ctx.val = self.jasmin.write_store_code(0 if ctx.getText() == 'False' else 1, ctx.type)

    def exitFunction_call_statement(self, ctx: RaimundoParserLib.Function_call_statementContext):
        ctx.type = self.symbol_table[ctx.ID().getText()].type
        args = []
        types = []
        for exp in ctx.expr():
            args.append(exp.val)
            types.append(exp.type)
        ctx.val = self.jasmin.write_function_call(ctx.ID().getText(), args, types)

    def exitL_function_call(self, ctx: RaimundoParserLib.L_function_callContext):
        target = ctx.function_call_statement()
        ctx.type = target.type
        ctx.val = target.val

    def exitProgram(self, ctx: RaimundoParserLib.ProgramContext):
        self.jasmin.close_file()

    def exitBreak_statement(self, ctx:RaimundoParserLib.Break_statementContext):
        self.jasmin.write_loopbreak_code(len(self.stack_block) - 1)
