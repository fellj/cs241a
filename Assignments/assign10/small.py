# Title:      Small Asteroid Class
# Filename:   small.py
# Purpose:    Creates a
#             class for a
#             small asteroid
#             object to be used in
#             the asteroid program.
# Date:       03/13/2021
###############################################
import arcade
import constants
import math
import random
from asteroid import Asteroid


class SmallAsteroid(Asteroid):
    """
    Initializes a small
    asteroid.
    """
    def __init__(self, rock, order):
        super().__init__()
        self.img       = "images\meteorGrey_small1.png"
        self.texture   = arcade.load_texture(self.img)
        self.height    = self.texture.height
        self.width     = self.texture.width
        self.radius    = constants.SMALL_ROCK_RADIUS
        self.speed     = constants.BIG_ROCK_SPEED 
        self.center.x  = rock.center.x
        self.center.y  = rock.center.y
        self.direction = rock.direction
        self.spin      = constants.SMALL_ROCK_SPIN
        self.type      = constants.ASTRD_SM_TYPE
        
        
        if order == 1:
            # The small asteroid has the original velocity
            # plus 5 pixels/frame to the right.
            self.velocity.dx = rock.velocity.dx + constants.SMALL_ROCK_DX1
            self.velocity.dy = rock.velocity.dy
            
        elif order == 2:
            # The small asteroid has the same velocity as the
            # original medium one plus 1.5 pixels/frame up and
            # 1.5 pixels/frame to the right.
            self.velocity.dx = rock.velocity.dx + constants.SMALL_ROCK_DXY2
            self.velocity.dy = rock.velocity.dy + constants.SMALL_ROCK_DXY2
            
        else:
            # The second, 1.5 pixels/frame down and 1.5 to the left.
            self.velocity.dx = rock.velocity.dx - constants.SMALL_ROCK_DXY2
            self.velocity.dy = rock.velocity.dy - constants.SMALL_ROCK_DXY2


    def hit(self):
        """
        Updates the score
        and breaks up a 
        large asteroid into
        smaller asteroids.
        """

        self.alive = False
        return self.points
    
    


