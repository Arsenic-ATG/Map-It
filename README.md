# Map-It
it’s tedious to copy a street address to the clipboard and bring up a map of it on Google Maps. You could take a few steps out of this task by writing a simple script to automatically launch the map in your browser using the contents of your clipboard. This way, you only have to copy the address to a clipboard and run the script, and the map will be loaded for you.

This is what your program does:

- Gets a street address from the command line arguments or clipboard.

- Opens the web browser to the Google Maps page for the address.

## Language used
- 🐍 python

### Setup required 🛠
- most of the stuff will be plain python scripts which will only require you to have **python installed on your device** and an **IDE/text editor** to see and make changes to the scripts on your system.
- if you don't have python on your machine then you can download it from [here](https://www.python.org/downloads/)
- 🌐 Install ```pyperclip``` (external module of python) using ```pip install pyperclip```

## 🏃‍♀️Get it running🏃‍♂️
- 👯‍♂️clone/download using ```git@github.com:Arsenic-ATG/Map-It.git```
- run the python script
- to run the script with command line arguments pass the argument at the time or running the program like this :-
  ```$python3 MapIt.py <location to be searched>```
  for example:-
  ```$python3 MapIt.py delhi```
  
 - to fetch the address from clipboard then run the script without command line arguments

## Note:
the script will use the command line arguments instead of the clipboard. If there are no command line arguments, then the program will know to use the contents of the clipboard.
