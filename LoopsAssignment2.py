"""
Write a program to print the multiplication table of the given number(N) up to ten Multiples in the format"N*i=M'
#Sample Input1:3
#Sample Input2:10
#Expected Output1: 3 table
#Expected Output2:10 table
"""
N = int(input())
for i in range(1, 11):
    table = str(N)+"x"+str(i)+"="+str(N*i)
    print(table)

#While Loop
N = int(input())
i = 1
while i < 11:
    table = str(N)+"x"+str(i)+"="+str(N*i)
    print(table)
    i += 1

"""
Write a program to print the reverse of the given string
#Sample Input1:Huray! we have won the match.
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
    if ((i=="a") or (i=="e") or (i=="i") or (i=="o") or (i=="u")):
        print(i, end="")


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
#Expected Output1:Perfect Number
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
result = "No Numbers Found"
for i in range(M,(N+1)):
    if(i%6==0):
        result = i
        if type(result)!=str:
            print(result)
if type(result)==str:
    print(result)
#Method2
n = int(input())
m = int(input())
count = 0
numbers_divisible_by_6 = ""
for i in range(m,(n+1)):
    if i%6==0:
        numbers_divisible_by_6 = numbers_divisible_by_6+str(i)+" "
        count+=1
if count==0:
    print("No Numbers Found")
else:
    print(numbers_divisible_by_6)
#While Loop
M = int(input())
N = int(input())
i = M
result = "No Numbers Found"
while(i<(N+1)):
    if(i%6==0):
        result = i
        if type(result)!=str:
            print(result)
    i+=1
if type(result)==str:
    print(result)


"""
Given two numbers M and N, Write a program to find the count of the numbers from M to N that are divisible by 9.
Print 'No Numbers Found' if the count of numbers from M to N that are divisible by 9 is 0.
otherwise, print the numbers from M to N separated bya space that are divisible by 9.
#Sample Input1:5,25
#Sample Input2:3,8
#Expected Output1:9 18
#Expected Output2:No Numbers Found
"""
M = int(input())
N = int(input())
count = 0
numbers_divisible_by_9 = ""
for i  in range(M,(N+1)):
    if(i%9==0):
        numbers_divisible_by_9 = numbers_divisible_by_9+str(i)+" "
        count+=1
if(count!=0):
    print(numbers_divisible_by_9)
else:
    print("No Numbers Found")


#While Loop
M = int(input())
N = int(input())
i = M
count = 0
numbers_divisible_by_9=""
while(i<(N+1)):
    if(i%9==0):
        numbers_divisible_by_9 = numbers_divisible_by_9+str(i)+" "
        count+=1
    i+=1
if(count!=0):
    print(numbers_divisible_by_9)
else:
    print("No Numbers Found")


"""
Given two numbers M and N, write a program to print the count of the total numbers of digits from M to N.
#Sample Input1:4,13
#Sample Input2:5,8
#Expected Output1:14
#Expected Output2:4
"""

M = int(input())
N = int(input())
count = 0
for i in range(M,(N+1)):
    i = str(i)
    count = count+len(i)
print(count)


#While Loop
M = int(input())
N = int(input())
count = 0
i = M
while(i<(N+1)):
    i = str(i)
    count = count+len(i)
    i= int(i)+1
print(count)


"""
Given a string write a program to find the count of Vowels in the string.
Print String has more than two vowels if the count of vowels is greater than 2. Other wise,print String doesn't have more than two vowels
#Sample Input1:indian
#Sample Input2:code
#Expected Output1:String has more than two vowels
#Expected Output2:String doesn't have more than two vowels
"""
String = input()
Count = 0
for i in String:
    if((i=='a')or(i=='e')or(i=='i')or(i=='o')or(i=='u')):
        Count+=1
if(Count>2):
    print("String has more than two vowels")

else:
    print("String doesn't have more than two vowels")


"""
Given a number N, write a program that checks if N is not divisible by any number from 2 to 9.
Print Divisible Number if the number N is divisible by any of the numbers from 2 to 9.
Print Indivisible Number if the number N is not divisible by any number from 2 to 9
#Sample Input1:15
#Sample Input2:103
#Expected Output1:Divisible Number
#Expected Output2:Indivisible Number
"""
N = int(input())
result = "Indivisible Number"
for i in range(2,10):
    if(N%i==0):
        print("Divisible Number")
print(result)

"""
Given a number N, write a program to print the N terms in the given series, each on a new line
series:
2, 22, 222, 2222, 22222,.......N terms
#Sample Input1:6
#Sample Input2:3
#Expected Output1:2
                  22
                  222
                  2222
                  22222
                  222222
