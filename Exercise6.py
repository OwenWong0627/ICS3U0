#-----------------------------------------------------------------------------
# Name:        Exercise 6 (Exercise6.py)
# Purpose:     Creating a sample program in python
#
# Author:      Owen Wong
# Created:     10/15/2018
# Updated:     10/22/2018
#-----------------------------------------------------------------------------

import math

def convertCToF(temperature_in_C):
  int(temperature_in_C)
  if temperature_in_C <=100 and temperature_in_C >= -100:
    return int((temperature_in_C * 9/5) +32)
  else:
    return ("Unacceptable input values.")

def convertFToC(temperature_in_F):
  int(temperature_in_F)
  if temperature_in_F <=100 and temperature_in_F >= -100:
    return int((temperature_in_F-32)* 5/9)
  else:
    return ("Unacceptable input values.")

def hypotenuse(side_a, side_b):
  if side_a>0 and side_b>0:
    return math.sqrt(math.pow(side_a,2)+math.pow(side_b,2))
  else:
    return ("Unacceptable input values.")

def convertCToFEveryFive(lowC, highC):
  output = ""
  if lowC <= highC:
    for count in range(lowC, highC+1, 5):
      output = (str(count)+"C = " + str(convertCToF(count)) + "F")
      print(output)
    return
  else:
    return ("Unacceptable input values.")