#-----------------------------------------------------------------------------
# Name:        Assignment 1 (Assignment1.py)
# Purpose:     Culminative assessment of basic Python knowledge
#
# Author:      Owen Wong
# Created:     10/19/2018
# Updated:     11/20/2018
#-----------------------------------------------------------------------------
import math
from random import randint

#-----------------------------------------------------------------------------
def menu_system():
  '''
  Displays the menu for the program.
  
  This menu system introduces the user to the program and gives instructions on how to use the program.

  Parameters
  ----------
  None
  
  Returns
  -------
  None
  '''
  print("\nHi "+ name_of_user+ ", welcome to Owen's leisurely program.")
  print("You can perform math operations or play games with our program!")
  print("Please choose an action you want to take:")
  print("Enter 1 if you want to find the volume of a cylinder.")
  print("Enter 2 if you want to find the surface area of a cylinder.")
  print("Enter 3 if you want to find out if the number you enter is a prime number or not.")
  print("Enter 4 if you want to find out all the positive factors for the number you enter.")
  print('''Enter 5 if you want to play "Rock Paper Scissors" with the program.''')
  print("Enter 6 if you want to find the reversed spelling of a word.")
  print("Enter 7 if you want to have all the vowels of a word printed out.")
  print("Enter 0 if you want to exit the program.")
  return

#-----------------------------------------------------------------------------
def repeat_menu_system():
  '''
  Displays the menu for the program.
  
  This menu system greets the user again instead of introducing the name of the program again.

  Parameters
  ----------
  None
  
  Returns
  -------
  None
  '''
  print("\nHi "+ name_of_user+ ", welcome again!")
  print("Please choose an action you want to take:")
  print("Enter 1 if you want to find the volume of a cylinder.")
  print("Enter 2 if you want to find the surface area of a cylinder.")
  print("Enter 3 if you want to find out if the number you enter is a prime number or not.")
  print("Enter 4 if you want to find out all the positive factors for the number you enter.")
  print('''Enter 5 if you want to play "Rock Paper Scissors" with the program.''')
  print("Enter 6 if you want to find the reversed spelling of a word.")
  print("Enter 7 if you want to have all the vowels of a word printed out.")
  print("Enter 0 if you want to exit the program.")
  return

#-----------------------------------------------------------------------------
def cylinder_volume(radius,height):
  '''
  Calculates the volume of a cylinder
  
  This function collects the radius and height input of the cylinder and performs the appropriate calculation and outputs the volume rounded to two decimal places.

  Parameters
  ----------
  parameter1 : float
    This is the radius of the cylinder.
  parameter2 : float
    This is the height of the cylinder.
  
  Returns
  -------
  float
    It outputs the volume of the cylinder rounded to two decimal places.
  str
		If the values are incorrect, it will return the string 'Invalid input. You will be redirected back to the menu!'
  '''
  if radius > 0 and height > 0:
    return ("The volume of the cylinder is: "+ str(round((math.pi*height*(radius**2)),2)))
  else:
    return ("Invalid input. You will be redirected back to the menu!")

# Check to make sure the function is working
#assert cylinder_volume(2,3) == "The volume of the cylinder is: 37.7"

# The following will break, this is just to show the error message that could pop up
#assert cylinder_volume(0,3) == "The volume of the cylinder is: 37.7", 'Expecting an error message saying: "Invalid input. You will be redirected back to the menu!"'

# The following will break, this is just to show the error message that could pop up
#assert cylinder_volume(2,3) == "The volume of the cylinder is: 37", 'Expecting cylinder with radius of 2 and height of 3 to output the message: "The volume of the cylinder is: 37.7"'

#-----------------------------------------------------------------------------
def cylinder_surface_area(radius, height):
  '''
  Calculates the surface area of a cylinder
  
  This function collects the radius and height input of the cylinder and performs the appropriate calculation and outputs the surface area rounded to two decimal places.

  Parameters
  ----------
  parameter1 : float
    This is the radius of the cylinder.
  parameter2 : float
    This is the height of the cylinder.
  
  Returns
  -------
  float
    It outputs the surface area of the cylinder rounded to two decimal places.
  str
		If the values are incorrect, it will return the string 'Invalid input. You will be redirected back to the menu!'
  '''
  if radius > 0 and height > 0:
    return ("The surface area of the cylinder is: "+ str(round(((2*math.pi*radius*height)+(2*math.pi*(radius**2))),2)))
  else:
    return ("Invalid input. You will be redirected back to the menu!")