#Expected Output2:2
                  22
                  222
"""
N = int(input())
term_num = '2'
for i in range(1,(N+1)):
    term = term_num*i
    print(term)

#While Loop
N = int(input())
term_num= '2'
i =1
while(i<(N+1)):
    term = term_num*i
    print(term)
    i+=1


"""
Given an integer N, Write a program to print the sum of N terms in the given series
series:
2, 22, 222, 2222,.......N terms
#Sample Input1:3
#Sample Input2:8
#Expected Output1:246
#Expected Output2:24691356
"""
N = int(input())
term_num = '2'
Sum = 0
for i in range(1,(N+1)):
    term = term_num*i
    Sum = Sum+int(term)
print(Sum)

#While Loop
N = int(input())
term_num = '2'
i = 1
Sum = 0
while(i<(N+1)):
    term = term_num*i
    Sum = Sum+int(term)
print(Sum)

"""
Given an integer N, write a program to print the sum of N terms in the given series.
Series:
1, 11, 111,....N terms
#Sample Input1:4
#Sample Input2:5
#Expected Output1:1234
#Expected Output2:12345
"""
N = int(input())
term_num = '1'
sum = 0
for i in range(1,(N+1)):
    term = term_num*i
    sum = sum+int(term)
print(sum)

#While Loop
N = int(input())
term_num = '1'
i = 1
sum = 0
while(i<(N+1)):
    term = term_num*i
    sum = sum+int(term)
    i+=1
print(sum)

"""
Given two numbers X and N, Write a program to print the sum of N terms in the given series.
Series: X,XX,XXX,.....N terms
#Sample Input1:7,4
#Sample Input2:6,2
#Expected Output1:8638
#Expected Output2:72
"""
term_X = input()
N = int(input())
Sum = 0
for i in range(1,(N+1)):
    term = term_X*i
    Sum = Sum+int(term)
print(Sum)

#While Loop
term_X = input()
N = int(input())
Sum = 0
i = 1
while(i<(N+1)):
    term = term_X*i
    Sum = Sum+int(term)
print(Sum)

"""
Given two numbers X and N, Write a program to print the sum of N terms in the given series.
Series:(X)^2, (XX)^2, (XXX)^2,........N terms
#Sample Input1:4,3
#Sample Input2:7,4
#Expected Output1:199088
#Expected Output2:61091436
"""
term_X = input()
N = int(input())
Sum = 0
for i in range(1,(N+1)):
    term = term_X*i
    squares_of_terms = int(term)**2
    Sum = Sum+squares_of_terms
print(Sum)

#While Loop
term_X = input()
N = int(input())
Sum = 0
i = 1
while(i<(N+1)):
    term = term_X*i
    squares_of_terms = int(term)**2
    Sum = Sum+squares_of_terms
    i+=1
print(Sum)


"""
Given two numbers X and N, Wrie a program to print the sum of N terms in the given series
Series: X^1, X^3, X^5.....N terms
#Sample Input1:2,6
#Sample Input2:5,3
#Expected Output1:2730
#Expected Output2:3255
"""
term_X = int(input())
N = int(input())
Sum_of_series = 0
for i in range(1,N+1):
        term = term_X**((2*i)-1)
        Sum_of_series = Sum_of_series+term
print(Sum_of_series)

#While Loop
term_X = int(input())
N = int(input())
Sum_of_series = 0
i = 1
while(i<(N+1)):
    term = term_X**((2*i)-1)
    Sum_of_series = Sum_of_series+term
    i+=1
print(Sum_of_series)
"""
Given two numbers X and N, Write a program to print the sum of N terms in the given series
Series: X^2, X^4, X^6.....N terms
#Sample Input1:3,4
#Sample Input2:-2,6
#Expected Output1:7380
#Expected Output2:5460
"""

term_X = int(input())
N = int(input())
Sum_of_series = 0
for i in range(1,N+1):
        term = term_X**(2*i)
        Sum_of_series = Sum_of_series+term
print(Sum_of_series)

#While Loop
term_X = int(input())
N = int(input())
Sum_of_series = 0
i = 1
while(i<(N+1)):
    term = term_X**(2*i)
    Sum_of_series = Sum_of_series+term
    i+=1
print(Sum_of_series)

"""
Given two numbers X and N, Write a program to print the sum of N terms in the given series
Series: X^2, -X^4, X^6, -X^8.....N terms
#Sample Input1:2,6
#Sample Input2:-7,3
#Expected Output1:-3276
#Expected Output2:115297
"""
term_X = int(input())
N = int(input())
Sum_of_series = 0
for i in range(1,N+1):
    power = 2*i
    if(power%4==0):
        term =-(term_X**power)
    else:
        term = term_X**power
    Sum_of_series = Sum_of_series+term
print(Sum_of_series)

#While Loop
term_X = int(input())
N = int(input())
i = 1
Sum_of_series = 0
while(i<(N+1)):
    power = 2*i
    if(power%4==0):
        term = -(term_X**power)
        Sum_of_series= Sum_of_series+term
    else:
        term = term_X**power
        Sum_of_series= Sum_of_series+term
    i+=1
print(Sum_of_series)


"""
Write a program that reads the number N and finds the count of digits from 1 to N
#Sample Input1:10
#Sample Input2:4
#Expected Output1:11
#Expected Output2:4
"""
N = int(input())
count = 0
for i in range(1,(N+1)):
    i = str(i)
    count = count+len(i)
print(count)

#While Loop
N = int(input())
i = 1
count = 0
while(i<(N+1)):
    count=count+len(str(i))
print(count)

"""
Given two numbers X and N, Write a program to print the sum of N terms in the given series
Series: X, -X^3, X^5, -X^7, -X^9,.....N terms
#Sample Input1:2,5
#Sample Input2:3,2
#Expected Output1:410
#Expected Output2:-24
"""
term_X = input()
N = int(input())
Sum_of_terms = 0
K = 1
for i in range(1,(N+1)):
    term = K*(term_X**(2*i+1))
    Sum_of_series = Sum_of_series+term
    K = K-1
print(Sum_of_series)
"""
Given a number N, Write a program to find the count of factors of N.
#Sample Input1:6
#Sample Input2:13
#Expected Output1:Number has more than 2 factors
#Expected Output2:Number doesn't have more than 2 factors
"""
N = int(input())
count = 0
for i in range(1,(N+1)):
    if(N%i==0):
        count= count+1
if(count>2):
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")

#While Loop
N = int(input())
count = 0
i = 1
while(i<(N+1)):
    if(N%i==0):
        count = count+1
    i+=1

if(count>2):
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")


"""
Given a string, Write a program to print substrings in expected pattern of N rows, where N is the lenght of the string
#Sample Input1:Rahul
#Sample Input2:Pavan
#Expected Output1:R
                  Ra
                  Rah
                  Rahu
                  Rahul
