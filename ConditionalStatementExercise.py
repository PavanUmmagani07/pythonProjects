#Write a program that reads a number and converts it into positive.
# If the given number is negative convert it into positive otherwise print the same number
#Sample Input: -1
#Expected Output: 1
A = int(input())
if(A<0):
    print(A*-1)
else:
    print(A)

#Write a program that reads student's marks as input and prints PASS or FAIL.
# If the student gets more than 50 print PASS, in all other cases print FAIL
#Sample Input1: 89
#Sample Input2: 50
#Sample Input3: 45
#Expected Output: PASS
#Expected Output: FAIL
#Expected Output: FAIL

marks = int(input())
if(marks>50):
    print("PASS")
else:
    print("FAIL")



#Write a program that reads Two numbers A and B and Prints the Greatest AmonG the number
#Sample Input: 89,48
#Expected Output: 89
A = int(input())
B = int(input())
if(A>B):
    print(A)
else:
    print(B)

#Write a program that reads age of a person and checks the age of person is greater than or equal to 18 for eligibity to vote
#Print Eligible , if the age is greater than or equal to 18 or else print Not Eligible
#Sample Input1:25
#Sample Input2:17
#Expected Output1: Eligible to Vote
#Expected Output2: Not Eligible to Vote

Age = int(input())
if(Age>=18):
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


#Write a program that reads two numbers X and Y and prints X<Y, if X is lessthan Y or else prints X>=Y
X = int(input())
Y = int(input())
if(X<Y):
    print("X<Y")
else:
    print("X>=Y")


#Write a program that reads the scores A and B of TWO players and checks if one of the scores is greater than 300 and sum of the score is less than 500.
#Print "Can team up" if one of the scores is greater than 300 and the sum of scores is lessthan 500 otherwise print "Cannot team up"
#Sample Input1:350,134
#Sample Input2: 450,82
#Expected Output1: Can team up
#Expected Output2: Cannot team up

A = int(input())
B = int(input())
if((A>300)or(B>300))and(A+B<500):
    print("Can team up")
else:
    print("Cannot team up")

#Write a program that checks  given two numbers  are equal
#sample Input1:5,5
#sample Input2:6,9
#Expected output1: Equal
#Expected output2: Not Equal

A = int(input())
B = int(input())
if(A==B):
    print("Equal")
else:
    print("Not Equal")


#Given the Length and Breadth of a box, check if it is a rectangle or square
#sample Input1:6,6
#sample Input 2:5,10
#Expected output1:Square
#Expected output2: Rectangle

A = int(input())
B = int(input())
if(A==B):
    print("Square")
else:
    print("Rectangle")

#Write a program that reads a temperature and checks if the given temperature is between 15 and 40.
# print "Can go for a walk" if the given temperature is between 15 and 40, otherwise print cannot go for a walk
#Sample Input1:26
#sample Input2:5
#Expected output1: Can go for  a walk
#Expected output2: Cannot go for a walk

A = int(input())
if(15<A<40):
    print("Can go for a walk")
else:
    print("Cannot go for a walk")

#Write a program that reads the size S and page count C of a book and checks if S is equal to large or C is greater than or equal to 300.
# print "Buy a Book" if S is equal to large or C is greater than 300.otherwise , print "Do Not Buy a Book"
#Sample Input1:large,80
#sample Input2:small,200
#Expected output1:Buy a Book
#Expected output2: Do Not Buy a Book
A = str(input())
B = int(input())
if(A=="large") or (C>=300):
    print("Buy a Book")
else:
    print("Do Not Buy a Book")


#Write a program that reads two numbers  A and B and checks if both A and B are lessthan or equal to 1000 or B is greater than 500.
# Print Pair if both A and B are lessthan or equal to 1000 or B is greater than 500. otherwise,Print Not a Pair
#Sample Input1:300,200
#sample Input2:1464,20
#Expected output1:Pair
#Expected output2:Not a Pair

A= int(input())
B =int(input())
if((A<=1000)and(B<=1000)) or (B>500):
    print("Pair")
else:
    print("Not a Pair")

#Write a program that reads a number and checks if the given number is equal to 0 or Positive
#Print "Zero" if the given number is equal to 0, Print "Positive if the givn number is a Positive
#Sample Input1:56
#sample Input2:0
#Expected output1:Positive
#Expected output2:Zero

A = int(input())
if(A==0):
    print("Zero")
else:
    print("Positive")


#Write a program that reads a number and checks if the given number is equal to 0 or Positive
#Print "Zero" if the given number is equal to 0, Print "Positive if the givn number is a Positive
#Print "Negative" if the given number is less than 0
#Sample Input1:56
#sample Input2:0
#sample Input:-86
#Expected output1:Positive
#Expected output2:Zero
#Expected output3: Negative
A = int(input())
if(A==0):
    print("Zero")
elif(A>0):
    print("Positive")
else:
    print("Negative")