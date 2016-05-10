import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = False

def p_program(p):
    'program : statements'
    if DEBUG: print "In p_program ", str( p[1] )
    p[0] = p[1]

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if DEBUG: print "In p_statements ", str( p[1:] )
    if len(p) > 2:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]

def p_statement(p):
    '''statement : expression
                 | variableDeclaration
                 | variableReassignment
                 | print
                 | ifStatement'''
    if DEBUG: print "Saw a statement", str( p[1] )
    p[0] = [ p[1] ]

def p_print(p):
    '''print : PRINT LPAREN RPAREN
             | PRINT LPAREN IDENTIFIER RPAREN
             | PRINT LPAREN INTEGER RPAREN
             | PRINT LPAREN decimal RPAREN
             | PRINT LPAREN STRING RPAREN'''
    if DEBUG: print "In p_print ", str( p[1:] )
    if len(p) > 4:
        p[0] = ["print", p[3] ] # Add the terms to a list and mark operation "print"
    else:
        p[0] = ["print", ""] # Print with no parameters

def p_variableReassignment(p):
    '''variableReassignment : IDENTIFIER EQUALS expression
                            | IDENTIFIER PEQ expression
                            | IDENTIFIER MEQ expression
                            | IDENTIFIER MUEQ expression
                            | IDENTIFIER DEQ expression'''
    if DEBUG: print "In p_variableReassignment ", str( p[1:] )
    p[0] = ["reassign", p[1], p[2], p[3] ] # Add the terms to a list and mark operation "reassign"

def p_variableDeclaration(p):
    '''variableDeclaration : VAR IDENTIFIER EQUALS expression
                           | LET IDENTIFIER EQUALS expression'''
    if DEBUG: print "In p_variableDeclaration ", str( p[1:] )
    p[0] = [ p[1], p[2], p[4] ]

def p_ifStatement(p):
    '''ifStatement : IF conditionalStatement codeBlock
                   | IF conditionalStatement codeBlock elseStatement'''
    if DEBUG: print "In p_ifStatement ", str( p[1:] )
    if len(p) > 4:
        p[0] = [ p[1], p[2], p[3], p[4] ]
    else:
        p[0] = [ p[1], p[2], p[3] ]

def p_elseStatement(p):
    '''elseStatement : ELSE codeBlock
                     | ifStatement'''
    if DEBUG: print "In p_elseStatement ", str( p[1:] )
    if len(p) > 2:
        p[0] = [ p[1], p[2] ]
    else:
        p[0] = [ p[1] ]

def p_codeBlock(p):
    'codeBlock : LCURLY statements RCURLY'
    if DEBUG: print "In p_codeBlock ", str( p[2] )
    p[0] = p[2]

def p_conditionalStatement(p):
    '''conditionalStatement : item boolOP item
                            | TRUE
                            | FALSE'''
    if DEBUG: print "In p_conditionalStatement ", str( p[1:] )
    if len(p) > 2:
        p[0] = [ p[1], p[2], p[3] ]
    else:
        p[0] = [ p[1] ]

def p_expression(p):
    '''expression : conjunction
                  | conjunction OR_OP expression'''
    if DEBUG: print "In p_expression ", str( p[1:] )
    p[0] = p[1]

def p_conjunction(p):
    '''conjunction : equality
                   | AND_OP equality'''
    if DEBUG: print "In p_conjunction ", str(p[1:] )
    if len(p) == 4:
        p[0] = [ p[1], p[2], p[3] ]
    else :
        p[0] = p[1]

def p_boolOP(p):
    '''boolOP : eqOP
              | relOP'''
    if DEBUG: print "In p_boolOP ", str( p[1] )
    p[0] = p[1]

def p_equality(p):
    '''equality : relation
                | relation eqOP equality'''
    if DEBUG: print "In p_equality ", str( p[1:] )
    if len(p) == 4:
        p[0] = [ p[1], p[2], p[3] ]
    else :
        p[0] = p[1]

def p_eqOP(p):
    '''eqOP : EQ_OP
            | NE_OP'''
    if DEBUG: print "In p_eqOP ", str( p[1] )
    p[0] = p[1]

def p_relation(p):
    '''relation : addition
                | addition relOP relation'''
    if DEBUG: print "In p_relation ", str( p[1:] )
    if len(p) == 4:
        p[0] = [ p[1], p[2], p[3] ]
    else :
        p[0] = p[1]

def p_relOP(p):
    '''relOP : LT_OP
             | LE_OP
             | GT_OP
             | GE_OP'''
    if DEBUG: print "In p_relOP ", str( p[1] )
    p[0] = p[1]

def p_addition(p):
    '''addition : term
                | term addOP addition'''
    if DEBUG: print "In p_addition ", str( p[1:] )
    if len(p) == 4:
        p[0] = ["arithmetic", p[1], p[2], p[3]] # Add the terms to a list and mark operation "arithmetic"
    else :
        p[0] = p[1]

def p_addOP(p):
    '''addOP : PLUS
             | MINUS'''
    if DEBUG: print "In p_addOP ", str( p[1] )
    p[0] = p[1]

def p_term(p):
    '''term : factor
            | factor mulOP term'''
    if DEBUG: print "In p_term ", str( p[1:] )
    if len(p) == 4:
        p[0] = ["arithmetic", p[1], p[2], p[3]] # Add the terms to a list and mark operation "arithmetic"
    else :
        p[0] = p[1]

def p_mulOP(p):
    '''mulOP : MULT
             | DIV
             | MOD'''
    if DEBUG: print "In p_mulOP ", str( p[1] )
    p[0] = p[1]

def p_factor(p):
    'factor : primary'
    if DEBUG: print "In p_literal ", str( p[1] )
    if len(p) == 4:
        p[0] = [ p[1], p[2], p[3] ]
    else:
        p[0] = p[1]

def p_primary(p):
    '''primary : literal'''
    if DEBUG: print "In p_primary ", str( p[1] )
    p[0] = p[1]

def p_literal(p):
    '''literal : INTEGER
               | decimal
               | STRING
               | IDENTIFIER
               | TRUE
               | FALSE'''
    if DEBUG: print "In p_literal ", str( p[1] )
    p[0] = p[1]

def p_item(p):
    '''item : INTEGER
            | IDENTIFIER
            | STRING
            | decimal'''
    if DEBUG: print "In p_item ", str( p[1] )
    p[0] = p[1]

def p_decimal(p):
    '''decimal : INTEGER "." INTEGER'''
    if DEBUG: print "In p_decimal ", str( p[1:] )
    number = str(p[1]) + str(p[2]) + str(p[3])
    p[0] = float(number)

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ", p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()