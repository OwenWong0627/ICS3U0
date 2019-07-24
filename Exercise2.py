#-----------------------------------------------------------------------------
# Name:        Exercise 2 (Exercise2.py)
# Purpose:     Using variables in Python
#
# Author:      Owen Wong
# Created:     10/10/2018
# Updated:     10/12/2018
#-----------------------------------------------------------------------------
Greetings = "Hello Class" #printing a String
Greetings_2 = ", we will be talking about Python"
print(Greetings+Greetings_2)
First_Number=20
Second_Number=5
Third_Number=4.5
Fourth_Number=1.5
print(First_Number+Second_Number) #Addition of integers +
print(Third_Number-Fourth_Number) #Subtraction of float values -
print(Third_Number*Fourth_Number) #Multiplication of float values *
print(First_Number/Second_Number) #Division of integers /
print(First_Number//Second_Number) #Using integer division //
print(First_Number%Second_Number) #Modulo using integers %
integer = int(Third_Number)
print(integer) #Converting between floats and integers int() and float()
equation_with_float_answer = (First_Number/Second_Number//2+Third_Number*Fourth_Number-39%8) #An operation that uses all operators above
print(equation_with_float_answer)
equation_with_integer_answer = int(equation_with_float_answer) #Convert answer to an integer
print(equation_with_integer_answer)