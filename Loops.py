"""
Python executes code in a sequence and each Block of code is executed once
Can we control the flow execution to make a block of  code to execute more than once??
LOOPS
Loops allows us to execute a block of code several
In python there are two primary ways for looping.
#1 While Loop
#2 For Loop
"""
#WHILE LOOP
"""
while loop is used to execute a block of code several times as long as the condition is TRUE
#SYNTAX
while condition:
    block of code
"""
#EXAMPLE
#Write a code to print next 3 consecutive numbers of the given integer input.
"""
#Sample Input1:1
#Sample Input2:22
#Expected Output1:2,3,4
#Expected Output2:23,24,26
"""
A = int(input())
counter = 0 #Initalization
while (counter<3): #Termination condition
    A = A+1
    print(A)
    counter = counter+1 #Updation
print("End")

"""
Initialization
while termination condition:
    Block of code(Repeating)
    Updation
"""
#Common Mistakes
#1 Missing Initalization(output: NameError)
#2 Incorrect Termination Condition (Infinite loop)
#Example:
"""
a = int(input())
counter = 0
condition = (counter<3)
while condition:
    a = a+1
    print(a)
    counter = counter+1
    
Output: Returns an infinite loop since the while block will keep repeating as the value in condition variable is true
"""
#3 Not updating the variable

#EXAMPLE(Square Pattern)
"""
Write a program to print sstars in Nrows and N columns, Where interger N is given as an input.
#Sample Input1:4
#Sample Input2:2
#Expected Output1:* * * *
                  * * * *
                  * * * * 
                  * * * *
                  
#Expected Output2:* *
                  * *
"""
N = int(input())
counter = 0
while (counter<N):
    row = "* "*N
    print(row)
    counter = counter+1
