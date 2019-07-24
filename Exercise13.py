#-----------------------------------------------------------------------------
# Name:        Exercise 13 (Exercise13.py)
# Purpose:     Using dictionaries in python
#
# Author:      Owen Wong
# Created:     12/03/2018
# Updated:     12/04/2018
#-----------------------------------------------------------------------------

word = '''Hello World'''
print(word)

letter=word[0] #Use [ ] to access characters in a string
print(letter)

print(len(word)) # print the length of the word in terms of characters

print("There are " + str(word.count('l')) + " 1's")	# count how many times l is in the string

print("The letter H is at character number " + str(word.find("H")))  	# find the word H in the string

print("the word 'World' is at index " + str(word.index("World"))) 	# find the letters World in the string

phrase =  'Count, the number     of /tspaces'

print("There are " + str(phrase.count(' ')) + " spaces")

#Slicing
#Use [ # : # ] to get set of letter

print(word[0])          #get one char of the word
print(word[0:1])        #get one char of the word (same as above)
print(word[0:3])        #get the first three char
print(word[:3])         #get the first three char
print(word[-3:])        #get the last three char
print(word[3:])         #get all but the three first char
print(word[:-3]+"\n")        #get all but the three last character

#-----------------------------------------------------------------------------

string = "PrOgRaMiZ"
number_of_uppercase_letters = 0
number_of_lowercase_letters = 0
for character in string:
    if character.isupper():
      number_of_uppercase_letters = number_of_uppercase_letters + 1
    elif character.islower():
      number_of_lowercase_letters = number_of_lowercase_letters + 1
print("There are " + str(number_of_uppercase_letters) + " uppercase letters and " + str(number_of_lowercase_letters) + " lowercase letters in the word 'PrOgRaMiZ'")

print(string.lower()) # turn each character of 'PrOgRaMiZ' into lowercase

print(string.upper()) # turn each character of 'PrOgRaMiZ' into uppercase

print() # this split function seperates the words whenever there is a space

words_list = "This will split all words into a list".split()

print(words_list)
words_list[2] = 'combine'
words_list[7] = 'string'
print(' '.join(words_list)) # This function joins the sperated words_list back into a string with modified element

print('Happy New Year'.find('ew')) # print the index where 'ew' is found

print('Happy New Year'.replace('Happy','Brilliant') + "\n-----------------------------------------------------------------------------") # replaces 'Happy' with 'Brilliant'

#-----------------------------------------------------------------------------

# Using isalpha(), isalnum(), isdecimal(), isspace(), and istitle()
def analysis_of_each_character(sentence):
  for character in sentence:
    if character.istitle():
        print('\"' + character + '\" is a titlecased string')
    elif character.isdecimal():
        print('\"' + character + '\" is a number')
    elif character.isspace():
        print('\"' + character + '\" is a space!')
    elif not character.isalnum():
        print('\"' + character + '\" is not an alpha numeric character')

sentence = "My name is Owen, I am 13, and it is almost Christmas."
analysis_of_each_character(sentence)

#-----------------------------------------------------------------------------

str = str(input("Enter a string"))
  
# Printing the original string 
print ("The original string is : \n", str, "\n") 
  
# Printing the center aligned string  
print ("The center aligned string is : ") 
print (str.center(40), "\n") 
  
# Printing the center aligned  
# string with fillchr 
print ("Center aligned string with fillchr: ") 
print (str.center(40, '#')) 

# Printing the left aligned  
# string with "-" padding  
print ("The left aligned string is : ") 
print (str.ljust(40, '-')) 

# Printing the right aligned string 
# with "-" padding  
print ("The right aligned string is : ") 
print (str.rjust(40, '-')) 

#-----------------------------------------------------------------------------

string = ' xoxo heart xoxo   '

# Spaces are removed
print(string.strip())

print(string.strip(' xoxoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('sti'))

string = 'android is awesome and apple sucks'
print(string.strip('and')) # The and in the middle does not get removed


website = 'https://www.programiz.com/     https:'
print(website.lstrip('https:')) # The ending 'https: does not get removed'
print(website.rstrip('https:')) # The beginning 'https: does not get removed'