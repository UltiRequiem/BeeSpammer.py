import time
import pyautogui
import sys


def get_spam_file(configuration_file: str) -> str:
    try:
        with open(configuration_file, "r") as reader:
            return reader.read()
    except FileNotFoundError:
        print("spam.txt not found!")
        sys.exit(0)


def main():
    print("Starting in 5 seconds...")
    time.sleep(5)

    spam_txt = get_spam_file("spam.txt")

    for word in spam_txt:
        pyautogui.typewrite(word)
        pyautogui.press("enter")


if __name__ == "__main__":
    main()
