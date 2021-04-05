# Spam Bot for Whatsapp or any Messenger Service
Bot made in Python that sends messages automatically on WhatsApp and other messaging applications.

### Dependencies

* A 3.X Python version
* PIP3

### Installing
* Make a git clone or dowloand the zip of the proyect
* Install PyAutogui module:
```bash
pip install pyautogui
```

### Executing program
* Get in the Autofollow-Bot-for-Instagram directory
* Open a terminal in the directory
```
python spammer.py
```
## Explanation:

### import pyautogui 
Time imports the necessary modules for the python program. Pyautogui is used for automating keyboard and mouse functions, and time is used for letting the program wait before executing the next line(s). 

### time.sleep(5) 
Calls the sleep function from the time module and makes the program wait 5 seconds before spamming.

### f = open('text.txt', 'r') 
Opens a file (in this example we called it 'text') and puts it in read mode, then it assigns it to a variable (f).

### for word in f: 
Says that for each word (or line) there is in the 'f' variable (which contains our file in read mode), it will do certain actions based on what's in the loop.

### pyautogui.typewrite(word) 
Calls the typewrite function of the pyautogui module on the variable in the for loop. Basically it automatically types the word or line of your text based on the contents of the text file.

### pyautogui.press('enter') 
Calls the keyboard press function of the pyautogui module, and makes the program hit the enter key (as specified in the program).

### time.sleep(5)
Will spam someone, so make sure to click on the text box of whatever messaging app you're using to spam before your 5 seconds is up!
