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