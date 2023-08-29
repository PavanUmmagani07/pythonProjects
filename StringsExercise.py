#Write a program that prints the sum of the digits of the given three-digit number
#Sample Input1:326
#sample Input2:222
#Expected output1:11
#Expected output2:6
Num= input()
Sum = int(Num[0])+int(Num[1])+int(Num[2])
print(Sum)


#Given a word W and an integer N, Write a Program to Print the Character present at the index N in the word W
#Sample Input1:Chocolate,2
#sample Input2:Table,1
#Expected output1:o
#Expected output2:a
Word = input()
Num = int(input())
print(Word[Num])

#Given a word and a number N, wwrite a program to print the given word,N number of times in a single line
#Sample Input1:Ball,2
#sample Input2:Hand,3
#Expected output1:BallBall
#Expected output2:HandHandHandHand
Word = input()
Num = int(input())
print(Word*Num)

#Write a program to read a single line of input and print the first three characters in it?
#Sample Input1:Four
#sample Input2:Strawberrry
#Expected output1:Fou
#Expected output2:Str
A = input()
print(A[:3])

#write a program that reads a word and an index and prints a part of the word from the given index to the end of the word
#Sample Input1:Unhappy,2
#sample Input2:goodnight,4
#Expected output1:happy
#Expected output2:night
Word = input()
Num = int(input())
print(Word[Num:])

#Write a program that reads a word and two indices (X,Y) and prints a part of the word from the index X to index Y
#Sample Input1:Growing,3,6
#sample Input2:scrabble,1,5
#Expected output1:wing
#Expected output2:crabb

Word = input()
X = int(input())
Y = int(input())
print(Word[X:Y])

#Write a program that reads a word and two indices (X,Y) and prints a part of the word from the index X to index Y
#"Y should also include in the output"
#Sample Input1:Growing,3,6
#sample Input2:scrabble,1,5
#Expected output1:wing
#Expected output2:crabb

Word = input()
X = int(input())
Y = int(input())
print(Word[X:Y+1])


#Write a program that reads a word and a number N and prints the first N characters of the word
#Sample Input1:superman,5
#sample Input2:impossible,2
#Expected output1:super
#Expected output2:im
Word = input()
Num = int(input())
print(Word[:Num])

#Write a program that reads a word and a number N and prints the last N characters of the word
#Sample Input1:Forgive,4
#sample Input2:hamburger,6
#Expected output1:give
#Expected output2:burger
Word = input()
Num = int(input())
Start_index: len(Word)-Num
print(Word[Start_index:])

#Write a program that reads a string and prints the second part of the string that has digits
#NOTE
#THE GIVEN STRING CONTAINS 2 PARTS
#THE FIRST PART CONTAINS ONLY TWO CHARCTERS
#THE SECOND PART CONTAINS ONLY DIGITS
#EXAMPLES:OF63,AB395
String = input()
print(String[2:])

#Write a program that reads a
#NOTE
#THE GIVEN STRING CONTAINS 2 PARTS
#THE FIRST PART CONTAINS ONLY DIGITS
#THE SECOND PART CONTAINS ONLY ONE CHARACTER
#EXAMPLES: 10Y, 1A
String = input()
print(String[:-1])


"""
Write a program that reads two words W1 and W2.W1 contains two parts.The first part contains W2 and the second part contains the remaining letters in W1.
print W1 with the first part as stars(*)
#Sample Input1:
#Sample Input2:
#Expected Output1:
#Expected Output2:
"""
