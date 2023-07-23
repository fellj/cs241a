# Title:      Velocity Class
# Filename:   velocity.py
# Purpose:    To aid in moving the ball and
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

class Velocity:
    
    """
    This class keeps track
    of the speed of
    the bullet or target
    during the game.
    
    """
    
    def __init__(self):
        
        self.dx = 0.0
        self.dy = 0.0
        