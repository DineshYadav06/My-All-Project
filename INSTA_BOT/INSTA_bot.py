# instagram_bot.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Instagram credentials (replace with yours)
USERNAME = "your_username"
PASSWORD = "your_password"

# Step 1: Open Instagram
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/")
time.sleep(3)

# Step 2: Log in
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

time.sleep(5)

# Step 3: Handle pop-ups (optional)
try:
    not_now = driver.find_element(By.XPATH, "//button[contains(text(), 'Not now')]")
    not_now.click()
    time.sleep(3)
except:
    pass

# Step 4: Search for a profile
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_box.send_keys("cristiano")  # Example: Cristiano Ronaldo
time.sleep(3)
search_box.send_keys(Keys.ENTER)
time.sleep(1)
search_box.send_keys(Keys.ENTER)
time.sleep(5)

# Step 5: Follow user (if not followed)
try:
    follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
    follow_button.click()
    print(" Followed the user!")
except:
    print("Already following or button not found.")

time.sleep(5)
driver.quit()
