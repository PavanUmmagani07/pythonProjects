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
(print(User[-6:-1]))

"""
EXTENDED SLICING
Syntax:
variable = [start_index:end_index:step]
STEP determines the increment between each for index for slicing
"""
#Example
Word = "-P-A-V-A-N-K-A-L-Y-A-N-"
print(Word[1:10:2])
#Output: PAVAN
string = "-R-A-V-I-"
print(string[1:8:2])
#Output:RAVI
A = "WaterFall"
print(A[1:6:3])
#Output= ar
# first it will return the value at index 1,
# goes 3 steps forward and returns the value at index 4,
# goes 3 forward to the index value 7 but the end_index in the above input is 6.
# the index 7 is out range so it doesnt returns any value

"""
Isdigit
syntax:
str_var.isdigit()
Gives True if all the characters are digits.Otherwise False
"""
#EXAMPLE
pin = "7997"
is_digit = pin.isdigit()
print(is_digit)
#Output: True

pin = "7erf5897"
is_digit = pin.isdigit()
print(is_digit)
#Output:False

"""
Strip
Syntax: str_var.strip()
Removes all the leading(first) and trailing(end) spaces from a string
"""
#Example
Pin1 = " 789456123 "
Pin2 = "789456123"
is_equal = (Pin1==Pin2)
print(is_equal)
#Output: False

Pin = " 7889758 "
print(Pin.strip())
#Output:7889758

"""
We can also specify characters that need to be removed
Removes specified characters that are leading or trailing
Syntax:
str_var = strip(chars)
"""
#EXAMPLE
name = "PAVAN KALYAN>>>"
print(name.strip(">"))
#Output:PAVAN KALYAN

num = "//., .,/123456/../ ,/"
print(num.strip(" /,."))
#Output:123456

"""
REPLACE
syntax:
str_var.replace(old,new)
Gives a new string after replacing all the occurences of
the old substring with new substring
"""
#Example
Sentence = "teh cat and teh dog"
print(Sentence.replace('teh','the'))
#output:the cat and the dog

Sen = "Stay Angry"
print(Sen.replace('Angry','Cool'))
#Output:Stay Cool

"""
Startswith
Syntax:
str_var.startswith(value)
Gives True if the string starts with the specified value.Otherwise False
"""
#Example
url = "https://onthegomodel.com"
is_secure_url = url.startswith("https://")
print(is_secure_url)
#Output: True

"""
Endswith
Syntax:
str_var.endswith(value)
Gives True if the String ends with the specified value.otherwise,False
"""
#Example
gmail_id = "pavanummagani85@gmail.com"
is_gmail = gmail_id.endswith("@gmail.com")
print(is_gmail)
#Output: True

"""
Upper
Syntax:Str_var.upper()
Gives an uppercase string of the given string
"""
#Example
Name = "Pavan kalyan"
print(Name.upper())
#Output:PAVAN KALYAN

"""
Lower
Syntax:Str_var.lower()
Gives an Lowercase string of the given string
"""
Name = "PaVan kalYAn"
print(Name.lower())
#Output:pavan kalyan

"""
Capitalize
Syntax: str_var.capitalize()
Gives a new string after converting the first letter in the string to the upper case and all other letters to lowercase
"""
#Example
Capitalized = "the Planet Earth"
print(Capitalized.capitalize())
#Output:The planet earth

"""
Title
Syntax:str_var.title()
Gives a new string after converting the first letter of every word to upper case
If a word contains a number or a special charcter, the first character after that is converted to uppercase
"""
#Example1
title_case = "the planet earth"
print(title_case.title())
#Output:The Planet Earth

#Example2
title_case = "the @planet $earth"
print(title_case.title())
#Output: The @Planet $Earth

"""
Swapcase
Syntax:
str_var.swapcase()
Gives a nwe string after converting the upper case to lower case and vice versa
"""
#Example
swapped = "mY nAme Is PaVan"
print(swapped.swapcase())
#Output:My NaME iS pAvAN


#Classification Methods
#These Methods are used to check the charcteristics of individual charcters in a string

"""
Isalpha
Syntax:
str_var.isaipha()
Gives True if all the characters in a srting are alphabets.otherwise False 
"""
#Eample
is_alpha = "Pavan"
print(is_alpha.isalpha())
#OutPut:True

#Example2
is_alpha = "Pavan7997"
print(is_alpha.isalpha())
#output: False

"""
Isdecimal
Syntax:
str_var.isdecimal()
Gives True if all the characters are decimals.otherwise,False
"""
#Example1
is_decimal = "7674912346"
print(is_decimal.isdecimal())
#outPut:True

#Example2
is_decimal= "7895.rd"
print(is_decimal.isdecimal())
#output:False

#Example3
is_decimal="767.256"
print(is_decimal.isdecimal())
#Output:False

