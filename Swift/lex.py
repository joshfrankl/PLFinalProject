#------------------------------------------------------------
# lex.py
#
# Swift tokenizer - adapted from Dr. Cannata's "HMM PLY Version"
# ------------------------------------------------------------

import ply.lex as lex

DEBUG = False

# Reserved words
reserved = {
    'VAR'   : 'var',
    'LET'   : 'let',
    'INT'	: 'int',
    'FLOAT'	: 'float',
    'DOUBLE': 'double',
    'BOOL'	: 'bool',
    'TRUE'	: 'true',
    'FALSE'	: 'false',
    'IF'	: 'if',
    'ELSE'	: 'else',
    'STRING': 'string',
    'PRINT' : 'print'
}

# List of token names.
tokens = [
          'AND_OP', 'OR_OP', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LCURLY', 'RCURLY', \
          'EQ_OP', 'NE_OP', 'LE_OP', 'GE_OP', 'LT_OP', 'GT_OP', \
          'PLUS', 'MINUS', 'MULT', 'DIV', 'MOD', 'PEQ', 'MEQ', 'MUEQ', 'DEQ', \
          'SQUOTE', 'IDENTIFIER', 'EQUALS', 'INTEGER', 'STRINGVALUE'
         ] + list(reserved.keys())

literals = ['.', ]


# Regular expression rules for simple tokens

t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_EQ_OP = r'=='
t_NE_OP = r'!='
t_LE_OP = r'<='
t_GE_OP = r'>='
t_LT_OP = r'<'
t_GT_OP = r'>'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_PEQ = r'\+='
t_MEQ = r'-='
t_MUEQ = r'\*='
t_DEQ = r'/='
t_SQUOTE = r'\''

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)    
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    if DEBUG: print "In t_INTEGER, saw: ", t.value
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        t.type = t.value.upper()
    if DEBUG: print "In t_IDENTIFIER, saw: ", t.value
    return t

def t_STRINGVALUE(t):
    r'"[a-zA-Z0-9_+\*\- :,.!]*"'
    t.type = "STRING" # STRING is a reserved word
    if DEBUG: print "In t_STRINGVALUE, saw: ", t.value
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()