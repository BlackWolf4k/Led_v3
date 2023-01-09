import time
import neopixel
from machine import Pin
import ctypes

from Shared_Informations import shared_informations
from Animation import animation

# Store the leds
leds = neopixel.NeoPixel( Pin( shared_informations.generals[ "led_pin"], Pin.OUT ), shared_informations.generals["number_of_leds"] )

# Function to play animations patterns
def play_no_pattern( decoded_animation ):
	for i in range( 0, len( decoded_animation[ "body" ] ) , 1 ):
		for j in range( 0, len( decoded_animation[ "body" ][i] ), 1 ):
			print( decoded_animation[ "body" ][ i ][j] )
	return

# Plays an animation that follows the rainbow pattern
# Requires the decoded animaion as argument
def play_rainbow_pattern( decoded_animation ):
	# Keep track of the times the leds have been changed
	turn = 0

	# Play the animation untill the button is pressed
	while ( shared_informations.button_pressed == 0 ):
		# Set all led values
		for i in range( 0, shared_informations.generals["number_of_leds"], 1 ):
			leds[i] = decoded_animation[ "body" ][0][ ( i + turn ) % shared_informations.generals["number_of_leds"] ]
		
		# Write the changings
		leds.write()

		turn += 1
		
		# Sleep for the delay time
		time.sleep( decoded_animation[ "delay" ] / 1000 )

# Play a static animation
# Write the colors just once and than waits for the button to be pressed
# Requires the decoded animaion as argument
def play_static( decoded_animation ):
	# Set all led values
	for i in range( 0, shared_informations.generals["number_of_leds"], 1 ):
		leds[i] = decoded_animation[ "body" ][0][i]
	
	# Write the changings
	leds.write()
	
	# Wait for the button to be pressed
	while ( shared_informations.button_pressed == 0 ):
		# Sleep for 1 second
		time.sleep( 1 )


# Relations between pattern number and function to play the pattern
# 0 = default animation
# 1 = rainbow animation
# 2 = static animation
patterns = [ play_no_pattern, play_rainbow_pattern, play_static ]

# Store the file names
animations = []

# Keep track of the animation that is beeing played
actual_animation = 0

# Initialize the led system
def init_leds():
	global leds
	global animations

	# Initialize the led
	leds = neopixel.NeoPixel( Pin( shared_informations.generals["led_pin"], Pin.OUT ), shared_informations.generals["number_of_leds"] )

	# Get the filenames
	animations = animation.get_file_names()

	print( animations )

# Get the next animation
# When the board is started, it starts from 0
# Returns the filename of the animation
def get_next_animation():
	global actual_animation
	global animations

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
	animation_descriptor = ctypes.struct( ctypes.addressof( animation_binary_content ), animation.animation_descriptor_t, ctypes.LITTLE_ENDIAN )

	# Remove the animation descriptor from the content
	animation_binary_content = animation_binary_content[ 11 : ]

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
				pixel[ k ] = animation_binary_content[ i * animation_descriptor.line_length + j + k ]

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
	patterns[ decoded_animation[ "pattern" ] ]( decoded_animation )
	return

def play():
	print( "Started to play animations" )

	# Play animation forever
	while True:
		shared_informations.button_pressed = 0
		select_play_method( decode_animation( get_next_animation() ) )
		print( "Changing Animation" )