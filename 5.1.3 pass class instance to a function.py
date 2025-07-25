#This problem uses the same Pet, Owner, and Name classes from
#the previous problem.
#
#In this one, instead of printing a string that lists a single
#pet's owner, you will print a string that lists all of a
#single owner's pets.
#
#Write a function called get_pets_string. get_pets_string should
#have one parameter, an instance of Owner. get_pets_string
#should return a list of that owner's pets according to the
#following format:
#
#David Joyner's pets are: Boggle Joyner, Artemis Joyner

class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.owner.pets.append(self)
        
class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
        
#Add your get_pets_string function here!
def get_pets_string(owner):
    ownerFirstName = owner.name.first
    ownerLastName = owner.name.last
    ownerPets = owner.pets
    pet_list = []
    for pet in ownerPets:
        if pet not in pet_list:
            petFirstName = pet.name.first
            petLastName = pet.name.last
            pet_list.append(petFirstName+" "+petLastName)
    petNames = ", ".join(pet_list)
    result = ownerFirstName + " " + ownerLastName + "'s pets are: " + petNames
    return result
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#David Joyner's pets are: Boggle Joyner, Artemis Joyner
#Audrey Hepburn's pets are: Pippin Hepburn
owner_1 = Owner(Name("David", "Joyner"))
owner_2 = Owner(Name("Audrey", "Hepburn"))

pet_1 = Pet(Name("Boggle", "Joyner"), owner_1)
pet_2 = Pet(Name("Artemis", "Joyner"), owner_1)
pet_3 = Pet(Name("Pippin", "Hepburn"), owner_2)

owner_1.pets.append(pet_1)
owner_1.pets.append(pet_2)
owner_2.pets.append(pet_3)

print(get_pets_string(owner_1))
print(get_pets_string(owner_2))