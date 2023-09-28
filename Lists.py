"""
Lists holds an ordred of items
In Lists each item is seperated by a comma
Items in the List are enclosed with the square brackets[]
Items in list are of any datatype
"""
#Example-1
list_a =[5,"Six",8.2,]
print(type(list_a))
print(list_a)

#Example-2
a=2
list_a = [5,'Six',8.2,a]
print(list_a)

#The item in the list can be an another list
#Example-3
a = 2
list_a = [5,'six',8.2,a]
list_b = [7,8.9,list_a]
print(list_a)
print(list_b)

#Length of List
#It returns the No.of Items present in the List
#Example-4
a = 2
list_a = [5,'six',a,8.3]
print(len(list_a))

#If a List is present inside the list the len() considers the list as single item
#Example-5
list_a = [5,88,8.8,'sixes']
list_b = ['pavan',list_a]
print(len(list_a))
print(len(list_b))


#Accessing List Elements
#To access elements of a list we use "Indexing"
list_a=[5,95,'five','Pavan']
print(list_a[1])
#print(list_a[9]) Returns(IndexError: list index out of range)

#Iterating Over a List
a = "Pavan"
list_a = [5,2.3,'rat',a]
for item in list_a:
    print(item)

#Operations On Lists
#1)Concatenation
list_a = [1,2,3,4]
list_b = ['a','b','c','d']
print(list_a+list_b)

list_a = [3,56,8.8,'LIST']
list_b = [5,'o',9.3,'Pavan',[45,2.65,"Kalyan"]]
print(list_a+list_b)

#2)Adding Items to List
list_a = []
print(list_a)
for i in range(1,5):
    list_a+=[i] #[]+[1]=[1]
print(list_a)#[1, 2, 3, 4]

#3)Repetition
list_a = [1,2]
list_b = list_a*3 # *operator repeats items in the lists
print(list_b)#[1, 2, 1, 2, 1, 2]

#4)Obtain Part of a List(List Slicing)
list_a = [5,'six',2,8.2]
print(list_a[:2])#[5, 'six']
print(list_a[:])#Returns entire list
print(list_a[1:3])#['six', 2]

#5)Extended Slicing
#Similar to string extended slicing, we can extract alternate itr=ems using step
list_a = ['r','a','i','n','b','o','w']
print(list_a[1:6:2]) #['a','n','o']

#6)Converting to List
#list(sequence)=>Takes a sequence and converts it into list
name = "PAVANKALYAN"
list_a = list(name)
print(list_a)#['P', 'A', 'V', 'A', 'N', 'K', 'A', 'L', 'Y', 'A', 'N']

list_a = list(range(5))
print(list_a) #[0, 1, 2, 3, 4]

#Lists are MUTABLE. Lists can be modified items at any position can be updated
list_a = [1,2,3,5]
print(list_a)
list_a[3] = 4
print(list_a) #[1, 2, 3, 4]

#Exapmle problem
animals = ['cat', 'dog']
wild_animals = ['Tiger','Fox']
animals= animals+[wild_animals]
print(animals)

#OBJECT
"""
in general,anything that can be assigned to a variable in python is referred as object.
Strings, Integers,Float,List etc. are all objects 
Ex: "A", 85, 1.25, [1,3,5,'six','a']

#Identity of an Object

When ever an object is created in python, it will be given a unique identifier(id)
This unique id can be different for each time you run the program
Ex: 'A'=> id:140035229724336
[1,2,3]=> id:139630925071104

Every object that you use in a python program will be stored in computer Memory
The unique id will be related to the location where the object is stored in computer memory

#Finding Id
We can use the id() to find the id of a object.
id()=>Gives id of this object
Ex:print(id('Hello'))
"""
print(id('Hello')) #This unique id can be different for each time you run the program.

#Example
A = 'Hello'
print(id(a))

#Example
list_a =[5,"Six",8.2,]
print(id(list_a))

a = 'Hello'
print(id(a))
a+='World!'
print(id(a))

#Modifying Lists
list_a = [1,2,3]
print(id(list_a))

list_a = [1,2,3]
list_b = [1,2,3]
print(id(list_a[0]))
print(id(list_b[0]))
print(id(list_a))
print(id(list_b))

list_a = [1,2,3]
list_b = list_a
print(id(list_a))
print(id(list_b))

#Modifying Lists
list_a = [1,2,3,5]
list_b=list_a
list_b[3]= 4
print('list a: '+str(list_a))
print('list b: '+str(list_b))

