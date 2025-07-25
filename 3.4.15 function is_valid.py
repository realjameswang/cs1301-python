#There are a lot of use cases where we want to check to see
#if a string has any invalid characters in it. For example,
#when asking for a credit card number, we want to make sure
#there are no non-numerals (although we might accept dashes
#or spaces). When asking for a name, we want to make sure
#all the characters are letters, spaces, or the occasional
#punctuation mark.
#
#Write a function called is_valid. is_valid should take two
#parameters: a string to check, and a string of all valid
#characters.
#
#is_valid should return the boolean True if all the
#characters in the string to check are present in the string
#of valid characters. It should return False if any character
#in the checked string does not appear.


#Add your code here!
def is_valid(string_to_check, valid_characters):
    num_of_invalid = 0
    for i in string_to_check:
        # If i is in valid_characters
        # Which means as long as i is in valid_characters, it will print TRUE
        # We want to validate if invalid numbers exist, whether there are one, or two, or three
        # As long as the number of invalid numbers is > 0, invalid number exists, ---> return False
        # else ---> return True
        if i not in valid_characters:
            # for every i in the loop, if i is not in the valid list, then it's invalid
            # num_invalid will add 1 everytime when there is an invalid number
            num_of_invalid += 1
    
    # if the number of invalid number is great than 1
    # it means the there is invalid characters, thus return False
    if num_of_invalid >0:
        return False
    # if the number of invalid number is 0
    # if means there isn't invalid characters, thus return True
    else:
        return True

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print True, then False
sample_valid_string = "1234-5678-9011-1111"
sample_invalid_string = "1234!5678.9011?1111"
valid_characters = "0123456789-"

print(is_valid(sample_valid_string, valid_characters))
print(is_valid(sample_invalid_string, valid_characters))