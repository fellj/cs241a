# Title:      Safe Target Class
# Filename:   safe.py
# Purpose:    Creates the safe 
#             target class to be used 
#             in the skeet program.
# Date:       02/11/2021
###############################################
import constants
import arcade
from standard import Standard

# Requirements
######################################################################
# Safe Target

# Rendered as a square.

# Use the arcade.draw_rectangle_filled function to assist you.

# This target should not be hit.

# It is destroyed with a single hit.

# A penalty of 10 points is incurred if this target is hit.

class Safe(Standard):
    """
    The safe target
    type class.
    """
    
    def __init__(self):
        """
        Initialize the
        safe target
        type instance.
        """
        super().__init__()
        
        self.shape  = constants.TARGET_SHAPE_SAFE
        self.color  = constants.TARGET_COLOR_SAFE
        self.points = constants.TARGET_POINTS_SAFE
        self.width  = constants.TARGET_WIDTH_SAFE
        self.height = constants.TARGET_HEIGHT_SAFE
        