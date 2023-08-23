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