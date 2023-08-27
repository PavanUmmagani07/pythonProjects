"""
Given a number N, write a program to print a Square of N rows using (*) in the borders and Zeros(0) inside the Square
#Sample Input1:5
#Sample Input2:6
#Expected Output1:
* * * * *
* 0 0 0 *
* 0 0 0 *
* 0 0 0 *
* * * * *

#Expected Output2:
* * * * * *
* 0 0 0 0 *
* 0 0 0 0 *
* 0 0 0 0 *
* 0 0 0 0 *
* * * * * *
"""
N = int(input())
for i in range(1,(N+1)):
    if(i==1):
        print("* "*N)
    elif(i==N):
        print("* "*N)
    else:
        zeros = (("0 ")*(N-2))
        print("* "+zeros+"* ")

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    if(i==1):
        print("* "*N)
    elif(i==N):
        print("* "*N)
    else:
        zeros = (("0 ")*(N-2))
        print("* "+zeros+"* ")
    i+=1

"""
Given two numbers M and N, write a program to print Rectangle of M rows and N columns using stars(*) in the borders and Zeros(0) inside the triangle
#Sample Input1:4,8
#Sample Input2:7,5
#Expected Output1:
* * * * * * * * 
* 0 0 0 0 0 0 * 
* 0 0 0 0 0 0 * 
* * * * * * * * 

#Expected Output2:
* * * * * 
* 0 0 0 * 
* 0 0 0 * 
* 0 0 0 * 
* 0 0 0 * 
* 0 0 0 * 
* * * * * 
"""
M = int(input())
N= int(input())
for i in range(1,(M+1)):
    if(i==1):
        print("* "*N)
    elif(i==M):
        print("* "*N)
    else:
        zeros = "0 "*(N-2)
        print("* "+zeros+"* ")

#While loop
M = int(input())
N = int(input())
i = 1
while(i<(M+1)):
    if(i==1):
        print("* "*N)
    elif(i==M):
        print("* "*N)
    else:
        zeros = "0 "*(N-2)
        print("* "+zeros+"* ")
    i+=1

"""
Given a number N,write a program to print a Right Angled Triangle of N rows using dots(.) in the borders and Zeros (0) inside the right angled triangle
#Sample Input1:7
#Sample Input2:6
#Expected Output1:
. 
. . 
. 0 . 
. 0 0 . 
. 0 0 0 . 
. 0 0 0 0 . 
. . . . . . . 
#Expected Output2:
. 
. . 
. 0 . 
. 0 0 . 
. 0 0 0 . 
. . . . . . 
"""
N = int(input())
for i in range(1,(N+1)):
    if(i==1):
        print(". ")
    elif(i==N):
        print(". "*N)
    else:
        hollow_Zeros = "0 "*(i-2)
        print(". "+hollow_Zeros+". ")

#While Loop
N= int(input())
i = 1
while(i<(N+1)):
    if(i==1):
        print(". ")
    elif(i==N):
        print(". "*N)
    else:
        hollow_Zeros = "0 "*(i-2)
        print(". "+hollow_Zeros+". ")
    i+=1


"""
Given a number N, write a program to print a Square of N rows using stars(*)
#Sample Input1:4
#Sample Input2:6
#Expected Output1:
* * * * 
*     * 
*     * 
* * * *
#Expected Output2:
* * * * * * 
*         * 
*         * 
*         * 
*         * 
* * * * * * 
"""
N = int(input())
for i in range(1,(N+1)):
    if(i==1):
        print("* "*N)
    elif(i==N):
        print("* "*N)
    else:
        hollow_Spaces = (N-2)*"  "
        print("* "+hollow_Spaces+"* ")


#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    if(i==1):
        print("* "*N)
    elif(i==N):
        print("* "*N)
    else:
        hollow_Spaces = (N-2)*"  "
        print("* "+hollow_Spaces+"* ")
    i+=1


"""
Given two numbers M and N, write a program to print a Rectangle of M rows and N columns using stars
#Sample Input1:4,6
#Sample Input2:8,5
#Expected Output1:
* * * * * * 
*         * 
*         * 
* * * * * *

#Expected Output2:
* * * * * 
*       * 
*       * 
*       * 
*       * 
*       * 
*       * 
* * * * *
"""
M = int(input())
N = int(input())
for i in range(1,(M+1)):
    if(i==1):
        print("* "*N)
    elif(i==M):
        print("* "*N)
    else:
        hollow_Spaces = (N-2)*"  "
        print("* "+hollow_Spaces+"* ")


#While Loop
M = int(input())
N = int(input())
i = 1
while(i<(M+1)):
    if(i==1):
        print("* "*N)
    elif(i==M):
        print("* "*N)
    else:
        hollow_Spaces = (N-2)*"  "
        print("* "+hollow_Spaces+"* ")
    i+=1

"""
Given a number N, write a program to print a Right Angled Triangle of N rows using stars(*)
#Sample Input1:5
#Sample Input2:3
#Expected Output1:
* 
* * 
*   * 
*     * 
* * * * *
#Expected Output2:
* 
* * 
* * * 
"""
N = int(input())
for i in range(1,(N+1)):
    if(i==1):
        print("* ")
    elif(i==N):
        print("* "*N)
    else:
        hollow_Spaces = (i-2)*"  "
        print("* "+hollow_Spaces+"* ")

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    if(i==1):
        print("* ")
    elif(i==N):
        print("* "*N)
    else:
        hollow_Spaces = (i-2)*"  "
        print("* "+hollow_Spaces+"* ")
    i+=1
