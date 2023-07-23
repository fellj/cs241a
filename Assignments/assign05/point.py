# Title:      Point Class
# Filename:   point.py
# Purpose:    To aid in locating the ball and
#             the paddle.
# Date:       02/03/2021
###############################################

# Requirements

# The ball should bounce along the top, left, and bottom edges of the screen.
# If it goes of the right side of the screen, it should be lost.

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
import random

SCREEN_WIDTH    = 400
SCREEN_HEIGHT   = 300
BALL_RADIUS     = 10
PADDLE_WIDTH    = 10
PADDLE_HEIGHT   = 50
PADDLE_START_X  = 350

class Point:
    
    """
    This class keeps track
    of the location of
    the pong during
    the game.
    
    It will be used by
    the ball and paddle
    classes.
    """
    
    def __init__(self, obj_type):
        
        if obj_type == "Ball":
            self.x = random.randrange(BALL_RADIUS, SCREEN_WIDTH - BALL_RADIUS)
            self.y = random.randrange(BALL_RADIUS, SCREEN_HEIGHT - BALL_RADIUS)
        else:
            self.x = PADDLE_START_X
            self.y = random.randrange(PADDLE_HEIGHT, SCREEN_HEIGHT - PADDLE_HEIGHT)            