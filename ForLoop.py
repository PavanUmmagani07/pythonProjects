#For Loop
# for statement iterates over each item of sequence
# 1) Sequence of Characters(String)
# 2)Sequence of numbers, etc.
"""
for each_item in sequence:
    Block of code

"""
#EXAMPLE(Sequence of characters)
Word = "Python"
for each_char in Word:
    print(each_char)


"""
#EXAMPLE(Sequence of Numbers)
Syntax
for each_number in sequence_of_numbers:
    Repeating block of code
"""

"""
RANGE
range(n) => Stops before n(n is not included)
range generates a sequence of integers starting from 0
"""
#EXAMPLE
for number in range(5):
    print(number)

A = int(input())
for number in range(A):
    print(number)


"""
Write a program to print right angle triangular pattern where integer N is given as input
#Sample Input1:4
#Sample Input2:3
#Expected Output1:*
                  * *
                  * * *
                  * * * *
                  
#Expected Output2:*
                  * *
                  * * *
"""
N = int(input())
for counter in range(N):
    print("* "*(counter+1)) #Since range starts from ZERO

#Method2
N = int(input())
for counter in range(1,(N+1)):
    print("* "*counter)
"""
             ||-->Stops before end(End is not included)
range(start,end)
       ||-->Generates a sequence of numbers starting from this
#If we donot specify the start it will start from zero and goes till end.
"""

#Example
for counter in range(2,12):
    print(counter)