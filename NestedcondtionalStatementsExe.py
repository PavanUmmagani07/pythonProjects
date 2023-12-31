"""
Write a program that reads a number X and Checks,
#1 if X is greater than 30.
#2 if X is greater than 30, checks if X is also greater than 50.
print "X is greater than 30" if X is greater than 30
print "X is greater than 30 and X is greater than 50" on each line if X is greater than 50
#Sample Input1:45
#Expected Output1: X is Greater than 30
#Sample Input2:99
#Expected Output2: X is greater than 30
                   X is greater than 50
"""
X = int(input())
Condition_1 = (X>30)
Condition_2 = (X>30) and(X>50)

if(Condition_2== True):
    print("X is Greater than 30")
    print("X is Greater than 50")
else:
    if(Condition_1==True):
        print("X is Greater than 30")


"""
Write a program that reads the Rank R of a student and checks,
#1 if R is lessthan or equal to 3
#2 if R is not less than or equal to 3 , check if R is less than or equal to 10
Print "One of Top 3" if the R is less than or equal to 3
print "Not Top 3 but One of Top 10" if R is less than or equal to 10 but not less thaan or equal to 3
#Sample Input1:7
#Expected Output1:Not Top 3 but One of Top 10
#Sample Input2:3
#Expected Output2:One of Top 3
"""

Rank = int(input())
Condition_1 = (Rank<=3)
Condition_2 = (Rank<=10)
if(Condition_1==True):
    if(Condition_2==True):
        print("One of Top 3")
    else:
        print("Not Top 3 but One of Top 10")


"""
Write a program that reads the weight W of a box in kg and checks,
#1 if W is greater than or equal to 100.
#2 if W is not greater than or equal to 100,check if W is greater than or equal to 30.
Print Box is Heavier if W is greater than or equal to 100.
print Box is heavy if W is not greater than or equal to 100 but greater than or equal to 30
#Sample Input1:60
#Expected Output1:Box is Heavy
#Sample Input2:150
#Expected Output2:Box is Heavier
"""

Box_Weight = int(input())
Condition_1 = (Box_Weight>=30)
Condition_2 = (Box_Weight>=100)
if(Condition_2==True):
    print("Box is Heavier")
else:
    if(Condition_1==True):
        if(Condition_2==False):
            print("Box is Heavier")

"""
Write a program that reads two strings H and I and checks,
#1 if H is Equal to "Y".
#2 if H is not  equal to "Y", check if I is equal to "Y".
Print "Allowed to Exam - Has Hall ticket if H is equal to "Y".
Print Allowed to Exam - Has Identification Card if H is not equal to "Y" and I is equal to "Y".
#Sample Input1:Y,N
#Expected Output1:Allowed to Exam - Has Hall ticket
#Sample Input2:
#Expected Output2:
"""

H = input()
I = input()
Condition_1 = (H=="Y")
Condition_2 = (H!="Y") and(I=="Y")
if(Condition_1==True):
    print("Allowed to Exam - Has Hall ticket")
else:
    if(Condition_2==True):
        print("Allowed to Exam - Has Identification Card")


"""
Write a Program that a number N and Checks if N is Divisible by 5 and 10.
Print Divisible by 10 if N is Divisible by 10.
Print Divisible by 5 if N is Divisible by 5 .but not divisible by 10.
Print Divisible by 10 or 5 if N is not divisible by 10 and N is not divisible by 5

#Sample Input1:5
#Expected Output1:Divisible by 5
#Sample Input2:15
#Expected Output2:Divisible by 5
"""
Num =int(input())
is_divisible_by_5 = (Num%5==0)
is_divisible_by_10 = (Num%10==0)
if (is_divisible_by_10 ==True):
    print("Divisible by 10")
elif (is_divisible_by_5==True) and (is_divisible_by_10==False):
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")

"""
Write a program that reads three numbers A,B and C and Prints the greatest number among the three given numbers
#Sample Input1:10,15,20
#Expected Output1:20
#Sample Input2:-10,59,34
#Expected Output2:59
"""

A= int(input())
B =int(input())
C = int(input())
if((A>B) and(A>C)):
    print(A)
