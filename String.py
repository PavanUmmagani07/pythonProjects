#STRINGS is a sequence of CHARACTERS
#Strings in python are surrounded by either single quotation marks, or double quotation marks.

#ASSIGNING A STRING TO Variable
A = "PAVAN KALYAN"
print(A)


#String as input
A = input()
print(A)
print(type(A))

#STRING CHECK
#To check if a certain phrase or character is present in a string, we can use the keyword 'in'.
#IF the Character or Stream of Character Presents in the given input it returns True or else False
TEXT = "PAVAN UMMAGANI WILL BECOME A FULLSTACK WEB DEVELOPER"
print('A' in TEXT)
print('X' in TEXT)

#Checking characters through Conditional Statements
TXT= input()
if "PAVAN" in TXT:
    print("PAVAN is in the TXT")
else:
    print('PAVAN is not in the TXT')

#Check if NOT
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

TEXT = "PAVAN UMMAGANI WILL BECOME A FULLSTACK WEB DEVELOPER"
print('Z' not in TEXT)
print('X' not in TEXT)

#Checking characters through Conditional Statements
TXT= input()
if "PAVAN" not in TXT:
    print("PAVAN is not the TXT")
else:
    print('PAVAN is  in the TXT')

#Joining strings together is called string concatenation.
A = 'PAVAN'+' '+'KALYAN'
print(A)

A = input()
B = input()
print(A+" "+B)

#Concatenation Errors
#String Concatenation is possible only with strings.
a = "*" + 10
print(a)


#String Indexing
#We can access an individual character in a string using their positions (which start from 0). These positions are also called as index.
UserName = input()
print(UserName[0])
print(UserName[-1]) #Negative Indexing returns the first Character from last
#Postive Indexing Start from 0
#Negative Indexing Start from -1

#IndexError
#Attempting to use an index that is too large will result in an error:

User = "PAVAN"
print(User[7]) #Throws an Error as "STRING INDEX OUT of RANGE"

#STRINGMODIFYING FILE
#UPPER CASE
#The 'upper()' method returns the string in upper case:
a = "pavan kalyan"
print(a.upper())

#LOWER CASE
#The lower() method returns the string in lower case:
a = "PAVAN KALYAN"
print(a.lower())

#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
#The strip() method removes any whitespace from the beginning or the end:
a = " PAVAN KALYAN "
#print(len(a))
A = a.strip()
#print(A)
print(len(A))

#REPLACING STRINGS
#The replace() method replaces a string with another string:
a = "PAVAN  KALYAN"
print(a.replace("P", "p"))

#Split String
#The split() method returns a list where the text between the specified separator becomes the list items.
a = "PAVAN KALYAN"
print(a.split( ))


#STRING REPETATION
#* operator is used for repeating strings any number of times as required.
A = "*"
print(A*5)
B = (A*4)+"PAVAN KALYAN UMMAGANI"+ (A*4)
print(B)

#SLICING
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
#The end Index will not be included in the output  characters, whereas the start index will be included in the output characters

#Get the characters from position 2 to position 5:

User = input()
print(User[2:5])

User = 123456789
User = str(User)
print(User[2:6])

#SLICING FROM THE START
#By leaving out the start index, the range will start at the first character:

User = "PAVAN KALYAN"
print(User[:8])

#SLICING TO THE END
#By leaving out the end index, the range will go to the end:

User = "PAVAN KALYAN"
print(User[1:])

#NEGATIVE INDEXING
#Use negative indexes to start the slice from the end of the string:

User = "PAVAN KALYAN"
print(User[-6:-1])