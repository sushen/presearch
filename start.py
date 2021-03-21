#    Copyright (c) 2021.
#    Version : 1.0.2
#    Script Author : Sushen Biswas
#
#    Sushen Biswas Github Link : https://github.com/sushen
#
#    !/usr/bin/env python
#    coding: utf-8


from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import random

#TODO : Random Key Word
#Change the messages as you wish, one of them will be randomly picked
keyWord = [
    "bitcoin",
    "etheium",
    "elon mask"
]

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

#TODO: Go to the Page
driver.get("https://presearch.org")
time.sleep(2)


# #TODO: Search Keyword
driver.find_element_by_id("search").send_keys(random.choice(keyWord))
driver.find_element_by_id("search").send_keys(Keys.ENTER)

time.sleep(2)

driver.quit()
