from machine import Pin
import time

from Shared_Informations import shared_informations

# Istance of the button
button = Pin( shared_informations.generals[ "button_pin" ], Pin.IN, Pin.PULL_DOWN )

def init_button():
	return

def wait():
	global button

	print( "Starting async wait of button" )

	# Wait that the button is pressed
	while True:
		# Is button being pressed
		if button.value():
			print( "Button Pressed" )
			# Change the value so that the other core will know that the button was pressed
			shared_informations.button_pressed = 1

			# Wait some time ( 1 second )
			time.sleep( 1 )