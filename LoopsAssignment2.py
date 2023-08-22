"""
Write a program to print the multiplication table of the given number(N) up to ten Multiples in the format"N*i=M'
#Sample Input1:3
#Sample Input2:10
#Expected Output1: 3 table
#Expected Output2:10 table
"""
N = int(input())
for i in range(1,11):
    table = str(N)+"x"+str(i)+"="+str(N*i)
    print(table)

#While Loop
N = int(input())
i = 1
while(i<11):
    table = str(N)+"x"+str(i)+"="+str(N*i)
    print(table)
    i+=1

"""
Write a program to print the reverse of the given string
#Sample Input1:Huuray! we have won the match.
#Sample Input2:Competitive Programming
#Expected Output1:.hctam eht now evah eW !yarruH
#Expected Output2:gnimmargorP evititepmoC
"""
String = input()
String = reversed(String)
for i in String:
    print(i, end="")

"""
Given a string S, Write a program to find the vowels in the given string S.
#Sample Input1:container
#Sample Input2:oiae
#Expected Output1:queue
#Expected Output2:ueue
"""
Word = input()
for i in Word:
    if((i=="a")or(i=="e")or(i=="i")or(i=="o")or(i=="u")):
        print(i,end="")


"""
Given a number N,Write a program to print the sum of the Kth power of all the digits in the given number
K indicates the number of digits of the number
#Sample Input1:24753
#Sample Input2:17
#Expected Output1:21231
#Expected Output2:50
"""
N = input()
K = len(N)
Sum = 0
for i in N:
    Kth_power = int(i)**K
    Sum = Sum+Kth_power
print(Sum)

#While Loop
N = input()
K = len(N)
Sum = 0
i = 0
while(i<N):
    Kth_power = int(i)**K
    Sum = Sum+Kth_power
print(Sum)


"""
Write a program that reads a number N and checks if N is an Armstrong Number
Print Armstrong Number is the given number is an Armstrong Number.Otherwise, print Not an Armstrong Number
#Sample Input1:153
#Sample Input2:24
#Expected Output1:Armstrong Number
#Expected Output2:Not an Armstrong Number
"""
N = input()
K = len(N)
Sum = 0
for i in N:
    Sum = Sum+ (int(i)**K)

if(Sum==int(N)):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

"""
Given a number N, Write a program to print the factors of the number N
'If a number N is divisible by X, then X is a factor of N.'
#Sample Input1:6
#Sample Input2:18
#Expected Output1:1,2,3,6
#Expected Output2:1,2,3,6,9,18
"""
N = int(input())
for i in range(1,(N+1)):
    if(N%i==0):
        print(i)

#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    if(N%i==0):
        print(i)
    i+=1

"""
Given a number N, write a program to prit all the factors of N separated by a space as shown in the sample output 
#Sample Input1:15
#Sample Input2:9
#Expected Output1:1 3 5 15
#Expected Output2:1 3 9
"""
N = int(input())
for i in range(1,(N+1)):
    if(N%i==0):
        print(i,end=" ")
#While Loop
N = int(input())
i = 1
while(i<(N+1)):
    if(N%i==0):
        print(i,end=" ")

"""
Given a number N, write a program to print the sum of the factors of the numbers N
#Sample Input1:12
#Sample Input2:8
#Expected Output1:28
#Expected Output2:15
"""
N = int(input())
Sum = 0
for  i in range(1,(N+1)):
    if(N%i==0):
        Sum =Sum+i
print(Sum)

#While Loop
N = int(input())
Sum = 0
i = 1
while(i<(N+1)):
    if(N%i==0):
        Sum = Sum+i
    i+=1
print(Sum)


"""
Given a number N, write a program that reads N inputs and prints the greatest among the given inputs
#Sample Input1:5,8,11,96,49,25
#Sample Input2:3,10,10,10
#Expected Output1:96
#Expected Output2:10
"""
N = int(input())
for i in range(N+1):
    M = int(input())



"""
Write a program to check whether the given number is a perfect number or not.
A number is considered as a perfect number if sum of all factors excluding itself is equal to the number.  
#Sample Input1:6
#Sample Input2:21
#Expected Output1:Perfect Nummber
#Expected Output2:Not a Perfect Number
"""
N = int(input())
Sum = 0
for i in range(1,N):
    if(N%i==0):
        Sum = Sum+i
if(N==Sum):
    print("Perfect Number")
else:
    print("Not a Perfect Number")

#While Loop
N = int(input())
i = 0
Sum = 0
while(i<N):
    if(N%i==0):
        Sum = Sum+i
    i+=1
if(N==Sum):
    print("Perfect Number")
else:
    print("Not a perfect Number")


"""
Given two numbers M and N, Write a program to find the count of numbers from M to N that are divisible by 6
Print No Numbers Found if the count of numbers from M to N that are divisible by 6 is 0.
Otherwise,Print the numbers from M to N that are divisible by 6 separated bya space
#Sample Input1:6,23
#Sample Input2:2,5
#Expected Output1:6 12 18
#Expected Output2:No Numbers Found
"""
M = int(input())
N = int(input())
for i in range(M,(N+1)):
    if(i%6==0):
        print(i)
else:
    print("No Numbers Found")