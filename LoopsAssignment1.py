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
