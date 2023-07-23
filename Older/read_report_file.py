# Title:   Team Activity
# Name:    read_report_file.py
# Purpose: Receive a file from the user and report on its contents
# Date:    01/12/2021
#
# 
##############################################################################

##################################################################
# Requirements: 
# 
#                   (1) Create a function called prompt_filename() that
#                       prompts the user for a filename and returns it.
#                       Create a main() function that calls the 
#                       prompt_filename() function, and displays the text
#                       "Opening file ..." replacing the "..." with the 
#                       actual filename. Then, use the __name__ syntax
#                       to call the initial main() function. Run your
#                       program and ensure that it works correctly.
#
#
#                   (2) Create another function, parse_file() that should
#                       receive a filename from main(). It should then open
#                       the file and read through it line by line and word
#                       by word. For testing purposes, at this point print
#                       out each word in the file at this point.
#
#                   (3) Change your parse_file() function so that it does
#                       not print anything out, but instead counts the
#                       number of times the word "pride" occurs. Have the
#                       function return this number and then change main
#                       to display this to the screen (e.g., "The word
#                       pride occurs xx times in this file").
#
#
##################################################################
# Stretch Challenges (To be completed after team has already
#                    completed the program's requirements)
#
#
#                   (1) Change your program so that it is case insensitive. 
#                       In other words, both "Pride" and "pride" should be    
#                       counted.
#
#                   (2) Change your program so that it can count any word,
#                       not just "pride". Add a function to prompt the user
#                       for the word of their choice, then pass that word
#                       to the parse_file() function and use it when displaying
#                       your results.
#
#                   (3) Change your program so that it counts any words that
#                       contain the user's word as well. For example, if the
#                       user enters "pride" the words "prideful" would both
#                       be counted.
#
#
##################################################################

# This function prompts the user for a filename
def prompt_filename():
    """prompt_filename() - This function prompts the user for the full path of a text file. The return object is the filename path that will be used later. The function verifies the existance of the file. If the user does not enter a valid file after 5 attempts, they are prompted if they would like to exit the program.\n """
    import os.path
 
    valid = False
    attempts = 0
    yes_value = "yes"
    no_value  = "no"
    exit_program = no_value
    while not valid and exit_program != yes_value:
        in_file = str(input("\nPlease enter the full path, including extension, of the filename: "))
        if os.path.isfile(in_file):
            valid = True
            return in_file
        elif attempts > 4:
            exit_program = input("\nWould you like to exit the program (yes/no)? ")
        else:
            print("\nThis is not a valid file path. Please enter a valid file path with extension.")
            attempts += 1
            
# This function reads the input file and displays the contents
def parse_file_first(input_file):
    """parse_file() - This function reads a file and prints the contents for the user."""
    with open(input_file) as file:
        read_data = file.read()
        print (read_data)
        
# This function reads the input file and returns the number of words matching specific criteria
def parse_file_second(input_file):
    """parse_file() - This function reads a file and returns the number of words matching specific criteria."""
    search_word = input("Enter a word to search: ")
    word_counter = 0
    with open(input_file, encoding = 'cp850') as file:
        read_data = file.read()
        words = read_data.split(" ")
        for word in words:
            if search_word in word:
                word_counter += 1
    return word_counter, search_word

# This function reads the input file and returns the number of words matching specific criteria
def parse_file_challenge_1(input_file):
    """parse_file() - This function reads a file and returns the number of words matching specific criteria."""
    search_word = input("Enter a word to search: ")
    search_word_lower = search_word.lower()
    word_counter = 0
    with open(input_file, encoding = 'cp850') as file:
        read_data = file.read()
        lower_data = read_data.lower()
        words = lower_data.split(" ")
        for word in words:
            if search_word_lower in word:
                word_counter += 1
    return word_counter, search_word_lower

# This is the main function that carries out the program's tasks
def main():
    
    # Prompt the user for a file to read
    file_name = prompt_filename()
    
    # Display message opening file
    print("\nOpening file " + file_name + "\n")
    
    # Parse the file
    num_words, find_word = parse_file_challenge_1(file_name)
    
    # Display the number of times
    # the word "pride" is in the
    # file
    print("\nThe word '" + find_word + "' occurs " + str(num_words) + " time(s) in this file.")
    
if __name__ == "__main__":
    main()
