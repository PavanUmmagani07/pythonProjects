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
Given a string, Write a program to print only the alphabets in the given string
#Sample Input1:##P##Y##T##H##O##N##
#Sample Input2:--C--A--R--
#Expected Output1:PYTHON
#Expected Output2:CAR
"""
String = input()
print(String[2:-2:3])


"""
Given a string, write a program that checks if all the characters in the string are digits
Print True if all the characters in the string are digits otherwise False
#Sample Input1:5GNetwork
#Sample Input2:1245387
#Expected Output1:False
#Expected Output2:True
"""
String = input()
print(String.isdigit())

"""
Given a string S, write a program to prints the modified string by removing all the leading and trailing spaces from the string s
#Sample Input1:      PAVAN KALYAN          
#Sample Input2:   FULLSTACK WEB DEVELOPER
#Expected Output1:PAVAN KALYAN
#Expected Output2:FULLSTACK WEB DEVELOPER
"""
String = input()
print(String.strip())

"""
Given a string S, Write a program that modifies the string by removing the leading and trailing Stars(*)  from the string S
#Sample Input1:***PYTHON***
#Sample Input2:*****PAVAN KALYAN****
#Expected Output1:PYTHON
#Expected Output2:PAVAN KALYAN
"""
String = input()
print(String.strip("*"))

"""
Given a string, Write a program to print the string by converting all the characters in the string to lowercase
#Sample Input1:NOVEMBER
#Sample Input2:AMaziNG JouRNEY
#Expected Output1:november
#Expected Output2:amazing journey
"""
String = input()
print(String.lower())

"""
Given a string, Write a program to check if all the characters in the string are in uppercase
Print True if the string contains all uppercase characters, otherwise print false
#Sample Input1:IEEE
#Sample Input2:CommuNiTY
#Expected Output1:True
#Expected Output2:False
"""
String = input()
is_Upper = String.upper()
print(String==is_Upper)

"""
Given a string in the format dd-mm-yy S, write a program to convert the string from dd-mm-yy to dd/mm/yy format
#Sample Input1:07-11-2023
#Sample Input2:07-07-2000
#Expected Output1:07/11/2023
#Expected Output2:07/07/2000
"""
String = input()
print(String.replace("-","/"))


"""
Given a string S, write a program that prints the given string converting all the characters to lowercase and uppercase
#Sample Input1:Learning
#Sample Input2:Transportation
#Expected Output1:learning,LEARNING
#Expected Output2:transportation,TRANSPORTATION
"""
String = input()
print(String.lower())
print(String.upper())


"""
Given a string, Write a program that prints all the uppercase letters of the given string
#Sample Input1:SofTwArE
#Sample Input2:HACKthons
#Expected Output1:STAE
#Expected Output2:HACK
"""
String = input()
for i in range(len(String)):
    if(String[i].isupper()):
        print(String[i], end="")


"""
Given an url, write a program that checks if the given URl is a secured URL.
Print True if the given URL is a secured URL. otherwise, Print False
#Sample Input1:https://docs.google.com
#Sample Input2:learning.cccp.in
#Expected Output1:True
#Expected Output2:False
"""
Url = input()
is_Secured_Url = Url.startswith("https://")
print(is_Secured_Url)


"""
Given a file name with the file extension, write a program that checks if the given file is a python file.
print True if the  file is a python file Otherwise, print False
#Sample Input1:add_numbers.py
#Sample Input2:card.html
#Expected Output1:True
#Expected Output2:False
"""
file = input()
is_endswith = file.endswith(".py")
print(is_endswith)


"""
Given a string, check if the given string is a palindrome.
A palindrome is a sequence of characters that can be read the same way whether you start from the begining or the end
#Sample Input1:madam
#Sample Input2:batsman
#Expected Output1:True
#Expected Output2:False
"""
string = input()
reversed_string = ""
for i in string:
    reversed_string = i+reversed_string
is_palindrome = string == reversed_string
print(is_palindrome)

"""
You are given a string, write a program to find whether the string is palindrome or not
NOTE:Treat uppercase letters and lowercase letters as same when comparing letters 
#Sample Input1:Madam
#Sample Input2:Treat
#Expected Output1:True
#Expected Output2:False
"""
String = input()
String= String.casefold()
reversed_String=""
for i in String:
    reversed_String=i+reversed_String
is_palindrome = String==reversed_String
print(is_palindrome)

"""
Given a password S, checks if S is a valid password.
The password is valid only if it contains at least one digit
Print Valid Password if S is a valid Password. otherwise, print Invalid Password
#Sample Input1:Qwerty00
#Sample Input2: Dashboard
#Expected Output1:True
#Expected Output2:False
"""
String = input()
contains_digit = False
for char in String:
    is_digit = char.isdigit()
    if is_digit:
        contains_digit = True
print(contains_digit)


"""
Given a string, write a program to modify the string as given below
Add a space before each uppercase character excluding the first uppercase Character
print the modified string
#Sample Input1:TitleCase
#Sample Input2:TheLionKing
#Expected Output1:Title Case
#Expected Output2:The Lion King
"""
String = input()
new_Str = String[0]
for i in range(1,len(String)):
    each_Character = String[i]
    is_upper = each_Character.upper()
    if(is_upper==each_Character):
        new_Str = new_Str+" "+each_Character
    else:
        new_Str= new_Str+each_Character
print(new_Str)


"""
Given a string, write a program to modify the string as given below.
Add a hypen(-) before each upper-case character
Convert upper-case characters into lower-case characters
print the modified string
#Sample Input1:aChristmasStory
#Sample Input2:theFox
#Expected Output1:a-christmas-story
#Expected Output2:the-fox
"""


"""
Given a String, write a program to that checks if the given string is palindrome .
print Palindrome  if the given string is a palindrome. otherwise, print Not a Palindrome
#Sample Input1:Madam
#Sample Input2:Rover
#Expected Output1:Palindrome
#Expected Output2:Not a Palindrome
"""
String = input()
String = String.casefold()
reversed_string = String[::-1]
if(String==reversed_string):
    print("Palindrome")
else:
    print("Not a Palindrome")


"""
You are given a string, write a program to find whether the string is palindrome or not
NOTE: Treat uppercase letters and lower case letters as same as when comparing letters. ignore spaces and quotes within the string
#Sample Input1:No lemon no melon
#Sample Input2:Race Cars
#Sample Input3: God's Dog
#Expected Output1:True
#Expected Output2:False
#Expected Output3:True
"""
String = input()
String = String.casefold()
String = String.replace(" ","")
String = String.replace("'","")
reversed_string = String[::-1]
if(String==reversed_string):
    print(True)
else:
    print(False)



"""
Given a sentence S. Write a program to remove all the vowels in the given sentence
#Sample Input1:Hello World
#Sample Input2:Once upon a time
#Expected Output1:Hll Wrld
#Expected Output2:nc pn tm
"""
String = input()
result = ""
for i in String:
    X = i.lower()
    if(X=="a" or X=="e" or X=="i" or X=="o" or X=="u"):
        result+=""
    else:
        result = result + i
print(result)

"""
Given a character C, write a program to check if the C is a Lowercase Letter or Uppercase Letter or Digit or a Special character
#Sample Input1:9
#Sample Input2:A
#Sample Input3: e
#Sample Input4: @
#Expected Output1:Digit
#Expected Output2:Uppercase Letter
#Expected Output3:Lowercase Letter
#Expected Output4:Special Character
"""

String = input()
if(String.isdigit()):
    print("Digit")
elif(String.islower()):
    print("Lowercase Letter")
elif(String.isupper()):
    print("Uppercase Letter")
else:
    print("Special Character")

"""
Given a string, write a program to modify the string as given below.
1)Add a hypen(-) before each upper-case character.
2)Convert upper-case characters into lower-case characters.
Print the modified string
#Sample Input1:aChristmasStory
#Expected Output1:a-christmas-story
#Sample Input2:theFox
#Expected Output2:the-fox
"""
String = input()
result = ""
for i in String:
    if(i.isupper()):
        result = result+"-"+i.swapcase()
    else:
        result = result+i
print(result)

"""
Given two strings S1 and S2,write a program that checks if S2 is at the begining or ending of S1.
Print True if S2 is at the beginning or ending of S1.
Otherwise,print False.

