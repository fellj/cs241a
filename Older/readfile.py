# Title:   Checkpoint 02b
# Name:    readfile.py
# Purpose: Reading from a file
# Date:    01/12/21
###################################################

########################################################
# Requirements:
#                (1) Read a file for input.
#
#                (2) The file should have 3 lines
#                    and 10 words
#
#                (3) Open and read the file and
#                    report the number of lines
#                    and words
########################################################

# The path of the file for input
file_path = r'J:\John\Programming\Thonny\CS241\file1.txt'

# The data read from the file
read_data = ''

# Open the input file and read the
# number of lines and words
with open(file_path) as file:
    read_data = file.read()
    
# Print the contents of the file
#print(read_data)

# Count the number of lines
lines = read_data.split("\n")
num_lines = len(lines)

# Count the number of words
num_words = 0
for line in lines:
    num_words += len(line.split(" "))

# Report the results
print ("The files contains " + str(num_lines) + " lines and " + str(num_words) + " words.\n")
                
                

