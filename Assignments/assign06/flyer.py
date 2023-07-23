# Title:      Flyer Class
# Filename:   flyer.py
# Purpose:    Creates a base
#             class for flying
#             objects to be used in
#             the skeet program.
# Date:       02/11/2021
###############################################
import arcade
import constants
from velocity import Velocity
from point import Point

# Requirements
######################################################################

class Flyer:
    
    """
    Base class that defines
    important properties
    of flying objects.
    """
    
    def __init__(self, obj_type):
        """
        Initializes the
        flying object.
        """
        self.center        = Point(obj_type)      # The x and y location of the flying object
        self.velocity      = Velocity()           # Velocity of the flying object
        self.radius        = 0.0                  # Radius of the flying object
        self.alive         = True                 # Determines if the flying object is alive
        
    def is_off_screen(self, screen_width, screen_height):
        """
        Determines if the
        flying object is
        off the screen.
        """
        if self.center.x > screen_width and self.center.y > screen_height:
            self.alive = False
            return True
            
        
        
    def draw(self):
        """
        Draws the
        flying object
        on the screen.
        """
#         print("Target shape: {} \n Target color: {}\n".format(self.shape, self.color))
        if self.shape == constants.TARGET_BULLET_SHAPE:
            arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)

        else:
            arcade.draw_rectangle_filled(self.center.x, self.center.y, self.width, self.height, self.color)

            
    def advance(self):
        """
        Advances the
        flying object
        across the screen.
        """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy        