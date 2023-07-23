# Title:      Paddle Class
# Filename:   paddle.py
# Purpose:    Represents the paddle 
#             in the pong game.
# Date:       02/03/2021
###############################################

# Requirements

# The ball should bounce along the top, left, and bottom edges of the screen.
# If it goes off the right side of the screen, it should be lost.

# If the ball hits the paddle, it should bounce.

# The paddle should be on the right edge of the screen and move up and down with
# the arrow keys. It should not be able to move off the screen.

# The left and right arrow keys should move the paddle down and up.
# They should be able to be held down.

# At the start of the game, and after the ball is lost, it should start at a
# random location along the left edge of the screen, and with a random velocity
# (choose values that seem appropriate to you).

# The user is awarded 1 point for every time they hit the ball with the paddle.
# They lose 5 points for every time they miss.

# The screen is 400 pixels wide by 300 pixels high.

# The ball radius is 10.

# The paddle is 10 pixels wide by 50 pixels high.
# Each move of the paddle should be by 5 pixels.

from point import Point
import arcade
import random

PADDLE_WIDTH    = 10
PADDLE_HEIGHT   = 50
PADDLE_COLOR    = arcade.color.BLACK
PADDLE_DISTANCE = 5

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

class Paddle:
    
    """
    This class represents
    the paddle
    during
    the game.
    
    """
    
    def __init__(self):
        
        obj_type      = "Paddle"
        self.center    = Point(obj_type)
        
    def draw(self):
        """
        Draws the paddle
        at self.center.x
        and self.center.y
        with a width of
        PADDLE_WIDTH and
        a height of
        PADDLE_HEIGHT.
        The color is black.
        """

        arcade.draw_rectangle_filled(self.center.x, self.center.y, \
                                     PADDLE_WIDTH, PADDLE_HEIGHT,  \
                                     PADDLE_COLOR)
    
    def move_up(self):
        """
        Moves the pong paddle up
        along the left edge of
        the screen.
        """
        if self.center.y < SCREEN_HEIGHT - 30:
            self.center.y += PADDLE_DISTANCE
    
    def move_down(self):
        """
        Moves the pong paddle down
        along the left edge of
        the screen.
        """
        if self.center.y > 40:
            self.center.y -= PADDLE_DISTANCE