#Expected Output2:P
                  Pa
                  Pav
                  Pava
                  Pavan
"""
String  = input()
for index in range(1,len(String)+1):
    print(String[:index])


"""
Given a string S and N integers Where N is the length of string S
Print the characters as per the order of the integers given
#Sample Input1:goindc
              5,1,4,2,3,0
#Expected Output1:coding
#Sample Input2:abc
               0,1,2
#Expected Output2:abc

#Sample Input3:eimag
               1,2,3,4,0
#Expected Output3:image
"""

String = input()
updated_str=""
for i in range(len(String)):
     N = int(input())
     updated_str = updated_str+String[N]
print(updated_str)


"""
Write a program to print if the given number is a Prime number
Note: A prime Number is divisible only by itself and 1
#Sample Input1:5
#Sample Input2:4
#Expected Output1:Prime Number
#Expected Output2:Not a Prime Number
"""
N = int(input())
factors = 0
for i in range(1,N+1):
    if(N%i==0):
        factors = factors+1
if(factors>2):
    print("Not a Prime Number")
else:
    print("Prime Number")

N = input()
factors = 0
for i in range(2,N):
    if(N%i==0):
        factors+1
if(factors==0):
    print("Prime Number")
else:
    print("Not a Prime Number")



"""
Given a string and N indices, where N i the length of the string.
Write a Program to print the character of the string present at each index of the given N indices
#Sample Input1:tarc
               3,1,2,0
#Sample Input2:eesnv
               2,0,4,1,3
#Expected Output1:c
                  a
                  r
                  t
