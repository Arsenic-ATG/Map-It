
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
 
import webbrowser,sys,pyperclip

if len(sys.argv) > 1
	# Get length from command line
	address = ' '.join(sys.argv[1:])

else
	# Get address from clipboard
	address = pyperclip.paste()

# TODO: use webbrwoser to open thet webpage