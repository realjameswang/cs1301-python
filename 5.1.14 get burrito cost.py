#Copy your Burrito class from the last exercise. Now, add
#a method called "get_cost" to the Burrito class. It should
#accept zero arguments (except for "self", of course) and
#it will return a float. Here's how the cost should be
#computed:
#
# - The base cost of a burrito is $5.00
# - If the burrito's meat is "chicken", "pork" or "tofu", 
#   add $1.00 to the cost
# - If the burrito's meat is "steak", add $1.50 to the cost
# - If extra_meat is True and meat is not set to False, add
#   $1.00 to the cost
# - If guacamole is True, add $0.75 to the cost
#
#Make sure to return the result as a float even if the total
#is a round number (e.g. for burrito with no meat or
#guacamole, return 5.0 instead of 5).


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
    
    def get_cost(self):
        # - The base cost of a burrito is $5.00
        cost = 5
        meat = self.get_meat()
        
        if meat in ["chicken", "pork", "tofu"]:
            cost += 1
        elif meat == "steak":
            cost += 1.5

        
        if self.get_extra_meat() == True and meat != False:
            cost += 1
        # - If guacamole is True, add $0.75 to the cost
        if self.get_guacamole() == True:
            cost += 0.75
        return cost

            
            

#Below are some lines of code that will test your class.
#You can change the value of the variable(s) to test your
#class with different inputs.
#
#If your function works correctly, this will originally
#print: 7.75
a_burrito = Burrito("pork", False, "white", "black", extra_meat = True, guacamole = True)
print(a_burrito.get_cost())