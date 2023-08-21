"""
Write a program that reads a number and prints all the digits of the given number separated by a space.
#Sample Input1:165
#Sample Input2:45866
#Expected Output1:1 6 5
#Expected Output2:4 5 8 6 6
"""
#For Loop
N = int(input())
N = str(N)
Result = N[0]
for i in range(1, len(N)):
    Result = Result+' '+N[i]
print(Result)

#WhileLoop
N = int(input())
N = str(N)
Result = N[0]
i = 1
while i < len(N):
    Result = Result+" "+N[i]
    i += 1
print(Result)


"""
Write a program to print the sum of all the digits in the given number
#Sample Input1:151893
#Sample Input2:692
#Expected Output1:27
#Expected Output2:17
"""
N = int(input())
N = str(N)
Sum = 0
for i in range(0, len(N)):
    Sum = Sum+int(N[i])
print(Sum)

#While Loop
N = int(input())
N = str(N)
Sum = 0
i = 0
while i < len(N):
    Sum = Sum+int(N[i])
    i += 1
print(Sum)

"""
Write a program to print the factorial of N
Factorial is the product of all positive integers lessthan or equal to N.
#Sample Input1:4
#Sample Input2:7
#Expected Output1:24
#Expected Output2:5040
"""
N = int(input())
product = 1
for i in range(N):
    product = product*N
    N =N-1
print(product)

#While Loop
N = int(input())
Product = 1
i =1
while i<(N+1):
    Product = Product*i
    i+=1
print(Product)

"""
Write a program that reads a number N, and prints the Sum of the cubes of numbers from 1 to N.
#Sample Input1:3
#Sample Input2:6
#Expected Output1:36
#Expected Output2:441
"""

N = int(input())
Sum = 0
for i in range(1,(N+1)):
    cubes = i**3
    Sum = Sum+cubes
print(Sum)

#While Loop
N = int(input())
Sum = 0
i = 1
while i<(N+1):
    cubes = i**3
    Sum = Sum+cubes
    i+=1
print(Sum)

"""
Write a program that reads 10 inputs and prints the sum and average of the given 10 inputs.
#Sample Input1:4,7,14,25,1,8,24,38,99,10
#Sample Input2:20,35,99,-84,-93,2,7,53,23,11
#Expected Output1:230,23.0
#Expected Output2:73,7.3
"""
N = int(input())
Sum = 0
for i in range(N):
    M = int(input())
    Sum = Sum+M
print(Sum)
print(Sum/N)

#While Loop
N = int(input())
Sum = 0
i = 0
while i<N:
    M = int(input())
    Sum =Sum+M
print(Sum)
print(Sum/N)

"""
Write a program that reads a number N and prints the sum of the even numbers from 1 to N.
#Sample Input1:6
#Sample Input2:10
#Expected Output1:12
#Expected Output2:30
"""
N = int(input())
Sum = 0
for i in range(1,(N+1)):
    if(i%2==0):
        Sum = Sum+i
print(Sum)

#WhileLoop
N = int(input())
i = 1
Sum = 0
while i<(N+1):
    if(i%2==0):
        Sum = Sum+i
    i+=1
print(Sum)


"""
Write a program that reads a number N and prints the sum of the odd numbers from 1 to N
#Sample Input1:6
#Sample Input2:15
#Expected Output1:9
#Expected Output2:64
"""
N = int(input())
Sum = 0
for i in range(1,(N+1)):
    if(i%2==1):
        Sum = Sum+i
print(Sum)

#While Loop
N = int(input())
Sum = 0
i = 0
while(i<(N+1)):
    if(i%2==1):
        Sum = Sum+i
    i+=1
print(Sum)

"""
Write a program that reads numbers M and N and prints the sum of the even numbers from M to N
#Sample Input1:2,6
#Sample Input2:10,20
#Expected Output1:12
#Expected Output2:90
"""
M = int(input())
N = int(input())
Sum = 0
for i in range(M,(N+1)):
    if(i%2==0):
        Sum = Sum+i
