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

"""
Given a number N, write a program to print a Right Angled Triangle of N rows using underscore(_),pipr(|) and Forward slash(/)
#Sample Input1:5
#Sample Input2:7
#Expected Output1:

#Expected Output2:
"""
N = int(input())
print("- " * N)
for i in range(1, (N + 1)):
    hallow_Spaces = (N - i) * " "
    print("| " + hallow_Spaces + "/ ")

# While Loop
N = int(input())
print("- " * N)
i = 1
while (i < (N + 1)):
    hallow_Spaces = (N - i) * " "
    print("| " + hallow_Spaces + "/")
    i += 1

"""
Given a number N, write a program to print a Hollow pyramid of N rows using stars(*)
#Sample Input1:5
#Sample Input2:6
#Expected Output1:
    * 
   * *
  *   *
 *     *
* * * * * 
#Expected Output2:
     * 
    * *
   *   *
  *     *
 *       *
* * * * * *

"""

N = int(input())
for i in range(1,(N+1)):
    left_Spaces = (N - i) * " "
    if(i==1):
        print(left_Spaces+"* ")
    elif(i==N):
        print("* "*N)
    else:
        hollow_Spaces = (i - 2) * "  "
        print(left_Spaces + "* " + hollow_Spaces + "*")

#Using if-else
N = int(input())
for i in range(1,N+1):
    left_spaces = (N-i)*" "
    if((i>2) and(i<N)):
        hollow_Spaces = (i-2)*"  "
        print(left_spaces+"* "+hollow_Spaces+"*")
    else:
        print(left_spaces+"* "*i)

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    left_Spaces = (N-i)*" "
    if((i>2) and(i<N)):
        hollow_Spaces = (i-2)*"  "
        print(left_Spaces+"* "+hollow_Spaces+"*")
    else:
        print(left_Spaces+"* "*i)


"""
Given a number N, write a program to print a Hallow Right angled Triangle of N rows using Pluses(+) and Hashes(#)
#Sample Input1:6
#Sample Input2:7
#Expected Output1:
# # # # # # 
+       +
+     +
+   +
+ +
+
#Expected Output2:
# # # # # # # 
+         +
+       +
+     +
+   +
+ +
+ 

"""
N = int(input())
for i in range(N, 0, -1):
    if i == N:
        print("# " * N)
    elif i > 1:
        hollow_Spaces = (i - 2) * "  "
        print("+ " + hollow_Spaces + "+")
    else:
        print("+ ")

#While Loo[
N = int(input())
i = 1
while(i<(N+1)):
    if(i==1):
        print("# " * N)
    elif((i>1) and(i<N)):
        hallow_Spaces = (N-(i+1))*"  "
        print("+ "+hallow_Spaces+"+")
    else:
        print("+ ")
    i+=1


"""
Given a number N, write a program to print a Hollow Pyramid of 2*N-1 rows using Numbers
#Sample Input1:4
#Sample Input2:7
#Expected Output1:
1 
2 2
3   3
4     4
3   3
2 2
1 
#Expected Output2:
1 
2 2
3   3
4     4
5       5
6         6
7           7
6         6
5       5
4     4
3   3
2 2
1 
"""
N = int(input())
for i in range(1, N+1):
    if i == 1:
        print(str(i)+" ")
    else:
        hollow_Spaces = (i-2)*"  "
        print((str(i)+" ")+hollow_Spaces+str(i))

for j in range(1,N):
    num = N-j
    if(j==(N-1)):
        print("1 ")
    else:
        hollow_Spaces = (num-2)*"  "
        print((str(num)+" ")+hollow_Spaces+str(num))


"""
Given a number N, write a program to print the Hollow Right angled Triangle of N rows using stars(*)
#Sample Input1:5
#Sample Input2:3
#Expected Output1:
* * * * * 
*     *
*   *
* *
*
#Expected Output2:
* * * 
* *
*
"""
N = int(input())
for i in range(N,0,-1):
    if(i==N):
        print("* "*N)
    elif(i>1):
        hollow_Spaces ="  "*(i-2)
        print("* "+hollow_Spaces+"*")
    else:
        print("*")


"""
Given a Number N, write a  program to print the Hollow Right Angled Triangle of N rows using stars(*)
#Sample Input1:4
#Sample Input2:5
#Expected Output1:
      *
    * *
  *   *
* * * *
#Expected Output2:
        *
      * *
    *   *
  *     *
* * * * *
"""
N = int(input())
for i in range(1,(N+1)):
    left_Spaces = (N-i)*"  "
    if(i==N):
        print("* "*N)
    elif(i>1):
        hollow_Spaces ="  "*(i-2)
        print(left_Spaces+"* "+hollow_Spaces+"*")
    else:
        print(left_Spaces+"*")


#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    left_Spaces = (N-i)*"  "
    if(i==N):
        print("* "*N)
    elif(i>1):
        hollow_Spaces = "  "*(i-2)
        print(left_Spaces+"* "+hollow_Spaces+"*")
    else:
        print(left_Spaces+"*")
    i+=1

"""
Given a Number N, write a  program to print the Hollow Right Angled Triangle of N rows using stars(*)
#Sample Input1:4
#Sample Input2:5
#Expected Output1:
* * * * 
  *   *
    * *
      *
#Expected Output2:
* * * * * 
  *     *
    *   *
      * *
        *
"""
N = int(input())
for i in range(N,0,-1):
    left_Spaces = (N-i)*"  "
    if(i==N):
        print("* "*N)
    elif(i>1):
        hollow_Spaces ="  "*(i-2)
        print(left_Spaces+"* "+hollow_Spaces+"*")
    else:
        print(left_Spaces+"*")

"""
Given a number N, write a program to print the Hollow Inverted Full Pyramid of N rows using stars(*)
#Sample Input1:5
#Sample Input2:3
#Expected Output1:
* * * * * 
 *     *
  *   *
   * * 
    * 
#Expected Output2:
* * * 
 * * 
  *
"""
N = int(input())
for i in range(N,0,-1):
    left_Spaces = (N - i) * " "
    if(i==1):
        print(left_Spaces+"* ")
    elif(i==N):
        print("* "*N)
    else:
        hollow_Spaces = (i - 2) * "  "
        print(left_Spaces + "* " + hollow_Spaces + "*")

#Using if-else
N = int(input())
for i in range(N,0,-1):
    left_spaces = (N-i)*" "
    if((i>2) and(i<N)):
        hollow_Spaces = (i-2)*"  "
        print(left_spaces+"* "+hollow_Spaces+"*")
    else:
        print(left_spaces+"* "*i)


"""
Given a Number N, write a program to the Hollow Diamond of 2*N-1 rows using stars(*)
#Sample Input1:5
#Sample Input2:7
#Expected Output1:
#Expected Output2:
"""