import pyautogui
import time

time.sleep(1)

def mesaj():

    pyautogui.write("Kürt")
    pyautogui.write("Afgan")
    pyautogui.write("Zhimbabbeli")
    pyautogui.press('enter')

while True:
    mesaj()
    time.sleep(0.1)