# Generated from /home/jpedro/workspace/novo_compilador/Raimundo.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RaimundoParser import RaimundoParser
else:
    from RaimundoParser import RaimundoParser

# This class defines a complete generic visitor for a parse tree produced by RaimundoParser.

class RaimundoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RaimundoParser#program.
    def visitProgram(self, ctx:RaimundoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#global_variables_declaration.
    def visitGlobal_variables_declaration(self, ctx:RaimundoParser.Global_variables_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#functions_declaration.
    def visitFunctions_declaration(self, ctx:RaimundoParser.Functions_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#main_function_declaration.
    def visitMain_function_declaration(self, ctx:RaimundoParser.Main_function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#function_body_statements.
    def visitFunction_body_statements(self, ctx:RaimundoParser.Function_body_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#l_type.
    def visitL_type(self, ctx:RaimundoParser.L_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#l_void.
    def visitL_void(self, ctx:RaimundoParser.L_voidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#return_statement.
    def visitReturn_statement(self, ctx:RaimundoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:RaimundoParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#forloop_statement.
    def visitForloop_statement(self, ctx:RaimundoParser.Forloop_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#while_statement.
    def visitWhile_statement(self, ctx:RaimundoParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#break_statement.
    def visitBreak_statement(self, ctx:RaimundoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#if_statement.
    def visitIf_statement(self, ctx:RaimundoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#else_statement.
    def visitElse_statement(self, ctx:RaimundoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#print_statement.
    def visitPrint_statement(self, ctx:RaimundoParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#global_variable_declaration_statement.
    def visitGlobal_variable_declaration_statement(self, ctx:RaimundoParser.Global_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#global_single_variable_declaration_statement.
    def visitGlobal_single_variable_declaration_statement(self, ctx:RaimundoParser.Global_single_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#global_multiple_variable_declaration_statement.
    def visitGlobal_multiple_variable_declaration_statement(self, ctx:RaimundoParser.Global_multiple_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#local_variable_declaration_statement.
    def visitLocal_variable_declaration_statement(self, ctx:RaimundoParser.Local_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#local_single_variable_declaration_statement.
    def visitLocal_single_variable_declaration_statement(self, ctx:RaimundoParser.Local_single_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#local_multiple_variable_declaration_statement.
    def visitLocal_multiple_variable_declaration_statement(self, ctx:RaimundoParser.Local_multiple_variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_assigment.
    def visitE_assigment(self, ctx:RaimundoParser.E_assigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#input.
    def visitInput(self, ctx:RaimundoParser.InputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_plus_assigment.
    def visitE_plus_assigment(self, ctx:RaimundoParser.E_plus_assigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_mult_assigment.
    def visitE_mult_assigment(self, ctx:RaimundoParser.E_mult_assigmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#or_logic.
    def visitOr_logic(self, ctx:RaimundoParser.Or_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_term.
    def visitE_term(self, ctx:RaimundoParser.E_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#and_logic.
    def visitAnd_logic(self, ctx:RaimundoParser.And_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_term2.
    def visitE_term2(self, ctx:RaimundoParser.E_term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#comp_logic.
    def visitComp_logic(self, ctx:RaimundoParser.Comp_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_term3.
    def visitE_term3(self, ctx:RaimundoParser.E_term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#eq_logic.
    def visitEq_logic(self, ctx:RaimundoParser.Eq_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_term4.
    def visitE_term4(self, ctx:RaimundoParser.E_term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#sum_minus.
    def visitSum_minus(self, ctx:RaimundoParser.Sum_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_term5.
    def visitE_term5(self, ctx:RaimundoParser.E_term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_term6.
    def visitE_term6(self, ctx:RaimundoParser.E_term6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#time_div.
    def visitTime_div(self, ctx:RaimundoParser.Time_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#minus_not.
    def visitMinus_not(self, ctx:RaimundoParser.Minus_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#e_factor.
    def visitE_factor(self, ctx:RaimundoParser.E_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#l_expr.
    def visitL_expr(self, ctx:RaimundoParser.L_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#l_function_call.
    def visitL_function_call(self, ctx:RaimundoParser.L_function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#l_id.
    def visitL_id(self, ctx:RaimundoParser.L_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#l_int_value.
    def visitL_int_value(self, ctx:RaimundoParser.L_int_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#l_float_value.
    def visitL_float_value(self, ctx:RaimundoParser.L_float_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#l_str_value.
    def visitL_str_value(self, ctx:RaimundoParser.L_str_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#l_bool_value.
    def visitL_bool_value(self, ctx:RaimundoParser.L_bool_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RaimundoParser#r_input.
    def visitR_input(self, ctx:RaimundoParser.R_inputContext):
        return self.visitChildren(ctx)



del RaimundoParser