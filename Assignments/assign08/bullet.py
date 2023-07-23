# Title:      Bullet Class
# Filename:   bullet.py
# Purpose:    Creates the bullet
#             class to be used in
#             the asteroid program.
# Date:       02/11/2021
###############################################
import math
import constants
from flyer import Flyer

# Requirements
######################################################################
# Bullets
# 
# Rendered as a filled-in circle.
# 
# There is no limit to the number of bullets.
# 
# Clicking the mouse fires a new bullet.
# 
# New bullets should be aimed in the direction of the rifle.
# 
# Bullets travel at 10 pixels/frame at that angle at which they are fired.
# 
# Bullets should be removed if they leave the borders of the screen.
# 
# 
# Don't forget to make use of the Point and Velocity classes from the Pong project.
# 
# It is much easier to start bullets at the corner of the screen
# (inside the rifle) than at the tip of the barrel, and this will
#  be sufficient as long as the angle is correct.



class Bullet(Flyer):
    
    """
    Bullet class used
    in skeet program
    """
    def __init__(self):
        """
        Initialize a new
        bullet object
        inheriting from
        the Flyer class.
        """
        super().__init__("Bullet")
        self.color  = constants.BULLET_COLOR
        self.shape  = constants.BULLET_SHAPE
        self.radius = constants.BULLET_RADIUS
        

    def fire(self, angle):
        """
        Discharges the
        bullet from the
        rifle object.
        """
        self.velocity.dx = math.cos(math.radians(angle)) * constants.BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * constants.BULLET_SPEED
        
