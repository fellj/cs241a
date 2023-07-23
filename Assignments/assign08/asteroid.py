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
        self.radius        = 0.0                  # Radius of the flying object

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
        self.center.x += math.cos(math.radians(self.angle)) * self.speed
        self.center.y += math.cos(math.radians(self.angle)) * self.speed
