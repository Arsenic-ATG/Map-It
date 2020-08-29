# 🗺 Map-It 📌
It’s tedious to copy a street address to the clipboard and bring up a map of it on Google Maps. You could take a few steps out of this task by using this simple script which automatically launch the map in your browser using the contents of your clipboard. This way, you only have to copy the address to a clipboard and run the script, and the map will be loaded for you.

This is what your program does:

- Gets a street address from the command line arguments or clipboard.

- Opens the web browser to the Google Maps page for the address.

Table below👇 compares the steps needed to display a map with and without **mapIt.py**.

| **manually getting a map**       | **using mapIt.py**         |
| ------------- |:-------------:|
| Highlight the address     | Highlight the address |
| Copy the address     | Copy the address     |
| Open the web browser | Run mapIt.py      |
|Go to http://maps.google.com/|      |
| Click the address text field  |      |
| Paste the address  |      |
| Press enter   |      |

## Language used
- 🐍 python

### Setup required 🛠
- Most of the stuff is plain python scripts which will only require you to have **python installed on your device** and an **IDE/text editor** to see and make changes to the scripts on your system.
- If you don't have python on your machine then you can download it from [here](https://www.python.org/downloads/)
- 🌐 Install ```pyperclip``` (external module of python) using ```pip install pyperclip```

## 🏃‍♀️Get it running🏃‍♂️
- 👯‍♂️Clone/Download using ```git@github.com:Arsenic-ATG/Map-It.git```
- Run the python script :
  - to run the script with command line arguments pass the argument at the time or running the program like this :-
    ```$python3 MapIt.py <location to be searched>```
    for example:-
    ```$python3 MapIt.py delhi```
  
  - To fetch the address from clipboard then run the script without command line arguments

## Note:
The script will use the command line arguments instead of the clipboard. If there are no command line arguments, then the program will know to use the contents of the clipboard.

### Liked it ? 😃
- If you like this project then don't forget to give a star 
- For more automations like this you can head over to my [python automations](https://github.com/Arsenic-ATG/Python-Automations) repo
