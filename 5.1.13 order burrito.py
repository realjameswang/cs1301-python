#Copy your Burrito class from the last exercise. Now,
#write a getter and a setter method for each attribute. 
#Each setter should accept a value as an argument. If the 
#value is a valid value, it should set the corresponding 
#attribute to the given value. Otherwise, it should set the 
#attribute to False.
#
#Edit the constructor to use these new setters and getters.
#In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
#new_burrito.meat would be False because "spaghetti" is not
#one of the valid options. Note that you should NOT try to
#check if the new value is valid in both the constructor and
#the setter: instead, just call the setter from the
#constructor using something like self.set_meat(meat).
#
#Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
#Make sure you name each setter with the format: 
#"set_some_attribute" and "get_some_attribute"
#
#For example, the getter for meat would be get_meat. The
#getter for to_go would be get_to_go.
#
#Hint: Your code is going to end up *very* long. This
#will be the longest program you've written so far, but
#it isn't the most complex. Complexity and length are
#often very different!
#
#Hint 2: Checking for valid values will be much easier
#if you make a list of valid values for each attribute
#and check the new value against that.


#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat = False, guacamole = False, cheese = False, pico = False, corn = False):
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    def get_meat(self):
        return self.meat
    def set_meat(self, newMeat):
        if newMeat in ["chicken", "pork", "steak", "tofu", False]:
            self.meat = newMeat
        else:
            self.meat = False
                
    def get_to_go(self):
        return self.to_go
    def set_to_go(self,newTogo):
        if newTogo in [True, False]:
            self.to_go = newTogo
        else:
            self.to_go = False
    
    def get_rice(self):
        return self.rice
    def set_rice(self, newRice):
        if newRice in ["brown", "white", False]:
            self.rice = newRice
        else:
            self.rice = False
                
    def get_beans(self):
        return self.beans
    def set_beans(self, newBeans):
        if newBeans in ["black", "pinto", False]:
            self.beans = newBeans
        else:
            self.beans = False
                
    def get_extra_meat(self):
        return self.extra_meat
    def set_extra_meat(self, newExtraMeat):
        if newExtraMeat in [True, False]:
            self.extra_meat = newExtraMeat
        else:
            self.extra_meat = False
            
    def get_guacamole(self):
        return self.guacamole
    def set_guacamole(self, newGuacamole):
        if newGuacamole in [True, False]:
            self.guacamole = newGuacamole
        else:
            self.guacamole = False
            
    def get_cheese(self):
        return self.cheese
    def set_cheese(self, newCheese):
        if newCheese in [True, False]:
            self.cheese = newCheese
        else:
            self.cheese = False
    
    def get_pico(self):
        return self.pico
    def set_pico(self, newPico):
        if newPico in [True, False]:
            self.pico = newPico
        else:
            self.pico = False
            
    def get_corn(self):
        return self.corn
    def set_corn(self, newCorn):
        if newCorn in [True, False]:
            self.corn = newCorn
        else:
            self.corn = False 
            
#Feel free to add code below to test out the class that
#you've written. It won't be used for grading.


