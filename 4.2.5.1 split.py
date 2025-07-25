#Recall in Unit 3 you wrote a function that would count the
#number of words in a string using loops. Now that you know
#something about string methods, though, let's do that again
#using a different approach.
#
#Write a function called "num_words" that accepts a string 
#as an argument and returns the number of words in the 
#string. You can assume all words are separated by a space,
#and that the string has at least one word. You do not need
#to worry about punctuation.
#
#For example:
#
#  num_words("Veni, Vidi, Vici.") -> 3
#
#This time, you may not use any loops. Hint: split() might
#come in handy.


#Write your function here!
def num_words(my_string):
    my_string = my_string.split(" ")
    return len(my_string)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3, 2, 1, each on their own line.
print(num_words("Vini, Vidi, Vici."))
print(num_words("Hello, world!"))
print(num_words("HeyDavidwhyaren'ttherespacesinthissentence"))


