#This is a challenging one! The output will be very long as
#you'll be working on some pretty big dictionaries. We don't
#expect everyone to be able to do it, but it's a good chance
#to test how far you've come!
#
#Write a function called stars that takes in two
#dictionaries:
#
# - movies: a dictionary where the keys are movie titles and
#   the values are lists of major performers in the movie. For
#   example: movies["The Dark Knight"] = ["Christian Bale",
#   "Heath Ledger", "Maggie Gyllenhall", "Aaron Eckhart"]
# - tvshows: a dictionary where the keys are TV show titles
#   and the values lists of major performers in the show.
#   For example: tvshows["Community"] = ["Joel McHale", "Alison
#   Brie", "Danny Pudi", "Donald Glover", "Yvette Brown"]
#
#The function stars should return a new dictionary. The keys
#of the new dictionary should be the performers' names, and
#the values for each key should be the list of shows and
#movies in which that performer has appeared. Sort the shows
#and movies alphabetically.


#Write your function here!
def stars(movies, tvshows):
    finalDict = {}
    for key, values in movies.items():
        for name in values:
        #check if the performer
        #if the name is not in the dictionary
        #we create a new pair in that dictionary
        #if present in dictionary
        #we are not gonna create another entry
        #we add on that value to the existing key
            if name not in finalDict:
                finalDict[name] = []
                finalDict[name].append(key)
            else: #if the name is already in the dictionary
                finalDict[name].append(key)
    for key, values in tvshows.items():
        for name in values:
            if not name in finalDict:
                finalDict[name] = []
                finalDict[name].append(key)
            else:
                finalDict[name].append(key)
    for values in finalDict.values():
        values.sort()
    return finalDict
            
    

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#
#{'Portia de Rossi': ['Arrested Development'], 'Will Ferrell': ['The Lego Movie'], 'Yvette Brown': ['Community'], 'Rebel Wilson': ['How to Be Single'], 'Danny Pudi': ['Community'], 'Elizabeth Banks': ['30 Rock', 'The Lego Movie'], 'Alec Baldwin': ['30 Rock'], 'Alison Brie': ['Community', 'How to Be Single', 'The Lego Movie'], 'Tina Fey': ['30 Rock'], 'Dakota Johnson': ['How to Be Single'], 'Joel McHale': ['Community'], 'Jack McBrayer': ['30 Rock'], 'Tracy Morgan': ['30 Rock'], 'Donald Glover': ['Community'], 'Will Arnett': ['Arrested Development', 'The Lego Movie'], 'Jason Bateman': ['Arrested Development']}

movies = {"How to Be Single": ["Alison Brie", "Dakota Johnson",
                               "Rebel Wilson"],
          "The Lego Movie": ["Will Arnett", "Elizabeth Banks",
                             "Alison Brie", "Will Ferrell"]}
tvshows = {"Community": ["Alison Brie", "Joel McHale",
                         "Danny Pudi", "Yvette Brown",
                         "Donald Glover"],
           "30 Rock": ["Tina Fey", "Tracy Morgan", "Jack McBrayer",
                       "Alec Baldwin", "Elizabeth Banks"],
           "Arrested Development": ["Jason Bateman", "Will Arnett",
                                    "Portia de Rossi"]}
print(stars(movies, tvshows))



