# Importing required libraries

# pip install selenium

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Maximize the Chrome window
driver.maximize_window()

# Navigating to the Amazon.ca homepage
driver.get("https://www.whatsapp.com/")
time.sleep(2)

# Selecting a Features Tab from the Header
Features_link = driver.find_element("xpath",
                                    "/html/body/div[1]/div[1]/div[1]/header/div/nav/ul/li[1]/div/button/span/span")

# Click the element
Features_link.click()

# Waiting for Feature menu page to finish loading
time.sleep(2)

# Selecting a "Stay Connected1" option from Features Tab
Stay_connected = driver.find_element("xpath",
                                     "/html/body/div[1]/div[1]/div[1]/header/div/nav/ul/li[1]/div/div/ul/li[2]/a")

# Click the element
Stay_connected.click()

# Waiting to Open "Stay Connected" page
time.sleep(2)

# Scroll down the page using the END key
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll down the page slowly
scroll_height = driver.execute_script("return document.body.scrollHeight;")
scroll_increment = 600  # Adjust the scroll increment as needed
scroll_delay = 1  # Adjust the scroll delay (in seconds) as needed

for i in range(0, scroll_height, scroll_increment):
    driver.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(2)

# Selecting an "About us" option from Footer
About_us = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/footer/div[2]/div/div[3]/a[1]")

# Click the element
About_us.click()

# Waiting to load "About US" page
time.sleep(4)

# Selecting a "Whatsapp Web" option
Whatsapp_Web = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[1]/header/div/div[2]/span/span/a")

# Click the element
Whatsapp_Web.click()

# Waiting to load "Whatsapp_Web" page
time.sleep(7)


# Closing the webdriver
driver.close()
