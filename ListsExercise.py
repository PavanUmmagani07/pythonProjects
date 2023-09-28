"""
Write a program to print a list with the given elements
"Rose", 183,148,123.64,False
#Sample Input1:"Rose", 183,148,123.64,False
#Expected Output1:["Rose", 183,148,123.64,False]
#Sample Input2:
#Expected Output2:
"""
list_a = ["Rose", 183,148,123.64,False]
print(list_a)


"""
For this problem, the prefilled code will contain a list. write a program to print the element at the given index 
location
#Sample Input1:4
#Expected Output1: Green
#Sample Input2:2
#Expected Output2:Yellow
"""
color_list = ["Red", "Orange", "Yellow", "Pink", "Green", "Blue", "Purple", "Black", "White"]
# Write your code here
index = int(input())
print(color_list[index])


"""
For this problem, the prefilled code will contain a list. you need to write a program to read N integers, and print the 
elements at the index locations represented by those integers
#Sample Input1:
2
1
4
#Expected Output1:
Java
C++
#Sample Input2:
4
0
2
8
5
#Expected Output2:
Python
Ruby
Swift
Go
"""
programming_languages_list = ["Python", "Java", "Ruby", "C", "C++", "Go", "R", "JavaScript", "Swift", "PHP", "Kotlin", "Perl"]
# Write your code here
N = int(input())
for item in range(N):
    index = int(input())
    print(programming_languages_list[index])


"""
A list L is given in the prefilled code.
Write a program that reads a string S and checks if S is in the  given list L.Print True
if S is present in the list else, print False
#Sample Input1:Water
#Expected Output1:True
#Sample Input2:Java
#Expected Output2:False
"""
L = ["5", "eat", "9.80", "Water", "python", "-678", "7685.26", "-2.5", "sing"]
# Write your code here
String_S = input()
result = False
for item in L:
    if(item==String_S):
        print(True)
        break
print(result)


"""
For this problem , the prefilled code will contain a list. you need to concatenate the given number to the list.
The first list should have the number concatenated at the beginning. the second list should have number concatenated at the end

#Sample Input1:20
#Expected Output1:
[20,10,20,40,100]
[10,20,40,100,20]
#Sample Input2:-86
#Expected Output2:
[-86,10,20,40,100]
[10,20,40,100,-86]
"""
"""
#Prefilled Code
num_list =  [10, 20, 40, 100]
n = int(input())
first_list = # Add the number in the beginning
second_list = # Add the number at the end

print(first_list)
print(second_list)
"""

num_list = [10, 20, 40, 100]
n = int(input())
first_list = [n]+num_list
second_list = num_list+[n]

print(first_list)
print(second_list)

"""
A list L is given in the prefilled code.
Given a number N, write a program that reads N inputs and prints the list by adding the N inputs at the end of the list L.
L = ["apple","78","970.03"]

#Sample Input1:
2
38
grapes
#Expected Output1: ["apple", '78' ,'970.03','38','grapes']

#Sample Input2:
3
57.94
table
-990
#Expected Output2:L = ["apple","78","970.03", '57.94', 'table', '-990']
"""
L = ["apple","78","970.03"]
N = int(input())
for item in range(N):
    new_item = input()
    L=L+[new_item]
print(L)


"""
Write a program to print a list with the given N inputs
#Sample Input1:
5
20
Tiger
Cinema
5.5
93
#Expected Output1: ['20', 'Tiger', 'Cinema', '5.5', '93']

#Sample Input2:
3
12
17
43.5
#Expected Output2:['12', '17', '43.5']
"""
list_L = []
N = int(input())
for item in range(N):
    new_item = input()
    L+=[new_item]
print(L)


"""
You are given N numbers as input. Create a list and the N numbers which are given as input and print the list
#Sample Input1:
4
1
2
3
4
#Expected Output1:[1, 2, 3, 4] 
#Sample Input2:
3
13
21
19
#Expected Output2:[13,21,19]
"""
list_L =[]
N = int(input())
for i in range(N):
    new_item = int(input())
    list_L+=[new_item]