elif(B>C):
    print(B)
else:
    print(C)


"""
Write a program that reads the marks M of a student and checks,
#1 if M is greater than or equal to 90
#2 if M is greater than or equal to 50 but not greater than or equal to 90
print Discount is 200 if M is greater than or equal to 90
Print Discount is 100 if M is greater than or equal to 50 but not greater than or equal to 90. 
#Sample Input1:90
#Expected Output1:Discount is 200
#Sample Input2:35
#Expected Output2:No Discount
"""

Marks = int(input())
condition_1 = Marks>=90
Condition_2= Marks>=50
if(condition_1==True):
    print("Discount is 200")
elif((condition_1==False) and (Condition_2==True)):
    print("Discount is 100")
elif(Condition_2==False):
    print("No Discount")

"""
Write a program that reads the Two scors A and B and Compares A with the B.
Print Win if A is greater than B.
print Draw if A is equal to B
Print Lose if A is less than B

#Sample Input1:26,47
#Expected Output1:Lose
#Sample Input2:24,15
#Expected Output2:Win
"""

A = int(input())
B = int(input())
if (A>B):
    print("Win")
elif(A==B):
    print("Draw")
else:
    print("Lose")

"""
Write  program to calculate the grade of the student based on the marks he/she scored.Input will be a float value
OUTPUT
The output should be a single line containing a string representing the grade of the student.
# A should be printed if the given marks are greater than 85
#B Should be printed if the given marks are greaterthan 70 and lessthan equal to 85.
#C should be printed if the given marks are greater than or equal to 60 and lessthan or equal to 70.
#F Should be printed if the given marks are lessthan 60
#Sample Input1:70.5
#Expected Output1:B
#Sample Input2:90
#Expected Output2:A
"""
Marks = float(input())
if(Marks>85):
    print("A")
elif((Marks>70) and (Marks<=85)):
    print("B")
elif((Marks>=60) and(Marks<=70)):
    print("C")
else:
    print("F")



"""
write a program that reads a two-digit number N and checks,
1) if the number N is greater than 25
2)if the first digit of N is greater than the second digit of N.
print the result as shown in the sample output

#Sample Input1:28
#Expected Output1:
True
False
#Sample Input2:87
#Expected Output2:
True
True
"""
#Method_1
a=input()
print(int(a)>25)
print(a[0]>a[1])
#METHOD_2
N = input()
if(int(N)>25 and N[0]>N[1]):
    print(True)
    print(True)
elif(int(N)>25 and N[0]>N[1]):
    print(True)
    printN = input()
condition_1 = int(N)>25 and int(N[0])>int(N[1]) #True&True
condition_2 = int(N)>25 and int(N[0])<int(N[1])  #True&False
condition_3 = int(N)<25 and int(N[0])>int(N[1]) #False%True
condition_4 = int(N)>25 and int(N[0])==int(N[1]) #True&false
if(condition_1):
    print(True)
    print(True)
elif(condition_2):
    print(True)
    print(False)
elif(condition_3):
    print(False)
    print(True)
elif(condition_4):
    print(True)
    print(False)
else:
    print(False)
    print(False)

"""
Write a program that ereads two numbers A and B and checks ,
1)if A is less than or equal to B.
2)if B is less than or equal to A.
print the result as shown in the sample output
#Sample Input1:
5
3
#Expected Output1:
A <= B is False
B <= A is True

#Sample Input2:
21
64
#Expected output2:
A <= B is True
B <= A is False

#Sample Input3:
11
11
#Expected output3:
A <= B is True
B <= A is True
"""
A = int(input()) #5
B = int(input()) #3
Condition_1 = A<=B
Condition_2 = B<=A
if(Condition_1==False):
    print("A <= B is False")
    print("B <= A is True")
elif(Condition_1==Condition_2):
    print("A <= B is True")
    print("B <= A is True")
else:
    print("A <= B is True")
    print("B <= A is False")

"""
#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected output2:
"""


"""
#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected output2:
"""

"""
#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected output2:
"""

"""
#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected output2:
"""


"""
#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected output2:
"""