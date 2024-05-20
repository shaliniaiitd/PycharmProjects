from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open Calculator
        page.goto("calc.exe")

        # Wait for the Calculator window to appear
        page.wait_for_selector('title:has-text("Calculator")')

        # Click on the "1" button
        page.click('button:has-text("1")')


        # # Click on the "+" button
        # page.click('button:has-text("+")')
        #
        # # Click on the "2" button
        # page.click('button:has-text("2")')
        #
        # # Click on the "=" button
        # page.click('button:has-text("=")')


if __name__ == "__main__":
    main()
