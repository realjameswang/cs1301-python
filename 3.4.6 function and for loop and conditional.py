#Write a function called lucky_sevens that takes in one
#parameter, a string variable named a_string. Your function
#should return True if there are exactly three '7's in
#a_string. If there are less than three or more than three
#'7's, the function should return False.
#
#For example:3
#  - lucky_sevens("happy777bday") should return True.
#  - lucky_sevens("h7app7ybd7ay") should also return True.
#  - lucky_sevens("happy77bday") should return False.
#  - lucky_sevens("h777appy777bday") should also return False.
#
#Hint: Remember in Chapter 3.3, we covered how to use a loop
#to look at each character in a string.
def lucky_sevens(a_string):
    num = 0

    for i in a_string:
        if i == str(7):
            num += 1    
    if num == 3:
        return True
    else:
        return False

#Write your function here!



#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, each on their own line.
print(lucky_sevens("happy777bday"))
print(lucky_sevens("h7app7ybd7ay"))
print(lucky_sevens("happy77bday"))
print(lucky_sevens("h777appy777bday"))




