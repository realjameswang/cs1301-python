#Write a function called multiply_strings. Multiply
#strings should have one parameter, a list of strings.
#It should return a modified list according to the
#following changes:
#
# - Every string stored at an even index should be
#   doubled.
# - Every string stored at an index that is a multiple
#   of 3 should be tripled.
# - Every other string should remain unchanged.
#
#These changes should "stack": the string stored at index
#6 should be duplicated six times (2 * 3).
#
#Then, return the new list. You may assume that 0 is a
#multiple of 2 and 3.
#
#Hint: To do this, you need to modify the values of the
#list using their indices, e.g. a_list[1]. If you're not
#using their indices, your answer won't work!


#Write your function here!
def multiply_strings(myList):
    newList = []
    for i in myList:
        if myList.index(i) % 6 == 0:
            i = i * 6
            newList.append(i)
        elif myList.index(i) % 2 == 0:
            i = i * 2
            newList.append(i)
        elif myList.index(i) % 3 == 0:
            i = i * 3
            newList.append(i)
        else:
            newList.append(i)
    return newList

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#['AAAAAA', 'B', 'CC', 'DDD', 'EE', 'F', 'GGGGGG']
test_list = ["A", "B", "C", "D", "E", "F", "G"]
print(multiply_strings(test_list))


