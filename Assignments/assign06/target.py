# Title:      Target Class
# Filename:   target.py
# Purpose:    Creates the target
#             class to be used in
#             the skeet program.
# Date:       02/11/2021
###############################################
           import math
           import constants
from flyer import Flyer

# Requirements
######################################################################
# For this milestone, you need to first get the provided code to run,
# then implement bullets firing correctly as well as a single "normal"
# target flying across the screen.
# 
# You should recognize that a bullet and a target have many things
# in common, and create a base class with these common elements that
# they can both derive from.
# 
# Thus, at a minimum, you should have the following:
# 
# A base class for flying objects.
# 
# A class for a bullet.
# 
# A class for a target.
# 
# Demonstrate the rifle taking aim and firing bullets in the correct direction.
# 
# Demonstrate bullets flying across the screen.
# 
# Demonstrate a target flying across the screen.
# 
# The following are not specifically required at this point
# (although having them done already would be a great thing!):
# 
# All three types of targets
# 
# Bullets and targets dying when they collide
# 
# Bullets and targets dying when they leave the screen
# 
# Scoring
# 
# 
# Don't forget to make use of the Point and Velocity classes from the Pong project.
# 
# It is much easier to start bullets at the corner of the screen
# (inside the rifle) than at the tip of the barrel, and this will
#  be sufficient as long as the angle is correct.



class Target(Standard, Strong, Safe):
    
    """
    Target class used
    in skeet program
    """
    def __init__(self):
        """
        Initialize a new
        target object
        inheriting from
        the Flyer class.
        """
        super().__init__()
        
        # Randomly Create Target
        
        self.type = constants.TARGET_TYPE_STANDARD
        
        

    def fire(self, angle):
        """
        Discharges the
        bullet from the
        rifle object.
        """
        self.velocity.dx = math.cos(angle) * constants.BULLET_SPEED
        self.velocity.dy = math.sin(angle) * constants.BULLET_SPEED
