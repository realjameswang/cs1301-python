mystery_int = 7

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Use a loop to find the sum of all numbers between 0 and
#mystery_int, including bounds (meaning that if
#mystery_int = 7, you add 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7).
#Then, print the sum.
#
#However, there's a twist: mystery_int might be negative.
#So, if mystery_int was -4, you would -4 + -3 + -2 + -1 + 0.
#
#There are a lot of different ways you can do this. Most of
#them will involve using a conditional to decide whether to
#add or subtract 1 from mystery_int.
#
#You may use either a for loop or a while loop to solve this,
#although we recommend using a while loop.

sum = 0

if mystery_int > 0:
    for i in range(0, mystery_int+1):
        sum += i
else:
    for i in range(mystery_int, 0):
        sum += i
print(sum)