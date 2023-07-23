# Title:    Checkpoint 3 b
# Date:     01/18/2021
# Filename: check03b.py
# Purpose: Create a python class for complex
#          numbers, and write methods
#          (member functions) to prompt for
#          them and display them.
# 
# Assignment: Checkpoint 3b - https://bit.ly/3sIPOhO
#
# Associated files: 
#
#############################################

######################################################################################
# Requirements:
######################################################################################
# 
# Create a class for a Complex number that has two member variables, "real" and "imaginary".
#
# Create an initializer function for this class that sets each part to 0.
#
# Create a prompt method (member function) that will prompt the user for the two values and set them appropriately.
#
# Create a display method (member function) that displays the complex number in the form "3 + 4i". For this assignment, you need not worry about handling negative numbers, or about simplifying the display if either value is 0.
#
# Then, in your main function you should create two new complex numbers. Display them (which should show 0 + 0i), prompt the user for each one, and display them again.
#
# To help you see how to work with these values, a main function is provided for you. Your task is to create the Complex class to make this work.
######################################################################################
#
# Example Output
#
######################################################################################
#
# The values are:
# 0 + 0i
# 0 + 0i
#
# Please enter the real part: 3
# Please enter the imaginary part: 4
#
# Please enter the real part: 6
# Please enter the imaginary part: 10
# 
# The values are:
# 3 + 4i
# 6 + 10i
#
######################################################################################
#
#
#
#
# Define the complex number class
# 
class Complex():
    """
    Complex() - This class instantiates a
                new complex number with a
                real and imaginary property.
    """
    def __init__(self):
        """ Create a new complex number."""
        self.real       = 0
        self.imaginary  = 0
            
    # Prompt user for real and imagery 
    # properties of the complex number
    def prompt(self):
        """
        prompt(self) - This member function prompts the
                   user for real and imaginary parts
                   of the complex number.
        """
     
        valid = False
        attempts = 0
        yes_value = "yes"
        no_value  = "no"
        exit_program = no_value
        
        while not valid and not exit_program == yes_value:
            if attempts > 4:
                exit_program = input("\nWould you like to exit the program (yes/no)? ")
            else:
                number_real = str(input("Please enter the real part: "))
            if not number_real.isdigit():
                print ("The first part must be a number.")
                attempts += 1
            else:
                number_imaginary = str(input("Please enter the imaginary part: "))
                if not number_imaginary.isdigit():
                    print ("The imaginary part must be a number.")
                    attempts += 1
                else:
                    # Validate numbers
                    valid = True
                    
                    # Assign input
                    # values to
                    # object properties
                    self.real = number_real
                    self.imaginary  = number_imaginary

    # Display the real and
    # imaginary parts of
    # the complex number
    def display(self):
        """
        display(self) - Member function that displays
                        the real and imaginary parts
                        of the complex number.
                    
        Example Output:

        The values are:
        0 + 0i
        0 + 0i
        
        """
        plus = " + "
        imaginary = "i"
        print(str(self.real) + plus + \
              str(self.imaginary) + \
              imaginary)
           
def main():
    """
    This function tests your Complex class. It should have a prompt
    and a display member function to be called.

    You should not need to change this main function at all.
    """
    c1 = Complex()
    c2 = Complex()

    print("The values are:")
    c1.display()
    c2.display()

    print()
    c1.prompt()

    print()
    c2.prompt()

    print("\nThe values are:")
    c1.display()
    c2.display()

# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()