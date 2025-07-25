#Write a function called get_grade that will read a
#given .cs1301 file and return the student's grade.
#To do this, we would recommend you first pass the
#filename to your previously-written reader() function,
#then use the list that it returns to do your
#calculations. You may assume the file is well-formed.
#
#A student's grade should be 100 times the sum of each
#individual assignment's grade divided by its total,
#multiplied by its weight. So, if the .cs1301 just had
#these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
#Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


#Write your function here!
def reader(filename):
    with open(filename, "r") as input_file:
        new_list = []
        for lines in input_file:
            new_lines = lines.split()
            a = int(new_lines[0])
            b = str(new_lines[1])
            c = int(new_lines[2])
            d = int(new_lines[3])
            e = float(new_lines[4])
            
            aTuple = (a,b,c,d,e)
            new_list.append(aTuple)

        return new_list    
    
    input_file.close()

def get_grade(filename):
    new_list = reader(filename)
    sum = 0 
    for item in new_list:
        grade = item[2]
        total = item[3]
        weight = item[4]
        
        sum += (grade / total) * weight
        
    sum2 = sum * 100
        
    return sum2         

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 91.55 
print(get_grade("sample.cs1301"))