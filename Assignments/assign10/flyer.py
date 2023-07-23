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
import math
from velocity import Velocity
from point import Point
from abc import ABC

# Requirements
######################################################################

class Flyer(ABC):
    
    """
    Base class that defines
    important properties
    of flying objects.
    """
    
    def __init__(self):
        """
        Initializes the
        flying object.
        """
        self.center        = Point()                        # The x and y location of the flying object
        self.velocity      = Velocity()                     # Velocity of the flying object
        self.radius        = 0.0                            # Radius of the flying object
        self.alive         = True                           # Determines if the flying object is alive
        self.direction     = 0.0                            # Direction of the flying object
        self.angle         = 0                              # Angle of the flying object
        self.speed         = 0                              # Speed of the flying object
        self.img           = ""                             # Path to image file
        #self.texture       = arcade.load_texture(self.img) # Texture for arcade image
        self.height        = 0                              # Height in pixels of the image
        self.width         = 0                              # Width in pixels of the image


        
    def is_off_screen(self, screen_width, screen_height):
        """
        Determines if the
        flying object is
        off the screen.
        """
        if self.center.x > screen_width and self.center.y > screen_height:
            return True
            
        
  
    def draw(self):
        """
        Draws the
        flying object
        on the screen.
        """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle,
                                      constants.OBJECT_ALPHA)


    def advance(self):
        """
        Advances the
        flying object
        across the screen.
        """
        self.wrap()
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        
    def is_alive(self):
        """
        Returns the boolean
        attribute 'alive' checking
        if the flying object
        is alive.
        """
        return self.alive
    
    def wrap(self):
        """
        Moves flying
        object to
        other side of
        screen if
        it moves off
        of the screen.
        """
        if self.center.x > constants.SCREEN_WIDTH:
            self.center.x -= constants.SCREEN_WIDTH
        if self.center.x < 0:
            self.center.x += constants.SCREEN_WIDTH
        if self.center.y > constants.SCREEN_HEIGHT:
            self.center.y -= constants.SCREEN_HEIGHT
        if self.center.y < 0:
            self.center.y += constants.SCREEN_HEIGHT