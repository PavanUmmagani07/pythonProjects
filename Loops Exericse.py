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
counter =0
while (counter<N):
    row = "* "*N
    print(row)
    counter= counter+1

"""
Write a program that reads a number N and prints the number 0, N times on N lines
#Sample Input1:3
#Sample Input2:2
#Expected Output1:0
                  0
                  0
#Expected Output2:0
                  0
"""

N = int(input())
counter = 0
while (counter<N):
    # Column = "0"*1
    # print(Column)
    print(0)
    counter = counter+1

"""
Write a program to print integers from 1 to the given integer(N)
#Sample Input1:3
#Sample Input2:5
#Expected Output1:1
                  2
                  3
#Expected Output2:1
                  2
                  3
                  4
                  5
"""
N = int(input())
counter =1
while (counter<=N):
    print(counter)
    counter = counter+1

"""
Write a program that reads a number N and prints N natural numbers from 1
#Sample Input1:3
#Sample Input2:5
#Expected Output1:1
                  2
                  3
#Expected Output2:1
                  2
                  3
                  4
                  5
"""
N = int(input())
counter = 1
while (counter<=N):
    print(counter)
    counter = counter+1

"""
Given two integers numbers M and N, Write a program to print the integers from M to N
#Sample Input1:2 6
#Sample Input2:-2 2
#Expected Output1:2
                  3
                  4
                  5
                  6
#Expected Output2:-2
                    -1
                    0
                    1
                    2
"""
M = int(input())
N = int(input())
while(M<=N):
    print(M)
    M = M+1


"""
Write a program that reads a number N and prints the average of N numbers from 1
#Sample Input1:4
#Sample Input2:7
#Expected Output1:2.5
#Expected Output2:4
"""

N = int(input())
counter = 0
Sum =0
while (counter<N):
    Num = counter+1
    Sum = Sum+Num
    counter = counter+1
print(Sum/N)


"""
Write a program that reads a number N and prints the cubes of N number from 1
#Sample Input1:4
#Sample Input2:5
#Expected Output1:1,8,27,64
#Expected Output2:1,8,27,64,125
"""

N = int(input())
counter = 0
while(counter<N):
    num = counter+1
    print(num**3)
    counter = counter+1

"""
Given two integers M and N, Write a program to print a solid rectangle pattern of m rows and N columns using the asterisk character(*)
#Sample Input1:2,3
#Sample Input2:4,6
#Expected Output1: * * *
                   * * *
#Expected Output2:* * * * * *
                  * * * * * * 
                  * * * * * *
                  * * * * * *
"""

Rows = int(input())
Columns = int(input())
counter = 0
while (counter<Rows):
    Rectangle = "* "*Columns
    print(Rectangle)
    counter = counter+1

"""
Write a program that reads a number N and prints 10 numbers after N.
#Sample Input1:2
#Sample Input2:11
#Expected Output1:3,4,5,6,7,8,9,10,11,12
#Expected Output2:12,13,14,15,16,17,18,19,20,21
"""
N = int(input())
Counter = 0
while (Counter<10):
    N= N+1
    print(N)
    Counter = Counter+1

"""
Write a program that reads two numbers M and N and Prints N numbers after M.
#Sample Input1:
#Sample Input2:
#Expected Output1:
#Expected Output2:
"""
M = int(input())
N = int(input())
counter = 0
while (counter<N):
    M = M+1
    print(M)
    counter = counter+1


"""
Write a program that reads two numbers M and N and Prints the Sum of N numbers from M
#Sample Input1:7,3
#Sample Input2:2,10
#Expected Output1:24
#Expected Output2:65
"""

M = int(input())
N = int(input())
Num=0
Sum = 0
Counter = 0
while (Counter<N):
    Num = M+Counter
    Sum = Num+Sum
    Counter = Counter+1
print(Sum)

# M = int(input())
# N = int(input())
# Num=0
# Sum = 0
# Counter = 0
# while (Counter<N):
#     Sum = Sum + M
#     M = M+1
#     Counter = Counter+1
# print(Sum)

"""
Given an integer number(N) as input. Write a program to print the right-angled triangular pattern of N lines using an asterisk(*) character.
#Sample Input1:2
#Sample Input2:3
#Expected Output1:*
                  * *
#Expected Output2:*
                  * *
                  * * *
"""

N = int(input())
counter = 1
while(counter<=N):
    triangle = "* "*counter
    print(triangle)
    counter = counter+1


"""
Write a program that reads a number N and prints the sum of N natural Numbers.
#Sample Input1:6
#Sample Input2:3
#Expected Output1:21
#Expected Output2:6
"""
N = int(input())
counter = 0
Sum = 0
while(counter<N):
    N = N+1
    Sum = Sum+N
    print(Sum)
    counter = counter+1

