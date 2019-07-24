#-----------------------------------------------------------------------------
# Name:        Pre-exercise 6 (PreExercise6.py)
# Purpose:     Using all previous knowledge to complete a challenge in Python
#
# Author:      Owen Wong
# Created:     10/17/2018
# Updated:     10/17/2018
#-----------------------------------------------------------------------------

condition = True
while condition == True:
  question_1 = int(input("Choose an option below:\n1. Add two integers.\n2. Subtract two integers.\n3. Multiply two integers.\n4. Divide two integers.\n5. Perform integer division on two floats.\n6. Odd or even.\n7. Count to zero.\n8. Factorial!\n9. nth Triangle Number!\n0. Exit"))
  if question_1 == 0:
    condition = False
  elif question_1 == 1:
    question_2 = int(input("Enter the first number you want to add"))
    question_3 = int(input("Enter the second number you want to add to the first number"))
    print("This is your answer: "+str(question_2+question_3))
    condition = True
  elif question_1 == 2:
    question_4 = int(input("Enter the first number you want to subtract"))
    question_5 = int(input("Enter the second number you want to subtract from the first number"))
    print("This is your answer: "+str(question_4-question_5))
    condition = True
  elif question_1 == 3:
    question_6 = int(input("Enter the first number you want to multiply"))
    question_7 = int(input("Enter the second number you want to multiply with the first number"))
    print("This is your answer: "+str(question_6*question_7))
    condition = True
  elif question_1 == 4:
    question_8 = int(input("Enter the first number you want to have it divided by"))
    question_9 = int(input("Enter the second number to divide the first number"))
    print("This is your answer: "+str(question_8/question_9))
    condition = True
  elif question_1 == 5:
    question_10 = float(input("Enter the first number you want to have it divided by"))
    question_11 = float(input("Enter the second number to divide the first number"))
    print("This is your answer: "+str(question_10//question_11))
    condition = True
  elif question_1 == 6:
    question_12 = int(input("Enter a number to have it classified as either odd or even"))
    if question_12%2==1:
      print("This number is an odd number")
    else:
      print("This number is an even number")
    condition = True
  elif question_1 == 7:
    question_13 = int(input("Enter a number to count it up or down to zero"))
    if question_13 == 0:
      print("0")
    if question_13 < 0:
      for count in range(question_13, 1, 1):
        print(str(count))
    elif question_13 > 0:
      for count in range(question_13, -1, -1):
        print(str(count))
    condition = True
  elif question_1 == 8:
    question_14 = int(input("Enter a number you want to find the factorial of"))
    factorial = 1
    while question_14 > 1:
      factorial = factorial*question_14
      question_14= question_14-1
    print(str(factorial))
    condition = True
  elif question_1 == 9:
    question_15 = int(input("Enter a number you want to find the triangle number of"))
    triangle_number = 1
    while question_15 >1:
      triangle_number = triangle_number+question_15
      question_15 = question_15-1
    print(str(triangle_number))
    condition = True