#You've been sent a list of names. Unfortunately, the names
#come in two different formats:
#
#First Middle Last
#Last, First Middle
#
#You want the entire list to be the same. For this problem,
#we'll say you want the entire list to be First Middle Last.
#
#Write a function called name_fixer. name_fixer should have two
#parameters: an output filename (the first parameter) and the
#input filename (the second parameter). You may assume that every
#line will match one of the two formats above: either First Middle
#Last or Last, First Middle. 
#
#name_fixer should write to the output file the names all
#structured as First Middle Last. If the name was already structured
#as First Middle Last, it should remain unchanged. If it was
#structured as Last, First Middle, then Last should be moved
#to the end after a space and the comma removed.
#
#The names should appear in the same order as the original file.
#
#For example, if the input file contained the following lines:
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray
#
#...then the output file should contain these lines:
#David Andrew Joyner
#Melissa Joan Hart
#Billy Ray Cyrus


#Add your code here!
def name_fixer(output_filename, input_filename):
    
    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()
    
    with open(output_filename, "w") as output_file:
        correct_name = []
        for line in lines:
            if "," in line:
                words = line.split(",") # split line -> line become a list of words
                last_name = words[0] 
                first_name = words[1].strip()
                correct_name = [first_name, last_name]
                correct_name2 = " ".join(correct_name)
                output_file.write(correct_name2+"\n")        
            else:
                output_file.write(line)
        output_file.close()
        


#The code below will test your function. You can find the two
#files it references in the drop-down in the top left. If your
#code works, output_file.txt should have the text:
#David Andrew Joyner
#Melissa Joan Hart
#Billy Ray Cyrus
name_fixer("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")

#If you accidentally erase input_file.txt, here's its original
#text to copy back in (remove the pound signs):
#David Andrew Joyner
#Hart, Melissa Joan
#Cyrus, Billy Ray