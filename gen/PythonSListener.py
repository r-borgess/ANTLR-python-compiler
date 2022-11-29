# Generated from /home/jpedro/workspace/novo_compilador/Raimundo.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RaimundoParser import RaimundoParser
else:
    from RaimundoParser import RaimundoParser

# This class defines a complete listener for a parse tree produced by RaimundoParser.
class RaimundoListener(ParseTreeListener):

    # Enter a parse tree produced by RaimundoParser#program.
    def enterProgram(self, ctx:RaimundoParser.ProgramContext):
        pass

    # Exit a parse tree produced by RaimundoParser#program.
    def exitProgram(self, ctx:RaimundoParser.ProgramContext):
        pass


    # Enter a parse tree produced by RaimundoParser#global_variables_declaration.
    def enterGlobal_variables_declaration(self, ctx:RaimundoParser.Global_variables_declarationContext):
        pass

    # Exit a parse tree produced by RaimundoParser#global_variables_declaration.
    def exitGlobal_variables_declaration(self, ctx:RaimundoParser.Global_variables_declarationContext):
        pass


    # Enter a parse tree produced by RaimundoParser#functions_declaration.
    def enterFunctions_declaration(self, ctx:RaimundoParser.Functions_declarationContext):
        pass

    # Exit a parse tree produced by RaimundoParser#functions_declaration.
    def exitFunctions_declaration(self, ctx:RaimundoParser.Functions_declarationContext):
        pass


    # Enter a parse tree produced by RaimundoParser#main_function_declaration.
    def enterMain_function_declaration(self, ctx:RaimundoParser.Main_function_declarationContext):
        pass

    # Exit a parse tree produced by RaimundoParser#main_function_declaration.
    def exitMain_function_declaration(self, ctx:RaimundoParser.Main_function_declarationContext):
        pass


    # Enter a parse tree produced by RaimundoParser#function_body_statements.
    def enterFunction_body_statements(self, ctx:RaimundoParser.Function_body_statementsContext):
        pass

    # Exit a parse tree produced by RaimundoParser#function_body_statements.
    def exitFunction_body_statements(self, ctx:RaimundoParser.Function_body_statementsContext):
        pass


    # Enter a parse tree produced by RaimundoParser#l_type.
    def enterL_type(self, ctx:RaimundoParser.L_typeContext):
        pass

    # Exit a parse tree produced by RaimundoParser#l_type.
    def exitL_type(self, ctx:RaimundoParser.L_typeContext):
        pass


    # Enter a parse tree produced by RaimundoParser#l_void.
    def enterL_void(self, ctx:RaimundoParser.L_voidContext):
        pass

    # Exit a parse tree produced by RaimundoParser#l_void.
    def exitL_void(self, ctx:RaimundoParser.L_voidContext):
        pass


    # Enter a parse tree produced by RaimundoParser#return_statement.
    def enterReturn_statement(self, ctx:RaimundoParser.Return_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#return_statement.
    def exitReturn_statement(self, ctx:RaimundoParser.Return_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#function_call_statement.
    def enterFunction_call_statement(self, ctx:RaimundoParser.Function_call_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#function_call_statement.
    def exitFunction_call_statement(self, ctx:RaimundoParser.Function_call_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#forloop_statement.
    def enterForloop_statement(self, ctx:RaimundoParser.Forloop_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#forloop_statement.
    def exitForloop_statement(self, ctx:RaimundoParser.Forloop_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#while_statement.
    def enterWhile_statement(self, ctx:RaimundoParser.While_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#while_statement.
    def exitWhile_statement(self, ctx:RaimundoParser.While_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#break_statement.
    def enterBreak_statement(self, ctx:RaimundoParser.Break_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#break_statement.
    def exitBreak_statement(self, ctx:RaimundoParser.Break_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#if_statement.
    def enterIf_statement(self, ctx:RaimundoParser.If_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#if_statement.
    def exitIf_statement(self, ctx:RaimundoParser.If_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#else_statement.
    def enterElse_statement(self, ctx:RaimundoParser.Else_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#else_statement.
    def exitElse_statement(self, ctx:RaimundoParser.Else_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#print_statement.
    def enterPrint_statement(self, ctx:RaimundoParser.Print_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#print_statement.
    def exitPrint_statement(self, ctx:RaimundoParser.Print_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#global_variable_declaration_statement.
    def enterGlobal_variable_declaration_statement(self, ctx:RaimundoParser.Global_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#global_variable_declaration_statement.
    def exitGlobal_variable_declaration_statement(self, ctx:RaimundoParser.Global_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#global_single_variable_declaration_statement.
    def enterGlobal_single_variable_declaration_statement(self, ctx:RaimundoParser.Global_single_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#global_single_variable_declaration_statement.
    def exitGlobal_single_variable_declaration_statement(self, ctx:RaimundoParser.Global_single_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#global_multiple_variable_declaration_statement.
    def enterGlobal_multiple_variable_declaration_statement(self, ctx:RaimundoParser.Global_multiple_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#global_multiple_variable_declaration_statement.
    def exitGlobal_multiple_variable_declaration_statement(self, ctx:RaimundoParser.Global_multiple_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#local_variable_declaration_statement.
    def enterLocal_variable_declaration_statement(self, ctx:RaimundoParser.Local_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#local_variable_declaration_statement.
    def exitLocal_variable_declaration_statement(self, ctx:RaimundoParser.Local_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#local_single_variable_declaration_statement.
    def enterLocal_single_variable_declaration_statement(self, ctx:RaimundoParser.Local_single_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#local_single_variable_declaration_statement.
    def exitLocal_single_variable_declaration_statement(self, ctx:RaimundoParser.Local_single_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#local_multiple_variable_declaration_statement.
    def enterLocal_multiple_variable_declaration_statement(self, ctx:RaimundoParser.Local_multiple_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by RaimundoParser#local_multiple_variable_declaration_statement.
    def exitLocal_multiple_variable_declaration_statement(self, ctx:RaimundoParser.Local_multiple_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by RaimundoParser#e_assigment.
    def enterE_assigment(self, ctx:RaimundoParser.E_assigmentContext):
        pass

    # Exit a parse tree produced by RaimundoParser#e_assigment.
    def exitE_assigment(self, ctx:RaimundoParser.E_assigmentContext):
        pass


    # Enter a parse tree produced by RaimundoParser#input.
    def enterInput(self, ctx:RaimundoParser.InputContext):
        pass

    # Exit a parse tree produced by RaimundoParser#input.
    def exitInput(self, ctx:RaimundoParser.InputContext):
        pass


    # Enter a parse tree produced by RaimundoParser#e_plus_assigment.
    def enterE_plus_assigment(self, ctx:RaimundoParser.E_plus_assigmentContext):
        pass

    # Exit a parse tree produced by RaimundoParser#e_plus_assigment.
    def exitE_plus_assigment(self, ctx:RaimundoParser.E_plus_assigmentContext):
        pass


    # Enter a parse tree produced by RaimundoParser#e_mult_assigment.
    def enterE_mult_assigment(self, ctx:RaimundoParser.E_mult_assigmentContext):
        pass

    # Exit a parse tree produced by RaimundoParser#e_mult_assigment.
    def exitE_mult_assigment(self, ctx:RaimundoParser.E_mult_assigmentContext):
        pass


    # Enter a parse tree produced by RaimundoParser#or_logic.
    def enterOr_logic(self, ctx:RaimundoParser.Or_logicContext):
        pass

    # Exit a parse tree produced by RaimundoParser#or_logic.
    def exitOr_logic(self, ctx:RaimundoParser.Or_logicContext):
        pass


    # Enter a parse tree produced by RaimundoParser#e_term.
    def enterE_term(self, ctx:RaimundoParser.E_termContext):
        pass

    # Exit a parse tree produced by RaimundoParser#e_term.
    def exitE_term(self, ctx:RaimundoParser.E_termContext):
        pass


    # Enter a parse tree produced by RaimundoParser#and_logic.
    def enterAnd_logic(self, ctx:RaimundoParser.And_logicContext):
        pass

    # Exit a parse tree produced by RaimundoParser#and_logic.
    def exitAnd_logic(self, ctx:RaimundoParser.And_logicContext):
        pass


    # Enter a parse tree produced by RaimundoParser#e_term2.
    def enterE_term2(self, ctx:RaimundoParser.E_term2Context):
        pass

    # Exit a parse tree produced by RaimundoParser#e_term2.
    def exitE_term2(self, ctx:RaimundoParser.E_term2Context):
        pass


    # Enter a parse tree produced by RaimundoParser#comp_logic.
    def enterComp_logic(self, ctx:RaimundoParser.Comp_logicContext):
        pass

    # Exit a parse tree produced by RaimundoParser#comp_logic.
    def exitComp_logic(self, ctx:RaimundoParser.Comp_logicContext):
        pass


    # Enter a parse tree produced by RaimundoParser#e_term3.
    def enterE_term3(self, ctx:RaimundoParser.E_term3Context):
        pass

    # Exit a parse tree produced by RaimundoParser#e_term3.
    def exitE_term3(self, ctx:RaimundoParser.E_term3Context):
        pass


    # Enter a parse tree produced by RaimundoParser#eq_logic.
    def enterEq_logic(self, ctx:RaimundoParser.Eq_logicContext):
        pass

    # Exit a parse tree produced by RaimundoParser#eq_logic.
    def exitEq_logic(self, ctx:RaimundoParser.Eq_logicContext):
        pass


    # Enter a parse tree produced by RaimundoParser#e_term4.
    def enterE_term4(self, ctx:RaimundoParser.E_term4Context):
        pass

    # Exit a parse tree produced by RaimundoParser#e_term4.
    def exitE_term4(self, ctx:RaimundoParser.E_term4Context):
        pass


    # Enter a parse tree produced by RaimundoParser#sum_minus.
    def enterSum_minus(self, ctx:RaimundoParser.Sum_minusContext):
        pass

    # Exit a parse tree produced by RaimundoParser#sum_minus.
    def exitSum_minus(self, ctx:RaimundoParser.Sum_minusContext):
        pass


    # Enter a parse tree produced by RaimundoParser#e_term5.
    def enterE_term5(self, ctx:RaimundoParser.E_term5Context):
        pass

    # Exit a parse tree produced by RaimundoParser#e_term5.
    def exitE_term5(self, ctx:RaimundoParser.E_term5Context):
        pass


    # Enter a parse tree produced by RaimundoParser#e_term6.
    def enterE_term6(self, ctx:RaimundoParser.E_term6Context):
        pass

    # Exit a parse tree produced by RaimundoParser#e_term6.
    def exitE_term6(self, ctx:RaimundoParser.E_term6Context):
        pass


    # Enter a parse tree produced by RaimundoParser#time_div.
    def enterTime_div(self, ctx:RaimundoParser.Time_divContext):
        pass

    # Exit a parse tree produced by RaimundoParser#time_div.
    def exitTime_div(self, ctx:RaimundoParser.Time_divContext):
        pass


    # Enter a parse tree produced by RaimundoParser#minus_not.
    def enterMinus_not(self, ctx:RaimundoParser.Minus_notContext):
        pass

    # Exit a parse tree produced by RaimundoParser#minus_not.
    def exitMinus_not(self, ctx:RaimundoParser.Minus_notContext):
        pass


    # Enter a parse tree produced by RaimundoParser#e_factor.
    def enterE_factor(self, ctx:RaimundoParser.E_factorContext):
        pass

    # Exit a parse tree produced by RaimundoParser#e_factor.
    def exitE_factor(self, ctx:RaimundoParser.E_factorContext):
        pass


    # Enter a parse tree produced by RaimundoParser#l_expr.
    def enterL_expr(self, ctx:RaimundoParser.L_exprContext):
        pass

    # Exit a parse tree produced by RaimundoParser#l_expr.
    def exitL_expr(self, ctx:RaimundoParser.L_exprContext):
        pass


    # Enter a parse tree produced by RaimundoParser#l_function_call.
    def enterL_function_call(self, ctx:RaimundoParser.L_function_callContext):
        pass

    # Exit a parse tree produced by RaimundoParser#l_function_call.
    def exitL_function_call(self, ctx:RaimundoParser.L_function_callContext):
        pass


    # Enter a parse tree produced by RaimundoParser#l_id.
    def enterL_id(self, ctx:RaimundoParser.L_idContext):
        pass

    # Exit a parse tree produced by RaimundoParser#l_id.
    def exitL_id(self, ctx:RaimundoParser.L_idContext):
        pass


    # Enter a parse tree produced by RaimundoParser#l_int_value.
    def enterL_int_value(self, ctx:RaimundoParser.L_int_valueContext):
        pass

    # Exit a parse tree produced by RaimundoParser#l_int_value.
    def exitL_int_value(self, ctx:RaimundoParser.L_int_valueContext):
        pass


    # Enter a parse tree produced by RaimundoParser#l_float_value.
    def enterL_float_value(self, ctx:RaimundoParser.L_float_valueContext):
        pass

    # Exit a parse tree produced by RaimundoParser#l_float_value.
    def exitL_float_value(self, ctx:RaimundoParser.L_float_valueContext):
        pass


    # Enter a parse tree produced by RaimundoParser#l_str_value.
    def enterL_str_value(self, ctx:RaimundoParser.L_str_valueContext):
        pass

    # Exit a parse tree produced by RaimundoParser#l_str_value.
    def exitL_str_value(self, ctx:RaimundoParser.L_str_valueContext):
        pass


    # Enter a parse tree produced by RaimundoParser#l_bool_value.
    def enterL_bool_value(self, ctx:RaimundoParser.L_bool_valueContext):
        pass

    # Exit a parse tree produced by RaimundoParser#l_bool_value.
    def exitL_bool_value(self, ctx:RaimundoParser.L_bool_valueContext):
        pass


    # Enter a parse tree produced by RaimundoParser#r_input.
    def enterR_input(self, ctx:RaimundoParser.R_inputContext):
        pass

    # Exit a parse tree produced by RaimundoParser#r_input.
    def exitR_input(self, ctx:RaimundoParser.R_inputContext):
        pass



del RaimundoParser
