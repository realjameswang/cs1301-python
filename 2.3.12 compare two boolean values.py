a = True
b = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#There are six logical operations to compare two boolean
#values. They are:
#
#  And: True if both are True, False otherwise
#   Or: True if either is True, False otherwise.
#  Xor: True if exactly one is True; False if both are True
#       or both are False ("Exclusive Or")
# Nand: False if both are True, True otherwise.
#  Nor: False if either is True, True otherwise.
# Xnor: False if exactly one is True; True if both are True
#       or both are False.
#
#For a and b above, print the results of all six operations,
#with the following format:
#
#And: False
#Or: True
#Xor: True
#Nand: True
#Nor: False
#Xnor: False
#
#Add your code below! Be aware: there is no dedicated operator
#in Xor, Nand, Nor, or Xnor. You'll have to find those values
#through a combination of And, Or, and Not.

and_ok = a and b
or_ok = a or b
xor_ok = (a or b) and not (a and b)
nand_ok = not (a and b)
nor_ok = not (a or b)
xnor_ok = not ((a or b) and not (a and b))  # same as not xor

print("And:", and_ok)
print("Or:", or_ok)
print("Xor:", xor_ok)
print("Nand:", nand_ok)
print("Nor:", nor_ok)
print("Xnor:", xnor_ok)