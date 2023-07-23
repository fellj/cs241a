# Title:      Velocity Class
# Filename:   velocity.py
# Purpose:    To aid in moving
#             flying objects.
# Date:       02/03/2021
###############################################



class Velocity:
    
    """
    This class keeps track
    of the speed of
    flying objects
    during the game.
    
    """
    
    def __init__(self):
        
        self.dx = 0.0
        self.dy = 0.0
        