"""
Given an integer N, Write a program which reads N inputs and prints them
#Sample Input1:3,8,11,25
#Sample Input2:2,7,20
#Expected Output1:8,11,25
#Expected Output2:7,20
"""
N = int(input())
for counter in range(N):
    M = int(input())
    print(M)

"""
Given an integer N, write a program that reads N inputs and prints the product of the given inputs
#Sample Input1:3,2,3,7
#Sample Input2:4,11,2,4,9
#Expected Output1:42
#Expected Output2:792
"""
N = int(input())
product = 1
for counter in range(N):
    M = int(input())
    product = product*M
print(product)

"""
Given two integers M and N, write a program to print a solid rectangle pattern of M rows and N columns using the Asterisk character(*)
#Sample Input1:2,3
#Sample Input2:4,6
#Expected Output1:* * *
                  * * *
#Expected Output2:* * * * * *
                  * * * * * *
                  * * * * * *
                  * * * * * *
"""
M = int(input())
N = int(input())
for counter in range(M):
    print("* "*N)

"""
Given an integer number(N) as input.Write a program to print the right-angled triangular pattern of N lines using an asterisk(*) character 
#Sample Input1:4
#Sample Input2:2
#Expected Output1:*
                  * *
                  * * *
                  * * * *
#Expected Output2:*
                  * *
"""
N = int(input())
for counter in range(1,(N+1)):
    print("* "*counter)

"""
Given an integer N, write a program which reads N inputs and prints the sum of the given input integers
#Sample Input1:3,8,11,25
#Sample Input2:2,7,20
#Expected Output1:44
#Expected Output2:27
"""
N = int(input())
Sum = 0
for counter in range(N):
    M = int(input())
    Sum = Sum+M
print(Sum)

"""
Write a program that prints the individual characters of the given word seprated with hypens("-")
#Sample Input1:Python
#Sample Input2:Loops
#Expected Output1:P-y-t-h-o-n
#Expected Output2:L-o-o-p-s
"""
Word = input()
styled_word = Word[0]
for i in range(1,len(Word)):
    styled_word = styled_word+"-"+Word[i]
print(styled_word)

"""
Write a program that reads a number and prints number from 1 to N
#Sample Input1:3
#Sample Input2:5
#Expected Output1:1,2,3
#Expected Output2:1,2,3,4,5
"""
N = int(input())
for i in range(1,(N+1)):
    print(i)

"""
Write a program that reads N and prints the sum of natural numbers from 1 to N
#Sample Input1:6
#Sample Input2:21
#Expected Output1:3
#Expected Output2:6
"""
N = int(input())
Sum = 0
for i in range(N+1):
    Sum = Sum+i
print(Sum)

"""
Write a program that reads a string and prints the first charcter(The charcter at index 0) of the given string on N lines,where N is the length of the given string.
#Sample Input1:query
#Sample Input2:Lsit
#Expected Output1:q
                  q
                  q
                  q
                  q
#Expected Output2:L
                  L
                  L
                  L
"""
String = input()
for i in range(len(String)):
    print(String[0])

"""
Write a program that reads a string and prints each charcter of the given string on a new line
#Sample Input1:Python
#Sample Input2:Loops
#Expected Output1:
                  P
                  y
                  t
                  h
                  o
                  n
#Expected Output2:L
                  o
                  o
                  p
                  s
"""
Word = input()
for i in Word:
    print(i)

"""
write a program that reads a number N and prints Natural Numbers from 1 to N
#Sample Input1:5
#Sample Input2:2
#Expected Output1:1
                  2
                  3
                  4
                  5
#Expected Output2:1
                  2
"""
N = int(input())
for i in range(1,(N+1)):
    print(i)

"""
Write a program that reads a number N and prints the average of numbers from 1 to N
#Sample Input1:8
#Sample Input2:15
#Expected Output1:4.5
#Expected Output2:8.0
"""
N = int(input())
Sum = 0
for i in range(1,(N+1)):
    Sum = Sum+i
print(Sum/N)

