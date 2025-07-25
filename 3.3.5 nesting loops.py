#Imagine if we wanted to print the times tables for the numbers 1
#through 10. In other words, we want to multiply 1 times every number
#from 1 to 10, 2 by every number from 1 through 20, etc. How would we
#do that?
#
#Well, let's look at the phrasing: for every number from 1 to 10, we
#want to multiply it by every number from 1 to 10. Notice the word
#'every' is twice in that description. 'Every' is one of those words
#that gives away the need for a loop. So, it sounds like we're going
#to need two loops! Note also that the second loop is running through
#the numbers 1 to 10 for every number in the first loop.
#
#So, what would this look like?

print("First Example:")

#For every number from 1 to 10...
for i in range(1, 11):
    #For every number from 1 to 10...
    for j in range(1, 11):
        #Print the product of the two numbers.
        print(i, "times", j, "equals", i*j)
        
#Notice that the loop on line 20 is controlled by the loop on line 18.
#So, each iteration of the loop on line 18, the loop on line 20 runs
#10 times.
#
#That's an ugly flat list, though. What if we wanted to print them more
#like an actual table? We can do that! We just have to make use of a
#trick we haven't quite learned... you'll do that later!