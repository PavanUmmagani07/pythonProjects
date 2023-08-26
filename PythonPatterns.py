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
Write a program to print stars in N rows and N columns, Where integer N is given as an input.
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
Write a program that reads a number N and prints an Inverted Right Angled Triangle pf N rows using stars(*)
#Sample Input1:5
#Sample Input2:3
#Expected Output1:* * * * *
                  * * * *
                  * * *
                  * *
                  *
#Expected Output2:* * *
                  * *
                  *
"""
N = int(input())
for i in range(1,(N+1)):
    print("* "*N)
    N = N-1

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    print("* "*N)
    N=N-1

"""
Write a program that reads a number N and prints an inverted Right angled Triangle of N rows using Numbers 
#Sample Input1:4
#Sample Input2:3
#Expected Output1:4 4 4 4
                  3 3 3
                  2 2 
                  1
#Expected Output2:3 3 3
                  2 2 
                  1
"""
N = int(input())
for i in range(1,(N+1)):
    print((str(i)+" ")*N)
    N =  N-1

#While Loop
N = int(input())
i = 0
j = N
while (i<(N+1)):
    print((str("j ")+" ")*j)
    j = j-1
    i+=1

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
for i in range(1, (M + 1)):
    print(str(i) * M)

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
    print("*" * N)

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
for i in range(1, (N + 1)):
    print("*" * i)

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
for i in range(1, (N + 1)):
    print((str(i) + " ") * i)

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
for i in range(1, (N + 1)):
    if (i == N):
        print("+ " * i)
    else:
        print("* " * i)

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
Write a program that reads a number n and prints an Inverted Right Angled Triangle of N rows using stars(*) and pluses(+)
#Sample Input1:4
#Sample Input2:6
#Expected Output1:* * * *
                  + + +
                  + +
                  +
#Expected Output2:* * * * * *
                  + + + + +
                  + + + +
                  + + +
                  + +
                  +
"""
N = int(input())
for i in range(N, 0, -1):
    if (i == N):
        print("+ " * N)
    else:
        print("* " * i)
#While Loop
# N = int(input())
# i = 1
# while(i<(N+1),-1):
#     if(i==N):
#         print("+ "*i)
#     else:
#         print("* "*i)
#     i+=1

"""
Write a program that reads number N and prints a Right angled Triangle of N rows and an inverted Right angled Triangle of N rows using stars(*)
#Sample Input1:3
#Sample Input2:5
#Expected Output1:*
                  * *
                  * * *
                  * * *
                  * *
                  *

#Expected Output2:*
                  * *
                  * * *
                  * * * *
                  * * * * *
                  * * * * *
                  * * * *
                  * * *
                  * *
                  *

"""

N = int(input())
for i in range(1, (N + 1)):
    print("* " * i)
for i in range(N, 0, -1):
    print("* " * i)




"""
Given a number N, write a program to print the Right Angled Triangle of N rows using starts(*)
#Sample Input1:3
#Sample Input2:4
#Expected Output1:  *
                   **
                  ***
#Expected Output2:  *
                   **
                  ***
                 ****
"""
N = int(input())
for i in range(1,(N+1)):
    print((N-i)*" "+"*"*i)

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    print((N-i)*" "+"*"*i)
    i+=1


"""
Given a number N, write a program to print the Right Angled Triangle of N rows using (*)
#Sample Input1:4
#Sample Input2:3
#Expected Output1:      *
                      * *
                    * * *
                  * * * *
#Expected Output2:    *
                    * *
                  * * * 
"""
N = int(input())
for i in range(1,(N+1)):
    print((N-i)*"  "+"* "*i)

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    print((N-i)*"  "+"* "*i)
    i+=1



"""
Given a  number N, write a program to print the Right Angled Triangle of N rows using stars (*) and hashes(#)
#Sample Input1:4
#Sample Input2:3
#Expected Output1:    *
                     **
                    ***
                   ####
#Expected Output2:  *
                   **
                  ###
"""
N = int(input())
for i in range(1,(N+1)):
    if(i==N):
        print((N-i)*" "+"#"*i)
    else:
        print((N-i)*" "+"*"*i)

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    if(i==N):
        print((N-i)*" "+"#"*i)
    else:
        print((N-i)*" "+"*"*i)
    i+=1


"""
Given a number N, write a program to print a pyramid of N rows using stars(*)
#Sample Input1:4
#Sample Input2:5
#Expected Output1:
      *       
    * * *     
  * * * * *   
* * * * * * * 
#Expected Output2:
        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * *
"""
N = int(input())
for i in range(1,(N+1)):
    left_spaces = (N-i)*" "
    left_strs = "* "*i
    right_strs = "* "*(i-1)
    print(left_spaces+left_strs+right_strs+left_spaces)


#while Loop
N = int(input())
i = 1
while(i<(N+1)):
    left_spaces = (N-i)*" "
    left_strs = "* "*i
    right_strs = "* "*(i-1)
    print(left_spaces+left_strs+right_strs+left_spaces)
    i+=1


"""
Given a number N, write a program to print a pyramid of N rows using numbers
#Sample Input1:5
#Sample Input2:3
#Expected Output1:
        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5
#Expected Output2:
    1 
  2 2 2 
3 3 3 3 3
"""
N = int(input())
for i in range(1,(N+1)):
    left_spaces = (N-i)*"  "
    left_nums = (str(i)+" ")*i
    right_nums = (str(i)+" ")*(i-1)
    print(left_spaces+left_nums+right_nums)

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    left_spaces = (N-i)*"  "
    left_nums = (str(i)+" ")*i
    right_nums = (str(i)+" ")*(i-1)
    print(left_spaces+left_nums+right_nums)
    i+=1

"""
Given a number N, write a program to print an inverted Right angled triangle of N rows using numbers 
#Sample Input1:3
#Sample Input2:6
#Expected Output1:
333
 22
  1
  

#Expected Output2:
666666
 55555
  4444
   333
    22
     1
"""
N = int(input())
for i in range(N):
    left_spaces = i*"  "
    left_nums = str(N)*(N)
    print(left_spaces+left_nums)
    N=N-1

#While Loop
N = int(input())
i=0
while(i<N):
    left_spaces = i*" "
    left_nums = str(N-i)*(N-i)
    print(left_spaces+left_nums)
    i+=1

"""
Given a number N, write a program to print an inverted Right angled triangle of N rows using numbers 
#Sample Input1:3
#Sample Input2:6
#Expected Output1:
3 3 3
  2 2
    1

#Expected Output2:
6 6 6 6 6 6
  5 5 5 5 5
    4 4 4 4
      3 3 3
        2 2
          1
"""
N = int(input())
for i in range(N):
    left_spaces = i * "  "
    left_nums = (str(N)+" ") * (N)
    print(left_spaces + left_nums)
    N = N - 1

# While Loop
N = int(input())
i = 0
while (i < N):
    left_spaces = i * " "
    left_nums = (str(N - i)+" ") * (N - i)
    print(left_spaces + left_nums)
    i += 14


"""
Given a number N, write a program to print an Inverted Pyramid of N rows using stars(*)
#Sample Input1:4
#Sample Input2:9
#Expected Output1:
#Expected Output2:
"""
