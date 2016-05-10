1. Excess code from yacc.py and lis.py were removed

2. Use of the "exec" function

(+ 1 (exec 'from java.lang import Math; toReturn = Math.max(23, 34)'))
AST is:  ['+', 1, ['exec', "'from java.lang import Math; toReturn = Math.max(23, 34)'"]]
35

(+ 1 (exec 'import Addition; toReturn = Addition.add(23, 34)'))
AST is: ['+', 1, ['exec', "'import Addition; toReturn = Addition.add(23, 34)'"]]
58

(exec 'import QuadraticFormula; toReturn = QuadraticFormula.quadPlus(3, 4, -4)')
AST is:  ['exec', "'import QuadraticFormula; toReturn = QuadraticFormula.quadPlus(3, 4, -4)'"]
-2.66666666667

(exec 'import QuadraticFormula; toReturn = QuadraticFormula.quadMinus(3, 4, -4)')
AST is:  ['exec', "'import QuadraticFormula; toReturn = QuadraticFormula.quadMinus(3, 4, -4)'"]
-5.33333333333

Imaginary class:
-Method overloading (can pass int or double)
-Mixed return type (double and String)

(exec 'import Imaginary; toReturn = Imaginary.sqrt(-144)')
AST is:  ['exec', "'import Imaginary; toReturn = Imaginary.sqrt(-144)'"]
12.0i

3. Python Closures: Courses.py
-Models UT classes and grades

(exec 'import Courses; toReturn = Courses.createCourse("Elements of Data Visualization", "CS329E", "B")')
AST is:  ['exec', '\'import Courses; toReturn = Courses.createCourse("Elements of Data Visualization", "CS329E", "B")\'']
Elements of Data Visualization
CS329E
B

4. Java Stream Operations: ListComprehension.java, JavaStreams.java (reads input from files)

(exec 'import ListComprehension; toReturn = ListComprehension.executeStreams()')
AST is:  ['exec', "'import ListComprehension; toReturn = ListComprehension.executeStreams()'"]

(exec 'from src.martella import JavaStreams; toReturn = JavaStreams.main([])')
AST is:  ['exec', "'from src.martella import JavaStreams; toReturn = JavaStreams.main([])'"]

5. Python List Comprehension: ListComprehension.py

(exec 'import ListComprehensionPython; toReturn = ListComprehensionPython.executeStreams()')
AST is:  ['exec', "'import ListComprehensionPython; toReturn = ListComprehensionPython.executeStreams()'"]

(cons 1 '(1 2)) 
AST is:  ['cons', 1, ['quote', [1, 2]]]
[1, 1, 2]

(cons (list 1 2) (list 3 4))
AST is:  ['cons', ['list', 1, 2], ['list', 3, 4]]
[[1, 2], 3, 4]

(contains 2 '(1 3 4))
AST is:  ['contains', 2, ['quote', [1, 3, 4]]]
False

(addToList 14 '(1 4 9))
AST is:  ['addToList', 14, ['quote', [1, 4, 9]]]
[15, 18, 23]

6. Bugs fixed in mini-lisp.py:
-Prompt is now in English ("Welcome to MiniLisp")
-Comments are now in English
-Fixed TEXT regex in lex.py (from Dr. Cannata's latest push)
-Removed unused import statement