#-----------------------------------------------------------------------------
# Name:        Assignment 2 (Assignment2.py)
# Purpose:     Writing a program to incorporate all previous learned concept
#
# Author:      Owen Wong
# Created:     01/08/2019
# Updated:     01/19/2019
#-----------------------------------------------------------------------------
import random
import re
import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info('Start of program')
#-----------------------------------------------------------------------------
# The story.txt file is read and stored into the variable story
file = open("story.txt", 'r') # The story.txt file is opened
story = file.readlines() # The story.txt file is read and put into the story variable
file.close() # The story.txt file is closed

#-----------------------------------------------------------------------------
def menu_system():
  '''
  Displays the menu for the program.
  
  This menu system introduces the user to the program and gives instructions on how the user can use the program.

  Parameters
  ----------
  None
  
  Returns
  -------
  None
  '''
  logging.info('Starting menu_system function to display all menu options to user')
  print(("Hi "+ name_of_user+ ", welcome to Owen's advanced program.").center(80, '*'))
  print("You can perform operations or play games with our program!".center(80,'-'))
  print("\nPlease choose an action you want to take:\n")
  print("Enter 1:\tFind out whether a word is a palindrome.")
  print("Enter 2:\tConvert the string you enter to all uppercase and with no punctuation/number.")
  print('''Enter 3:\tPlay a game of "HANGMAN".''')
  print("Enter 4:\tSearch for a word in story.txt and output all appearances of that word.")
  print("Enter 5:\tWrite the first n lines of story.txt into a new file.")
  print("Enter 0:\tExit program.")
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
  logging.info('Starting repeat_menu_system function to display all menu options to user when the user completes at least one of the functions on the menu options')
  print("\n" + ("Hi "+ name_of_user+ ", welcome again!").center(80, '-'))
  print("\nPlease choose an action you want to take:\n")
  print("Enter 1:\tFind out whether a word is a palindrome.")
  print("Enter 2:\tConvert the string you enter to all uppercase and with no punctuation/number.")
  print('''Enter 3:\tPlay a game of "HANGMAN".''')
  print("Enter 4:\tSearch for a word in story.txt and output all appearances of that word.")
  print("Enter 5:\tWrite the first n lines of story.txt into a new file.")
  print("Enter 0:\tExit program.")
  return

#-----------------------------------------------------------------------------
def palindrome_checker(word):
  '''
  Check if the inputted string is a palindrome or not.
  
  This function goes through all the index of the user's string and compares it to the negative index of the user string to see if they are the same. If not, then it is not a palindrome.

  Parameters
  ----------
  word : str
    This is the word that is going to be checked in this function for whether it is a palindrome.
  
  Returns
  -------
  str
    It returns a message saying whether the word is actually a palinrome.
  
  Raises
    ------
    TypeError
      If word is not a str.
    ValueError
      If word has non-alphabetical characters like a space or punctuation/number.
    Exception
      If the palindrome checker's check goes awry (returns something unexpected).
  '''
  logging.debug('Starting palindrome_checker function with value: ' + word)
  if not isinstance(word, str):  
    logging.critical('The program ends because the input type is not a str')
    raise TypeError('palindrome_checker expecting a str as input')
  if not word.isalpha():
    logging.critical('The program ends because the input has non-alphabetical characters')
    raise ValueError('word has non-alphabetical characters')

  message = "This word is a palindrome."

  for count in range (0,len(word)):
    if word[count].lower() != word[len(word)-count-1].lower():
      logging.debug('The letters found not to match are: ' + word[count].lower() + ' and ' + word[len(word)-count-1].lower())
      message = "This word is not a palindrome."
      # message = "This word is not a palindrome."       This will trigger the exception
      if message != "This word is not a palindrome.":
        logging.critical('The program ends because palindrome_checker did not return a false message as expected')
        raise Exception('Palindrome check did not return a false message as expected.')
      break
  logging.debug('The message that the user is going to see is: ' + message)
  logging.debug("End of palindrome_checker function and it outputs a message telling the user whether the user's inputted string is a palindrome")
  return message

# Testing the palindrome_checker
# try:
#   print(palindrome_checker("racecar"))
#   print(palindrome_checker(199))
#   print(palindrome_checker("race car")) # Returns the ValueError message
# except (TypeError, ValueError) as a:
#   print('Something went wrong: ' + str(a))
# except Exception as a:
#   print('Something went wrong: ' + str(a))

