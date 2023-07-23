# Title:      Large Asteroid Class
# Filename:   large.py
# Purpose:    Creates a
#             class for a
#             large asteroid
#             object to be used in
#             the asteroid program.
# Date:       02/27/2021
###############################################
import arcade
import constants
import math
import random
from asteroid import Asteroid
from medium import MediumAsteroid
from small import SmallAsteroid
from abc import ABC

class LargeAsteroid(Asteroid):
    """
    Initializes a large
    asteroid.
    """
    def __init__(self):
        super().__init__()
        self.img       = "images\meteorGrey_big1.png"
        self.texture   = arcade.load_texture(self.img)
        self.height    = self.texture.height
        self.width     = self.texture.width
        self.radius    = constants.BIG_ROCK_RADIUS
        self.speed     = constants.BIG_ROCK_SPEED
        self.spin      = constants.BIG_ROCK_SPIN
        self.center.x  = random.randint(1, 50)
        self.center.y  = random.randint(1, 150)        
        self.direction = random.randint(1, 50)
        self.type      = constants.ASTRD_LG_TYPE

        # Set initial velocity based on direction and speed attributes
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed

    def hit(self):
        """
        Updates the score
        and destroys the 
        large asteroid.
        """

        self.alive = False
        return self.points
    
    def break_apart(self):
        """
        Large asteroids
        break apart
        into two medium
        asteroids
        and one small
        asteroid.
        """
        three_asteroids = []
        asteroid_med1 = MediumAsteroid(self, 1)
        asteroid_med2 = MediumAsteroid(self, 2)
        asteroid_sma1 = SmallAsteroid(self, 1)
        three_asteroids.append(asteroid_med1)
        three_asteroids.append(asteroid_med2)
        three_asteroids.append(asteroid_sma1)
        return three_asteroids