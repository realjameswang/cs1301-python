#Consult this blood pressures chart: http://bit.ly/2CloACs
#
#Write a function called check_blood_pressure that takes two
#parameters: a systolic blood pressure and a diastolic blood
#pressure, in that order. Your function should return "Low",
#"Ideal", "Pre-high", or "High" -- whichever corresponds to
#the given systolic and diastolic blood pressure.
#
#You should assume that if a combined blood pressure is on the
#line between two categories (e.g. 80 and 60, or 120 and 70),
#the result should be the higher category (e.g. Ideal and
#Pre-high for those two combinations).
#
#HINT: Don't overcomplicate this! Think carefully about in
#what order you should check the different categories. This
#problem could be easy or extremely hard depending on the
#order you change and whether you use returns or elifs wisely.


#Add your code here!

def check_blood_pressure(s,d):
    systolic = s
    diastolic = d
    if (s >= 70 and d >= 90) or (s >= 140 and d >= 40):
        return "High"
    elif (s >= 70 and d >= 80) or (s>=120 and d>=40) :
        return "Pre-high"
    elif (s >= 70 and d >= 60) or (s>= 90 and d>=40):
        return "Ideal"
    else:
        return "Low"
      
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: Ideal
test_systolic = 110
test_diastolic = 70

print(check_blood_pressure(test_systolic, test_diastolic))