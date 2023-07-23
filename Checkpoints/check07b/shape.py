"""
Abstract Base Class: Shape
"""
from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    
    
    def __init__(self):
        self.name = ""
    
    
    def display(self):
        """
        Abstract display
        method
        """
        print("{} - {:.2f}".format(self.name, self.get_area()))
        
    @abstractmethod
    def get_area(self):
        """
        Abstract method
        that retrieves
        the area of the
        shape
        """
        pass