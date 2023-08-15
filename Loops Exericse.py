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
    Column = "0"*1
    print(Column)
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
#Sample Input1:
#Sample Input2:
#Expected Output1:
#Expected Output2:
"""