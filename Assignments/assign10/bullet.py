# Title:      Bullet Class
# Filename:   bullet.py
# Purpose:    Creates the bullet
#             class to be used in
#             the asteroid program.
# Date:       02/11/2021
###############################################
import math
import constants
import arcade
from flyer import Flyer

# Requirements
######################################################################
# Pressing space bar will shoot a bullet.
# 
# Bullets are should start with the same velocity of the
# ship (speed and direction) plus 10 pixels per frame in
# the direction the ship is pointed. This means if the
# ship is traveling straight up, but pointed directly to
# the right, the bullet will have a velocity that is at
# an angle up and to the right (starting with an upward
# velocity from the ship, and adding to it a velocity to
# the right because of the direction the ship is pointed).
# 
# There is no limit to the number of bullets that can be fired.
# 
# Bullets only live for 60 frames, after which they should "die"
# and be removed from the game.
# 
# For collision detection, you can assume that bullets have a radius of 30
# 

class Bullet(Flyer):
    
    """
    Bullet class used
    in skeet program
    """
    def __init__(self):
        """
        Initialize a new
        bullet object
        inheriting from
        the Flyer class.
        """
        super().__init__()
        self.img      = "images\laserBlue01.png"
        self.texture  = arcade.load_texture(self.img)
        self.width    = self.texture.width
        self.height   = self.texture.height
        self.radius   = constants.BULLET_RADIUS
        self.distance = 0


    def spawn(self, ship):
        """
        Assigns the properties
        of the bullet in relation
        to the location, angle, and
        velocity of the ship
        """
        self.angle       = ship.angle + constants.ROTATE_OFFSET
        self.center.x    = ship.center.x
        self.center.y    = ship.center.y
        self.velocity.dx = ship.velocity.dx
        self.velocity.dy = ship.velocity.dy

                


    def fire(self):
        """
        Discharges the
        bullet from the
        rifle object.
        """
        self.velocity.dx = math.cos(math.radians(self.angle)) * constants.BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(self.angle)) * constants.BULLET_SPEED
        
    def advance(self):
        """
        Moves the bullet
        across the screen
        and kills the bullet
        after 60 frames.
        """
        super().advance()
        if self.distance <= 60:
            
            self.center.x += self.velocity.dx
            self.center.y += self.velocity.dy
            self.distance += 1
            
        else:
            
            self.alive = False
        