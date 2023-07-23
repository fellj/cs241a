# Title:      Phone Classes
# Filename:   check06b.py
# Purpose:    Demonstrates inheritance
#             with different phone classes.
# Date:       02/09/2021
###############################################

# Requirements
######################################################################
# Write a class Phone that contains a phone number,
# and then a class SmartPhone that extends the Phone
# class to add an email address according to the following:
# 
# The Phone class should contain three integers for the
# different parts of a phone number.
#
# Here is its class diagram:
# 
# Phone
# area_code : int
# prefix : int
# suffix : int
# prompt_number() : void
# display() : void
#
# The prompt_number method of the Phone class should ask
# the user to enter each element of a phone number.
# 
# The display method of the Phone class should display
# the number in the format "(areaCode)prefix-suffix".
# 
# The SmartPhone class should extend the Phone class and add the following:
# 
# SmartPhone
# email : string
# prompt() : void
# display() : void
# 
# The prompt method of the SmartPhone class should call
# the prompt_number method defined in the base class and
# then additionally prompt for an email address.
# 
# The display method of the SmartPhone class should call
# the display method defined in the base class and then
# display the email address. (Yes, it must call it, and yes,
# they must both be named display.)
# 
# For simplicity, you may again put all of your classes
# in the same file.

# Sample Output
######################################################################
# Phone:
# Area Code: 801
# Prefix: 123
# Suffix: 4567
# 
# Phone info:
# (801)123-4567
# 
# Smart phone:
# Area Code: 208
# Prefix: 867
# Suffix: 5309
# Email: jenny@test.com
# 
# Phone info:
# (208)867-5309
# jenny@test.com
######################################################################
PHONE_TYPE       = "Phone"
SMARTPHONE_TYPE  = "Smart phone"


# Phone Class
#
#
class Phone:
    
    def __init__(self):
        """
        Initialize the
        Phone class.
        """
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0
        self.type = PHONE_TYPE
 
    def prompt_number(self):
        """
        Prompts the user for
        Phone number
        information.
        """
        print("{}:".format(self.type))
        self.area_code      = input("Area Code: ")
        self.prefix         = input("Prefix: ")
        self.suffix         = input("Suffix: ")
         
    def display(self):
        if self.type == PHONE_TYPE:
            print("\nPhone info:")
            print("({}){}-{}\n".format(self.area_code, \
                                         self.prefix, \
                                         self.suffix))
        else:
            print("\nPhone info:")
            print("({}){}-{}".format(self.area_code, \
                                         self.prefix, \
                                         self.suffix))
# Smartphone Class
#
#
class SmartPhone(Phone):
                  
    def __init__(self):
        """
        Initialize the
        SmartPhone class
        inheriting from
        the Phone class.
        """
        # First call the base class version
        super().__init__()
        
        # Specify the type of phone
        self.type = SMARTPHONE_TYPE
        
        # Now define email member variable
        self.email = ""
                  
    def prompt(self):
        """
        Prompt the user
        for the smart
        phone number
        and email
        address.
        """
        self.prompt_number()
        self.email = input("Email: ")
                  
    def display(self):
        """
        Display the SmartPhone
        number and email
        address.
        """
        super().display()
        print("{}".format(self.email))
              
def main():
    """
    Where the phone program
    tasks are carried out.
    """
              
    # In main function, create a Phone object, call its
    # prompt_number method, and then its display method.
    # 
    phone = Phone()
    phone.prompt_number()
    phone.display()
    
    # After that, also in main, create a SmartPhone object,
    # call its prompt method, and then its display method.
    # 
    smart_phone = SmartPhone()
    smart_phone.prompt()
    smart_phone.display()

              
if __name__ == "__main__":
    main()