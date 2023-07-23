#  Title:   Checkpoint 07 a
#  
#  Author:  John W. Fell, Dr. Burton
#  
#  Date:    02/19/21
#  
#  Purpose: Practice the syntax of abstract base classes,
#           and use these principles to have lists of
#           related objects
#######################################################

# Requirements
#######################################################

# Import anything you need for Abstract Base Classes / methods
from abc import ABC
from abc import abstractmethod

# Convert this to an ABC 


class Shape(ABC):
    
    
    def __init__(self):
        self.name = ""
    
    
    def display(self):
        """
        Abstract display
        method
        """
        print("{} - {:.2f}".format(self.name, self.get_area()))
        


    # Add an abstractmethod here called get_area
    @abstractmethod
    def get_area(self):
        """
        Abstract method
        that retrieves
        the area of the
        shape
        """
        pass

# Create a Circle class here that derives from Shape
class Circle(Shape):
    """
    Circle shape
    class based
    on abstract base
    class Shape
    """
    def __init__(self):
        """
        Constructor for
        circle class
        """
        super().__init__()
        self.name   = "Circle"
        self.radius = 0.0
    
    def get_area(self):
        """
        Method based on
        abstract method
        in Shape class
        """
        return (3.14 * self.radius * self.radius)
    
# Create a Rectangle class here that derives from Shape
class Rectangle(Shape):
    """
    Rectangle shape
    class based
    on abstract base
    class Shape
    """
    
    def __init__(self):
        """
        Constructor for
        rectangle class
        """
        super().__init__()        
        self.name   = "Rectangle"
        self.length = 0.0
        self.width  = 0.0
        
    def get_area(self):
        """
        Method based
        on abstract
        method for
        base class Shape
        """
        return (self.length * self.width)
    
def main():

    # Declare your list of shapes here
    shapes = []

    command = ""

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")

        if command == "c":
            radius = float(input("Enter the radius: "))
            # Declare your Circle here, set its radius, and
            # add it to the list
            circle = Circle()
            circle.radius = radius
            shapes.append(circle)
        
        elif command == "r":
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            # Declare your Rectangle here, set its length
            # and width, and add it to the list
            rectangle = Rectangle()
            rectangle.length = length
            rectangle.width  = width
            shapes.append(rectangle)
            
    # Done entering shapes, now lets print them all out:

    # Loop through each shape in the list, and call its display function
    for shape in shapes:
        shape.display()


if __name__ == "__main__":
    main()