#-----------------------------------------------------------------------------
def convert_sentence_to_uppercase(sentence_or_word):
  '''
  Converting a sentence to all uppercase and with no punctuation/number.
  
  This function replaces every non-alphabetical character to a space, and splits the string at every space. Then joins the string and converting it all uppercase while removing all punctuation/number.

  Parameters
  ----------
  sentence_or_word : str
    This is the sentence or word that is going to be converted to all uppercase.
  
  Returns
  -------
  str
    It returns the converted string which is all uppercase and with no punctuation/number.
  
  Raises
    ------
    TypeError
      If sentence_or_word is not a str.
    Exception
      If the uppercase conversion goes awry and returns something that is not all uppercase.
  '''
  logging.debug('Starting convert_sentence_to_uppercase function with value: ' + sentence_or_word)
  if not isinstance(sentence_or_word, str):  
    logging.critical('The program ends because the input type is not a str')
    raise TypeError('convert_sentence_to_uppercase expecting a str as input')

  converted_list = re.sub('[^a-zA-Z]', ' ', sentence_or_word).split() # using regex(regular expression, a concept I learned outside of class)
  all_caps_sentence = ' '.join(converted_list).upper()
  logging.debug('The converted uppercase with no punctuation/number sentence/word is: ' + all_caps_sentence)
  # all_caps_sentence="HIMYNAME."    This will trigger the exception
  for character in all_caps_sentence:
    if not character.isupper() and not character.isalpha() and not character.isspace():
      logging.critical('The program ends because the all_caps_sentence either is not all uppercase, or it has punctuation/numbers')
      raise Exception('convert_sentence_to_uppercase did not return an uppercase with no punctuation/number string as expected')
  logging.debug('End of convert_sentence_to_uppercase function and it outputs the all_caps_sentence')
  return all_caps_sentence

