SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
SCREEN_TITLE = "Test Ball and Paddle Classes"

from ball import Ball
from paddle import Paddle

def update(ball, paddle):
    import arcade
    arcade.schedule(ball.advance, 1/80)
    
    
def draw_xy(self):
    """
    Puts the current Location on the screen
    """
    x_text = "X: {}".format(self.center.x)
    y_text = "Y: {}".format(self.center.y)
    start_x = 10
    start_y = SCREEN_HEIGHT - 20
    arcade.draw_text(x_text + "\n" + y_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)
    

def main():
    
    """
    Test classes
    """
    import arcade


    # Open arcade window
    # with white background
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)
    
    b1 = Ball()
    
   
    
    b1.draw()
    update(b1)
    
    p1 = Paddle()
    p1.draw()
    
    arcade.run()

    arcade.close_window()
    
if __name__ == "__main__":
    main()    