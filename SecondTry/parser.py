import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''program : function_definition'''
    p[0] = p[1]

def p_function_definition(p):
    '''function_definition : ID ID LPAREN RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function_definition', p[1], p[2], p[6])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : expression SEMI
                 | return_statement SEMI'''
    p[0] = p[1]

def p_return_statement(p):
    '''return_statement : ID expression'''
    p[0] = ('return', p[1], p[2])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = ('number', p[1])

def p_expression_id(p):
    '''expression : ID'''
    p[0] = ('id', p[1])

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