print(Sum)

#While Loop
M = int(input())
N = int(input())
Sum = 0
i = M
while i<(N+1):
    if(i%2==0):
        Sum =Sum+i
    i+=1
print(Sum)

"""
Write a program that reads numbers M and N and prints the sum of the even numbers from M to N
#Sample Input1:2,6
#Sample Input2:10,20
#Expected Output1:12
#Expected Output2:90
"""
M = int(input())
N = int(input())
Sum = 0
for i in range(M,(N+1)):
    if(i%2==1):
        Sum = Sum+i
print(Sum)

#While Loop
M = int(input())
N = int(input())
Sum = 0
i = M
while i<(N+1):
    if(i%2==1):
        Sum =Sum+i
    i+=1
print(Sum)


"""
Write a program that reads a number N and prints even numbers from 1 to N.
#Sample Input1:7
#Sample Input2:10
#Expected Output1:2,4,6
#Expected Output2:2,4,6,8,10
"""
N = int(input())
for i in range(1,(N+1)):
    if(i%2==0):
        print(i)

#WhileLoop
N = int(input())
i = 1
while(i<(N+1)):
    if(i%2==0):
        print(i)
    i+=1


"""
Write a program that reads a number N and prints odd numbers from 1 to N.
#Sample Input1:7
#Sample Input2:10
#Expected Output1:1,3,5,7
#Expected Output2:1,3,5,7,9
"""
N = int(input())
for i in range(1,(N+1)):
    if(i%2==1):
        print(i)

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    if(i%2==1):
        print(i)
    i+=1


"""
Write a program that reads two numbers M and N and prints odd numbers from M to N separated by a space
#Sample Input1:5,10
#Sample Input2:9,21
#Expected Output1:5 7 9
#Expected Output2:9 11 13 15 17 19 21
"""
M = int(input())
N = int(input())
for i in range(M,(N+1)):
    if(i%2==1):
        print(i,end=" ")

#WhileLoop
M = int(input())
N = int(input())
i = M
while(i<(N+1)):
    if(i%2==1):
        print(i,end=" ")
    i+=1

"""
Write a program that reads two numbers M and N, and prints the sum of squares of numbers from M to N
#Sample Input1:2,4
#Sample Input2:3,8
#Expected Output1:29
#Expected Output2:199
"""
M = int(input())
N = int(input())
Sum = 0
for i in range(M,(N+1)):
    squares = i**2
    Sum = Sum+squares
print(Sum)

#While Loop
M = int(input())
N = int(input())
i = M
Sum = 0
while(i<(N+1)):
    squares = i**2
    Sum = Sum+squares
    i+=1
print(Sum)

"""
Write a program that reads two numbers M and N, and prints the product of odd numbers from M to N
#Sample Input1:2,7
#Sample Input2:4,8
#Expected Output1:105
#Expected Output2:35
"""

M = int(input())
N = int(input())
K = 1
for i in range(M,(N+1)):
    if(i%2==1):
        K = K*i
print(K)

#While Loop
M = int(input())
N = int(input())
K = 1
i = M
while(i<(N+1)):
    if(i%2==1):
        K = K*i
    i+=1
print(K)

"""
Given three integers, write a program to print the sum pf the numbers divisibile by the given number T from M to N
#Sample Input1:2,5,9
#Sample Input2:10,20,200
#Expected Output1:14
#Expected Output2:2090
"""
T = int(input())
M = int(input())
N = int(input())
Sum = 0
for i in range(M,(N+1)):
    if(i%T==0):
        Sum = Sum+i
print(Sum)

#While Loop
T = int(input())
M = int(input())
N = int(input())
Sum = 0
i = M
while(i<(N+1)):
    if(i%T==0):
        Sum = Sum+i
    i+=1
