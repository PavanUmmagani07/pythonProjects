"""
Write a program to print a triangular pattern with numbers in N rows, wher integer N is given as input
Sample Input1:4
Expected Output1:
1
1 2
1 2 3
1 2 3 4
Sample Input2:5
Expected Output2:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
N = int(input())
rows = ""
for i in range(1,N+1):
    rows = rows+(str(i)+" ")
    print(rows)

#NESTED LOOPS
num = int(input())
for row_num in range(1,num+1):
    row_out=""
    # print(row_out)
    for seq_num in range(1,row_num+1):
        row_out = row_out+str(seq_num)+" "
    print(row_out)

"""
Given a number N, write a program to print a square of N rows using numbers starting from 1
#Sample Input1:3
#Expected Output1:
1 2 3 
1 2 3 
1 2 3
#Sample Input2:5
#Expected Output2:
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
"""
N = int(input())
for i in range(1,N+1):
    Num_seq = ""
    for j in range(1,N+1):
        Num_seq = Num_seq+str(j)+" "
    print(Num_seq)

#NESTED LOOPS
N = int(input())
for i in range(1,N+1):
    Num_seq = ""
    for j in range(1,N+1):
        Num_seq = Num_seq+str(j)+" "
    print(Num_seq)

"""
Given two numbers M and N , Write a program to print a Rectangle of M rows and N columns using numbers starting from 7
#Sample Input1:2,3
#Expected Output1:
7 8 9  
7 8 9 
#Sample Input2:5,4
#Expected Output2:
7 8 9 10 
7 8 9 10 
7 8 9 10 
7 8 9 10 
7 8 9 10 
"""
M = int(input())
N = int(input())
for i in range(1,M+1):
    Num_seq = ""
    for j in range(7,7+N):
        Num_seq = Num_seq+str(j)+" "
    print(Num_seq)

"""

#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected Output2:
"""