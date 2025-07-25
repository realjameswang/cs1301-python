#Recall that input from a user is always in the form of a string. 
#Write a function called "input_type" that gets user input and 
#determines what kind of string the user entered. The user input
#will be supplied as an argument to the function like normal.
#
#  - Your function should return "integer" if the string only
#    contains characters 0-9.
#  - Your function should return "float" if the string only
#    contains the numbers 0-9 and at most one period.
#  - You should return "boolean" if the user enters "True" or
#    "False". 
#  - Otherwise, you should return "string".

#Write your function here!
def input_type(string):
    x = string.count(".")
    if string == "True" or string == "False":
        return "boolean"
    elif string == "":
        return "string"
    elif string.count(".") >= 1:
        try:
            string = float(string)
            return "float"
        except ValueError as e:
            return "string"
    else:
        try:
            string = int(string)
            return "integer"
        except ValueError as e:
            return "string"
        
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#string
#boolean
#float
#integer
print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("2788"))
