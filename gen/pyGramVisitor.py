# Generated from /home/jpedro/workspace/jpedrodsp/novo_compilador/Raimundo.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pyGramParser import pyGramParser
else:
    from pyGramParser import pyGramParser

# This class defines a complete generic visitor for a parse tree produced by pyGramParser.

class pyGramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pyGramParser#program.
    def visitProgram(self, ctx:pyGramParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#global_variables_declaration.
    def visitGlobal_variables_declaration(self, ctx:pyGramParser.Global_variables_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#functions_declaration.
    def visitFunctions_declaration(self, ctx:pyGramParser.Functions_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#main_function_declaration.
    def visitMain_function_declaration(self, ctx:pyGramParser.Main_function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#function_body_statements.
    def visitFunction_body_statements(self, ctx:pyGramParser.Function_body_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#l_type.
    def visitL_type(self, ctx:pyGramParser.L_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#l_void.
    def visitL_void(self, ctx:pyGramParser.L_voidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#return_statement.
    def visitReturn_statement(self, ctx:pyGramParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:pyGramParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#forloop_statement.
    def visitForloop_statement(self, ctx:pyGramParser.Forloop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#while_statement.
    def visitWhile_statement(self, ctx:pyGramParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#break_statement.
    def visitBreak_statement(self, ctx:pyGramParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#if_statement.
    def visitIf_statement(self, ctx:pyGramParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#else_statement.
    def visitElse_statement(self, ctx:pyGramParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#print_statement.
    def visitPrint_statement(self, ctx:pyGramParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#global_variable_declaration_statement.
    def visitGlobal_variable_declaration_statement(self, ctx:pyGramParser.Global_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#global_single_variable_declaration_statement.
    def visitGlobal_single_variable_declaration_statement(self, ctx:pyGramParser.Global_single_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#global_multiple_variable_declaration_statement.
    def visitGlobal_multiple_variable_declaration_statement(self, ctx:pyGramParser.Global_multiple_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#local_variable_declaration_statement.
    def visitLocal_variable_declaration_statement(self, ctx:pyGramParser.Local_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#local_single_variable_declaration_statement.
    def visitLocal_single_variable_declaration_statement(self, ctx:pyGramParser.Local_single_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#local_multiple_variable_declaration_statement.
    def visitLocal_multiple_variable_declaration_statement(self, ctx:pyGramParser.Local_multiple_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_assigment.
    def visitE_assigment(self, ctx:pyGramParser.E_assigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#input.
    def visitInput(self, ctx:pyGramParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_plus_assigment.
    def visitE_plus_assigment(self, ctx:pyGramParser.E_plus_assigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_mult_assigment.
    def visitE_mult_assigment(self, ctx:pyGramParser.E_mult_assigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#or_logic.
    def visitOr_logic(self, ctx:pyGramParser.Or_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_term.
    def visitE_term(self, ctx:pyGramParser.E_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#and_logic.
    def visitAnd_logic(self, ctx:pyGramParser.And_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_term2.
    def visitE_term2(self, ctx:pyGramParser.E_term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#comp_logic.
    def visitComp_logic(self, ctx:pyGramParser.Comp_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_term3.
    def visitE_term3(self, ctx:pyGramParser.E_term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#eq_logic.
    def visitEq_logic(self, ctx:pyGramParser.Eq_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_term4.
    def visitE_term4(self, ctx:pyGramParser.E_term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#sum_minus.
    def visitSum_minus(self, ctx:pyGramParser.Sum_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_term5.
    def visitE_term5(self, ctx:pyGramParser.E_term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_term6.
    def visitE_term6(self, ctx:pyGramParser.E_term6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#time_div.
    def visitTime_div(self, ctx:pyGramParser.Time_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#minus_not.
    def visitMinus_not(self, ctx:pyGramParser.Minus_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#e_factor.
    def visitE_factor(self, ctx:pyGramParser.E_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#l_expr.
    def visitL_expr(self, ctx:pyGramParser.L_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#l_function_call.
    def visitL_function_call(self, ctx:pyGramParser.L_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#l_id.
    def visitL_id(self, ctx:pyGramParser.L_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#l_int_value.
    def visitL_int_value(self, ctx:pyGramParser.L_int_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#l_float_value.
    def visitL_float_value(self, ctx:pyGramParser.L_float_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#l_str_value.
    def visitL_str_value(self, ctx:pyGramParser.L_str_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#l_bool_value.
    def visitL_bool_value(self, ctx:pyGramParser.L_bool_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pyGramParser#r_input.
    def visitR_input(self, ctx:pyGramParser.R_inputContext):
        return self.visitChildren(ctx)



del pyGramParser