print(list_L)

"""
A list L is given in the prefilled code.
Given a number N, write a program that prints the list by repeating the prefilled list N times
L = [1,'two', '3', 4.0]
#Sample Input1:2
#Expected Output1:L = [1,'two', '3', 4.0, 1,'two', '3', 4.0]
#Sample Input2:3
#Expected Output2:L = [1,'two', '3', 4.0, 1,'two', '3', 4.0,1,'two', '3', 4.0]
"""
L = [1,'two', '3', 4.0]
N = int(input())
print(L*N)

"""
Given two integers M and N, write a program to create a list with element M repeated By N time
#Sample Input1:
5
4
#Expected Output1:[5, 5, 5, 5]
#Sample Input2:
-2
8
#Expected Output2:[-2, -2, -2, -2, -2, -2, -2, -2]
"""
M = int(input())
list_L = [M]
N = int(input())
print(list_L*N)

"""
Given a string, write a program to convert the string into a list
#Sample Input1:Python
#Expected Output1:['P', 'y', 't', 'h', 'o', 'n']
#Sample Input2:Pavan
#Expected Output2:['P', 'a', 'v' 'a', 'n']
"""
String = input()
print(list(String))


"""
A list L is given in the prefilled code.
Given an index I and a number N, Write a program that prints the list by replacing the element at index I with the number N.
L = [1,20,33,45,520,64,71,852,9999,101010]
#Sample Input1:
3
100
#Expected Output1:
L = [1,20,33,100,520,64,71,852,9999,101010]
#Sample Input2:
0
-55
#Expected Output2:L = [-55,20,33,45,520,64,71,852,9999,101010]
"""
L = [1,20,33,45,520,64,71,852,9999,101010]
index_I =int(input())
N = int(input())
L[index_I] = N
print(L)

"""
For this problem, the prefilled code will contain a list. Your program should create a new List.with all the elements 
existing list that are greater than given number.
NOTE: The order of elements in the new list should be as same as the order of those elements in the list given in the 
Prefilled code
num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]

Explanation:
For example if the given number is 50, your code should print the list of numbers that are greater than 50 in the given list. So the output should be
[93, 71]

#Sample Input1:50
#Expected Output1:[93, 71]
#Sample Input2: -45
#Expected Output2:[1, 6, 32, 71, -20, 30, 50]
"""
num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
list_L = []
N = int(input())
for i in num_list:
    if(i>N):
        list_L+=[i]
print(list_L)


"""
A List L is given in the prefilled code. Write a program that reads the two indices I1 and I2.
Replace the element in the I1 th index wit the element in I2 th index
Replace the element in the I2 th index with the element in I1 th index
print the Updated list.
L = [1, "two", 9, 5.09, "Three", -558, "four", -93.7, "six"]
#Sample Input1:
2
6
#Expected Output1:L = [1, "two", "four", 5.09, "Three", -558, 9, -93.7, "six"]
#Sample Input2:
4
1
#Expected Output2:L = [1, "Three", 9, 5.09, "two", -558, "four", -93.7, "six"]
"""



"""
You are given an integer N as input. Write a program to read N integers and print alist containing the first and last
two inputs

#Sample Input1:6
1
2
3
4
5
6
#Expected Output1:[1,2,5,6]
#Sample Input2:
5
1
11
13
21
19
#Expected Output2:[1, 11, 13, 21, 19] 
"""


"""
#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected Output2:
"""

"""
Given N numbers, and an index, write a program to store the numbers in a list and print the number at the given index.
For this problem, each input will contain T test cases. each test case will give an index Ki as input, 
which should be considered to print the number

#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected Output2:
"""



"""
#Sample Input1:
#Expected Output1:
#Sample Input2:
#Expected Output2:
"""

