# To use both cores
import _thread

from Led import led
from Button import button

# Initialize the system
# Initialize the button and the led
def init():
	led.init_leds()
	button.init_button()

# Main function
if __name__ == "__main__":
	print( "Debug of Led_v3 aka sLeds_v2" )
	print( "Initializing the system" )

	# Initialize the system
	init()

	print( "System Initialized" )

	# Wait for the button to be pressed
	# Task done by the second core
	client_thread = _thread.start_new_thread( button.wait, () )

	# Play the animations
	led.play()

	print( "Stopped" )