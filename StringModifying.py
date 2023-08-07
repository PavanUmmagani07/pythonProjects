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