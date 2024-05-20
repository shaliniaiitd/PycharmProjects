import pyautogui
import time

def main():
    # Open Calculator
    pyautogui.press('winleft')
    pyautogui.typewrite('calculator')
    pyautogui.press('enter')
    time.sleep(1)  # Wait for Calculator to open

    # Click on the "1" button
    pyautogui.click(x=240, y=550)
    pyautogui.press('enter')

    # # Click on the "+" button
    # pyautogui.click(x=225, y=405)
    #
    # # Click on the "2" button
    # pyautogui.click(x=320, y=405)
    #
    # # Click on the "=" button
    # pyautogui.click(x=415, y=405)
    # # Perform some calculations
    # pyautogui.click(x=320, y=400)  # Click on the "1" button
    # time.sleep(2)
    # pyautogui.click(x=200, y=600)  # Click on the "+" button
    # time.sleep(2)
    # pyautogui.click(x=440, y=400)  # Click on the "2" button
    # time.sleep(2)
    # pyautogui.click(x=520, y=600)  # Click on the "=" button
    # time.sleep(2)

if __name__ == "__main__":
    main()
