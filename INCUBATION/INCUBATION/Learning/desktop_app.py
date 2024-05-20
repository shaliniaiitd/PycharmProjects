import pyautogui
import time

def main():
    # Open Notepad
    pyautogui.press('winleft')
    pyautogui.typewrite('notepad')
    pyautogui.press('enter')
    time.sleep(1)  # Wait for Notepad to open

    # Type some text
    pyautogui.typewrite("Hello, this is desktop app test automation using python !\n")

    # Save the file
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)  # Wait for the Save dialog to appear
    pyautogui.typewrite("desktop_test_eg.txt")
    pyautogui.press('enter')

if __name__ == "__main__":
    main()