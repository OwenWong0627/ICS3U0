#-----------------------------------------------------------------------------
# Name:        Exercise 1 (Exercise1.py)
# Purpose:     Understanding basic mathematical operations in Python
#
# Author:      Owen Wong
# Created:     10/10/2018
# Updated:     10/10/2018
#-----------------------------------------------------------------------------
print("Hello Class") #printing a String
print(9+10) #Addition of integers +
print(9.5-4.5) #Subtraction of float values -
print(1.5*4.75) #Multiplication of float values *
print(4/2) #Division of integers /
print(5//2) #Using integer division //
print(5%2) #Modulo using integers %
float = 5.25
integer = int(float)
print(integer) #Converting between floats and integers int() and float()
equation_with_float_answer = (10/5//2+4*3-39%8) #An operation that uses all operators above
equation_with_integer_answer = int(equation_with_float_answer) #Convert answer to an integer
print(equation_with_integer_answer)