#Create a function called tup_to_dict. tup_to_dict should take one
#parameter: a list of tuples. You can assume each tuple in
#the list has exactly two values.
#
#The function should return a dictionary where the first item
#in each tuple is the key, and the second item in each tuple
#is the corresponding value.
#
#For example:
# colors = [("turquoise", "#40E0D0"), ("red", "#990000")]
# tup_to_dict(colors) -> {"turquoise":"#40E0D0", "red":"#990000"}
#
#Hint: the previous exercise is very similar; this just turns
#it into a function! All our tuples will be color name-color
#value pairs.


#Write your function here!
def tup_to_dict(list_of_tuples):
    #(a,b)
    color_tuples = {}
    
    for color_tuple in list_of_tuples:
        color_name = color_tuple[0]
        color_value = color_tuple[1]
        color_tuples[color_name] = color_value
    return color_tuples

#ta_dict = {ta_info[0][0]: ta_info[0][1], ta_info[1][0]: ta_info[1][1], ta_info[2][0]: ta_info[2][1]}

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:  {'Turquoise':'#40E0D0', 'Red':'#990000'}
#
#Don't worry if it prints those in the reverse order; that's
#still correct!
print(tup_to_dict([("Turquoise", "#40E0D0"), ("Red", "#990000")]))