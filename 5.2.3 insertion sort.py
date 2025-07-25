#Recall in the lesson on sorts that we had you complete the
#Bubble and Selection sort, and we showed you Merge sort.
#We didn't show any of insertion sort, and I bet you can
#guess why.
#
#Implement insertion sort below.
#
#Name your function 'insertion'. insertion should take as
#input a list, and return as output a sorted list. Note that
#even though technically a sorting method does not have to
#return the sorted list, yours should.
#
#If you're stuck on where to start, or having trouble
#visualizing or understanding how exactly insertion sort
#works, check out this website - https://visualgo.net/sorting
#It provides a visual representation of all of the sorting
#algorithms as well as pseudocode you can base your own code
#off of.

#Write your code here!
def insertion(myList):
    for i in range(1,len(myList)):
    # using for loop until len(myList)
    # but start from 1 (cause we gonna compare it with i - 1)
        temp = myList[i]
        j = i - 1

        # using while loop cause we wanna compare a condition
        while j >= 0 and temp < myList[j]:
            myList[j+1] = myList[j] #replace every myList[j+1] with [j]
            j -= 1 # until j = 0 OR key > myList [j]
        myList[j+1] = temp # insert temp on array[j+1]     
    
    return myList

#The code below will test your function. If your function
#works, it will print: [1, 2, 3, 4, 5].
print(insertion([5, 1, 3, 2, 4]))

#5 1 3 2 4
#1 5 3 2 4
#1 3 5 (2) 4
# here move 2 to before 3, so comparing 2 against everything before it
#1 (2) 3 5 4
#1 2 3 4 5
