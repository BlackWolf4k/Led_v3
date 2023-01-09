import time
import neopixel
from machine import Pin

from Shared_Informations import shared_informations
from Animation import animation

# Relations between pattern number and function to play the pattern
patterns = [ play_no_pattern, play_rainbow_pattern ]

# Store the leds
leds = 0

# Store the file names
animations = []

# Keep track of the animation that is beeing played
actual_animation = 0

# Initialize the led system
def init_leds():
	global leds

	# Initialize the led
	leds = neopixel.NeoPixel( Pin( shared_informations.generals["control_pin"], Pin.OUT ), shared_informations.generals["number_of_leds"] )

	# Get the filenames
	animations = animation.get_file_names()

# Get the next animation
# When the board is started, it starts from 0
# Returns the filename of the animation
def get_next_animation():
	global actual_animation

	# Get the filename
	filename = animations[ actual_animation ]

	# Change animation number
	actual_animation = ( actual_animation + 1 ) % len( animations )

	# Return the filename
	return filename

# Decode the animation from binary file
# Requires as input the name of the file
# Returns the decoded animation
def decode_animation( filename ):
	# Read the content of the animation
	animation_binary_content = animation.read_file( filename )

	# Decode the animation descriptor
	animation_descriptor = struct( addressof( animation_binary_content ), animation_descriptor_t, LITTLE_ENDIAN )

	# Remove the animation descriptor from the content
	del animation_binary_content[ :11 ]

	decoded_animation = {}

	# Store the needed informations about the animation descriptor
	decoded_animation[ "delay" ] = animation_descriptor.delay
	decoded_animation[ "pattern" ] = animation_descriptor.pattern
	decoded_animation[ "body" ] = []

	# Decode the animation
	# Read one line per time
	for i in range( 0, animation_descriptor.number_of_lines, 1 ):
		# Store the line
		line = []

		# Read the line content
		for j in range( 0, animation_descriptor.line_length, 3 ):
			# Store the RGB value of a pixel
			pixel = [ 0, 0, 0 ]

			# Read the colors
			for k in range ( 0, 3, 1 ):
				pixel[ i ] = animation_binary_content[ i * animation_descriptor.line_length + j + k ]

			# Add the pixel
			line.append( pixel )

		# Add the line
		decoded_animation[ "body" ].append( line )

	# Return the decoded animation
	return decoded_animation

# Select the method in which to play a animation passed
# Calls other function based on the type of pattern of the animation
# Requires as input a decoded animation
def select_play_method( decoded_animation ):
	# Play the animation based on the pattern
	patterns[ decoded_animation[ "pattern" ] ]( decode_animation )
	return

# Plays a rainbow animation
# Plays untill the button is pressed
# Requires as argument a decoded animation
def play_rainbow_pattern( decoded ):
	return