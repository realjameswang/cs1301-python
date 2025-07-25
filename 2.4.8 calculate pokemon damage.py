STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#In the Pokemon game franchise, damage is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@DamageCalc.png
#
#In that formula, the variable Modifier is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png
#
#Add code below such that the program prints the total damage
#caused based on the STAB, Type, Critical, Other, Random,
#Level, Attack, Defense, and Base given above.
#
#Hint: Don't try to do all these calculations at once! Break
#the complicated formual down into bite-sized little chunks.


#Add your code here!
stab1 = STAB
type1 = Type
critical1 = Critical
other1 = Other
random1 = Random
level1 = Level
attack1 = Attack
defense1 = Defense
base1 = Base

modifier = stab1 * type1 * critical1 * other1 * random1
damage = (((2*level1+10)/250)*(attack1/defense1)*base1+2)*modifier
print(damage)