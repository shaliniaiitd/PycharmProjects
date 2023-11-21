#Open – Google -> Search for google -> How many times google key word is present in the page. -> based on xpath.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://www.google.com')
page = driver.find_elements(By.XPATH, "//*[contains(text(),Google)]")
print(len(page))

# page_text = page.text
# page_text  = str(page_text).lower()
# counts = str(page_text).count("google")
# print(counts)
# print(str(page_text))