# Check to make sure the function is working
#assert cylinder_surface_area(2,3) == "The surface area of the cylinder is: 62.83"

# The following will break, this is just to show the error message that could pop up
#assert cylinder_surface_area(0,3) == "The surface of the cylinder is: 37.7", 'Expecting an error message saying: "Invalid input. You will be redirected back to the menu!"'

# The following will break, this is just to show the error message that could pop up
#assert cylinder_surface_area(2,3) == "The surface area of the cylinder is: 37.7", 'Expecting cylinder with radius of 2 and height of 3 to output the message: "The surface area of the cylinder is: 62.83"'

#-----------------------------------------------------------------------------
def prime_number_checker(number_to_be_checked):
  '''
  Check if user's input is a prime number.
  
  This function receives an input that is an integer greater than 1, and then performs a series of "checks" to see if the integer entered is a prime number or not.

  Parameters
  ----------
  parameter1 : int
    This is the number that is going to checked whether it is a prime number or not.
  
  Returns
  -------
  str
    The function outputs a message saying either if the number inputted is or isn't a prime number.
    str
		If the values are incorrect, it will return the string 'Invalid input. You will be redirected back to the menu!'
  '''
  if number_to_be_checked > 1:
    the_number_is_a_prime_number = True
    for count in range (2,number_to_be_checked+1):
      if number_to_be_checked%count == 0 and count !=number_to_be_checked:
        the_number_is_a_prime_number=False
        break
      else:
        the_number_is_a_prime_number=True
    if the_number_is_a_prime_number == True:
      return ("The number you inputted is a prime number.")
    elif the_number_is_a_prime_number == False:
      return ("The number you inputted is not a prime number.")
  else:
    return("Invalid input. You will be redirected back to the menu!")

# Check to make sure the function is working
#assert prime_number_checker(3) == "The number you inputted is a prime number."

# The following will break, this is just to show the error message that could pop up
#assert prime_number_checker(1) == "The number you inputted is not a prime number.",'Expecting an error message saying: "Invalid input. You will be redirected back to the menu!"'

# The following will break, this is just to show the error message that could pop up
#assert prime_number_checker(5) == "The number you inputted is not a prime number.", 'Expecting the number 3 to be a prime number'

#-----------------------------------------------------------------------------
def print_all_positive_factors(number_to_be_factored):
  '''
  Outputs all positive factors of a number
  
  This function receives an input that is an integer greater than 0, and then performs a loop of division and outputs the positive factors of the inputted number.

  Parameters
  ----------
  parameter1 : int
    The number that is going to have its positive factors listed.
  
  Returns
  -------
  None
  '''
  result = ""
  if number_to_be_factored > 0:
    print("These are all the factors of "+ str(number_to_be_factored) + ":")
    for count in range (1,number_to_be_factored+1):
      if number_to_be_factored%count == 0:
        result = str(int(number_to_be_factored/count))
        print(result)
    return
  else:
    print("Invalid input. You will be redirected back to the menu!")
    return

