import os
from ctypes import *

# ANIMATION DESCRIPTOR
# number_of_lines: 	the number of lines in the file
# line_length:		the length of a single line
# repeat: 			does the animation repeat ( 0 - 254: number of times to repeat, 255: loop )
# delays: 			pointer to the delays matrix
# pattern:			animations with a repeating patter ( 0: none, 1: rainbow )
animation_descriptor_t = {
		"number_of_lines" : 0 | INT32,
		"line_length" : 4 | INT32,
		"delay" : 8 | UINT8,
		"repeat" : 9 | UINT8,
		"pattern" : 10 | UINT8
}

# Get the names of all the animations
# Returns a array with the filenames
def get_file_names():
	# Get in the animations directory
	os.chdir( "Animation/Animations" ) # CHECK THIS ( path may be wrong )

	# Read the file names
	filenames = os.listdir()

	# Return the filenames
	return filenames

# Read a file an return the binary content
# Requires the filename as argument
# Returns the content as array of bytes
def read_file( filename ):
	# Create the string to store the file content
	content = ""

	# Read the content
	with open( filename, "rb" ) as file: # CHECK THIS ( path may be wrong )
		# Read one byte per time
		content = file.read()
		#while( byte := file.read( 1 ) ):
		#	# Store the content
		#	content.append( byte )
	
	# Return the file content
	return content