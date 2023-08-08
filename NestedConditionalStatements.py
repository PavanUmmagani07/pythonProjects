#Nested Conditions
#The conditional block inside another if/else conditional block is called as nested conditional block.
#In the below example, Block 2 is nested conditional block and condition B is called nested conditional statement.\
#EXAMPLE
"""
if condition A:
    Block 1
    if condition B:
        Block 2
    Block 3
Block 4
"""
#EXAMPLE
matches_won = int(input())
goals = int(input())
if matches_won > 8:
    if goals > 20:
        print("Hurray")
    print("Winner")

#Sample INPUT1:10,22
#Sample INPUT2:10,18
#Expected OUTPUT1:Hurray,Winner
#Expected OUTPUT2:Winner

#NESTED CONDITION IN ELSE BLOCK
#We can also write nested conditions in Else Statement.
#In the below example Block 2 is a nested conditional block.

#SYNTAX
'''
if condition A:
    Block 1
else:
    if condition B:
        Block 2
    Block 3
Block 4
'''
#EXAMPLE
a = 2
b = 3
c = 1
is_a_greatest = (a > b) and (a > c)
if is_a_greatest:
    print(a)
else:
    is_b_greatest = (b > c)
    if is_b_greatest:
        print(b)
    else:
        print(c)

#Expected Output:3

#ELIF STATEMENT
#Use the elif statement to have multiple conditional statements between if and else.
#The elif statement is optional.
"""
if condition A: 
    Block 1
elif condition B:
    Block 2
else:
    Block 3
"""
#MULTIPLE ELIF  STATEMENTS
"""
if condition A: 
    Block 1
elif condition B:
    Block 2
elif condition C:
    Block 3
else:
    Block 4
"""

#Execution of Elif Statement
#Python will execute the elif block whose expression evaluates to true.
#If multiple elif conditions are true, then only the first elif block which is True will be executed.
#Else statement is not compulsory after if - elif statements.

#EXAMPLE
number = 5
is_divisible_by_10 = (number % 10 == 0)
is_divisible_by_5 = (number % 5 == 0)
if is_divisible_by_10:
    print("Divisible by 10")
elif is_divisible_by_5:
    print("Divisible by 5")
else:
   print("Not Divisible by 10 or 5")

#EXPECTED OUTPUT: Divisible by 5

#Possible Mistake
#Cannot write an elif statement after else statement.