print(Sum)

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
Write a program that reads two numbers N and T,and Prints all the numbers from 1 to N that are divisible by T
#Sample Input1:10,3
#Sample Input2:3,6,9
#Expected Output1:21,5
#Expected Output2:5,10,15,20
"""
N = int(input())
T = int(input())
for i in range(1,(N+1)):
    if(i%T==0):
        print(i)

#While Loop
N = int(input())
T = int(input())
i = 1
while i<(N+1):
    if(i%T==0):
        print(i)
    i+=1

"""
Write a program that reads two numbers M and N, and prints the numbers from N to M.
#Sample Input1:2,5
#Sample Input2:3,10
#Expected Output1:5,4,3,2
#Expected Output2:10,9,8,7,6,5,4,3
"""
M = int(input())
N = int(input())
for i in range(M,(N+1)):
    print(N)
    N = N-1

#While Loop
M = int(input())
N = int(input())
j = N
while(i<(N+1)):
    print(j)
    j = j-1
    i+=1


"""
Write a program that reads a number N and prints the number from N to 1
#Sample Input1:5
#Sample Input2:3
#Expected Output1:5,4,3,2,1
#Expected Output2:3,2,1
"""
N = int(input())
for i in range(N):
    print(N)
    N = N-1

#While Loop
N = int(input())
i = 0
while(i<N):
    print(N)
    N = N-1


"""
Given three integers, write a program to print the sum of the numbers divisibile by the given number T from M to N
#Sample Input1:2,5,9
#Sample Input2:10,20,200
#Expected Output1:14
#Expected Output2:2090
"""
M = int(input())
N = int(input())
T = int(input())
Sum = 0
for i in range(M,(N+1)):
    if(i%T==0):
        Sum = Sum+i
print(Sum)

#While Loop
M = int(input())
N = int(input())
T = int(input())
Sum = 0
i = M
while (i<(N+1)):
    if(i%T==0):
        Sum = Sum+i
print(Sum)

"""
Write a program that reads a number N and prints all the numbers from 1 to N that are divisibile by both 2 and 3
#Sample Input1:15
#Sample Input2:6,12
#Expected Output1:9
#Expected Output2:6
"""
N = int(input())
for i in range(1,N+1):
    if((i%2==0) and(i%3==0)):
        print(i)

#While Loop
N = int(input())
i = 1
while (i<(N+1)):
    if((i%2==0) and(i%3==0)):
        print(i)
    i+=1


"""
Write a program that reads two numbers and prints the sum of the kth power of all the numbers from 1 to N
#Sample Input1:5,3
#Sample Input2:2,8
#Expected Output1:225
#Expected Output2:257
"""

N = int(input())
K = int(input())
Sum = 0
for i in range(1,(N+1)):
    Kth_power = i**K
    Sum =Sum+Kth_power
print(Sum)

#While Loop
N = int(input())
K = int(input())
Sum = 0
i = 1
while(i<(N+1)):
    Kth_power = i**K
    Sum = Sum+Kth_power
print(Sum)

"""
Given an integer N, and exponent M as input, Write a program to calculate N power M without using the power operator(**)
#Sample Input1:2,3
#Sample Input2:3,1
#Expected Output1:8
#Expected Output2:3
"""
N = int(input())
M = int(input())
K = 1
i = 0
for i in range(M):
    K = K*N
print(K)

#While Loop
N = int(input())
M = int(input())
K = 1
i = 0
while(i<M):
    K = K*N
    i+=1
print(K)


"""
Given two integers M, N. Write a program to print the product of numbers in the range M and N(inclusive of M and N)
#Sample Input1:2,5
#Sample Input2:1,4
#Expected Output1:120
#Expected Output2:24
"""
M = int(input())
N = int(input())
K = 1
for i in range(M,(N+1)):
    K = K*i
print(K)

#While Loop
M = int(input())
N = int(input())
i = M
K = 1
while(i<(N+1)):
    K = K*i
print(K)

"""
Write a program that reads two numbers M and N and finds the products of the numbers from M to N that are divisible by 3
Print the product of the numbers from M to N that are divisible by 3. if there are no numbers that are divisible by 3 from M to N. otherwise print 1
#Sample Input1:2,7
#Sample Input2:12,14
#sample Input3 = 1,2
#Expected Output1:18
#Expected Output2:12
#Expected Output: 1
"""
M = int(input())
N = int(input())
K = 1
for i in range(M,(N+1)):
    if(i%3==0):
        K = K*i
print(K)

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
for i in range(1,(N+1)):
    if(i!=N):
        print("+ "*i)
    else:
        print("* "*N)
    N = N-1


"""
Write a program that reads a number N and prints the count of numbers from 1 to N that are divisible by both 6 and 8
#Sample Input1:50
#Sample Input2:175
#Expected Output1:2
#Expected Output2:7
"""
N = int(input())
count = 0
for i in range(1,(N+1)):
    if((i%6==0) and (i%8==0)):
        count+=i
print(count)

#While Loop
N = int(input())
count = 0
i = 1
while (i<(N+1)):
    if((i%6==0) and(i%8==0)):
        count+=1
        i+=1
print(count)

"""
Write a program that reads two numbers N and T and prints the count of numbers from 1 to N that are divisible by T
#Sample Input1:12,3
#Sample Input2:4
#Expected Output1:25,5
#Expected Output2:5
"""
N = int(input())
T = int(input())
count = 0
for  i in range(1,(N+1)):
    if(i%T==0):
        count+=1
print(count)

#While Loop
N = int(input())
T = int(input())
count = 0
i =1
while (i<(N+1)):
    if(i%T==0):
        count+=1
    i+=1
print(count)

"""
Write a program that reads a number N and prints the count of numbers from 1 to N that are divisible by both 2 and 3
#Sample Input1:12
#Sample Input2:21
#Expected Output1:2
#Expected Output2:3
"""
N = int(input())
count = 0
for i in range(1,(N+1)):
    if((i%2==0) and(i%3==0)):
        count+=1
print(count)

#While Loop
N = int(input())
count = 0
i = 1
while(i<(N+1)):
    if((i%2==0) and(i%3==0)):
        count+=1
    i+=1
print(count)

"""
Write a program that reads a string and prints the a and Z characters in the string
#Sample Input1:zigzag
#Sample Input2:zap
#Expected Output1:z,z,a
#Expected Output2:z,a
"""
Word = input()
for i in Word:
    if((i=="a") and(i=="z")):
        print(i)


"""
Write a program that reads a string and prints the vowels in the string
#Sample Input1:indian
#Sample Input2:i,i,a
#Expected Output1:nxtwave
#Expected Output2:a,e
"""
Word = input()
for i in Word:
    if((i=='a') or (i=='e') or(i=='i') or(i=='o') or(i=='u')):
        print(i)


"""
Write a program that reads a string and prints the count of vowels in the string
#Sample Input1:code
#Sample Input2:developer
#Expected Output1:2
#Expected Output2:4
"""
Word = input()
count = 0
for i in Word:
    if ((i == 'a') or (i == 'e') or (i == 'i') or (i == 'o') or (i == 'u')):
        count+=1
print(count)


"""
Write a program that reads a string and prints the character of a string in reverse order
#Sample Input1:scale
#Sample Input2:Metrics
#Expected Output1:elacs
#Expected Output2:scirteM
"""
Word = input()
Word = reversed(Word)
for i in Word:
    print(i)


"""
Write a program that reads two numbers M and N, and prints the odd numbers from N to M separated by a space
#Sample Input1:1,10
#Sample Input2:5,15
#Expected Output1:9 7 5 3 1
#Expected Output2:15 13 11 9 7 5
"""
M = int(input())
N = int(input())
for i in range(N,(M-1),-1):
    if(i%2!=0):
        print(i,end=" ")