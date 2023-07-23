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


class MediumAsteroid(Asteroid):
    """
    Initializes a medium
    asteroid.
    """
    def __init__(self, break_speed):
        super().__init__()
        self.img       = "images\meteorGrey_med1.png"
        self.texture   = arcade.load_texture(self.img)
        self.height    = self.texture.height
        self.width     = self.texture.width
        self.radius    = constants.MEDIUM_ROCK_RADIUS
        self.speed     = constants.BIG_ROCK_SPEED
        self.center.x  = random.randint(1, 50)
        self.center.y  = random.randint(1, 150)        
        self.direction = random.randint(1, 50)

        # Set initial velocity based on direction and speed attributes
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed 
        self.velocity.dy = math.sin(math.radians(self.direction)) * (self.speed + break_speed)