"""
Write a program that reads a number N and prints the cube of numbers from 1 to N
#Sample Input1:3
#Sample Input2:5
#Expected Output1:1
                  8
                  27
#Expected Output2:1
                  8
                  27
                  64
                  125
"""
N = int(input())
for i in range(1,(N+1)):
    cubes = i**3
    print(cubes)

"""
Given two integer numbers M and N,write a program to print the integers from 
#Sample Input1:2,6
#Sample Input2:2,3,4,5,5,6
#Expected Output1:-2,2
#Expected Output2:-2,-1,0,1,2
"""
M = int(input())
N = int(input())
for i in range(M,(N+1)):
    print(i)

"""
Given two integers M and N, Write a program to print the sum of the numbers from M to N
#Sample Input1:2,6
#Sample Input2:10,20
#Expected Output1:20
#Expected Output2:165
"""
M = int(input())
N = int(input())
Sum = 0
for i in range(M,(N+1)):
    Sum = Sum+i
print(Sum)

"""
Write a program that reads a number M and prints a square of M rows and M columns using Stars(*)
#Sample Input1:4
#Sample Input2:2
#Expected Output1:* * * *
                  * * * *
                  * * * *
                  * * * *
#Expected Output2:* *
                  * *
"""
M = int(input())
for i in range(M):
    print("* "*M)

"""
Write a program that reads a number N and prints 10 numbers after N
#Sample Input1:4
#Sample Input2:9
#Expected Output1:5,6,7,8,9,10,11,12,13,14
#Expected Output2:10,11,12,13,14,15,16,17,18,19,
"""
N = int(input())
for i in range(10):
    N = N+1
    print(N)

"""
Write a program that reads number M and prints a square of M rows and M columns using numbers
#Sample Input1:4
#Sample Input2:5
#Expected Output1:1111
                  2222
                  3333
                  4444
#Expected Output2:11111
                  22222
                  33333
                  44444
                  55555
"""
M = int(input())
for i in range(1,(M+1)):
    print(str(i)*M)

"""
Write a program that reads two numbers M and N, and prints a Rectangle of M rows and N columns using stars(*)
#Sample Input1:3,4
#Sample Input2:5,7
#Expected Output1:****
                  ****
                  ****
#Expected Output2:*******
                  *******
                  *******
                  *******
                  *******
"""
M = int(input())
N = int(input())
for i in range(M):
    print("*"*N)

"""
Write a program that reads a number(N) and prints a Right Angled Triangle of N rows using stars(*)
#Sample Input1:4
#Sample Input2:7
#Expected Output1:*
                  **
                  ***
                  ****
                  
#Expected Output2:*
                  **
                  ***
                  ****
                  *****
                  ******
                  *******
"""
N = int(input())
for i in range(1,(N+1)):
    print("*"*i)

"""
Write a program that reads a number(N) and prints a Right Angled Triangle of N rows using numbers
#Sample Input1:6
#Sample Input2:3
#Expected Output1:1
                  22
                  333
                  4444
                  55555
                  666666
#Expected Output2:1
                  22
                  333
"""
N = int(input())
for i in range(1,(N+1)):
    print((str(i)+" ")*i)

"""
Write a program that reads a number N and prints a right angled triangle of N rows using starts(*) and pluses(+)
#Sample Input1:4
#Sample Input2:8
#Expected Output1:*
                  * *
                  * * *
                  + + + +
#Expected Output2:*
                  * * 
                  * * *
                  * * * *
                  * * * * *
                  * * * * * *
                  * * * * * * *
                  + + + + + + + +
"""
N = int(input())
for i in range(1,(N+1)):
    if(i==N):
        print("+ "*i)
    else:
        print("* "*i)

"""
Write a program that reads a number N and prints two Right abgled Triangles of N rows,using numbers starting from 1
#Sample Input1:4
#Sample Input2:2
#Expected Output1:1
                  22
                  333
                  4444
                  1
                  22
                  333
                  4444
#Expected Output2:1
                  22
                  1
                  22
"""
N = int(input())
for i in range(2):
    for j in range(1,(N+1)):
        print(str(j)*j)


