#Define a variable `is_raining` and ask the user to input either "True" or "False" (as a string). Convert the input to a boolean and print its type.
#**Expected Input:** "True" or "False"
#**Expected Output:** The data type of the converted boolean.

is_raining= input()
print(is_raining)
is_raining=bool(is_raining)
print(type(is_raining))