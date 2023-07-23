# Title:      Medium Asteroid Class
# Filename:   medium.py
# Purpose:    Creates a
#             class for a
#             medium asteroid
#             object to be used in
#             the asteroid program.
# Date:       03/01/2021
###############################################
import arcade
import constants
import math
import random
from asteroid import Asteroid
from small import SmallAsteroid


class MediumAsteroid(Asteroid):
    """
    Initializes a medium
    asteroid.
    """
    def __init__(self, large_rock, order):
        super().__init__()
        self.img       = "images\meteorGrey_med1.png"
        self.texture   = arcade.load_texture(self.img)
        self.height    = self.texture.height
        self.width     = self.texture.width
        self.radius    = constants.MEDIUM_ROCK_RADIUS
        self.speed     = constants.BIG_ROCK_SPEED
        self.center.x  = large_rock.center.x
        self.center.y  = large_rock.center.y
        self.direction = large_rock.direction
        self.type      = constants.ASTRD_MD_TYPE

        
        if order == 1:
            # The first medium asteroid has the same velocity as the
            # original large one plus 2 pixel/frame in the up direction.
            self.velocity.dx = large_rock.velocity.dx
            self.velocity.dy = large_rock.velocity.dy + constants.MEDIUM_ROCK_DY1
        else:
            # The second medium asteroid has the same velocity as the
            # original large one plus 2 pixel/frame in the down direction.
            self.velocity.dx = large_rock.velocity.dx
            self.velocity.dy = large_rock.velocity.dy - constants.MEDIUM_ROCK_DY1


    def hit(self):
        """
        Updates the score
        and breaks up a 
        large asteroid into
        smaller asteroids.
        """

        self.alive = False
        return self.points
    
    def break_apart(self):
        """
        Medium asteroids
        break apart
        into two small
        asteroids.
        """
        two_small_asteroids = []
        asteroid_sma2 = SmallAsteroid(self, 2)
        asteroid_sma3 = SmallAsteroid(self, 3)        
        two_small_asteroids.append(asteroid_sma2)
        two_small_asteroids.append(asteroid_sma2)
        return two_small_asteroids    
    