"""
IsLower
Syntax: str_var.islower()
Gives True if all letters in the string are in lowercase otherwise, False
"""
#Example1
is_lower = "hello world!"
print(is_lower.islower())
#Output: True

#Example2
is_lower = "Hello Pavan"
print(is_lower.islower())
#Output:False

"""
Syntax:str_var.isupper()
Gives True if all letters in the string are in uppercase. otherwise False
"""
is_upper = "Hello World!"
print(is_upper.isupper())
#Output: False

is_upper = "PAVAN KALYAN"
print(is_upper.isupper())
#Output: True

"""
Isalnum
Syntax:str_var.isalnum()
Gives True if the string is alphanumeric(a letter or number) other wise, False
"""
is_alnum = "Pavan123"
print(is_alnum.isalnum())
#Output:True

is_alnum = "pavan"
print(is_alnum.isalnum())
#Output:True

is_alnum = "Pavan@123"
print(is_alnum.isalnum())
#output: False

#Counting and Searching Methods
#These Methods are used to count the occurences of a substring in a string and to find the position of a substring in a string

"""
Count
Syntax:str_var.count(str,start_index,end_index)
Here, the start_index and the end_index are optional.

The count() method gives the number of times the specified string str appears in the string. It searches the complete string as default.

If start_index and end_index are provided, it searches between these indices. The end_index is not included.
"""

#Example1
text = "Hello World!"
letter_count = text.count('l')
print(letter_count)
#Output:3

#Example2
text = "Hello, World!"
letter_count = text.count("l",2,10)
print(letter_count)
#Output:2

"""
Index
Syntax: str_var(str,start_index, end_index)
Here, the start_index and the end_index are optional.

The index() method gives the index at the first occurrence of the specified string str.

It results in an error if the specified string str is not found.

The index() method searches the complete string as default. 
If start_index and end_index are provided, it searches between these indices. The end_index is not included.
"""

#Example1:
text = "I have a spare key, if I lose my key"
word_index = text.index("key")
print(word_index)
#Output:15

#Example2:
text = "I have a spare key, if I lose my key"
word_index = text.index("key",2,18)
print(word_index)
#Output:15

#Example3:
text = "I have a spare key, if I lose my key"
word_index = text.index("else")
print(word_index)
#Output:ValueError: substring not found

"""
rIndex
Syntax:str_var.index(str,start_index, end_index)
Here, the start_index and the end_index are optional.

The rindex() method gives the index at the last occurrence of the specified string str.

It results in an error if the specified string str is not found.

The rindex() method searches the complete string as default. 
If start_index and end_index are provided, it searches between these indices. The end_index is not included.
"""
#Example1:
text = "I have a spare key, if I lose my key"
word_index = text.rindex("key")
print(word_index)
#Output:33

#Example2:
text = "I have a spare key, if I lose my key"
word_index = text.rindex("key",2,36)
print(word_index)
#Output:33

#Example3:
text = "I have a spare key, if I lose my key"
word_index = text.rindex("else")
print(word_index)
#Output:ValueError: substring not found

"""
Find
Syntax:
str_var.find(str,start_index,end_index)
Here, the start_index and the end_index are optional.

The find() method gives the index at the first occurrence of the specified string str.

If the specified string str is not found, it returns -1.

The find() method searches the complete string as default. 
If start_index and end_index are provided, it searches between these indices. The end_index is not included.

It works similarly to the index() method. 
The only difference is that the index() method results in an error if the specified string is not found, while find() does not.
"""
#Example1:
text = "I have a spare key, if I lose my key"
word_index = text.index("key")
print(word_index)
#Output:15

#Example2:
text = "I have a spare key, if I lose my key"
word_index = text.index("key",2,18)
print(word_index)
#Output:15

#Example3:
text = "I have a spare key, if I lose my key"
word_index = text.index("else")
print(word_index)
#Output:-1

"""
rFind
Syntax: str_var.rfind(str,start_index,end_index)
Here, the start_index and the end_index are optional.

The rfind() method gives the index at the last occurrence of the specified string str.

If the specified string str is not found, it returns -1.

The rfind() method searches the complete string as default. 
If start_index and end_index are provided, it searches between these indices. The end_index is not included.

It works similarly to the rindex() method. 
The only difference is that the rindex() method results in an error if the specified string is not found, while rfind() does not.
"""

#Example1:
text = "I have a spare key, if I lose my key"
word_index = text.rindex("key")
print(word_index)
#Output:33

#Example2:
text = "I have a spare key, if I lose my key"
word_index = text.rindex("key",2,36)
print(word_index)
#Output:33

#Example3:
text = "I have a spare key, if I lose my key"
word_index = text.rindex("else")
print(word_index)
#Output:-1

#Changing a Character
message = 'sea you soon'
#message[2]='e'
#print(message) #Type error: 'str' object doesnot support item assignment
#Strings are Immuatble