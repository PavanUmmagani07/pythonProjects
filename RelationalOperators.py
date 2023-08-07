#RELATIONAL OPERATORS
#Relational Operators are used to compare values.
#Gives True or False as the result of a comparison.

#These are different relational operators
#Operator	    Name
#  >	        Is greater than
#  <	        Is less than
#  ==	        Is equal to
#  <=	        Is less than or equal to
# >=	        Is greater than or equal to
#  !=	        Is not equal to

#WRITE A PROGRAM TO CHECK IF THE FIRST THREE CHARACTERS OF A STRINGS ARE SAME
A = input()
B = input()
print((A[0:3]==B[0:3]))

print(5 < 10) #True
print(2 < 1) #False
#print(3=3) SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
#print(2 < = 3) invalid syntax,"Space between relational operators ==, >=, <= , != is not valid in Python."

#COMPARING NUMBERS
print(2 <= 3)
print(2.53 >= 2.55)

#COMPARING INTEGERS AND FLOATS
print(12 == 12.0)
print(12 == 12.1)

#COMPARING STRINGS
print("ABC" == "ABC")
print("CBA" != "ABC")

#CASE SENSITIVE
print("ABC" == "abc")
#"Python is case sensitive."
#It means X (Capital letter) and x (small letter) are not the same in Python.

#STRINGS AND EQUALITY OPERATORS
print(True == "True")
print(123 == "123")
print(1.1 == "1.1")