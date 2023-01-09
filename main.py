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
	init()
	print( "System Initialized" )
	print( "Started to play animations" )
	led.select_play_method( led.decode_animation( led.get_next_animation() ) )
	print( "Stopped" )