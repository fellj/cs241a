# Title:      Strong Target Class
# Filename:   strong.py
# Purpose:    Creates the strong 
#             target class to be used 
#             in the skeet program.
# Date:       02/11/2021
###############################################
import random
import constants
import arcade
from standard import Standard

# Requirements
######################################################################
# Strong Target

# Rendered as a circle with a number inside of it.

# The strong target should move more slowly than the others as defined below.

# It takes 3 hits to destroy this target.

# 1 point is awarded for each of the first two hits.

# 5 points are awarded for the third hit that destroys the target.

class Strong(Standard):
    """
    Class for the strong
    type of target.
    """

    def __init__(self):
        """
        Initialize the
        strong target
        class.
        """
        super().__init__()
        
        self.speed       = constants.TARGET_SPEED_STRONG
        self.lives       = constants.TARGET_LIVES_STRONG
        
        # To give the user a greater chance to hit
        # the strong target, it should move more
        # slowly than the others. In particular,
        # its horizontal velocity should be taken
        # from the range: 1 to 3, and it's vertical
        # velocity from the range -2 to +3.        
        self.velocity.dx = random.uniform( 1.0, 3.0)
        self.velocity.dy = random.uniform(-2.0, 3.0)

    def draw(self):
        """
        Draw the strong
        target object
        on the screen.
        """
        arcade.draw_circle_filled(self.center.x, self.center.y, (self.radius + 3), self.color)
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, constants.TARGET_COLOR_FOREGRND)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.lives), text_x, text_y, self.color, font_size=constants.TARGET_FONT_STRONG)

 
        
    def advance(self):
        """
        Advances the
        safe target
        type.
        """
        super().advance()
        
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
        For this implementation,
        the strong target type
        adds 5 points instead of 1.
        """
        self.hits  += 1
        self.lives -= 1
        if self.lives < 1:
            self.points = 5
            self.alive = False
        return self.points
        
    def is_off_screen(self, screen_width, screen_height):
        """
        Determines if the
        target is off
        the screen.
        """
        super().is_off_screen(screen_width, screen_height)
