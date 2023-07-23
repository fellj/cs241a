# Title:      Rifle Class
# Filename:   rifle.py
# Purpose:    Creates the rifle
#             class to be used in
#             the skeet program.
# Date:       02/12/2021
###############################################
import constants
import arcade

# Requirements
######################################################################
# Rifle

# Rendered as a rectangle.

# The aim is controlled to match the mouse cursor.
class Rifle:
    """
    Rifle class
    for the skeet
    program.
    """

    def __init__(self):
        """
        Initialize the
        rifle class.
        """
        self.color  = constants.RIFLE_COLOR
        self.height = constants.RIFLE_HEIGHT
        self.width  = constants.RIFLE_WIDTH
        self.angle  = 0.0
        
    def draw(self):
        """
        Draws the
        rifle object.
        """
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.width,
                                    self.height, self.color)