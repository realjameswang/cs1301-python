operation = "*"
first_number = 4
second_number = 7

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#You're doing your math homework when you realize, you can
#write a program to do all the simple operations!
#
#The five possible values for operation are:
#
# - "+": Add first_number and second_number
# - "-": Subtract second_number from first_number
# - "*": Multiply first_number by second_number
# - "/": FLoor-divide first_number by second_number (use //)
# - "%": Find the remainder of dividing first_number by
#        second_number
#
#Your calculator should print the full operation according to
#the following format:
#
#[first_number] [operation] [second_number] = [result]
#
#For example, for the initial values above, your calculator
#would print:
#
#4 * 7 = 28
#
#Notice that for division, we're asking you to use floor
#division to avoid worrying about rounding errors.`
#
##If the operation is not one of the five listed above, print
#"That operation does not exist!" 


#Add your code here!

n1 = first_number
n2 = second_number

add = n1 + n2
subtract = n1 - n2
multiply = n1 * n2
floor = n1 // n2
remainder = n1 % n2

if operation == "+":
    print (n1, operation, n2, "=", add)
elif operation == "-":
    print (n1, operation, n2, "=", subtract)
elif operation == "*":
    print (n1, operation, n2, "=", multiply)
elif operation == "/":
    print (n1, operation, n2, "=", floor)
elif operation in "%":
    print (n1, operation, n2, "=", remainder)
else:
    print ("That operation does not exist!")