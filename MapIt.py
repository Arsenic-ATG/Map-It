
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
 
import webbrowser,sys

if len(sys.argv) > 1
	# Get length from command line
	address = ' '.join(sys.argv[1:])

# TODO: get address from clipboard

# TODO: use webbrwoser to open thet webpage