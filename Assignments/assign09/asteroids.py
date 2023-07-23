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
            
        self.ship.draw()
        
        for bullet in self.bullets:
            bullet.draw()


    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_off_screen()

        # TODO: Tell everything to advance or move forward one step in time
        for asteroid in self.asteroids:
            asteroid.advance()
            
        self.ship.advance()
        
        for bullet in self.bullets:
            if bullet.alive:
                bullet.advance()
            else:
                self.bullets.remove(bullet)


        # TODO: Check for collisions
        #self.check_collisions()
        #print("Delta time: {}".format(delta_time))

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.turn_right()

        if arcade.key.UP in self.held_keys:
            self.ship.increase_velocity()

        if arcade.key.DOWN in self.held_keys:
            self.ship.decrease_velocity()

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
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

        for bullet in self.bullets:
            for asteroid in self.asteroids:

                # Make sure they are both alive before checking for a collision
                if bullet.is_alive and asteroid.is_alive:
                    too_close = bullet.radius + asteroid.radius

                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                                abs(bullet.center.y - asteroid.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += asteroid.hit()

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
            if not bullet.is_alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.is_alive:
                self.asteroids.remove(asteroid)            

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = constants.SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def check_off_screen(self):
        """
        Checks to see if flying objects have left the screen
        and if so, wraps them to the other side of the screen.
        :return:
        """
#         for bullet in self.bullets:
#             if bullet.is_off_screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT):
#                 bullet.wrap()
#                 
#         for asteroid in self.asteroids:
#             if asteroid.is_off_screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT):
#                 asteroid.wrap()
# 
#         if self.ship.is_off_screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT):
#             ship.wrap()

# Creates the game and starts it going
window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
arcade.run()