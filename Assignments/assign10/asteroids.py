"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others

This program implements the asteroids game.
"""
import arcade
import constants
from large import LargeAsteroid
from ship import Ship
from bullet import Bullet

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # Declare anything here you need the game class to track
        self.score     = 0
        self.ship      = Ship()
        self.bullets   = []
        self.asteroids = []
        
        self.create_asteroids()

    def create_asteroids(self):
        """
        Creates five large
        asteroids.
        """
        for i in range(constants.INITIAL_ROCK_COUNT):
            bigAst = LargeAsteroid()
            self.asteroids.append(bigAst)
            
    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        for asteroid in self.asteroids:
            asteroid.draw()
            
        if not self.ship == None:
            self.ship.draw()
        else:
            self.game_over()
        
        for bullet in self.bullets:
            bullet.draw()
            
        self.draw_score()        


    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # Tell everything to advance or
        # move forward one step in time
        for asteroid in self.asteroids:
            asteroid.advance()

        if not self.ship == None:    
            self.ship.advance()
        
        for bullet in self.bullets:
            if bullet.alive:
                bullet.advance()
            else:
                self.bullets.remove(bullet)


        # Check for collisions
        self.check_collisions()
        #print("Delta time: {}".format(delta_time))

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            if not self.ship == None:
                self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys:
            if not self.ship == None:
                self.ship.turn_right()

        if arcade.key.UP in self.held_keys:
            if not self.ship == None:
                self.ship.increase_velocity()

        if arcade.key.DOWN in self.held_keys:
            if not self.ship == None:
                self.ship.decrease_velocity()

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if not self.ship == None:
            if self.ship.alive:
                self.held_keys.add(key)

                if key == arcade.key.SPACE:
                    # Fire the bullet here!
                    bullet = Bullet()
                    bullet.spawn(self.ship)
                    bullet.fire()
                    self.bullets.append(bullet)


    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
            
    def check_collisions(self):
        """
        Checks to see if bullets have hit asteroids.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your asteroids list "asteroids"
        if not self.ship == None:
            for bullet in self.bullets:
                for asteroid in self.asteroids:

                    # Make sure they are both alive before checking for a collision
                    if bullet.is_alive() and asteroid.is_alive():
                        too_close      = bullet.radius + asteroid.radius

                        if (abs(bullet.center.x - asteroid.center.x) < too_close and
                                    abs(bullet.center.y - asteroid.center.y) < too_close):
                            # its a hit!
                            self.score += asteroid.hit()
                            if asteroid.type != constants.ASTRD_SM_TYPE:
                                self.asteroids.extend(asteroid.break_apart())

                            bullet.alive = False
                            asteroid.alive = False
                            
                            if len(self.asteroids) == 0:
                                self.create_asteroids()

            # Check if the ship has collided with an asteroid
            for asteroid in self.asteroids:
                if self.ship.is_alive() and asteroid.is_alive():
                    ship_too_close = self.ship.radius + asteroid.radius                
                    
                    if (abs(self.ship.center.x - asteroid.center.x) < ship_too_close and
                       abs(self.ship.center.y - asteroid.center.y) < ship_too_close):

                            self.ship.alive = False
                            asteroid.alive  = False

        # We will wait to remove the dead objects until after we
        # finish going through the list
                      
 
        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or asteroids from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.is_alive():
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.is_alive():
                self.asteroids.remove(asteroid)
                
        if not self.ship == None:        
            if not self.ship.is_alive():
                self.ship = None

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 30
        start_y = constants.SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.AUREOLIN)

    def game_over(self):
        """
        Puts the text 'GAME OVER'
        in the center of the screen
        """
        score_text = "GAME OVER"
        start_x = (constants.SCREEN_WIDTH / 2) - 60
        start_y = constants.SCREEN_HEIGHT / 2
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=30, color=arcade.color.AUREOLIN)

# Creates the game and starts it going
window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
arcade.run()
