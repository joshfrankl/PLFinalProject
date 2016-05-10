commandTest.py:
-Used to test an individual line of Swift code and output an abstract syntax tree (AST)
-Useful in debugging
-For example, "let a = 4" will output "[['let', 'a', 4]]"

lex.py, yacc.py, and mini-lisp.py each have an optional "DEBUG" boolean
-When DEBUG = True, each step in the parsing process is printed

To run the project, run mini-lisp.py
-Each of the test cases (.swift files) will be run

Project Features:
-Can assign variables and constants (constants cannot be changed)
-Can perform arithmetic operations (+, -, *, /, %) and +=, -=, *=, /=
-Can perform simple if/else statements
-Accepts "print" statement such as print(), print("Hello"), print(varName), and print(3)