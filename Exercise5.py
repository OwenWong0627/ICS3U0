#-----------------------------------------------------------------------------
# Name:        Exercise 5 (Exercise5.py)
# Purpose:     Understading  statement coding in Python
#
# Author:      Owen Wong
# Created:     10/12/2018
# Updated:     10/15/2018
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#First Program
Levels,line,letter,indent = 5,'','',1
spaces = ' '*Levels

for i in range(Levels):
  spaces = spaces[0:Levels-i]
  letter = ''
  for j in range(indent):
    letter += "X"
  line += spaces+letter+'\n'
  indent += 2

print (line)
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#Second Program
while True:
  Question_7 = int(input("What's 1+1?"))
  if Question_7 ==2:
    print("Correct")
    break
  print("Wrong, the answer is not " + str(Question_7))
#-----------------------------------------------------------------------------