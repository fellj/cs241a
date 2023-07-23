# Title:      Standard Target Class
# Filename:   standard.py
# Purpose:    Creates the standard 
#             target class to be used 
#             in the skeet program.
# Date:       02/11/2021
###############################################
import constants
import arcade
import random
from flyer import Flyer

# Requirements
######################################################################
# Standard Target

# Rendered as a circle with a 20px diameter.

# Destroyed with one hit.

# 1 point is awarded for hitting it.

# Use the arcade.draw_circle_filled to assist you.

# The target type, direction, velocity, and timing to release (delay)
# are random according to the following constraints:
# 
# The initial position of the target is anywhere along the top half
# of the left side the screen.
# 
# The horizontal component of the velocity should be between 1 and 5 pixels/frame.
# 
# The vertical component of the velocity should be between -2 and +5 pixels/frame.
# 
# To give the user a greater chance to hit the strong target, it should
# move more slowly than the others. In particular, its horizontal velocity
# should be taken from the range: 1 to 3, and it's vertical velocity from
# the range -2 to +3.
# 
# New targets should be created in the "update" function with 1/50 probability.
# This can be achieved by drawing a random number from 1 to 50 and checking if it's 1.
# 
# There is no limit to the number of targets that can be on the screen at a time,
# but they should be removed from the game when they leave the screen.

class Standard(Flyer):
    """
    Class for the
    standard target type.
    """

    def __init__(self):
        """
        Initializes the
        standard target
        type.
        """
        super().__init__("Target")
        
        self.radius      = constants.TARGET_RADIUS
        self.color       = constants.TARGET_COLOR
        self.hits        = 0
        self.points      = 1
        self.shape       = constants.TARGET_BULLET_SHAPE
        self.lives       = 1                    # How many hits can be taken before the flying object dies

        # The horizontal component of the velocity
        # should be between 1 and 5 pixels/frame.
        self.velocity.dx = random.uniform(1.0, 5.0)
        
        # The vertical component of the velocity
        # should be between -2 and +5 pixels/frame.
        self.velocity.dy = random.uniform(-2.0, 5.0)
        
        
    def hit(self):
        """
        Represents the target
        being hit and should
        either kill the target
        (or decrement the number
        of hits remaining for the
        strong target) and return
        an integer representing
        the points scored for
        that hit.
        """
        self.hits += 1
        self.lives -= 1
        if self.lives < 1:
            self.alive = False
        return self.points
    
        