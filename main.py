#   Copyright (c) 2021.
#   Version : 1.0.2
#   Script Author : Sushen Biswas
#
#   Sushen Biswas Github Link : https://github.com/sushen
#
#   !/usr/bin/env python
#   coding: utf-8

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("K:\\Project\\Python\\presearch\\chromedriver.exe",chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds
# What will be searched

# Time waiting for page
waiting_for_page = 10

driver.get("https://engine.presearch.org")
time.sleep(2)
print(input("Enter your Username and Password Menually then enter 1: "))
driver.get("https://presearch.org")
print(input("Enter your Username and Password Menually then enter 1: "))
driver.find_element_by_id("search").send_keys("username")
print(input("Enter your Username and Password Menually then enter 1: "))
time.sleep(1)
driver.find_element_by_id("token-animation").click()
print(input("Enter your Username and Password Menually then enter 1: "))

driver.quit()

