import pyautogui,time

print("Ready for Spam OwO")
time.sleep(5)
f = open("iwannabeadmi.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
  
