#-----------------------------------------------------------------------------
# Name:        Exercise 7 (Exercise7.py)
# Purpose:     Using documentation
#
# Author:      Owen Wong
# Created:     10/18/2018
# Updated:     10/22/2018
#-----------------------------------------------------------------------------

import math

def convertCToF(temperature_in_C):
  '''
	Converts Celsius degrees to Fahrenheit degrees

	This function  only accept values between -100C to +100C.
  It returns the Fahrenheit value as an integer

	Parameters
	----------
	temperature_in_C : float
		The inputted Celsius value

	Returns
	-------
	int
		integer output of a degrees in Fahrenheit
	'''
  int(temperature_in_C)
  if temperature_in_C <=100 and temperature_in_C >= -100:
    return int((temperature_in_C * 9/5) +32)
  else:
    return ("Unacceptable input values.")

def convertFToC(temperature_in_F):
  '''
	Converts Fahrenheit degrees to Celsius degrees

	This function  only accept values between -100C to +100C.
  It returns the Celsius value as an integer

	Parameters
	----------
	temperature_in_F : float
		The inputted fahrenheit value

	Returns
	-------
	int
		integer output of a degrees in Celsius
	'''
  int(temperature_in_F)
  if temperature_in_F <=100 and temperature_in_F >= -100:
    return int((temperature_in_F-32)* 5/9)
  else:
    return ("Unacceptable input values.")

def hypotenuse(side_a, side_b):
  '''
	Outputs hypotenuse of a right-angled triangle

	Calculates the hypotenuse and returns it to the sender based on
	sideA and sideB given

	Parameters
	----------
	sideA : float
		One of the arms of the right angle of the triangle
	sideB : float
		The other arm of the right angle of the triangle

	Returns
	-------
	float
		The hypotenuse value
	'''
  if side_a>0 and side_b>0:
    return math.sqrt(math.pow(side_a,2)+math.pow(side_b,2))
  else:
    return ("Unacceptable input values.")

def convertCToFEveryFive(lowC, highC):
  '''
	Converts every five Celsius degrees to a fahrenheit degree

	This function outputs a chart of values between lowC and highC.
	The lowC is less than highC.

	Parameters
	----------
	lowC : float
		The lowest value in the chart of Celsius values
	highC : float
		The highest value in the chart of Celsius values

	Returns
	-------
	str
		A list of every 5 Celsius value and its corresponding fahrenheit value
	'''
  output = ""
  if lowC <= highC:
    for count in range(lowC, highC+1, 5):
      output = (str(count)+"C = " + str(convertCToF(count)) + "F")
      print(output)
    return
  else:
    return ("Unacceptable input values.")