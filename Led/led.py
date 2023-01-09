import time
import neopixel
from machine import Pin

# Relations between pattern number and function to play the pattern
patterns = [ play_no_pattern, play_rainbow_pattern ]

# Store the leds
leds = 0

# Initialize the led system
def init_leds():
	global leds
	leds = neopixel.NeoPixel( Pin( generals["control_pin"], Pin.OUT ), generals["number_of_leds"] )

# Get the next animation
# When the board is started, it starts from 0
# Returns the filename of the animation
def get_next_animation():
	return filename

# Decode the animation, from binary file to json
# Requires as input the name of the file
# Returns the json containing the animation
def decode_animation( filename ):
	return decoded_animation

# Select the method in which to play a animation passed
# Calls other function based on the type of pattern of the animation
# Requires as input a json animation
def select_play_method( json_animation ):
	return

# Plays a rainbow animation
# Plays untill the button is pressed
# Requires as argument a json animation
def play_rainbow_pattern( json_animation ):
	return