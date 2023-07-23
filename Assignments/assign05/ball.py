# Title:      Ball Class
# Filename:   ball.py
# Purpose:    Represents the ball being
#             struck by the paddle.
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
from velocity import Velocity
import arcade
import random


# Constants
BALL_RADIUS = 10
BALL_COLOR = arcade.color.GREEN
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
RESTART_LEFT_SIDE = 375

class Ball:
    
    """
    This class represents
    the ball
    during
    the game.
    
    """
    
    def __init__(self):
        """
        Initializes the
        ball object.
        """
        obj_type      = "Ball"
        self.center   = Point(obj_type)
        self.velocity = Velocity()
        

        
    def draw(self):
        """
        Draws the
        ball at
        position self.center.x,
        self.center.y
        with a radius of
        BALL_RADIUS and
        a color of
        BALL_COLOR.
        (See global constants.)
        """
        arcade.draw_circle_filled(self.center.x, self.center.y, BALL_RADIUS, BALL_COLOR)


    def advance(self):
        """
        Moves the ball
        across the
        screen.
        """

        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy


        
    def bounce_horizontal(self):
        """
        Moves the ball
        horizontally
        
        """
        self.velocity.dx *= -1

    def bounce_vertical(self):
        """
        Moves the ball
        vertically
        
        """
        self.velocity.dy *= -1
        

    def restart(self):
        """
        Places the ball at
        a random location
        along the left
        edge of the
        screen
        after restarting
        game play.
        """
 
        self.center.x = random.uniform(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS)
        self.center.y = random.uniform(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS)

        
    def draw_xy(self):
        """
        Puts the current Location on the screen
        """
        x_text = "X: {}".format(round(self.center.x, 2))
        y_text = "Y: {}".format(round(self.center.y, 2))
        start_x = 20
        start_y = SCREEN_HEIGHT - 80
        arcade.draw_text(x_text + "\n" + y_text, start_x=start_x, start_y=start_y, \
                         font_size=12, color=arcade.color.NAVY_BLUE)

    def draw_dxdy(self):
        """
        Puts the current
        velocity on the screen
        """
        x_text = "dX: {}".format(round(self.velocity.dx, 2))
        y_text = "dY: {}".format(round(self.velocity.dy, 2))
        start_x = 80
        start_y = SCREEN_HEIGHT - 80
        arcade.draw_text(x_text + "\n" + y_text, start_x=start_x, start_y=start_y, \
                         font_size=12, color=arcade.color.RED)