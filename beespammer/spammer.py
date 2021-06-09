import time
import pyautogui

def main():
    print("Starting in 5 seconds...")
    time.sleep(5)
    f = open("spam.txt", 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    
if __name__ == '__main__':
    main()
