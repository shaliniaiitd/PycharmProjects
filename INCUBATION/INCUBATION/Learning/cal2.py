import pyautogui
import time

def main():
    # Open Calculator
    pyautogui.press('winleft')
    pyautogui.typewrite('calculator')
    pyautogui.press('enter')
    time.sleep(1)  # Wait for Calculator to open

    # Define button images
    one_button_image = 'one_button.png'
    plus_button_image = 'plus_button.png'
    two_button_image = 'two_button.png'
    equal_button_image = 'equal_button.png'

    # Click on the "1" button
    one_button_location = pyautogui.locateCenterOnScreen(one_button_image)
    pyautogui.click(one_button_location)

    # Click on the "+" button
    plus_button_location = pyautogui.locateCenterOnScreen(plus_button_image)
    pyautogui.click(plus_button_location)

    # Click on the "2" button
    two_button_location = pyautogui.locateCenterOnScreen(two_button_image)
    pyautogui.click(two_button_location)

    # Click on the "=" button
    equal_button_location = pyautogui.locateCenterOnScreen(equal_button_image)
    pyautogui.click(equal_button_location)

if __name__ == "__main__":
    main()