"""
Given an integer N, write a program which reads N inputs and prints them.
#1 The first line of input will contain a positive integer, N
#2 The following N lines will contain an integer in each line 
#Sample Input1:3,8,11,25
#Sample Input2:2,7,20
#Expected Output1:8,11,25
#Expected Output2:7,20
"""

N = int(input())
counter =0
while(counter<N):
    M = int(input())
    print(M)
    counter = counter+1

"""
Given a number N, write a program that reads N numbers as input and prints the product of the given N numbers.
#Sample Input1:3,2,3,7
#Sample Input2:4,11,2,4,9
#Expected Output1:42
#Expected Output2:792
"""
N = int(input())
counter = 0
Product = 1
while(counter<N):
    M = int(input())
    Product =Product*M
    counter = counter+1
print(Product)


"""
Given an integer N, write a program which reads N inputs and prints the sum of the given input integers
#Sample Input1:3,8,11,25
#Sample Input2:2,7,20
#Expected Output1:44
#Expected Output2:27
"""
N = int(input())
counter = 0
sum = 0
while(counter<N):
    M = int(input())
    sum +=M
    counter+=1
print(sum)

"""
Write a program that reads a word and prints each character of the word in a new line.
#Sample Input1:PYTHON
#Sample Input2:LOOPS
#Expected Output1:P
                  Y
                  T
                  H
                  O
                  N
#Expected Output2:L
                  O
                  O
                  P
                  S
"""
Word = input()
counter =0
while(counter<len(Word)):
    print(Word[counter])
    counter+=1


"""
Write a program that reads a number N and prints a Square of N rows and N columns using stars(*)
#Sample Input1:3
#Sample Input2:2
#Expected Output1:* * *
                  * * *
                  * * *
#Expected Output2:* *
                  * *
"""
N = int(input())
counter = 0
while(counter<N):
    print("* "*N)
    counter+=1

"""
Write a program that reads two numbers M and N, and prints a rectangle of M rows and N columns using pluses(+)
#Sample Input1:3,5
#Sample Input2:4, 4
#Expected Output1: + + + + +
                   + + + + +
                   + + + + +
#Expected Output2: + + + + 
                   + + + +
                   + + + +
                   + + + +
"""
M = int(input())
N = int(input())
counter = 0
while(counter<M):
    print("+ "*N)
    counter+=1

"""
Write a program that reads a string a prints the first character of the given string on N lines, where N is the length of the given string.
#Sample Input1:Cool
#Sample Input2:Ball
#Expected Output1:C
                  C
                  C
                  C
                  C
#Expected Output2:B
                  B
                  B
"""
Word = input()
counter =0
while(counter<len(Word)):
    print(Word[0])
    counter+=1

"""
Write a program that reads a string and prints each character of the given string on a new line
#Sample Input1:Shine
#Sample Input2:Big Bull
#Expected Output1:S
                  h
                  i
                  n
                  e
#Expected Output2:B
                  i
                  g
                  
                  B
                  u
                  l
                  l
"""
String = input()
counter =0
while(counter<len(String)):
    print(String[counter])
    counter+=1


"""
Write a program that reads a number N and prints a Square of N rows and N columns using numbers starting from 1
#Sample Input1:4
#Sample Input2:3
#Expected Output1:1111
                  2222
                  3333
                  4444
#Expected Output2:111
                  222
                  333
"""
N = int(input())
counter = 1
while(counter<=N):
    print(str(counter)*N)
    counter+=1

"""
Write a program that reads two numbers m and N, and prints a Rectangle of M rows and N columns using starts(*)
#Sample Input1:4,5
#Sample Input2:3,2
#Expected Output1:*****
                  *****
                  *****
                  *****
#Expected Output2:**
                  **
                  **
"""
M = int(input())
N = int(input())
counter = 0
while(counter<M):
    print("*"*N)
    counter+=1

"""
Write a program that reads a number N and prints a Right Angled Triangle of N rows using stars(*)
#Sample Input1:3
#Sample Input2:4
#Expected Output1:*
                  **
                  ***
#Expected Output2:*
                  **
                  ***
                  ****
"""
N = int(input())
counter=1
while(counter<=N):
    print("*"*counter)
    counter+=1


"""
Write a program that reads a number N and prints a Right Angled Triangle of N rows using numbers starting from 1.
#Sample Input1:3
#Sample Input2:4
#Expected Output1:1
                  22
                  333
#Expected Output2:1
                  22
                  333
                  4444
"""
N = int(input())
counter=1
while(counter<=N):
    print((str(counter)+" ")*counter)
    counter+=1