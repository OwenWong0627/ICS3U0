#-----------------------------------------------------------------------------
# Name:        Pre-Exam Question (ExamQuestion.py)
# Purpose:     Showing my understading of documentations, headers, assertions, try/excep/raise, logging
#
# Author:      Owen Wong
# Created:     01/22/2019
# Updated:     01/22/2019
#-----------------------------------------------------------------------------
import logging
logging.basicConfig(filename='debug.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info('Start of program')

#-----------------------------------------------------------------------------
def volume_of_rectangular_prism(length, width, height):
  '''
  Solves for volume of a rectangular prism.
  
  First, the function solves for the area of the 2D rectangle, then it uses that area and times it by the height (third parameter) to find the volume of the rectangular prism.
  
  
  
  Parameters
  ----------
  length : float
    This is the length of the rectangular prism.
  width : float
    This is the width of the rectangular prism.
  height : float
    This is the height of the rectangular prism.
  Returns
  -------
  float
    The volume of the rectangular prism.
  Raises
  ------
  TypeError
    If length, width, or height is not an int or float.
  ValueError
    If length, width, or height is smaller than or equal to 0.
  Exception
    If the area calculation goes awry
  Exception
    If the volume calculation goes awry.
  '''
  logging.debug('Start of volume_of_rectangular_prism function with values, length: ' + str(length) + ', width: ' + str(width) + ', height: ' + str(height) + '.')

  # assert isinstance(length, (int, float)), 'Expecting an int or float for length'
  # assert isinstance(width, (int, float)), 'Expecting an int or float for width'
  # assert isinstance(height, (int, float)), 'Expecting an int or float for height'

  if not isinstance(length, (int, float)) or not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
    logging.critical('volume_of_rectangular_prism expecting an int or float as input for all three parameters')
    raise TypeError('volume_of_rectangular_prism expecting an int or float as input for all three parameters')
  if length<=0 or width<=0 or height<=0:
    logging.critical('one of the three input not within expected range (greater than 0)')
    raise ValueError('one of the three input not within expected range (greater than 0)')

  area_of_rectangle = length * width
  # assert isinstance(area_of_rectangle, (int, float)), 'Expecting an int or float for area_of_rectangle'
  logging.debug('Calculating area of the 2D rectangle using length and width. The result is: '+ str(area_of_rectangle))
  if not isinstance(area_of_rectangle, (float, int)):
    logging.critical('Area calculation did not return an int or float value as expected.')
    raise Exception('Area calculation did not return an int or float value as expected.')
  volume = area_of_rectangle * height
  # assert isinstance(volume, (int, float)), 'Expecting an int or float for volume'

  logging.debug('Calculating volume of rectangular prism using area_of_rectangle and height. The result is: ' + str(volume))
  
  if not isinstance(volume, (float, int)):
    logging.critical('Volume calculation did not return an int or float value as expected.')
    raise Exception('Volume calculation did not return an int or float value as expected.')
  logging.debug('End of volume_of_rectangular_prism function')
  return volume

# assert volume_of_rectangular_prism(3, 4, 5) == 60, 'Expecting prism with sides 3, 4 and height of 5 to have a volume of 60'
# assert isinstance(volume_of_rectangular_prism(3,4,5), float), 'Expecting prism with sides 3, 4 and height of 5 to have a volume value that is an int'    # This will trigger an error
# assert volume_of_rectangular_prism(1, 2, 5) == 42, 'Expecting prism with sides 1, 2 and height of 5 to have a volume of 10' 3     # This will trigger an error.
try:
  print(volume_of_rectangular_prism(2,3,4))
  print(volume_of_rectangular_prism(0,3,4))
except (TypeError, ValueError) as a:
  print('Something went wrong: ' + str(a))
except Exception as a:
  print('Something went wrong: ' + str(a))

try:
  print(volume_of_rectangular_prism(1,"hi",4))
except (TypeError, ValueError) as b:
  print('Something went wrong: ' + str(b))
except Exception as b:
  print('Something went wrong: ' + str(b))

# Start of program here
print(volume_of_rectangular_prism(3,4,5))
logging.info('The program ends')