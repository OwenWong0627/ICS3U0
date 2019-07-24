#-----------------------------------------------------------------------------
# Name:        Exercise 4 (Exercise4.py)
# Purpose:     Understading if statement coding in Python
#
# Author:      Owen Wong
# Created:     10/11/2018
# Updated:     10/12/2018
#-----------------------------------------------------------------------------
import math
#-----------------------------------------------------------------------------
#First Program
Question_1 = int(input("Rate your day from 1-10\n1 being a bad day\n10 being an awesome day"))
if Question_1 <=3 and Question_1 >=2:
  print("I hope you feel better in the coming days")
elif Question_1 ==1:
  print('"I better stay away from this person"')
elif Question_1 >3 and Question_1 <6:
  print("What happened that made you a little sad?")
elif Question_1 >=6 and Question_1 <=7:
  print("What should I do to make this the best day in your life")
elif Question_1 >=8 and Question_1 <=9:
  print("That's really good")
elif Question_1 == 10:
  print("You can spread your happiness to your peers!")
else:
  print("Number entered is not from 1-10\nplease retry")
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#Second Program
Random_Number = 1
while Random_Number == 1:
    Question_2 = float(input("Enter 1 if you want to find the trigonometric ratio using sin\nEnter 2 if you want to find the trigonometric ratio using cos\nEnter 3 if you want to find the trigonometric ratio using tan"))
    if Question_2 == 1:
      Question_3 = float(input("Enter the angle value to find the sin of this angle"))
      print(math.sin(math.radians(Question_3)))
    elif Question_2 == 2:
      Question_4 = float(input("Enter the angle value to find the cos of this angle"))
      print(math.cos(math.radians(Question_4)))
    elif Question_2 == 3:
      Question_5 = float(input("Enter the angle value to find the tan of this angle"))
      print(math.tan(math.radians(Question_5)))
    else:
      print("Please stop entering numbers outside of 1-3, or a decimal, plz")
    Question_6= int(input("Enter 1 if you want to find more trig ratio, enter any other number to exit program"))
    if Question_6 ==1:
      Random_Number = 1
    elif Question_6 !=1:
      break
#-----------------------------------------------------------------------------