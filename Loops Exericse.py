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