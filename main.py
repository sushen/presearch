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
from selenium.webdriver.common.keys import Keys



chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("./chromedriver.exe",chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds
# What will be searched

# Time waiting for page
waiting_for_page = 10

driver.get("https://engine.presearch.org")
time.sleep(2)
# print(input("Enter your Username and Password Menually then enter 1: "))
driver.get("https://presearch.org")
# print(input("Enter your Username and Password Menually then enter 1: "))
driver.find_element_by_id("search").send_keys("username")
driver.find_element_by_id("search").send_keys(Keys.ENTER)
# print(input("Enter your Username and Password Menually then enter 1: "))
time.sleep(2)
# driver.find_element_by_id("token-animation").click()
# print(driver.find_element_by_xpath("//button[@type='submit']"))
# driver.find_element_by_xpath("//input[@type='submit']").click();
# print(input("Enter your Username and Password Menually then enter 1: "))

driver.execute_script("window.open('https://engine.presearch.org');")
driver.close()
# driver.get("https://presearch.org")
# driver.find_element_by_id("search").send_keys("username")
# driver.find_element_by_id("search").send_keys(Keys.ENTER)

time.sleep(2)

driver.quit()