# Testing the convert_sentence_to_uppercase
# try:
#   print(convert_sentence_to_uppercase("hi my###name    is owen"))
#   print(convert_sentence_to_uppercase("hi"))
#   print(convert_sentence_to_uppercase(200)) 
# except TypeError as b:
#   print('Something went wrong: ' + str(b))
# except Exception as b:
#   print('Something went wrong: ' + str(b))
#-----------------------------------------------------------------------------
def hangman(difficulty):
  '''
  Plays hangman.
  
  The user inputs the difficulty in which the user wants their hangman to be. Then the user has 10 turns to guess the letters in the word, and he/she does not lose a turn after guessing the letter right. The final message is printed saying wether the user won.

  Parameters
  ----------
  difficulty : str
    This word informs the function whether to choose a word from the easy_wordList, moderate_wordlist, or hard_wordlist for the user to guess from.
  
  Returns
  -------
  None
  
  Raises
    ------
    TypeError
      If difficulty is not a str.
    ValueError
      If the if not one of the three difficulties stated (easy, moderate, hard).
    Exception
      If the secret_word fails to generate a word from the pre-generated word lists.
    Exception
      If the word_being_guessed list has an element that is not a string.
    Exception
      If the number of letters already guessed does not match the number of letters in the letter_storage, which is a list that stores all the guessed letters.
  '''
  logging.debug('Starting hangman function with the value' + difficulty)
  
  if not isinstance(difficulty, str):  
    logging.critical('The program ends because the input type is not a str')
    raise TypeError('hangman expecting a str as input')
  if difficulty.lower() != "easy" and difficulty.lower() != "moderate" and difficulty.lower() != "hard":
    logging.critical('The program ends because the input is not one of the three difficulties stated')
    raise ValueError('The difficulty inputted is not one of the three difficulties stated!')
  
  turns = 10
  word_being_guessed = []
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  letter_storage = [] # This list stores all the letters that have been guessed

  easy_wordList = ["lion", "dog", "cat", "oy", "haze", "menu", "paw", "swim", "q", name_of_user] # 1-4 letters and your name
  moderate_wordlist = ["window", "glass", "juice", "chair", "laptop", "lemon", "cable", "mirror", "jumbo", "fringe"] # 5 or 6 letters
  hard_wordlist = ["umbrella", "computer", "desktop", "hangman", "python", "complex", "waterloo", "science", "uranoob","supercalifragilisticexpialidocious"] # 7 or 8 letters and a super long word

  if difficulty.lower() == "easy":
    logging.debug('The secret word is created from the easy_wordList')
    secret_word = random.choice(easy_wordList) # Randomize a single word from the easy_wordList
  elif difficulty.lower() == "moderate":
    logging.debug('The secret word is created from the moderate_wordlist')
    secret_word = random.choice(moderate_wordlist) # Randomize a single word from the moderate_wordlist
  elif difficulty.lower() == "hard":
    logging.debug('The secret word is created from the hard_wordlist')
    secret_word = random.choice(hard_wordlist) # Randomize a single word from the hard_wordlist
  
  if not secret_word in easy_wordList and not secret_word in moderate_wordlist and not secret_word in hard_wordlist:
    logging.critical('the program ends because the program fails to generate a secret from one of the three pre-generated lists')
    raise Exception('The secret_word has failed to generate a word from the pre-generated lists')
  
  length_of_secret_word = len(secret_word)
  for character in secret_word: # printing - for each letter in secret word
    word_being_guessed.append("-")
  print("\nOk, so the word You need to guess has " + str(length_of_secret_word) + " characters")
  print("Be aware that You can enter only 1 letter from a-z")
  print("Also, you can only have 10 tries to guess the word, and you don't lose a turn if guess the letter correctly!")
  logging.debug("The word to guess is: " + secret_word)
  print("Word to guess: {0}".format(" ".join(word_being_guessed)))

  guess_taken = 0
  while guess_taken < turns:
    guess = input("\nInput a letter\n").lower()
    logging.debug('Ensuring input is an str')
    assert isinstance(guess, str), 'Expecting a str'
    if len(guess) > 1: # Checking string's length, is it only one character long?
      logging.debug('The user has inputted a guess that is not valid')
      print("Please input an one character string!")
    elif not guess in alphabet: # Checking input is valid or not (it is part of the alpbabet?)
      logging.debug('The user has inputted a guess that is not valid')
      print("Please enter a letter from the alphabet! (a-z)")
    elif guess in letter_storage: # checking if letter has been already used
      logging.debug('The user has inputted a guess that is not valid')
      print("You have already guessed that letter!")
    else: 
      letter_storage.append(guess) # Stores the letters already guessed into letter_storage
      if guess in secret_word:
        logging.debug('The user has guessed a letter correctly')
        print("\nYou guessed correctly!")
        for i in range(0, length_of_secret_word):
          if secret_word[i] == guess:
            word_being_guessed[i] = guess
        print("Word to guess: {0}".format(" ".join(word_being_guessed)))
        if not '-' in word_being_guessed:
          logging.debug('The hangman function ends with a message to the user stating that the user has won')
          print("You won!".center(80,"*"))
          break
      else:
        guess_taken += 1
        logging.debug('The user fails to guess a letter correctly')
        if guess_taken == 10:
          logging.debug('The hangman function ends with a message to the user stating that the user has lost')
          print((" Sorry, You lost :( The secret word was " + secret_word + " ").center(80,"!"))
          break
        print("\nThe letter is not in the word. Try Again!\nYou still have " + str(turns-guess_taken) + " turn(s) left")

    count = 0
    for letter in word_being_guessed:
      if not isinstance(letter, str):
        logging.critical('The program ends because the word_being_guessed has an element that is not a string')
        raise Exception('The word_being_guessed has an element that is not a string')
    for letter in word_being_guessed:
      if letter.isalpha():
        count += 1
        if count != len(letter_storage):
          logging.critical('The program ends because the number of letters already guessed does not match the number of letters in the letter_storage, which is a list that stores all the guessed letters')
          raise Exception('The number of letters already guessed does not match the number of letters in the letter_storage, which is a list that stores all the guessed letters')

