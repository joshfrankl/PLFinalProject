# -*- coding: utf-8 -*-

### This program can handle variables and constants, simple "if" statements, arithmetic, and "print" statements

from yacc import yacc

DEBUG = False

vars = {}
constants = {}

def booleanHelper(first, operation, second):
    # Used to evaluate a boolean expression and return True or False
    if operation == "==":
        return first == second
    elif operation == "!=":
        return first != second
    elif operation == ">":
        return first > second
    elif operation == "<":
        return first < second
    elif operation == ">=":
        return first >= second
    elif operation == "<=":
        return first <= second

def evaluate(ast):
    for commands in ast:
        if commands[0] == 'var':
            if DEBUG: print "eval: var"
            if commands[1] not in vars: # Add the new variable to the dictionary
                vars[commands[1]] = commands[2]
                if isinstance(commands[2], (list)) and commands[2][0] == 'arithmetic': # Variable is arithmetic operation
                    vars[commands[1]] = eval("".join(str(x) for x in commands[2][1:]))
            else:
                raise Exception("Variable already defined")

        elif commands[0] == 'let':
            if DEBUG: print "eval: let"
            if commands[1] not in constants: # Add the new constant to the dictionary
                constants[commands[1]] = commands[2]
                if isinstance(commands[2], (list)) and commands[2][0] == 'arithmetic': # Variable is arithmetic operation
                    constants[commands[1]] = eval("".join(str(x) for x in commands[2][1:]))
            else:
                raise Exception("Cannot change a constant")

        elif commands[0] == 'print':
            if DEBUG: print "eval: print"
            if commands[1] == "": # Empty print
                print ""
            elif commands[1] in vars: # Printing a variable
                print vars[commands[1]]
            elif commands[1] in constants: # Printing a constant
                print constants[commands[1]]
            elif isinstance(commands[1], (int, float)): # Printing a number
                print commands[1]
            elif commands[1][0] == '"' and commands[1][-1] == '"': # Printing a string literal
                print commands[1][1:-1]
            else: # Error
                raise Exception("No such variable " + commands[1])

        elif commands[0] == 'arithmetic':
            if DEBUG: print "eval: arithmetic"
            print(eval("".join(str(x) for x in commands[1:]))) # 3+3 prints 6

        elif commands[0] == 'reassign':
            if DEBUG: print "eval: reassign"
            if commands[1] in constants: # Attempting to change a constant
                raise Exception("Cannot change a constant")
            elif commands[1] in vars:
                if commands[2] == "=" and isinstance(commands[3], (int, float)): # a = 3
                    vars[commands[1]] = commands[3]
                elif commands[2] == "+=":
                    vars[commands[1]] = vars[commands[1]] + float(commands[3])
                elif commands[2] == "-=":
                    vars[commands[1]] = vars[commands[1]] - float(commands[3])
                elif commands[2] == "*=":
                    vars[commands[1]] = vars[commands[1]] * float(commands[3])
                elif commands[2] == "/=":
                    vars[commands[1]] = vars[commands[1]] / float(commands[3])
                else: # Arithmetic expression
                    vars[commands[1]] = eval("".join(str(x) for x in commands[3][1:]))
            else:
                raise Exception("Variable " + commands[1] + " not defined")

        elif commands[0] == 'if':
            if DEBUG: print "eval: if"
            if commands[1][0] in vars and isinstance(commands[1][2], (int, float)): # a == 3
                if booleanHelper(vars[commands[1][0]], commands[1][1], commands[1][2]): # if statement evaluates to true
                    evaluate(commands[2]) # Execute code block
                elif len(commands) == 4: # Else statement
                    evaluate(commands[3][1])
            elif isinstance(commands[1][0], (int, float)) and commands[1][2] in vars: # 3 == a
                if booleanHelper(commands[1][0], commands[1][1], vars[commands[1][2]]): # if statement evaluates to true
                    evaluate(commands[2]) # Execute code block
                elif len(commands) == 4: # Else statement
                    evaluate(commands[3][1])
            elif commands[1][0] in constants and isinstance(commands[1][2], (int, float)): # a == 3, where a is a constant
                if booleanHelper(constants[commands[1][0]], commands[1][1], commands[1][2]): # if statement evaluates to true
                    evaluate(commands[2]) # Execute code block
                elif len(commands) == 4: # Else statement
                    evaluate(commands[3][1])
            elif isinstance(commands[1][0], (int, float)) and commands[1][2] in constants: # 3 == a, where a is a constant
                if booleanHelper(commands[1][0], commands[1][1], constants[commands[1][2]]): # if statement evaluates to true
                    evaluate(commands[2]) # Execute code block
                elif len(commands) == 4: # Else statement
                    evaluate(commands[3][1])
            elif isinstance(commands[1][0], (int, float)) and isinstance(commands[1][0], (int, float)): # 3 == 3
                if booleanHelper(commands[1][0], commands[1][1], commands[1][2]): # if statement evaluates to true
                    evaluate(commands[2]) # Execute code block
                elif len(commands) == 4: # Else statement
                    evaluate(commands[3][1])
            elif commands[1][0] in vars and isinstance(commands[1][2], (str)): # a == "word"
                if booleanHelper(vars[commands[1][0]], commands[1][1], commands[1][2]): # if statement evaluates to true
                    evaluate(commands[2]) # Execute code block
                elif len(commands) == 4: # Else statement
                    evaluate(commands[3][1])
            elif commands[1][0] in constants and isinstance(commands[1][2], (str)): # a == "word", where a is a constant
                if booleanHelper(constants[commands[1][0]], commands[1][1], commands[1][2]): # if statement evaluates to true
                    evaluate(commands[2]) # Execute code block
                elif len(commands) == 4: # Else statement
                    evaluate(commands[3][1])
            else:
                raise Exception("Symbol not found")

print("***test-helloworld.swift***")
with open('test-helloworld.swift', 'r') as content_file:
    content = content_file.read()
content_file.close()
ast = yacc.parse(content)

print "ast is: " + str(ast)
evaluate(ast)
# Clear dictionaries for the next files
vars.clear()
constants.clear()
print("\n\n")

print("***test-arithmetic.swift***")
with open('test-arithmetic.swift', 'r') as content_file:
    content = content_file.read()
content_file.close()
ast = yacc.parse(content)

print "ast is: " + str(ast)
evaluate(ast)
# Clear dictionaries for the next files
vars.clear()
constants.clear()
print("\n\n")

print("***test-conditional.swift***")
with open('test-conditional.swift', 'r') as content_file:
    content = content_file.read()
content_file.close()
ast = yacc.parse(content)

print "ast is: " + str(ast)
evaluate(ast)
# Clear dictionaries for the next files
vars.clear()
constants.clear()