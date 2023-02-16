# Generated from C:/Users/rodri/novo_compilador\PythonS.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PythonSParser import PythonSParser
else:
    from PythonSParser import PythonSParser

# This class defines a complete generic visitor for a parse tree produced by PythonSParser.

class PythonSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PythonSParser#program.
    def visitProgram(self, ctx:PythonSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#global_variables_declaration.
    def visitGlobal_variables_declaration(self, ctx:PythonSParser.Global_variables_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#functions_declaration.
    def visitFunctions_declaration(self, ctx:PythonSParser.Functions_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#main_function_declaration.
    def visitMain_function_declaration(self, ctx:PythonSParser.Main_function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#function_body_statements.
    def visitFunction_body_statements(self, ctx:PythonSParser.Function_body_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#l_type.
    def visitL_type(self, ctx:PythonSParser.L_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#l_void.
    def visitL_void(self, ctx:PythonSParser.L_voidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#return_statement.
    def visitReturn_statement(self, ctx:PythonSParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:PythonSParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#forloop_statement.
    def visitForloop_statement(self, ctx:PythonSParser.Forloop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#while_statement.
    def visitWhile_statement(self, ctx:PythonSParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#break_statement.
    def visitBreak_statement(self, ctx:PythonSParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#if_statement.
    def visitIf_statement(self, ctx:PythonSParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#else_statement.
    def visitElse_statement(self, ctx:PythonSParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#print_statement.
    def visitPrint_statement(self, ctx:PythonSParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#global_variable_declaration_statement.
    def visitGlobal_variable_declaration_statement(self, ctx:PythonSParser.Global_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#global_single_variable_declaration_statement.
    def visitGlobal_single_variable_declaration_statement(self, ctx:PythonSParser.Global_single_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#global_multiple_variable_declaration_statement.
    def visitGlobal_multiple_variable_declaration_statement(self, ctx:PythonSParser.Global_multiple_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#local_variable_declaration_statement.
    def visitLocal_variable_declaration_statement(self, ctx:PythonSParser.Local_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#local_single_variable_declaration_statement.
    def visitLocal_single_variable_declaration_statement(self, ctx:PythonSParser.Local_single_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#local_multiple_variable_declaration_statement.
    def visitLocal_multiple_variable_declaration_statement(self, ctx:PythonSParser.Local_multiple_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_assigment.
    def visitE_assigment(self, ctx:PythonSParser.E_assigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#input.
    def visitInput(self, ctx:PythonSParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_plus_assigment.
    def visitE_plus_assigment(self, ctx:PythonSParser.E_plus_assigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_mult_assigment.
    def visitE_mult_assigment(self, ctx:PythonSParser.E_mult_assigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#or_logic.
    def visitOr_logic(self, ctx:PythonSParser.Or_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_term.
    def visitE_term(self, ctx:PythonSParser.E_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#and_logic.
    def visitAnd_logic(self, ctx:PythonSParser.And_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_term2.
    def visitE_term2(self, ctx:PythonSParser.E_term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#comp_logic.
    def visitComp_logic(self, ctx:PythonSParser.Comp_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_term3.
    def visitE_term3(self, ctx:PythonSParser.E_term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#eq_logic.
    def visitEq_logic(self, ctx:PythonSParser.Eq_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_term4.
    def visitE_term4(self, ctx:PythonSParser.E_term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#sum_minus.
    def visitSum_minus(self, ctx:PythonSParser.Sum_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_term5.
    def visitE_term5(self, ctx:PythonSParser.E_term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_term6.
    def visitE_term6(self, ctx:PythonSParser.E_term6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#time_div.
    def visitTime_div(self, ctx:PythonSParser.Time_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#minus_not.
    def visitMinus_not(self, ctx:PythonSParser.Minus_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#e_factor.
    def visitE_factor(self, ctx:PythonSParser.E_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#l_expr.
    def visitL_expr(self, ctx:PythonSParser.L_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#l_function_call.
    def visitL_function_call(self, ctx:PythonSParser.L_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#l_id.
    def visitL_id(self, ctx:PythonSParser.L_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#l_int_value.
    def visitL_int_value(self, ctx:PythonSParser.L_int_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#l_float_value.
    def visitL_float_value(self, ctx:PythonSParser.L_float_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#l_str_value.
    def visitL_str_value(self, ctx:PythonSParser.L_str_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#l_bool_value.
    def visitL_bool_value(self, ctx:PythonSParser.L_bool_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PythonSParser#r_input.
    def visitR_input(self, ctx:PythonSParser.R_inputContext):
        return self.visitChildren(ctx)



del PythonSParser