# Testing with try and except does not apply, because it requires user's input and it has no return value.
#-----------------------------------------------------------------------------
def word_searcher(word_to_be_searched, fileContent):
  '''
  Searches for a word in story.txt.
  
  The user inputs a word that they want to search for in fileContent, the program outputs all appearances of the word in the format of a dictionary. The key will be which line number the word appears in, and the value will be a list stating the index range(s) in which the word appears in the corresponding line.

  Parameters
  ----------
  word_to_be_searched : str
    This the word that the function is looking for in story.txt.
  fileContent : list
    This is the list that word_to_be_searched is going to search through. This is also story.txt.
  
  Returns
  -------
  dict
    It returns a dicionary to list all appearances of word_to_be_searched in fileContent.
  
  Raises
    ------
    TypeError
      If word_to_be_searched is not a str.
    TypeError
      If fileContent is not a list.
    ValueError
      If word_to_be_searched has non-alphabetical characters like a space or punctuation/number(other than apostrophe).
    Exception
      If the list_of_words contains non-alphabetical characters(Not including apostrophe).
    Exception
      If word_searcher searching algorithm goes awry and returns a different type of return value than expected.
  '''
  logging.debug('Starting the word_searcher function with value: ' + word_to_be_searched + ', as the word that is going to search through fileContent')
  if not isinstance(word_to_be_searched, str):
    logging.critical('The program ends because the input type is not a str for the first parameter')
    raise TypeError('word_searcher expecting a str as its first parameter')
  if not isinstance(fileContent, list):
    logging.critical('The program ends because the input type is not a list for the second parameter')
    raise TypeError('word_searcher expecting a list as its second parameter')
  for character in word_to_be_searched:
    if not character.isalpha():
      if character != "'":
        logging.critical('The program ends because the first parameter contains a non-alphabetical(Not including apostrophe)')
        raise ValueError('word_to_be_searched has non-alphabetical characters(Not including apostrophe)')

  searched_word_dictionary = {}
  value_list = []
  line_number = 1
  logging.debug('Starting the search for word_to_be_searched through the entire fileContent')
  for line in fileContent:
    for word in re.sub("[^a-zA-Z' ]", ' ', line).split(' '):
      if word_to_be_searched.lower() == word.lower():
        key = "Line number: " + str(line_number) # The key for the dictionary
        list_of_words = re.sub("[^a-zA-Z' ]", ' ', line).split(' ') # From this line to the next 8 lines is converting the line to lowercase and storing the lowercase words into a list called lowercase_words
        lowercase_words = []
        for words in list_of_words:
          for character in words:
            if not character.isalpha():
              if character != "'":
                logging.critical('The program ends because the list_of_words contains non-alphabetical characters(Not including apostrophe)')
                raise Exception('The list_of_words list is not alphabetical(Not including apostrophe)')
          lowercase_words.append(words.lower())
        number_of_matching_words = lowercase_words.count(word_to_be_searched.lower())
        for count in range(0, number_of_matching_words): # In this for loop, I am trying to determine the position of the word
          index = lowercase_words.index(word_to_be_searched)
          position = 0
          for i,word in enumerate(lowercase_words):
            if i>=index:
              break
            position += (1 + len(word)) # The plus 1 is adding for the spaces removed from the re.sub
          for count in range (0, len(lowercase_words)):
            if lowercase_words[count].lower() == word_to_be_searched.lower():
              lowercase_words[count] = ''
              break
          value_list.append("Index range: "+ str(position) + "-" + str(position + len(word_to_be_searched)-1))
        searched_word_dictionary[key] = value_list
        break
    line_number += 1
    value_list=[] # Resetting the value list by making it empty
  logging.debug('The search for word_to_be_searched has finished')
  if searched_word_dictionary == {}:
    logging.debug("The word_searcher function ends with a message telling the user that there is no match for the user's inputted word in fileContent")
    return ('There seems to be no match for you word')
  if not isinstance(searched_word_dictionary, dict):
    logging.critical("The program ends because the word_searcher's return type is not dict")
    raise Exception('word_searcher searching algorithm did not return a dictionary as expected')
  logging.debug("The word_searcher function ends with the function outputting the dictionary listing all appearances of the user's inputted word")
  return searched_word_dictionary

# try:
#   print(word_searcher("witch", story))
#   print(word_searcher("100macbeth", story))
#   print(word_searcher(3, story)) # Returns the TypeError message
# except (TypeError, ValueError) as c:
#   print('Something went wrong: ' + str(c))
# except Exception as c:
#   print('Something went wrong: ' + str(c))

