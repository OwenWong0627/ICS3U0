#-----------------------------------------------------------------------------
# Name:        Exercise 11 (Exercise11.py)
# Purpose:     Using exceptions and the logging module
#
# Author:      Owen Wong
# Created:     11/25/2018
# Updated:     11/28/2018
#-----------------------------------------------------------------------------
import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# A debug message stating that the program has initiated
logging.debug('Start of program')

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
  bool
    The function outputs a boolean verifying whether the number inputted is a prime number.
	
	Raises
  ------
  TypeError
    If number_to_be_checked is not an int
  ValueError
    If number_to_be_checked is outside the required range
  Exception
    If the prime_number_checker calculation goes awry
  '''
  
  # A logging to indicate the start of the function
  logging.info ('Starting prime_number_checker function')
  
  # Checking if the input is an int with an assertion
  logging.debug('Ensuring input is an int')
  assert isinstance(number_to_be_checked, (int)), 'Expecting an int'
  
  # A TypeError is raised if the number_to_be_checked is not an int
  if not isinstance(number_to_be_checked, (int)):
    raise TypeError('prime_number_checker is expecting an int as input')
  
  # A loggin message signaling that the input is indeed an int
  logging.debug('The value is an int, starting to verify if the input is a prime number')

  # A ValueError is raised when the number_to_be_checked is smaller than 2
  if number_to_be_checked < 2:
    raise ValueError('Values not within expected range (2, ∞)')
  
  # 
  the_number_is_a_prime_number = True
  for count in range (2,number_to_be_checked+1):
    if number_to_be_checked%count == 0 and count !=number_to_be_checked:
      the_number_is_a_prime_number=False
      break
    else:
      the_number_is_a_prime_number=True
#     the_number_is_a_prime_number="hi"          This will trigger the exception, because the inputted value is supposed to be a prime number

  # A debug logging to verify if the the_number_is_a_prime_number is actually a boolean
  logging.debug('Ensuring the final value is a boolean value')
  assert isinstance(the_number_is_a_prime_number, bool), 'Expecting a boolean'
  
  # A error logging to verify if the the_number_is_a_prime_number is actually a boolean
  if not isinstance(the_number_is_a_prime_number, bool):
    logging.error('Error!')

  if not isinstance(the_number_is_a_prime_number, (bool)):
    raise Exception('prime_number_checker calculation did not return a boolean value as expected.')
  
  logging.debug('Final value of the_number_is_a_prime_number is: ' + str(the_number_is_a_prime_number))
  logging.info('End function')

  return the_number_is_a_prime_number

# Testing
while True:
    print('Please enter an integer that is greater than 1:')
    value = input()
    if value == '':
      break
    try:
      answer = prime_number_checker(int(value))
      if answer == True:
        print("The number you inputted is a prime number.")
      elif answer == False:
        print("The number you inputted is not a prime number.")
    except (TypeError, ValueError) as e:
      print('That value did not work, please try again')
      continue
    except Exception as e:
      print('Something went wrong: ' + str(e))
      break

# A debug message stating that the program has ended
logging.debug('End of program')