# Title:    Checkpoint 3 a
# Date:     01/18/2021
# Filename: checkpoint03a.py
# Purpose: Create a python class for student
#          and display the first and last
#          names along with the student id.
# Assignment:
#
#
#
#############################################

######################################################################################
# Requirements:
######################################################################################

# Create a class for a Student, that contains a first name, a last name, and an id.

# Create an __init__ function in your class that initializes the first name, last name, and id to "", "", and 0, respectively.

# Create a regular function (not a member function just yet) called prompt_student that creates a new student object, then prompts the user for a first name, last name, and id. The function should assign these to the appropriate properties of the object and return it.

# Create a regular function (not a member function) called display_student that accepts a student object, and displays its information in the following format: "id - FirstName LastName".

# Then, create a main function that does the following:

# Calls the prompt_student function and saves the returned value in a variable called "user".

# Pass the user object to the display_student function to be displayed.

######################################################################################
# Sample Output
#
# The following is an example of output for this program:
#######################################################################################

# Please enter your first name: Ashley
# Please enter your last name: Smith
# Please enter your id number: 12512

# Your information:
# 12512 - Ashley Smith
######################################################################################
######################################################################################


# Create the student class
#class Student(first_name, last_name, student_id):
class Student():
    """Student(first_name, last_name, id): This class instantiates a new student with a first and last name and an id. """

    def __init__(self):
            """ Create a new student."""
            self.first_name = ""
            self.last_name  = ""
            self.student_id = 0
            
# Prompt user for student information and create a new instance of the student class
# This function prompts the user for a filename
def prompt_student():
    """prompt_student() - This function prompts the student information. The function then creates a student object and stores the input into the new instance of the class. """
 
    valid = False
    attempts = 0
    yes_value = "yes"
    no_value  = "no"
    exit_program = no_value
    
    while not valid and exit_program != yes_value:
        if attempts > 4:
            exit_program = input("\nWould you like to exit the program (yes/no)? ")
        else:
            name_first = str(input("Please enter your first name: "))
        if name_first.isdigit():
            print ("The first name may not contain numbers.")
            attempts += 1
        else:
            name_last = str(input("Please enter your last name: "))
            if name_last.isdigit():
                print ("The last name may not contain numbers.")
                attempts += 1
            else:
                id_student = int(input("Please enter your id number: "))
                if not isinstance(id_student, int):
                    print ("The id number must be an integer.")
                    attempts += 1
                else:
                    valid = True


    return_student = Student()
    return_student.first_name = name_first
    return_student.last_name  = name_last
    return_student.student_id = id_student
    
    return return_student

# Display required values for a given student
def display_student(student):
    """display_student(student): - Displays the student object's first and last names with id in the following format: "id - FirstName LastName"."""

    print(str(student.student_id) + " - " + student.first_name + " " + student.last_name)

def main():
    """main() - The main function that executes requirements of the program."""
    user = prompt_student()
    print("\nYour information:")
    display_student(user)
    #print(str(current_student.student_id) + " - " + current_student.first_name + " " + current_student.last_name)

if __name__ == "__main__":
    main()