#Expected Output2:s
                  e
                  v
                  e
                  n
"""
String = input()
for i in range(len(String)):
     N = int(input())
     print(String[N])

"""
Given a number N, write a program to print a square of N rows and N columns using numbers starting from 0
#Sample Input1:3
#Sample Input2:4
#Expected Output1:0 0 0
                  1 1 1
                  2 2 2
#Expected Output2:0 0 0 0
                  1 1 1 1
                  2 2 2 2
                  3 3 3 3
"""
N = int(input())
for i in range(N):
    print((str(i)+" ")*N)

"""
Write a program to print numbers from 1 to N in each column forming a square pattern of N rows and N columns
#Sample Input1:3
#Expected Output1:
1 1 1 
2 2 2 
3 3 3
#Sample Input2:7
#Expected Output2:
1 1 1 1 1 1 1 
2 2 2 2 2 2 2 
3 3 3 3 3 3 3 
4 4 4 4 4 4 4 
5 5 5 5 5 5 5 
6 6 6 6 6 6 6 
7 7 7 7 7 7 7 
"""
N = int(input())
for i in range(1,N+1):
    print((str(i)+" ")*N)


"""
Write a program to print numbers from 1 to N in each row forming a rectangulae pattern of M rows and N columns
#Sample Input1:2,3
#Expected Output1:
1 2 3 
1 2 3 
#Sample Input2:5,4
#Expected Output2:
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4 
1 2 3 4
"""
M = int(input())
N = int(input())
Number_Pattern = ""
for i in range(1,N+1):
    Number_Pattern = Number_Pattern+(str(i)+' ')
for k in range(1,M+1):
    print(Number_Pattern)

"""
Given a starting number S and a number N, write a program that prints a square of N rows and N columns using numbers starting from S
#Sample Input1:3,4
#Sample Input2:8,5
#Expected Output1:3 4 5 6
                  3 4 5 6
                  3 4 5 6
                  3 4 5 6
#Expected Output2:8 9 10 11 12
                  8 9 10 11 12
                  8 9 10 11 12
                  8 9 10 11 12
                  8 9 10 11 12
"""
M = int(input())
N = int(input())
Number_Pattern = ""
for i in range(M,N+M):
    Number_Pattern = Number_Pattern+(str(i)+' ')
for k in range(1,N+1):
    print(Number_Pattern)

"""
Given a number N, write a program to find the count of 0's in N.
Print Count of Zeros is grater than three if there are more than three 0's in the given number
otherwise, print count of zeroes is not grater than three
#Sample Input1:1030800
#Expected Output1:Count of zeroes is greater than three
#Sample Input2:84020
#Expected Output2:Count of Zeroes is not greater than three
"""
N=input()
Count = 0
for i in N:
    if(i=="0"):
        Count = Count+1
if(Count>3):
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")


"""
Given a number N, write a program to find the count of even digits in N.
Print Count of even digits is greater than two if there are moorethan two even digits in the given number.
Otherwise, Print Count of even digits is not greater than two.

#Sample Input1:2563408
#Expected Output1:Count of even digits is greater than two
#Sample Input2:32
#Expected Output2:Count of even digits is not greater than two
"""
N=input()
Count = 0
for i in N:
    i = int(i)
    if(i%2==0):
        Count = Count+1
if(Count>2):
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")




"""
Given a number N, write a program to print a Right Angled Triangle of N rows using stars(*)
#Sample Input1:3
#Expected Output1:*
                  * * *
                  * * * * *
#Sample Input2:6
#Expected Output2:*
                  * * *
                  * * * * *
                  * * * * * * *
                  * * * * * * * * *
                  * * * * * * * * * * *
"""
N = int(input())
stars = 1
for i in range(N):
    row = "* "*stars
    stars = stars+2
    print(row)


"""
Given a number N, write a program to print an Inverted Right Angled Triangle of N rows using stars(*)
#Sample Input1:3
#Expected Output1:
* * * 
* * 
* 

#Sample Input2:7
#Expected Output2:
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""
N = int(input())
for i in range(N):
    print("* "*N)
    N=N-1

"""
Given a number N, write a program that prints a Hollow Square of N+2 rows using pluses(+)
#Sample Input1:5
#Expected Output1:
+ - - - - - +
|           |
|           |
|           |
|           |
|           |
+ - - - - - +

#Sample Input2:2
#Expected Output2:
+ - - +
|     |
|     |
+ - - +
"""
N = int(input())
print("+ "+"- "*N+"+")
for i in range(1,N+1):
    hollow_spaces="  "*N
    print("| "+hollow_spaces+"|")
