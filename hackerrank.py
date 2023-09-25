"""
Task1
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""

n = int(input())
odd = n%2!=0
even = n%2==0
condition_1 = n>=2 and n<=5
condition_2 = n>=6 and n<=20
condition_3 = n>=20
if(odd):
    print("Weird")
elif(even and condition_1):
    print("Not Weird")
elif(even and condition_2):
    print("Weird")
elif(even and condition_3):
    print("Not Weird")