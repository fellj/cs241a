#  Title:   Checkpoint 07 a
#  
#  Author:  John W. Fell
#  
#  Date:    02/19/21
#  
#  Purpose: Practice the syntax of polymorphism
#######################################################

# Requirements
#######################################################

# Copy the template file /home/cs241/check07a.py to your working directory.
# 
# Create a class for a Car that has the member variables and methods as
# described above. Notice that the method, get_door_specs() does not print
# the data to the screen, but rather returns it.
# 
# Fill in a default get_door_specs() method that returns the string
# "Unknown doors". In the init funtion, set the name variable to be
# "Unknown model".
# 
# Next create a class Civic that inherits from the Car class and overrides
# the get_door_specs() to return the string "4 doors". In the constructor,
# set the name variable to be "Civic".
# 
# Next create a class Odyssey that inherits from the Car class and overrides
# the get_door_specs() to return the string "2 front doors, 2 sliding doors,
# 1 tail gate". In the constructor, set the name variable to be "Odyssey".
# 
# Next create a class Ferrari that inherits from the Car class and overrides
# the get_door_specs() to return the string "2 butterfly doors". In the
# constructor, set the name variable to be "Ferrari".
# 
# A main function is provided that creates one of each of these cars, and
# passes it to a method called "attach_doors". You need to write this method.
# It should accept any type of car and display the text: "Attaching doors to
# Civic - 4 doors". (Of course, replace "Civic" with the appropriate name, and
# "4 doors" with the result of calling the get_door_specs() method.)
# 
# You must make a single function attach_doors that handles any type of car.
# You cannot have three separate functions or a single function that takes
# three parameters.

# Create a base car class here
class Car:
    """
    Base car
    class
    """
    
    def __init__(self):
        """
        Initialize car
        class
        """
        self.name = "Unknown model"
        

    def get_door_specs(self):
        """
        Return car door
        specifications as
        string
        """
        door_specs = "Unknown doors"
        return door_specss

# Create a civic class here
class Civic(Car):
    """
    Civic car class
    that inherits
    from Car class.
    """
    def __init__(self):
        """
        Initialize
        the civic
        class
        """
        self.name = "Civic"
        
    def get_door_specs(self):
        """
        Overrides
        car class
        get_door_specs
        method.
        """
        door_specs = "4 doors"
        return door_specs
        
# Create an odyssey class here
class Odyssey(Car):
    """
    Odyssey class
    that inherits
    from the Car
    class.
    """
    def __init__(self):
        """
        Constructor for
        Odyssey class
        """
        self.name = "Odyssey"
        
    def get_door_specs(self):
        """
        Overrides the
        get_door_specs
        method in the
        Car class
        """
        door_specs = "2 front doors, 2 sliding doors, 1 tail gate"
        return door_specs
    
# Create a Ferrari class here
class Ferrari(Car):
    """
    Ferrari class
    that inherits
    from the Car
    class.
    """
    def __init__(self):
        """
        Constructor for
        Ferrari class
        """
        self.name = "Ferrari"
        
    def get_door_specs(self):
        """
        Overrides the
        get_door_specs
        method in the
        Car class
        """
        door_specs = "2 butterfly doors"
        return door_specs


# TODO: Create your attach_doors function here
# It should accept any type of car and use its
# name and get_door_specs function to print out
# the necessary data.
# It should not be a member function of any class,
# but rather just a "regular" function.
def attach_doors(car):
    """
    Displays the
    door specs data
    for the type of
    car instance
    passed to the
    method
    """
    print("Attaching doors to {} - {}".format(car.name, car.get_door_specs()))

def main():
    car1 = Civic()
    car2 = Odyssey()
    car3 = Ferrari()

    attach_doors(car1)
    attach_doors(car2)
    attach_doors(car3)

if __name__ == "__main__":
    main()