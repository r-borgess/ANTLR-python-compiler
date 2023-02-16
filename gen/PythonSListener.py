# Generated from C:/Users/rodri/novo_compilador\PythonS.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonSParser import PythonSParser
else:
    from PythonSParser import PythonSParser

# This class defines a complete listener for a parse tree produced by PythonSParser.
class PythonSListener(ParseTreeListener):

    # Enter a parse tree produced by PythonSParser#program.
    def enterProgram(self, ctx:PythonSParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonSParser#program.
    def exitProgram(self, ctx:PythonSParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonSParser#global_variables_declaration.
    def enterGlobal_variables_declaration(self, ctx:PythonSParser.Global_variables_declarationContext):
        pass

    # Exit a parse tree produced by PythonSParser#global_variables_declaration.
    def exitGlobal_variables_declaration(self, ctx:PythonSParser.Global_variables_declarationContext):
        pass


    # Enter a parse tree produced by PythonSParser#functions_declaration.
    def enterFunctions_declaration(self, ctx:PythonSParser.Functions_declarationContext):
        pass

    # Exit a parse tree produced by PythonSParser#functions_declaration.
    def exitFunctions_declaration(self, ctx:PythonSParser.Functions_declarationContext):
        pass


    # Enter a parse tree produced by PythonSParser#main_function_declaration.
    def enterMain_function_declaration(self, ctx:PythonSParser.Main_function_declarationContext):
        pass

    # Exit a parse tree produced by PythonSParser#main_function_declaration.
    def exitMain_function_declaration(self, ctx:PythonSParser.Main_function_declarationContext):
        pass


    # Enter a parse tree produced by PythonSParser#function_body_statements.
    def enterFunction_body_statements(self, ctx:PythonSParser.Function_body_statementsContext):
        pass

    # Exit a parse tree produced by PythonSParser#function_body_statements.
    def exitFunction_body_statements(self, ctx:PythonSParser.Function_body_statementsContext):
        pass


    # Enter a parse tree produced by PythonSParser#l_type.
    def enterL_type(self, ctx:PythonSParser.L_typeContext):
        pass

    # Exit a parse tree produced by PythonSParser#l_type.
    def exitL_type(self, ctx:PythonSParser.L_typeContext):
        pass


    # Enter a parse tree produced by PythonSParser#l_void.
    def enterL_void(self, ctx:PythonSParser.L_voidContext):
        pass

    # Exit a parse tree produced by PythonSParser#l_void.
    def exitL_void(self, ctx:PythonSParser.L_voidContext):
        pass


    # Enter a parse tree produced by PythonSParser#return_statement.
    def enterReturn_statement(self, ctx:PythonSParser.Return_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#return_statement.
    def exitReturn_statement(self, ctx:PythonSParser.Return_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#function_call_statement.
    def enterFunction_call_statement(self, ctx:PythonSParser.Function_call_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#function_call_statement.
    def exitFunction_call_statement(self, ctx:PythonSParser.Function_call_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#forloop_statement.
    def enterForloop_statement(self, ctx:PythonSParser.Forloop_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#forloop_statement.
    def exitForloop_statement(self, ctx:PythonSParser.Forloop_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#while_statement.
    def enterWhile_statement(self, ctx:PythonSParser.While_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#while_statement.
    def exitWhile_statement(self, ctx:PythonSParser.While_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#break_statement.
    def enterBreak_statement(self, ctx:PythonSParser.Break_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#break_statement.
    def exitBreak_statement(self, ctx:PythonSParser.Break_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#if_statement.
    def enterIf_statement(self, ctx:PythonSParser.If_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#if_statement.
    def exitIf_statement(self, ctx:PythonSParser.If_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#else_statement.
    def enterElse_statement(self, ctx:PythonSParser.Else_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#else_statement.
    def exitElse_statement(self, ctx:PythonSParser.Else_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#print_statement.
    def enterPrint_statement(self, ctx:PythonSParser.Print_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#print_statement.
    def exitPrint_statement(self, ctx:PythonSParser.Print_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#global_variable_declaration_statement.
    def enterGlobal_variable_declaration_statement(self, ctx:PythonSParser.Global_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#global_variable_declaration_statement.
    def exitGlobal_variable_declaration_statement(self, ctx:PythonSParser.Global_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#global_single_variable_declaration_statement.
    def enterGlobal_single_variable_declaration_statement(self, ctx:PythonSParser.Global_single_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#global_single_variable_declaration_statement.
    def exitGlobal_single_variable_declaration_statement(self, ctx:PythonSParser.Global_single_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#global_multiple_variable_declaration_statement.
    def enterGlobal_multiple_variable_declaration_statement(self, ctx:PythonSParser.Global_multiple_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#global_multiple_variable_declaration_statement.
    def exitGlobal_multiple_variable_declaration_statement(self, ctx:PythonSParser.Global_multiple_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#local_variable_declaration_statement.
    def enterLocal_variable_declaration_statement(self, ctx:PythonSParser.Local_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#local_variable_declaration_statement.
    def exitLocal_variable_declaration_statement(self, ctx:PythonSParser.Local_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#local_single_variable_declaration_statement.
    def enterLocal_single_variable_declaration_statement(self, ctx:PythonSParser.Local_single_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#local_single_variable_declaration_statement.
    def exitLocal_single_variable_declaration_statement(self, ctx:PythonSParser.Local_single_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#local_multiple_variable_declaration_statement.
    def enterLocal_multiple_variable_declaration_statement(self, ctx:PythonSParser.Local_multiple_variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by PythonSParser#local_multiple_variable_declaration_statement.
    def exitLocal_multiple_variable_declaration_statement(self, ctx:PythonSParser.Local_multiple_variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by PythonSParser#e_assigment.
    def enterE_assigment(self, ctx:PythonSParser.E_assigmentContext):
        pass

    # Exit a parse tree produced by PythonSParser#e_assigment.
    def exitE_assigment(self, ctx:PythonSParser.E_assigmentContext):
        pass


    # Enter a parse tree produced by PythonSParser#input.
    def enterInput(self, ctx:PythonSParser.InputContext):
        pass

    # Exit a parse tree produced by PythonSParser#input.
    def exitInput(self, ctx:PythonSParser.InputContext):
        pass


    # Enter a parse tree produced by PythonSParser#e_plus_assigment.
    def enterE_plus_assigment(self, ctx:PythonSParser.E_plus_assigmentContext):
        pass

    # Exit a parse tree produced by PythonSParser#e_plus_assigment.
    def exitE_plus_assigment(self, ctx:PythonSParser.E_plus_assigmentContext):
        pass


    # Enter a parse tree produced by PythonSParser#e_mult_assigment.
    def enterE_mult_assigment(self, ctx:PythonSParser.E_mult_assigmentContext):
        pass

    # Exit a parse tree produced by PythonSParser#e_mult_assigment.
    def exitE_mult_assigment(self, ctx:PythonSParser.E_mult_assigmentContext):
        pass


    # Enter a parse tree produced by PythonSParser#or_logic.
    def enterOr_logic(self, ctx:PythonSParser.Or_logicContext):
        pass

    # Exit a parse tree produced by PythonSParser#or_logic.
    def exitOr_logic(self, ctx:PythonSParser.Or_logicContext):
        pass


    # Enter a parse tree produced by PythonSParser#e_term.
    def enterE_term(self, ctx:PythonSParser.E_termContext):
        pass

    # Exit a parse tree produced by PythonSParser#e_term.
    def exitE_term(self, ctx:PythonSParser.E_termContext):
        pass


    # Enter a parse tree produced by PythonSParser#and_logic.
    def enterAnd_logic(self, ctx:PythonSParser.And_logicContext):
        pass

    # Exit a parse tree produced by PythonSParser#and_logic.
    def exitAnd_logic(self, ctx:PythonSParser.And_logicContext):
        pass


    # Enter a parse tree produced by PythonSParser#e_term2.
    def enterE_term2(self, ctx:PythonSParser.E_term2Context):
        pass

    # Exit a parse tree produced by PythonSParser#e_term2.
    def exitE_term2(self, ctx:PythonSParser.E_term2Context):
        pass


    # Enter a parse tree produced by PythonSParser#comp_logic.
    def enterComp_logic(self, ctx:PythonSParser.Comp_logicContext):
        pass

    # Exit a parse tree produced by PythonSParser#comp_logic.
    def exitComp_logic(self, ctx:PythonSParser.Comp_logicContext):
        pass


    # Enter a parse tree produced by PythonSParser#e_term3.
    def enterE_term3(self, ctx:PythonSParser.E_term3Context):
        pass

    # Exit a parse tree produced by PythonSParser#e_term3.
    def exitE_term3(self, ctx:PythonSParser.E_term3Context):
        pass


    # Enter a parse tree produced by PythonSParser#eq_logic.
    def enterEq_logic(self, ctx:PythonSParser.Eq_logicContext):
        pass

    # Exit a parse tree produced by PythonSParser#eq_logic.
    def exitEq_logic(self, ctx:PythonSParser.Eq_logicContext):
        pass


    # Enter a parse tree produced by PythonSParser#e_term4.
    def enterE_term4(self, ctx:PythonSParser.E_term4Context):
        pass

    # Exit a parse tree produced by PythonSParser#e_term4.
    def exitE_term4(self, ctx:PythonSParser.E_term4Context):
        pass


    # Enter a parse tree produced by PythonSParser#sum_minus.
    def enterSum_minus(self, ctx:PythonSParser.Sum_minusContext):
        pass

    # Exit a parse tree produced by PythonSParser#sum_minus.
    def exitSum_minus(self, ctx:PythonSParser.Sum_minusContext):
        pass


    # Enter a parse tree produced by PythonSParser#e_term5.
    def enterE_term5(self, ctx:PythonSParser.E_term5Context):
        pass

    # Exit a parse tree produced by PythonSParser#e_term5.
    def exitE_term5(self, ctx:PythonSParser.E_term5Context):
        pass


    # Enter a parse tree produced by PythonSParser#e_term6.
    def enterE_term6(self, ctx:PythonSParser.E_term6Context):
        pass

    # Exit a parse tree produced by PythonSParser#e_term6.
    def exitE_term6(self, ctx:PythonSParser.E_term6Context):
        pass


    # Enter a parse tree produced by PythonSParser#time_div.
    def enterTime_div(self, ctx:PythonSParser.Time_divContext):
        pass

    # Exit a parse tree produced by PythonSParser#time_div.
    def exitTime_div(self, ctx:PythonSParser.Time_divContext):
        pass


    # Enter a parse tree produced by PythonSParser#minus_not.
    def enterMinus_not(self, ctx:PythonSParser.Minus_notContext):
        pass

    # Exit a parse tree produced by PythonSParser#minus_not.
    def exitMinus_not(self, ctx:PythonSParser.Minus_notContext):
        pass


    # Enter a parse tree produced by PythonSParser#e_factor.
    def enterE_factor(self, ctx:PythonSParser.E_factorContext):
        pass

    # Exit a parse tree produced by PythonSParser#e_factor.
    def exitE_factor(self, ctx:PythonSParser.E_factorContext):
        pass


    # Enter a parse tree produced by PythonSParser#l_expr.
    def enterL_expr(self, ctx:PythonSParser.L_exprContext):
        pass

    # Exit a parse tree produced by PythonSParser#l_expr.
    def exitL_expr(self, ctx:PythonSParser.L_exprContext):
        pass


    # Enter a parse tree produced by PythonSParser#l_function_call.
    def enterL_function_call(self, ctx:PythonSParser.L_function_callContext):
        pass

    # Exit a parse tree produced by PythonSParser#l_function_call.
    def exitL_function_call(self, ctx:PythonSParser.L_function_callContext):
        pass


    # Enter a parse tree produced by PythonSParser#l_id.
    def enterL_id(self, ctx:PythonSParser.L_idContext):
        pass

    # Exit a parse tree produced by PythonSParser#l_id.
    def exitL_id(self, ctx:PythonSParser.L_idContext):
        pass


    # Enter a parse tree produced by PythonSParser#l_int_value.
    def enterL_int_value(self, ctx:PythonSParser.L_int_valueContext):
        pass

    # Exit a parse tree produced by PythonSParser#l_int_value.
    def exitL_int_value(self, ctx:PythonSParser.L_int_valueContext):
        pass


    # Enter a parse tree produced by PythonSParser#l_float_value.
    def enterL_float_value(self, ctx:PythonSParser.L_float_valueContext):
        pass

    # Exit a parse tree produced by PythonSParser#l_float_value.
    def exitL_float_value(self, ctx:PythonSParser.L_float_valueContext):
        pass


    # Enter a parse tree produced by PythonSParser#l_str_value.
    def enterL_str_value(self, ctx:PythonSParser.L_str_valueContext):
        pass

    # Exit a parse tree produced by PythonSParser#l_str_value.
    def exitL_str_value(self, ctx:PythonSParser.L_str_valueContext):
        pass


    # Enter a parse tree produced by PythonSParser#l_bool_value.
    def enterL_bool_value(self, ctx:PythonSParser.L_bool_valueContext):
        pass

    # Exit a parse tree produced by PythonSParser#l_bool_value.
    def exitL_bool_value(self, ctx:PythonSParser.L_bool_valueContext):
        pass


    # Enter a parse tree produced by PythonSParser#r_input.
    def enterR_input(self, ctx:PythonSParser.R_inputContext):
        pass

    # Exit a parse tree produced by PythonSParser#r_input.
    def exitR_input(self, ctx:PythonSParser.R_inputContext):
        pass



del PythonSParser