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