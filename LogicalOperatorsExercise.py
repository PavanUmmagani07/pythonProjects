#Write a program that reads two numbers and checks if both the given numbers are greater than 9
A = int(input())
B = int(input())
print((A>9) and (B>9))

#Write a program that reads two numbers and checks if both the numbers are NEGATIVE
A = int(input())
B = int(input())
print((A<0) and (B<0))


#Write a program that reads two numbers and checks if both the numbers are POSITVE
A = int(input())
B = int(input())
print((A>0) and (B>0))


#Write a program that reads two numbers and checks if any one  the numbers are POSITVE
A = int(input())
B = int(input())
print((A>0) or (B>0))

#Write a program that reads two numbers and checks if the sum of two numbers is not greater than 100
A = int(input())
B = int(input())
Result = A+B
print(not(Result>100))


#Write a program that reads two numbers and checks both the numbers are greater than 35 or first number greater than Second Number
A = int(input())
B = int(input())
Result= ((A>35) and (B>35)) or (A>B)
print(Result)

#Write a program that reads two numbers A and B, Checks if one of the given number is negative  and Sum of the given numbers is greater than 7
A = int(input())
B =int(input())
Result = ((A<0) or (B<0)) and (A+B>7)
print(Result)


#Write a program that reads two numbers A and B, Checks if both A and B are positive or A and B lessthan 70
A = int(input())
B = int(input())
Result = ((A>0) and (B>0)) or ((A<70) and (B<70))
print(Result)

#Write a program that reads two numbers A and B, checks if one of A and B are lessthan 60 and One of A and B are Greaterthan 80
A = int(input())
B = int(input())
Result = ((A<60)or (B<60)) and((A>80) or (B>80))
print(Result)