#Sample Input1:
Manager
Man
#Expected Output1:True
#Sample Input2:
Helicopter
cop
#Expected Output2:False
#Sample Input3:
Programmer
ammer
#Expected Output3:True
"""
S1 = input()
S2 = input()
len_S2 = len(S2)
str_start = S1[:len_S2]
str_end = S1[(len_S2):]
if((S2== str_start) or (S2==str_end)):
    print(True)
else:
    print(False)


"""
Write a Program that reads two words A, B, and an Index I. Check if B starts at index I in A.
#Sample Input1:
Repeat
pea
2
#Expected Output1:True
#Sample Input2:
Banana
Ball
0
#Expected Output2:False
"""
A = input()
B = input()
Index = int(input())
Word = A[Index:Index+len(B)]
if(B == Word):
    print(True)
else:
    print(False)


"""
Write a program that reads two words A and B and checks if the second word B is the last part of the first word A.
#Sample Input1:
Blackhole
hole
#Expected Output1: True

#Sample Input2:
boomerang
boom
#Expected output2:False

#sample Input3:
nxtwave ccbp
ccbp
#Expected output3:True
"""
A = input()
B = input()
start_index = len(A)-len(B)
Word = A[start_index:]
print(Word)
if(B==Word):
    print(True)
else:
    print(False)

"""
Write  a program that reads two numbers A and B and checks if the A is greater than B and checks if the A is greatr than B. print the result as shown n the sample output 
#Sample Input1:
8
5
#Expected Output1: A > B is True
#Sample Input2:
12
32
#Expected output2: A > B is False
"""
A = int(input())
B = int(input())
if(A>B):
    print("A > B is True")
else:
    print("A > B is False")

"""
Write a program that reads two numbers A and B, and checks if B is greater than A by one
#Sample Input1:
2
3
#Expected Output1:True
#Sample Input2:
2
5
#Expected output2:False
"""
A = int(input())
B = int(input())
C = A+1
if(B==C):
    print(True)
else:
    print(False)

"""
Write a program that reads a word and checks if the first letter and last letter of the word are not the same.
#Sample Input1:Python
#Expected Output1:True
#Sample Input2:label
#Expected output2:False
"""
Word = input()
if(A[0]!=A[:-1]):
    print(True)
else:
    print(False)

"""
Write a program that reads two digit number N. The N consists of only two digits. check if the sum of the digits of N is greater than 7
#Sample Input1:45
#Expected Output1:True
#Sample Input2:12
#Expected output2:False
"""
N = input()
Condition=int(N[0])+int(N[1])>7
if Condition:
    print(True)
else:
    print(False)

"""
Write a program to check if the given string is a valid password or not. A string is considered as a valid password if the number of characters present is greater than 7
#Sample Input1:passwd
#Expected Output1:False
#Sample Input2:1@q92$482%f
#Expected output2:True
"""
String = input()
if(len(String)>7):
    print(True)
else:
    print(False)

"""
Write a program to check if the first three characters in the two given strings are the same.
#Sample Input1:
Apple
Application
#Expected Output1:True
#Sample Input2:
Android
Application
#Expected output2:False
"""
String1 = input()
String2 = input()
if(String1[:3]==String2[:3]):
    print(True)
else:
    print(False)
