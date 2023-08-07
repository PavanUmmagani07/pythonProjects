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