list_a = [1,2]
list_b = list_a
list_a = [6,7]
print('list a :'+ str(list_a))
print('list b :'+str(list_b))

list_a = [1,2]
list_b = list_a
list_a = list_a+[6,7]
print('list a :'+ str(list_a))
print('list b :'+str(list_b))


#Compound assignment operator updates the objects in place
#Compound assignment operators updates the same object
list_a = [1,2]
list_b = list_a
list_a+=[6,7]
print('list a:' + str(list_a))
print('list b:' + str(list_b))


list_a = [1,2]
list_b = [3,list_a]
list_a[1] = 4
print(list_a)
print(list_b)


a =2
list_a = [1,a]
print(list_a)
a =3
print(list_a)

#Splitting a String
"""
Syntax: str_var.split(separator)
Splits a string into a list
if no separator is specified Default separator is white space
"""
#Example
nums = "1 2 3 4"
num_list = nums.split()
print(num_list) #['1', '2', '3', '4']

#Multiple whitespaces are considered as single when splitting
#Example
nums = "1    2   3 4"
num_list = nums.split()
print(num_list) #['1', '2', '3', '4']

nums = "1    2   3 4"
num_list = nums.split(" ")
print(num_list) #['1', '', '', '', '2', '', '', '3', '4']

#New line(\n) and tab space(\t) are also whitespace
#Example
nums = "1\n2\t3 4"
num_list = nums.split()
print(num_list) #['1', '2', '3', '4']

#Breaks up a string at the specified separator
#Example
nums = '1,2,3,4'
num_list = nums.split(',')
print(num_list) #['1', '2', '3', '4']

nums = '1,2,,3,4'
num_list = nums.split(',')
print(num_list) #['1', '2', '', '3', '4']

nums = '1,2,,3,4,'
num_list = nums.split(',')
print(num_list) #['1', '2', '', '3', '4', '']

String_S = "Python is a programming language"
string_list = String_S.split("a")
print(string_list)#['Python is ', ' progr', 'mming l', 'ngu', 'ge']

String_S = "step-by-step execution of code"
string_list = String_S.split("step")
print(string_list)#['', '-by-', ' execution of code']


#Example
String_S = "PAVAN KALYAN"
string_list = String_S.split("A")
print(string_list) #['P', 'V', 'N K', 'LY', 'N']


#JOINING STRING
"""
Syntax: str.join(sequence)
Takes all the items in a 'sequence of strings' and joins them into one string
"""
#Example:
list_a = ['Python is ', ' progr', 'mming l', 'ngu', 'ge']
string_a = "a".join(list_a)
print(string_a) #Python is a programming language

#Example
# list_a = list(range(5))
# string_a = ",".join(list_a)
# print(string_a)
#TypeError: sequence item 0: expected str instance, int found
#Sequence should not contain any non-string values

#NEGATIVE INDEXING
"""
Using a negative index returns the nth item from the end of list
Last item in the list can be accessed with index -1
"""

list_a = [5, 4, 3, 2, 1]
item = list_a[-4]
print(item) #4

#Slicing
#you can also specify negative indices while slicing a list.
list_a = [5, 4, 3, 2, 1]
list_b = list_a[-3:-1]
print(list_b) #[3, 2]

#While slicing, index can go out of bounds
list_a = [5, 4, 3, 2, 1]
list_b = list_a[-7:-1]
print(list_b) #[5, 4, 3, 2]

#Extended Slicing(Negative Step Size)
"""
Syntax:variable[start:end:negative_step]
Negative step determines the decrement between each index for slicing
Start must be greater than end (start>end)
"""
list_a = [5, 4, 3, 2, 1]
list_b = list_a[4:1:-1]
print(list_b) #[1, 2, 3]

#Negative step requires the start to be greater than end.
#if start > end we get an empty list

list_a = [5, 4, 3, 2, 1]
list_b = list_a[2:4:-1]
print(list_b) #[] -> Empty List

#Prints the list as it is if start and end indices are not specified
#Example
list_a = [5, 4, 3, 2, 1]
list_b = list_a[::]
print(list_b) #[5, 4, 3, 2, 1]

#-1 for step will reverse the order of items(Reversing the entire list)
list_a = [5, 4, 3, 2, 1]
list_b = list_a[::-1]
print(list_b) #[1, 2, 3, 4, 5]
