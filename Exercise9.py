#-----------------------------------------------------------------------------
# Name:        Exercise 9 (Exercise9.py)
# Purpose:     Using lists
#
# Author:      Owen Wong
# Created:     11/14/2018
# Updated:     11/19/2018
#-----------------------------------------------------------------------------
list1 = []                      # Empty list
list2 = [1, 2, 3, "cat"]        # A list with mixed item types
list3 = [0.5,1.5,2.5]
list1.append("cat")             # Add a single member, at the end of the list
list1.extend(["dog", "mouse"])  # Add several members
list1.insert(0, "fly")          # Insert at the beginning
list1[0:0] = ["cow", "doe"]     # Add members at the beginning
doe = list1.pop(1)              # Remove item at index 1

if "cat" in list1:              # Test if cat is in list1
  list1.remove("cat")           # Remove the element

if "moose" not in list1:           # Test if moose is not in list1
  list1.append("moose")         # Add moose if moose is not in list1

for item in list1:              # Print everything in list1
  print(item)

print ("Item count:", len(list1)) # Length of list1

for i in range(0, len(list3)):  # Modify each element
  list3[i] += 1                 # Access each element and modifying them

last = list3[-1]                # Last item
print(last)

nextToLast = list3[-2]          # Next-to-last item
print(nextToLast)

empty = False
while empty == False:           # Remove all elements from list2 using a while loop
  del list2[-1]
  if len(list2) == 0:           # Test for emptiness
    empty = True

list4 = ["cat", "dog"]
list5 = list4[:]                # Copy
list4equal5 = list4==list5      # True: same by value
list4refEqual5 = list4 is list5 # False: not same by reference
list6 = list4.copy()            # Copy

print(list6)
del list6[:]                    # Clear a list

list7 = [1, 2] + [2, 3, 4]      # Concatenation

list8 = [list4,list7]           # Joining two lists
def lastchar(list_to_be_modified):
  # Return last element in string.
  return list_to_be_modified[-1]

def addchar(list_to_be_modified):
  # Add an element
  element_to_be_added = int(input("please enter a number"))
  list_to_be_modified.append(element_to_be_added)
  return

print (list1, list2, list3, list4, list5, list6, list7,list8)
print (list4equal5, list4refEqual5)
print (list3[1:3], list3[1:], list3[:2]) # Slices
print (max(list3 ), min(list3 ), sum(list3))
print(lastchar(list3)) # Using the function I created to print the last element in list1
addchar(list1)
print(list1)
