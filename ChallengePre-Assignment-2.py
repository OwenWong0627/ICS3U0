#-----------------------------------------------------------------------------
# Name:        Challenge 2 (Challenge2.py)
# Purpose:     File writing
#
# Author:      Owen Wong
# Created:     12/22/2018
# Updated:     01/08/2019
#-----------------------------------------------------------------------------
import re
# TODO: What do I do with the punctuations and \n
# TODO: If i remove the \n's what do I need with the empty strings
# TODO: Ordering specifications?

def getAllWords(fileContent):
    all_words = []
    for line in fileContent:
        for word in line.split(' '):
            all_words.append(word)
    return all_words

def addAllNumbers(fileContent):
    compiled_number = 0
    for line in fileContent:
        for character in line:
            if character.isdecimal():
                compiled_number += int(character)
    return compiled_number

def countVowels(fileContent):
  vowels = list('aeiou')
  vowel_count = 0
  for line in fileContent:
    print(line)
    for character in line:
      if character.lower() in vowels:
       vowel_count += 1
  return vowel_count

def countConsonants(fileContent):
    consonant_count = 0
    for line in fileContent:
        consonant_count += len(re.findall('(?i)[bcdfghjklmnpqrstvwxyz]', line))
    return consonant_count

def countNonAlpha(fileContent):
    non_alpha_count = 0
    for line in fileContent:
        for character in line:
            if not character.isalpha():
                non_alpha_count += 1
    return non_alpha_count

def findLastLetter(fileContent):
    last_letter = []
    for line in fileContent:
        if line.endswith('\n'):
            if line == '\n':
                # TODO: what should the last letter be if there is an empty line?
                last_letter.append(line[-1])
            else:
                last_letter.append(line[-2])
        else:
            # TODO: Punctuations count as the last letter?
            last_letter.append(line[-1])
    return last_letter

def removeNewLines(fileContent):
    no_newline_file = []
    for line in fileContent:
        no_newline_file.append(line.strip('\n'))
    file = open('hamlet-no-newline.txt', 'w')
    file.write(''.join(no_newline_file))
    file.close()

def sortAlphaLines(fileContent):
    # TODO: Should empty lines or quotations be counted?
    hamlet_alpha_by_line = sorted(fileContent, reverse = False, key=str.lower)
    file = open('hamlet-alpha-by-line.txt', 'w')
    file.write(''.join(hamlet_alpha_by_line))
    file.close()

# TODO: Does the new list include \n's or should I remove them?
# TODO: Is the order by ASCII code order where capital letters go first or 
# is it ordered so that the new list order is case-insensitive?
def sortAlphaWords(fileContent):
    sorted_words = []
    for word in getAllWords(fileContent):
        if '\n' in word:
            sorted_words.append(word)
        else:
            sorted_words.append(word+'\n')
    sorted_words.sort(key=str.lower)
    file = open('hamlet-alpha-by-word.txt', 'w')
    file.write(''.join(sorted_words))
    file.close()

def groupWordsByLetter(fileContent):
    dictionary = {}
    alphabet = 'abcdefghijklmnopqrsuvwxyz'
    for letter in alphabet:
        dictionary[letter] = []
    for word in getAllWords(fileContent):
        first_char = word[0].lower()
        if first_char in alphabet:
            dictionary[first_char].append(word)
    return dictionary

def frequencyOfLetter(fileContent, letter):
    frequency = 0
    for line in fileContent:
        for character in line:
            if character == letter:
                frequency += 1
    return frequency

# c:/Users/Owen/Documents/src/cs11/challenge2/hamlet.txt
file = open("hamlet.txt", 'r')
fileContents = file.readlines()
file.close()
# print(addAllNumbers(fileContents))
print(countVowels(fileContents))
print(countConsonants(fileContents))
print(countNonAlpha(fileContents))
# print(findLastLetter(fileContents))
# removeNewLines(fileContents)
# sortAlphaLines(fileContents)
# sortAlphaWords(fileContents)
# print(groupWordsByLetter(fileContents))
# print(frequencyOfLetter(fileContents, "E"))