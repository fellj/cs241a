import arcade
import random

# These are Global constants to use throughout the game
######################################################################

## Screen Constants
SCREEN_WIDTH          = 600
SCREEN_HEIGHT         = 500

## Rifle Constants
RIFLE_WIDTH           = 100
RIFLE_HEIGHT          = 20
RIFLE_COLOR           = arcade.color.DARK_RED

## Bullet Constants
BULLET_RADIUS         = 10
BULLET_COLOR          = arcade.color.BLACK_OLIVE
BULLET_SPEED          = 10
BULLET_SHAPE          = "Circle"
TARGET_BULLET_SHAPE   = BULLET_SHAPE
BULLET_START_X        = 5
BULLET_START_Y        = 0

## Target Constants
TARGET_RADIUS         = 20
TARGET_COLOR          = arcade.color.CARROT_ORANGE

# # New targets should be created in the "update"
# # function with 1/50 probability. This can be
# # achieved by drawing a random number from 1 to 50
# # and checking if it's 1.
# TARGET_PROBABILITY    = (random.randint(1, 50) == 1)

# The initial position of the target is
# anywhere along the top half of the left
# side the screen.
TARGET_START_X        = random.randint(TARGET_RADIUS, (SCREEN_WIDTH / 2))
TARGET_START_Y        = random.randint((SCREEN_HEIGHT / 2), SCREEN_HEIGHT - 100)

### Standard Target Constants
TARGET_TYPE_STANDARD  = 1
TARGET_SPEED_STANDARD = 7

### Strong Target Constants
TARGET_TYPE_STRONG    = 2
TARGET_SPEED_STRONG   = 3
TARGET_FONT_STRONG    = 20
TARGET_COLOR_FOREGRND = arcade.color.WHITE
TARGET_LIVES_STRONG   = 3


### Safe Target Constants
TARGET_TYPE_SAFE      = 3
TARGET_SPEED_SAFE     = 7
TARGET_COLOR_SAFE     = arcade.color.AIR_FORCE_BLUE
TARGET_RADIUS_SAFE    = 15
TARGET_SHAPE_SAFE     = "Square"
TARGET_WIDTH_SAFE     = 40
TARGET_HEIGHT_SAFE    = TARGET_WIDTH_SAFE
TARGET_POINTS_SAFE    = -10

