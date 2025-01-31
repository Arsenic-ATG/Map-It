# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser,sys,pyperclip
# pyperclip is an external module so you should install it before running script 
# to do so open terminal and type command " $ pip install pyperclip"

if len(sys.argv) > 1:
	# Get length from command line
	address = ' '.join(sys.argv[1:])

else:
	# Get address from clipboard
	address = pyperclip.paste()

# Use webbrwoser to open thet webpage
webbrowser.open('https://www.google.com/maps/place/' + address)