#-----------------------------------------------------------------------------
def write_the_first_n_lines(number_of_lines_to_be_written, fileContent):
  '''
  Writes the first n lines from story.txt into a new file.
  
  The user inputs the number of lines they want to write out, and the function creates a new file and writes the first n lines of story.txt into the new file.

  Parameters
  ----------
  number_of_lines_to_be_written : int
    This is the number of lines that the function if going to output into the new file.
  fileContent : list
    This is the list that number_of_lines_to_be_written is going to scan through. This is also story.txt.
  
  Returns
  -------
  None
  
  Raises
    ------
    TypeError
      If number_of_lines_to_be_written is not an int.
    TypeError
      If fileContent is not a list.
    ValueError
      if number_of_lines_to_be_written is outside of required range
    Exception
      If first_n_lines is not a list as the function expects
  '''
  logging.debug('Starting write_the_first_n_lines function with value: ' + str(number_of_lines_to_be_written) + ', to scan through fileContent')

  if not isinstance(number_of_lines_to_be_written, int):
    logging.critical('the program ends because the input type for the first parameter is not an int')
    raise TypeError('word_searcher expecting an int as its first parameter')
  if not isinstance(fileContent, list):
    logging.critical('the program ends because the input type for the second parameter is not a list')
    raise TypeError('word_searcher expecting a list as its second parameter')
  if number_of_lines_to_be_written<=0 or number_of_lines_to_be_written > len(fileContent):
    logging.critical('The program ends because the number_of_lines_to_be_written is outside of expected rane(1, ' + str(len(fileContent)) + ')')
    raise ValueError('number_of_lines_to_be_written not within expected range (1, ' + str(len(fileContent)) + ')')

  first_n_lines = []
  logging.debug('A new file called: The first ' + str(number_of_lines_to_be_written) + ' line(s) of story.txt is opened')
  new_file = open('The first ' + str(number_of_lines_to_be_written) + ' line(s) of story.txt', 'w')
  for count in range(0,number_of_lines_to_be_written):
    if count == number_of_lines_to_be_written-1:
      fileContent[count] = fileContent[count].strip('\n') # Removes the last \n to avoid printing an extra empty line in the new file
    first_n_lines.append(fileContent[count])
  logging.debug('The first_n_lines has been created and is going to be joined into a string and written into the new file')
  if not isinstance(first_n_lines, list):
    logging.critical('The program ends because first_n_lines is not a list')
    raise Exception('The first_n_lines function is not a list, which is not expected')

  new_file.write(' '.join(first_n_lines))
  logging.debug('the the first n lines of story.txt is written into the new file')
  new_file.close()
  logging.debug('The new file is closed')

# Testing with try and except does not apply because this function has no return value and it deals with file writing which can't be tested with try/except

#-----------------------------------------------------------------------------
#Here, it asks for the user's name.
logging.debug("The program asks for user's name")
name_of_user = str(input("What is your name?\n"))

#-----------------------------------------------------------------------------
def main():
  '''
  This function runs all other functions in this program
  
  This function has all the functions required for the user to interact with the program, going through functions I wrote etc.

  Parameters
  ----------
  None
  
  Returns
  -------
  None
  '''
  logging.debug('Starting main function')

  condition = 1
  while condition == 1 or condition ==2:
  
    #Outputs the introductory menu system when condition is equal to 1.
    if condition == 1:
      menu_system()
      condition = 2
  
    #Outputs the a re-greet menu system when condition is equal to 2.
    elif condition == 2:
      repeat_menu_system()
  
    #user_choice receives input on the choice the user made on the menu system.
    logging.debug('The user inputs a menu option')
    user_choice = int(input())
    
    # Invalid input check
    if user_choice > 5 or user_choice <0:
      print('Please input a valid option')
    
    #Here, it proceeds to the palindrome_checker function.
    if user_choice == 1:
      question_to_ask_for_word = input("Please enter a single word:")
      print(palindrome_checker(question_to_ask_for_word))
    
    # Here, it proceeds to the convert_sentence_to_uppercase function
    if user_choice == 2:
      question_to_ask_for_sentence = input("Please enter a sentence")
      print(convert_sentence_to_uppercase(question_to_ask_for_sentence))
    
    # Here, it proceeds to the hangman function
    if user_choice == 3:
      question_to_ask_for_difficulty = input("Please type the difficulty of the unkown word in this function\nType either 'easy', 'moderate', or 'hard':\n")
      hangman(question_to_ask_for_difficulty)
    
    # Here, it proceeds to the word_searcher function
    if user_choice == 4:
      question_to_ask_for_word_to_be_searched = input("Please type the word you want to search for in the story.txt file (Case-insensitive) (apostrophe matters - thus and 'thus are different):")
      print(word_searcher(question_to_ask_for_word_to_be_searched, story))
    
    # Here, it proceeds to the write_the_first_n_lines function
    if user_choice == 5:
      question_to_ask_number_of_lines = int(input("How many line(s) do you want to write in a new file? (Has to be within the number of lines in the story)"))
      write_the_first_n_lines(question_to_ask_number_of_lines, story)
    
    #If the user enters 0 on for the menu system question, the loop breaks, ending the while loop for the program. Therefore, ending the program entirely.
    elif user_choice == 0:
      print("Thank you for using Owen's advanced program. See you next time!")
      logging.debug('The program ends')
      break
main() # Calling the main function so that the user can interact with the program!