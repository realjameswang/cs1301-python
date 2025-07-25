#Write a function called average_file. average_file should
#have one parameter: a filename.
#
#The file should have an integer on each line. average_file
#should return the average of these integers. However, if
#any of the lines of the file are _not_ integers,
#average_file should return the string "Error reading file!"
#
#Remember, by default, every time you read a line from a
#file, it's interpreted as a string.

4
#Add your function here!
def average_file(filename):
    with open(filename, "r") as input_file:
        total = 0
        lines = 0
        for line in input_file:
        # how to determine the number is integer or not
            line = line.strip()
            try:
                number = int(line)
                total += number
                lines += 1

            except ValueError as e:
                return "Error reading file!"
        if lines == 0:
            return "Error reading file!"
        else:
            avg = total / lines
            return avg
        
        input_file.close()

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 5.0, then Error reading file!
#
#You can select valid_file.txt and invalid_file.txt from
#the dropdown in the top left to preview their contents.
print(average_file("valid_file.txt"))
print(average_file("invalid_file.txt"))