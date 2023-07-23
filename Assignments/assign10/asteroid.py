# Title:      Asteroid Base Class
# Filename:   asteroid.py
# Purpose:    Creates an abstract base
#             class for asteroid
#             objects to be used in
#             the asteroid program.
# Date:       02/27/2021
###############################################
import arcade
import constants
import math
from flyer import Flyer
from abc import ABC

# Requirements
######################################################################

class Asteroid(Flyer, ABC):
    
    """
    Abstract Base class that defines
    important properties
    of asteroids.
    """
    
    def __init__(self):
        """
        Initializes the
        asteroid.
        """
        super().__init__()
        self.points        = 1                  # Number of points per asteroid
        self.spin          = 0                  # Spin rate
        
    def hit(self):
        """
        When the asteroid
        gets hit by a bullet.
        """
        pass
    
    def rotate(self):
        """
        When the asteroid
        rotates.
        """
        self.angle += self.spin
        
    def advance(self):
        """
        Moves and
        rotates the
        asteroid.
        """
        super().advance()
        self.rotate()
        