#-----------------------------------------------------------------------------
# Name:        Exercise 10 (Exercise10.py)
# Purpose:     Using tuples in python
#
# Author:      Owen Wong
# Created:     11/15/2018
# Updated:     11/28/2018
#-----------------------------------------------------------------------------
list_num = [1,2,3,4] # Creating a list
tup_num = (1,2,3,4) # Creating a tuple

print(list_num) # Printing out the list
print(tup_num) # Printing out the tuple
print(type(list_num)) # Printing out: "<class 'list'>"
print(type(tup_num)) # Printing out: "<class 'tuple'>"
print(tup_num.index(2)) # Printing out the index in which the number 2 appears

list_num[2] = 5  # Modifying a list by changing the value at index 2 to a value of 5
print(list_num)

#tup_num[2] = 5       This will output an error as you can not modify a tuple

combined_tuple = (list_num,tup_num) # Combining a list and a tuple
print(combined_tuple) # Printing out the combined list and tuple as a single tuple

name = str(input("What is your name?"))
age = int(input("What is your age?"))
grade = int(input("What is your grade in percentage"))

# Three students are already preset, and the last student is completed through the user's input
list_of_students = [("Owen", 15, 60), ("Aaron", 9, 99), ("Thomas", 16, 75),(name, age, grade)]

# Print out all students' name, age, and grade in percentage
for student in list_of_students:
  name, age, grade_in_percentage = student
  print(name)
  print(age)
  print(grade_in_percentage)
  print()

# A function to determine how many vowels are there in the inputted phrase from the user
def number_of_vowels():
    vowels=['A','a','E','e','I','i','O','o','U','u']
    print('Please give me a phrase')
    inputphrase=input()
    inputphrase=tuple(inputphrase)
    index = 0
    i = 0
    while index < len(inputphrase):
      if inputphrase[index] in vowels:
        i += 1
      index += 1
    print(i)

number_of_vowels() # Utilizing the function number_of_vowels