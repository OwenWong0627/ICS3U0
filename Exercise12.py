#-----------------------------------------------------------------------------
# Name:        Exercise 12 (Exercise12.py)
# Purpose:     Using dictionaries in python
#
# Author:      Owen Wong
# Created:     11/27/2018
# Updated:     11/28/2018
#-----------------------------------------------------------------------------

# First we define the dictionary
# it will have nothing in it this time
ages = {}

# Add a couple of names to the dictionary
ages['Sue'] = 23
ages['Peter'] = 19
ages['Andrew'] = 78
ages['Karren'] = 45

# Check if Sue is in the ages dictionary
if "Sue" in ages.keys():
  print ("Sue is in the dictionary. She is", ages['Sue'], "years old")
else:
  print ("Sue is not in the dictionary")

# Print out all the keys in the dictionary
print ("The following people are in the dictionary:")
print (ages.keys())

#-----------------------------------------------------------------------------

emptyDict = {} #This creates an empty Dictionary
myDict = {'a':1,'b':2,'c':3} #This creates a Dictionary with its associated Key:Value pairs
myDict['d'] = 4 #This Adds a key:value to the Dictionary
myDict['a'] = 2 #This Changes the key "a"'s value to 2 rather than 1
print (myDict['a'])
#This returns 2 - the associated value to the key "a"

print (myDict)
#This returns {'a': 2, 'b': 2, 'c': 3, 'd': 4} - the entire Dictionary

print("These are all the items in My Dictionary:")
for i in myDict.items():
	print(i)

print (myDict.values())
#This returns [2, 2, 3, 4] - a list containing all of the Values of the each Key

del myDict['b'] # This deletes the Key "b" and its associated value of 2
print (myDict)

#-----------------------------------------------------------------------------

age = []

# Converting the values in the ages dictionary into an age list
age=list(ages.values())
age.sort()
print(age)


def addchar(list_to_be_modified):
  '''
  Adds an integer that the user inputted to a list

  Parameters
  ----------
  parameter1 : int
    This is the number that is going to be added to the list.
  
  Returns
  -------
  None
	
	Raises
  ------
  TypeError
    If element_to_be_added is not an int
  ValueError
    If number_to_be_checked is outside the required range
  '''

  element_to_be_added = int(input("please enter a number"))

  # A TypeError is raised if the element_to_be_added is not an int
  if not isinstance(element_to_be_added, (int)):
    raise TypeError('addchar is expecting an int as input')

  # A ValueError is raised when the element_to_be_added is smaller than 0
  if element_to_be_added < 0:
    raise ValueError('Values not within expected range (0, ∞)')
  
  # The list is modified
  list_to_be_modified.append(element_to_be_added)
  return

addchar(age)
print(age)

#-----------------------------------------------------------------------------

# Getting all the tuple in the ages dictionary and converting it into a tuple
name = tuple(ages.keys())
print(name)

list_of_students = [(name[0], age[0]), (name[1], age[1]), (name[2], age[2]), (name[3], age[3])]

# Print out all students' name and age <-The age is from the age list I created above
for student in list_of_students:
  name, age = student
  print(name)
  print("Age: " + str(age))
  print()