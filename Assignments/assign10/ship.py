import arcade
import constants
import math
from flyer import Flyer

class Ship(Flyer):
    """
    Class for
    drawing the ship.
    """
    
    def __init__(self):
        super().__init__()
        self.img       = "images\playerShip1_orange.png"
        self.texture   = arcade.load_texture(self.img)
        self.height    = self.texture.height
        self.width     = self.texture.width
        self.radius    = constants.SHIP_RADIUS
        self.angle     = constants.SHIP_STARTING_ANGLE
        self.direction = 0
        self.center.x  = (constants.SCREEN_WIDTH  / 2)
        self.center.y  = (constants.SCREEN_HEIGHT / 2)
        
    def turn_left(self):
        """
        Rotates the ship
        by the turn amount
        every time the left
        arrow key
        is pressed.
        """
        self.angle += constants.SHIP_TURN_AMOUNT
        
    def turn_right(self):
        """
        Rotates the ship
        by the turn amount
        every time the right
        arrow key
        is pressed.
        """
        self.angle -= constants.SHIP_TURN_AMOUNT
        
    def increase_velocity(self):
        """
        Increases the ship's
        velocity in the
        direction the ship
        is pointed.
        """
        self.velocity.dx += math.sin(math.radians(self.angle)) * -constants.SHIP_THRUST_AMOUNT
        self.velocity.dy += math.cos(math.radians(self.angle)) * constants.SHIP_THRUST_AMOUNT

    def decrease_velocity(self):
        """
        Decreases the ship's
        velocity in the
        opposite direction
        the ship
        is pointed.
        """
        self.velocity.dx -= math.sin(math.radians(self.angle)) * -constants.SHIP_THRUST_AMOUNT
        self.velocity.dy -= math.cos(math.radians(self.angle)) * constants.SHIP_THRUST_AMOUNT

    