print("+ "+"- "*N+"+")


"""
Given a title case string, write a program to modify the string as given below.
Add a hypen(-) before each uppercase character excluding the first uppercase
Convert all uppercase characters into lowercase characters
#Sample Input1:TitleCase
#Expected Output1:title-case
#Sample Input2:AToyStory
#Expected Output2:a-toy-story
"""


"""
Write a program to print the sum of even numbers in first N natural Numbers
#Sample Input1:5
#Expected Output1:6
#Sample Input2:4
#Expected Output2:6
"""
N = int(input())
Sum = 0
for i in range(1,N):
    if(i%2==0):
        Sum = Sum+i
print(Sum)

"""
Write a program to print the sum of odd numbers in first N natural Numbers
#Sample Input1:10
#Expected Output1:25
#Sample Input2:5
#Expected Output2:9
"""
N = int(input())
Sum = 0
for i in range(1,N):
    if(i%2!=0):
        Sum = Sum+i
print(Sum)


"""
Given an integer N, Write a program to find if the given number is a composite number or not. if it is composite, print True or else print False
#Sample Input1:12
#Expected Output1:True
#Sample Input2:3
#Expected Output2:False
"""
N = int(input())
output =True
for i in range(1,N):
    if(N%i!=0):
        output = False
print(output)


"""
Given an integer number M, N as input. Write a programe to print a stripped rectangular pattern of M rows and N columns using (+ and -)Character
#Sample Input1:5,7
#Expected Output1:
+ + + + + + + 
- - - - - - - 
+ + + + + + + 
- - - - - - - 
+ + + + + + + 
#Sample Input2:7,5
#Expected Output2:
+ + + + + 
- - - - - 
+ + + + + 
- - - - - 
+ + + + + 
- - - - - 
+ + + + +
"""

M = int(input())
N = int(input())
for i in range(1,M+1):
    if(i%2!=0):
        print("+ "*N)
    else:
        print("- "*N)


"""
Given two numbers M and N, Write a program to print a Hollow Rectangle of M+2 rows and N+2 columns using pluses(+), Hypens(-) and pipes(|)
#Sample Input1:3,10
#Expected Output1:
+----------+
|          |
|          |
|          |
+----------+

#Sample Input2:5,10
#Expected Output2:
+----------+
|          |
|          |
|          |
|          |
|          |
+----------+
"""
M = int(input())
N = int(input())
print("+"+"-"*N+"+")
for i in range(1,M+1):
    hollow_Spaces = " "*N
    print("|"+hollow_Spaces+"|")
print("+"+"-"*N+"+")


"""
Given a word W, write a program that prints the letters of the word in N rows as an Inverted Right Angled Triangle as shown in the sample output,where N is the length of the word W
#Sample Input1:game
#Expected Output1:
game
gam
ga
g
#Sample Input2:TUPLE
#Expected Output2:
TUPLE
TUPL
TUP
TU
T
#Sample Input3:uNiCoRn
#Expected output3:
uNiCoRn
uNiCoR
uNiCo
uNiC
uNi
uN
u
"""
Word = input()
for i in range(len(Word),0,-1):
    print(Word[:i])

"""
Given two strings S1 and S2 of equal length, write a program that prints a new string by appending characters from S1 frist and then from S2 alternately
NOTE: The two strings S1 and S2 given as inputs will always have equal length
#Sample Input1:
bring
camel
#Expected Output1:
baieg

#Sample Input2:
APPRECIATE
BACKPACKER
#Expected Output2:
AAPKEAIKTR

#Sample Input3
PAVAN
MOUSE
#Expected Output3:
POVSN
"""

"""
Given a number N, write a program to print an Inverted Right Angled triangle of N rows using stars(*)
#Sample Input1:5
#Expected Output1:
* * * * * * * * * 
    * * * * * * * 
        * * * * * 
            * * * 
                *
#Sample Input2:
#Expected Output2:
"""
# N = int(input())
# stars = 2*N-1
# for i in range(N,0,-1):
#     hollow_Spaces =
#     rows = hollow_Spaces+"* "*stars
#     stars = stars-2
#     print(rows)
#


"""
#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected Output2:
"""
