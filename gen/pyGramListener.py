# Generated from /home/jpedro/workspace/jpedrodsp/novo_compilador/pyGram.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pyGramParser import pyGramParser
else:
    from pyGramParser import pyGramParser

# This class defines a complete listener for a parse tree produced by pyGramParser.
class pyGramListener(ParseTreeListener):

    # Enter a parse tree produced by pyGramParser#program.
    def enterProgram(self, ctx:pyGramParser.ProgramContext):
        pass

    # Exit a parse tree produced by pyGramParser#program.
    def exitProgram(self, ctx:pyGramParser.ProgramContext):
        pass


    # Enter a parse tree produced by pyGramParser#global_variables_declaration.
    def enterGlobal_variables_declaration(self, ctx:pyGramParser.Global_variables_declarationContext):
        pass

    # Exit a parse tree produced by pyGramParser#global_variables_declaration.
    def exitGlobal_variables_declaration(self, ctx:pyGramParser.Global_variables_declarationContext):
        pass


    # Enter a parse tree produced by pyGramParser#functions_declaration.
    def enterFunctions_declaration(self, ctx:pyGramParser.Functions_declarationContext):
        pass

    # Exit a parse tree produced by pyGramParser#functions_declaration.
    def exitFunctions_declaration(self, ctx:pyGramParser.Functions_declarationContext):
        pass


    # Enter a parse tree produced by pyGramParser#main_function_declaration.
    def enterMain_function_declaration(self, ctx:pyGramParser.Main_function_declarationContext):
        pass

    # Exit a parse tree produced by pyGramParser#main_function_declaration.
    def exitMain_function_declaration(self, ctx:pyGramParser.Main_function_declarationContext):
        pass


    # Enter a parse tree produced by pyGramParser#function_body_statements.
    def enterFunction_body_statements(self, ctx:pyGramParser.Function_body_statementsContext):
        pass

    # Exit a parse tree produced by pyGramParser#function_body_statements.
    def exitFunction_body_statements(self, ctx:pyGramParser.Function_body_statementsContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_type.
    def enterL_type(self, ctx:pyGramParser.L_typeContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_type.
    def exitL_type(self, ctx:pyGramParser.L_typeContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_void.
    def enterL_void(self, ctx:pyGramParser.L_voidContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_void.
    def exitL_void(self, ctx:pyGramParser.L_voidContext):
        pass


    # Enter a parse tree produced by pyGramParser#return_statement.
    def enterReturn_statement(self, ctx:pyGramParser.Return_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#return_statement.
    def exitReturn_statement(self, ctx:pyGramParser.Return_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#function_call_statement.
    def enterFunction_call_statement(self, ctx:pyGramParser.Function_call_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#function_call_statement.
    def exitFunction_call_statement(self, ctx:pyGramParser.Function_call_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#forloop_statement.
    def enterForloop_statement(self, ctx:pyGramParser.Forloop_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#forloop_statement.
    def exitForloop_statement(self, ctx:pyGramParser.Forloop_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#while_statement.
    def enterWhile_statement(self, ctx:pyGramParser.While_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#while_statement.
    def exitWhile_statement(self, ctx:pyGramParser.While_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#break_statement.
    def enterBreak_statement(self, ctx:pyGramParser.Break_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#break_statement.
    def exitBreak_statement(self, ctx:pyGramParser.Break_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#if_statement.
    def enterIf_statement(self, ctx:pyGramParser.If_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#if_statement.
    def exitIf_statement(self, ctx:pyGramParser.If_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#else_statement.
    def enterElse_statement(self, ctx:pyGramParser.Else_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#else_statement.
    def exitElse_statement(self, ctx:pyGramParser.Else_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#print_statement.
    def enterPrint_statement(self, ctx:pyGramParser.Print_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#print_statement.
    def exitPrint_statement(self, ctx:pyGramParser.Print_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#global_variable_declaration_statement.
    def enterGlobal_variable_declaration_statement(self, ctx:pyGramParser.Global_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#global_variable_declaration_statement.
    def exitGlobal_variable_declaration_statement(self, ctx:pyGramParser.Global_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#global_single_variable_declaration_statement.
    def enterGlobal_single_variable_declaration_statement(self, ctx:pyGramParser.Global_single_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#global_single_variable_declaration_statement.
    def exitGlobal_single_variable_declaration_statement(self, ctx:pyGramParser.Global_single_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#global_multiple_variable_declaration_statement.
    def enterGlobal_multiple_variable_declaration_statement(self, ctx:pyGramParser.Global_multiple_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#global_multiple_variable_declaration_statement.
    def exitGlobal_multiple_variable_declaration_statement(self, ctx:pyGramParser.Global_multiple_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#local_variable_declaration_statement.
    def enterLocal_variable_declaration_statement(self, ctx:pyGramParser.Local_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#local_variable_declaration_statement.
    def exitLocal_variable_declaration_statement(self, ctx:pyGramParser.Local_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#local_single_variable_declaration_statement.
    def enterLocal_single_variable_declaration_statement(self, ctx:pyGramParser.Local_single_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#local_single_variable_declaration_statement.
    def exitLocal_single_variable_declaration_statement(self, ctx:pyGramParser.Local_single_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#local_multiple_variable_declaration_statement.
    def enterLocal_multiple_variable_declaration_statement(self, ctx:pyGramParser.Local_multiple_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by pyGramParser#local_multiple_variable_declaration_statement.
    def exitLocal_multiple_variable_declaration_statement(self, ctx:pyGramParser.Local_multiple_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_assigment.
    def enterE_assigment(self, ctx:pyGramParser.E_assigmentContext):
        pass

    # Exit a parse tree produced by pyGramParser#e_assigment.
    def exitE_assigment(self, ctx:pyGramParser.E_assigmentContext):
        pass


    # Enter a parse tree produced by pyGramParser#input.
    def enterInput(self, ctx:pyGramParser.InputContext):
        pass

    # Exit a parse tree produced by pyGramParser#input.
    def exitInput(self, ctx:pyGramParser.InputContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_plus_assigment.
    def enterE_plus_assigment(self, ctx:pyGramParser.E_plus_assigmentContext):
        pass

    # Exit a parse tree produced by pyGramParser#e_plus_assigment.
    def exitE_plus_assigment(self, ctx:pyGramParser.E_plus_assigmentContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_mult_assigment.
    def enterE_mult_assigment(self, ctx:pyGramParser.E_mult_assigmentContext):
        pass

    # Exit a parse tree produced by pyGramParser#e_mult_assigment.
    def exitE_mult_assigment(self, ctx:pyGramParser.E_mult_assigmentContext):
        pass


    # Enter a parse tree produced by pyGramParser#or_logic.
    def enterOr_logic(self, ctx:pyGramParser.Or_logicContext):
        pass

    # Exit a parse tree produced by pyGramParser#or_logic.
    def exitOr_logic(self, ctx:pyGramParser.Or_logicContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term.
    def enterE_term(self, ctx:pyGramParser.E_termContext):
        pass

    # Exit a parse tree produced by pyGramParser#e_term.
    def exitE_term(self, ctx:pyGramParser.E_termContext):
        pass


    # Enter a parse tree produced by pyGramParser#and_logic.
    def enterAnd_logic(self, ctx:pyGramParser.And_logicContext):
        pass

    # Exit a parse tree produced by pyGramParser#and_logic.
    def exitAnd_logic(self, ctx:pyGramParser.And_logicContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term2.
    def enterE_term2(self, ctx:pyGramParser.E_term2Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term2.
    def exitE_term2(self, ctx:pyGramParser.E_term2Context):
        pass


    # Enter a parse tree produced by pyGramParser#comp_logic.
    def enterComp_logic(self, ctx:pyGramParser.Comp_logicContext):
        pass

    # Exit a parse tree produced by pyGramParser#comp_logic.
    def exitComp_logic(self, ctx:pyGramParser.Comp_logicContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term3.
    def enterE_term3(self, ctx:pyGramParser.E_term3Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term3.
    def exitE_term3(self, ctx:pyGramParser.E_term3Context):
        pass


    # Enter a parse tree produced by pyGramParser#eq_logic.
    def enterEq_logic(self, ctx:pyGramParser.Eq_logicContext):
        pass

    # Exit a parse tree produced by pyGramParser#eq_logic.
    def exitEq_logic(self, ctx:pyGramParser.Eq_logicContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term4.
    def enterE_term4(self, ctx:pyGramParser.E_term4Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term4.
    def exitE_term4(self, ctx:pyGramParser.E_term4Context):
        pass


    # Enter a parse tree produced by pyGramParser#sum_minus.
    def enterSum_minus(self, ctx:pyGramParser.Sum_minusContext):
        pass

    # Exit a parse tree produced by pyGramParser#sum_minus.
    def exitSum_minus(self, ctx:pyGramParser.Sum_minusContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_term5.
    def enterE_term5(self, ctx:pyGramParser.E_term5Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term5.
    def exitE_term5(self, ctx:pyGramParser.E_term5Context):
        pass


    # Enter a parse tree produced by pyGramParser#e_term6.
    def enterE_term6(self, ctx:pyGramParser.E_term6Context):
        pass

    # Exit a parse tree produced by pyGramParser#e_term6.
    def exitE_term6(self, ctx:pyGramParser.E_term6Context):
        pass


    # Enter a parse tree produced by pyGramParser#time_div.
    def enterTime_div(self, ctx:pyGramParser.Time_divContext):
        pass

    # Exit a parse tree produced by pyGramParser#time_div.
    def exitTime_div(self, ctx:pyGramParser.Time_divContext):
        pass


    # Enter a parse tree produced by pyGramParser#minus_not.
    def enterMinus_not(self, ctx:pyGramParser.Minus_notContext):
        pass

    # Exit a parse tree produced by pyGramParser#minus_not.
    def exitMinus_not(self, ctx:pyGramParser.Minus_notContext):
        pass


    # Enter a parse tree produced by pyGramParser#e_factor.
    def enterE_factor(self, ctx:pyGramParser.E_factorContext):
        pass

    # Exit a parse tree produced by pyGramParser#e_factor.
    def exitE_factor(self, ctx:pyGramParser.E_factorContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_expr.
    def enterL_expr(self, ctx:pyGramParser.L_exprContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_expr.
    def exitL_expr(self, ctx:pyGramParser.L_exprContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_function_call.
    def enterL_function_call(self, ctx:pyGramParser.L_function_callContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_function_call.
    def exitL_function_call(self, ctx:pyGramParser.L_function_callContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_id.
    def enterL_id(self, ctx:pyGramParser.L_idContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_id.
    def exitL_id(self, ctx:pyGramParser.L_idContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_int_value.
    def enterL_int_value(self, ctx:pyGramParser.L_int_valueContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_int_value.
    def exitL_int_value(self, ctx:pyGramParser.L_int_valueContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_float_value.
    def enterL_float_value(self, ctx:pyGramParser.L_float_valueContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_float_value.
    def exitL_float_value(self, ctx:pyGramParser.L_float_valueContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_str_value.
    def enterL_str_value(self, ctx:pyGramParser.L_str_valueContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_str_value.
    def exitL_str_value(self, ctx:pyGramParser.L_str_valueContext):
        pass


    # Enter a parse tree produced by pyGramParser#l_bool_value.
    def enterL_bool_value(self, ctx:pyGramParser.L_bool_valueContext):
        pass

    # Exit a parse tree produced by pyGramParser#l_bool_value.
    def exitL_bool_value(self, ctx:pyGramParser.L_bool_valueContext):
        pass


    # Enter a parse tree produced by pyGramParser#r_input.
    def enterR_input(self, ctx:pyGramParser.R_inputContext):
        pass

    # Exit a parse tree produced by pyGramParser#r_input.
    def exitR_input(self, ctx:pyGramParser.R_inputContext):
        pass



del pyGramParser