"""
Write a program that reads two numbers M and N, and prints a Rectangle of M rows and N columns using numbers
#Sample Input1:2,3
#Sample Input2:5,4
#Expected Output1:1 1 1
                  2 2 2
#Expected Output2:1 1 1 1
                  2 2 2 2
                  3 3 3 3
                  4 4 4 4
                  5 5 5 5
"""
M = int(input())
N = int(input())
for i in range(M):
    print(str(i)*i)

"""
Write a program that reads two numbers M and N,and prints a Rectangle of M rows and N columns using numbers
#Sample Input1:2,3
#Sample Input2:5,4
#Expected Output1:1 1 1
                  2 2 2
#Expected Output2:1 1 1 1
                  2 2 2 2
                  3 3 3 3
                  4 4 4 4
                  5 5 5 5
"""
M = int(input())
N = int(input())
for i in range(1,(M+1)):
    print((str(i)+" ")*N)

"""
Write a program to print the sum of the squares of the first N natural numbers
#Sample Input1:6
#Sample Input2:3
#Expected Output1:91
#Expected Output2:14
"""
N = int(input())
Sum = 0
for i in range(1,(N+1)):
    Square = i**2
    Sum =Sum+Square
print(Sum)

"""
You are given an integer N as input. Write aa program to print integers from N to 1
#Sample Input1:5
#Sample Input2:3
#Expected Output1:5
                  4
                  3
                  2
                  1
#Expected Output2:3
                  2
                  1
"""
N = int(input())
for i in range(N):
    print(N)
    N-=1

"""
Write a program to print a rectangle pattern of M rows and N columns using the plus cgaracter(+)
#Sample Input1:3,5
#Sample Input2:4,4
#Expected Output1:+ + + + +
                  + + + + +
                  + + + + +

#Expected Output2:+ + + +
                  + + + +
                  + + + +
                  + + + +
"""
M = int(input())
N= int(input())
for i in range(M):
    print("+ "*N)

"""
Given an integer number N as input. Write a program to print the double triangular pattern of N lines using an Asterisk(*) character as shown below
#Sample Input1:4
#Sample Input2:5
#Expected Output1:*
                  * *
                  * * *
                  * * * *
                  *
                  * *
                  * * *
                  * * * *
#Expected Output2:*
                  * *
                  * * *
                  * * * *
                  * * * * *
                  *
                  * *
                  * * *
                  * * * *
                  * * * * *
"""
N = int(input())
for i in range(2):
    for j in range(1,(N+1)):
        print("* "*j)

"""
Write a program that reads a number N and prints the number from 0 to N
#Sample Input1:4
#Sample Input2:5
#Expected Output1:0
                  1
                  2
                  3
                  4
#Expected Output2:0
                  1
                  2
                  3
                  4
                  5
"""
N = int(input())
for i in range(N+1):
    print(i)

"""
Given a number N,write a program that reads N inputs and prints the average pf the given N inputs
#Sample Input1:4,3,4,6,7
#Sample Input2:2,24,15
#Expected Output1:5.0
#Expected Output2:19.5
"""

N = int(input())
Sum = 0
for i in range(N):
    M = int(input())
    Sum = Sum+M
print(Sum/N)

"""
Write a program that reads a number, and prints two Right Angled triangels of N rows using starts(*)
#Sample Input1:4
#Sample Input2:3
#Expected Output1:*
                  * *
                  * * *
                  * * * *
                  *
                  * *
                  * * *
                  * * * *
#Expected Output2:*
                  * *
                  * * *
                  *
                  * * 
                  * * *
"""
N = int(input())
for i in range(2):
    for j in range(1,(N+1)):
        print("* "*j)

"""
Write a program that reads two numbers M and N, and prints the product of numbers from M to N
#Sample Input1:5,7
#Sample Input2:9,14
#Expected Output1:210
#Expected Output2:2162160
"""
M = int(input())
N = int(input())
product = 1
for i in range(M,(N+1)):
    product = product*M
    M =M+1
print(product)