#-----------------------------------------------------------------------------
def rock_paper_scissors(number_of_rounds):
  '''
  Plays Rock Paper Scissors with the program.
  
  This function receives an input on how many rounds does the user want to play with the program,
  the user selects from the three choices of Rock, Paper, and Scissors.
  There will be points recorded if the game is best of 3

  Parameters
  ----------
  parameter1 : int
    This number is the number of rounds that is going to be played between the user and the program.
  
  Returns
  -------
  None
  '''
  computer = ["Rock", "Paper", "Scissors"]
  if number_of_rounds == 1:
    question_to_get_user_input = str(input("\nPlease enter Rock, Paper, or Scissors:"))
    if question_to_get_user_input == "Rock" or question_to_get_user_input == "Paper" or question_to_get_user_input == "Scissors":
      computer_choice = computer[randint(0,2)]
      if question_to_get_user_input == computer_choice:
        print("The program selects "+ computer_choice + ".")
        print("Tie!")
        rock_paper_scissors(1)
      elif question_to_get_user_input == "Rock":
        if computer_choice == "Paper":
          print("the program selects "+ computer_choice + ".")
          print("You lose! "+ computer_choice+ " covers "+ question_to_get_user_input + ".")
        else:
          print("the program selects "+ computer_choice + ".")
          print("You win! "+ question_to_get_user_input+ " smashes "+ computer_choice + ".")
      elif question_to_get_user_input == "Paper":
        if computer_choice == "Scissors":
          print("the program selects "+ computer_choice + ".")
          print("You lose! "+ computer_choice+ " cut "+ question_to_get_user_input + ".")
        else:
          print("the program selects "+ computer_choice + ".")
          print("You win! "+ question_to_get_user_input+ " covers "+ computer_choice + ".")
      elif question_to_get_user_input == "Scissors":
        if computer_choice == "Rock":
          print("the program selects "+ computer_choice + ".")
          print("You lose... "+ computer_choice+ " smashes "+ question_to_get_user_input + ".")
        else:
          print("the program selects "+ computer_choice + ".")
          print("You win! "+ question_to_get_user_input+ " cut "+ computer_choice + ".")
    else:
        print("That's not a valid play. Check your spelling or capitalization!")
        rock_paper_scissors(1)
  elif number_of_rounds == 3:
    print("Scores will be displayed as computer:user.")
    computer_score = 0
    user_score = 0
    rounds = True
    while rounds == True:
      if computer_score == 2:
        print("The program wins!")
        rounds = False
      elif user_score == 2:
        print("congratulations! You won.")
        rounds = False
      elif computer_score<3 and user_score<3:
        question_to_get_user_input = str(input("\nPlease enter Rock, Paper, or Scissors:"))
        if question_to_get_user_input == "Rock" or question_to_get_user_input == "Paper" or question_to_get_user_input == "Scissors":
          computer_choice = computer[randint(0,2)]
          if question_to_get_user_input == computer_choice:
            print("The program selects "+ computer_choice + ".")
            print("Tie!")
            print("The score is "+ str(computer_score) + ":" + str(user_score) + ".")
          elif question_to_get_user_input == "Rock":
            if computer_choice == "Paper":
              print("the program selects "+ computer_choice + ".")
              print("You lose! "+ computer_choice+ " covers "+ question_to_get_user_input + ".")
              print("The score is "+ str(computer_score+1) + ":" + str(user_score) + ".")
              computer_score = computer_score+1
            else:
              print("the program selects "+ computer_choice + ".")
              print("You win! "+ question_to_get_user_input+ " smashes "+ computer_choice + ".")
              print("The score is "+ str(computer_score) + ":" + str(user_score+1) + ".")
              user_score = user_score+1
          elif question_to_get_user_input == "Paper":
            if computer_choice == "Scissors":
              print("the program selects "+ computer_choice + ".")
              print("You lose! "+ computer_choice+ " cut "+ question_to_get_user_input + ".")
              print("The score is "+ str(computer_score+1) + ":" + str(user_score) + ".")
              computer_score = computer_score+1
            else:
              print("the program selects "+ computer_choice + ".")
              print("You win! "+ question_to_get_user_input+ " covers "+ computer_choice + ".")
              print("The score is "+ str(computer_score) + ":" + str(user_score+1) + ".")
              user_score = user_score+1
          elif question_to_get_user_input == "Scissors":
            if computer_choice == "Rock":
              print("the program selects "+ computer_choice + ".")
              print("You lose... "+ computer_choice+ " smashes "+ question_to_get_user_input + ".")
              print("The score is "+ str(computer_score+1) + ":" + str(user_score) + ".")
              computer_score = computer_score+1
            else:
              print("the program selects "+ computer_choice + ".")
              print("You win! "+ question_to_get_user_input+ " cut "+ computer_choice + ".")
              print("The score is "+ str(computer_score) + ":" + str(user_score+1) + ".")
              user_score = user_score+1
        else:
          print("That's not a valid play. Check your spelling or capitalization!")
  else:
    print("Invalid input. You will be redirected back to the menu!")

#-----------------------------------------------------------------------------
def print_the_reversed_word (word):
  '''
  Print the reversed spelling of a word.
  
  This function receives an input that is a word, puts the word in a loop, reverse the loop, and output the letters in the reversed loop to get the reversed spelling of the inputted word.

  Parameters
  ----------
  parameter1 : str
    This is the word that is going to be reversed in spelling.
  
  Returns
  -------
  str
    The function outputs the word in reversed spelling.
  str
		If the values are incorrect, it will return the string 'Invalid input. You will be redirected back to the menu!'
  '''
  result = ""
  if word.isalpha():
    for letter_from_the_back in reversed(word):
      result = result + letter_from_the_back
    return("Here is the reversed word: " + result + ".")
  else:
    return("Invalid input. You will be redirected back to the menu!")

# Check to make sure the function is working
#assert print_the_reversed_word("racecar") == "Here is the reversed word: racecar."

