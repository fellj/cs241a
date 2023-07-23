# test arcade

import arcade 


# Size of the screen 
WIDTH = 600
HEIGHT = 600
TITLE = "Robust Ball "

# Size of the circle. 
BALL_RADIUS = 50

# How strong the gravity is. 
GRAVITATIONAL_CONSTANT = 0.3

# Percent of velocity maintained on a bounce. 
BOUNCE = 0.9


def draw(_delta_time): 

	# Start the render. 
	arcade.start_render() 

	# Draw ball 
	arcade.draw_circle_filled(draw.x, draw.y, BALL_RADIUS, 
							arcade.color.RED) 
	draw.x += draw.delta_x 
	draw.y += draw.delta_y 

	draw.delta_y -= GRAVITATIONAL_CONSTANT 

	# Figure out if we hit the left or 
	# right edge and need to reverse. 
	if draw.x < BALL_RADIUS and draw.delta_x < 0: 
		draw.delta_x *= -BOUNCE 
	elif draw.x > WIDTH - BALL_RADIUS and draw.delta_x > 0: 
		draw.delta_x *= -BOUNCE 

	# See if we hit the bottom 
	if draw.y < BALL_RADIUS and draw.delta_y < 0: 

		if draw.delta_y * -1 > GRAVITATIONAL_CONSTANT * 15: 
			draw.delta_y *= -BOUNCE 
		else: 
			draw.delta_y *= -BOUNCE / 2

arcade.schedule(draw, 1 / 80)
draw.x = BALL_RADIUS 
draw.y = HEIGHT 
draw.delta_x = 3
draw.delta_y = 3


def main(): 
	# Open up our window 
	arcade.open_window(WIDTH, HEIGHT, TITLE) 
	arcade.set_background_color(arcade.color.GREEN) 

	# Tell the computer to call the draw command 
	# at the specified interval. 
	arcade.schedule(draw, 1 / 80) 

	# Run the program 
	arcade.run() 

	# When done running the program, close the window. 
	arcade.close_window() 


main() 
