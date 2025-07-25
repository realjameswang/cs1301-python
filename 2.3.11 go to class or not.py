exam = False
sunny = False
sunblock = False
morning_classes = True
night_classes = True
raining = False
rain_jacket = True
snowing = False
friends_are_going = True
fluffy_coat = False
snow_boots = True
really_want_to_go = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you commute to your classes and want to write code to 
#determine when it is appropriate for you to go to class based
#on the following conditions:
#
# - If you have an exam, then you should go to class, regardless
#   of the weather.
# - If you do not have an exam and it is sunny outside, then you
#   want to go to class if either of the following are true: you
#   have sunblock  and your classes are in the morning or your
#   classes are at night.
# - If you do not have an exam and it is raining outside, then
#   you want to go to class if you have a rain jacket.
# - If you do not have an exam and it is snowing, then you want
#   to go if any of the following are true: your friends are
#   going and you have a fluffy coat, you have snow boots and a
#   fluffy coat, or you just really want to go to class.

#If none of the previously stated conditions are true, then you
#do not want to go to class.

#Once you have determined if you should go to class, print the 
#following statement without the quotation marks, where "___"
#corresponds to the boolean that you have found:
#"True or false: I should go to class: ___"

#Add your code here! #With the initial inputs, your code
#should print:
#True or false: I should go to class: False

go_to_class = False

if exam:
    go_to_class = True

if sunny and not exam:
    if (sunblock and morning_classes) or night_classes:
        go_to_class = True

if raining and not exam:
    if rain_jacket:
        go_to_class = True

if snowing and not exam:
    if (friends_are_going and fluffy_coat) or (snow_boots and fluffy_coat) or really_want_to_go:
        go_to_class = True

print(f"True or false: I should go to class: {go_to_class}")