# The following will break, this is just to show the error message that could pop up
#assert print_the_reversed_word("hi") == "Here is the reversed word: hi.", 'Expecting the word "hi" to output the reversed word which is "ih"'

#-----------------------------------------------------------------------------
def print_all_vowels_in_word(word):
  '''
  Print all the vowels of a word.
  
  This function receives an input that is a word, puts the word in a loop, checks each individual letters, and output the vowels of the inputted word.

  Parameters
  ----------
  parameter1 : str
    This is the word that is checked for vowels.
  
  Returns
  -------
  str
    The function outputs all the vowels of the inputted word.
  str
		If the values are incorrect, it will return the string 'Invalid input. You will be redirected back to the menu!'
  '''
  result = ""
  if word.isalpha():
    for vowel in word:
      if vowel == "a":
        result = result + vowel + " "
      elif vowel == "e":
        result = result + vowel + " "
      elif vowel == "i":
        result = result + vowel + " "
      elif vowel == "o":
        result = result + vowel + " "
      elif vowel == "u":
        result = result + vowel + " "
      elif vowel == "A":
        result = result + vowel + " "
      elif vowel == "E":
        result = result + vowel + " "
      elif vowel == "I":
        result = result + vowel + " "
      elif vowel == "O":
        result = result + vowel + " "
      elif vowel == "U":
        result = result + vowel + " "
    if result == "":
      return("There are no vowels in this word.")
    else:
      return("Here are all the vowels of " + word + ": " + result)
  else:
    return("Invalid input. You will be redirected back to the menu!")

# Check to make sure the function is working
#assert print_all_vowels_in_word("racecAr") == "Here are all the vowels of racecAr: a e A "

# The following will break, this is just to show the error message that could pop up
#assert print_all_vowels_in_word("hi") == "There are no vowels in this word.", 'Expecting the word "hi" to output vowel "i"'

# Check to make sure the function is working
#assert print_all_vowels_in_word("h") == "There are no vowels in this word."

#-----------------------------------------------------------------------------
#Here, it asks for the user's name.
name_of_user = str(input("What is your name?" + "\n"))

#-----------------------------------------------------------------------------
condition = 1
while condition == 1 or condition ==2:

  #Outputs the introductory menu system when condition is equal to 1.
  if condition == 1:
    menu_system()
    condition = 2

  #Outputs the a re-greet menu system when condition is equal to 2.
  elif condition == 2:
    repeat_menu_system()

  #question_1 receives input on the choice the user made on the menu system.
  question_1 = int(input())

  #Here, it proceeds to the cylinder volume function.
  if question_1 == 1:
    question_radius = float(input("Please enter the radius of this cylinder(greater than 0):"))
    question_height = float(input("Please enter the height of this cylinder(greater than 0):"))
    print(cylinder_volume(question_radius,question_height))

  #Here, it proceeds to the cylinder surface area function.
  elif question_1 == 2:
    question_radius = float(input("Please enter the radius of this cylinder(greater than 0):"))
    question_height = float(input("Please enter the height of this cylinder(greater than 0):"))
    print(cylinder_surface_area(question_radius,question_height))

  #Here, it proceeds to the prime number checker function.
  elif question_1 == 3:
    question_for_number_to_be_checked = int(input("Please enter an integer that is greater than 1:"))
    print(prime_number_checker(question_for_number_to_be_checked))

  #Here, it proceeds to the function where it prints all positive factors of the inputted number.
  elif question_1 == 4:
    question_for_number_to_be_factored = int(input("Please enter an integer that is greater than 0:"))
    print_all_positive_factors(question_for_number_to_be_factored)

  #Here, it proceeds to the "Rock Paper Scissors" function.
  elif question_1 == 5:
    question_for_number_of_rounds = int(input("Please select if you want to play to the best of 1 or best of 3 (Enter 1 or 3):"))
    rock_paper_scissors(question_for_number_of_rounds)

  #Here, it proceeds to the function where the reversed spelling of a word is printed.
  elif question_1 == 6:
    question_to_ask_for_word = input("Please enter a word:")
    print(print_the_reversed_word(question_to_ask_for_word))

  #Here, it proceeds to the function where all vowels of the inputted word ara outputted.
  elif question_1 == 7:
    question_to_ask_for_word = input("Please enter a word:")
    print(print_all_vowels_in_word(question_to_ask_for_word))

  #If the user enters 0 on for the menu system question, condition equals to 3, ending the while loop for the program. Therefore, ending the program entirely.
  elif question_1 == 0:
    condition = 3
    print("Thank you for using Owen's leisurely program. See you next time!")