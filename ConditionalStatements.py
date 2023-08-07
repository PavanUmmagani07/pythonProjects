#CONDITIONAL STATEMENTS
#Conditional Statement allows you to execute a block of code only when a specific condition is True

#IF CONDITION
#EXMAPLE
if True:
    print("If Block")
    print("Inside If")


"""
POSSIBLE ERRORS IN if CONDITION
Each statement inside a conditional block should have the same indentation (spacing).
if True:
    print("If Block")
            print("Inside If")
"""

#if-else CONDITION
#When If - Else conditional statement is used, Else block of code executes if the condition is False
#EXAMPLE
a = int(input())
if a > 0:
    print("Positive")
else:
    print("Not Positive")
print("End")


"""
POSSIBLE MISTAKES
Else can only be used along with if condition. It is written below if conditional block
if False:
    print("If Block")
print("After If")
else:
    print("Else Block")
print("After Else")
"""
