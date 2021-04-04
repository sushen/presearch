#   Copyright (c) 2021.
#   Version : 1.0.2
#   Script Author   : Sushen Biswas
#                   : Abdullah Al Mohin Jaki
#
#   Sushen Biswas Github Link : https://github.com/sushen
#   Abdullah Al Mohin Jaki Github Link : https://github.com/jakiiii
#
#   !/usr/bin/env python
#   coding: utf-8

import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from parsel import Selector

# TODO: Make a Long List of keyword
all_keys = ["username", "password", "country", "income", "funny"]

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
driver.implicitly_wait(25)  # seconds
# What will be searched

actions = ActionChains(driver)

# Time waiting for page
waiting_for_page = 10

driver.get("https://engine.presearch.org")
time.sleep(2)

# TODO: Make a login strong system in environment veriable
print(input("Enter your Username and Password Menually then enter 1: "))
driver.get("https://presearch.org")
# print(input("Enter your Username and Password Menually then enter 1: "))
driver.find_element_by_id("search").send_keys(random.choice(all_keys))
driver.find_element_by_id("search").send_keys(Keys.ENTER)

# search_query = driver.find_element_by_name('q')
# search_query.send_keys('selenium new tab python')
# search_query.send_keys(Keys.RETURN)

# print(input("Enter your Username and Password Manually then enter 1: "))
time.sleep(2)

actions.send_keys(Keys.TAB * 10)
search_key = random.choice(all_keys)
actions.send_keys(search_key)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(20)
prev_search_key = search_key

while True:
    for i in range(len(prev_search_key)):
        actions.send_keys(Keys.BACK_SPACE)

    time.sleep(4)
    search_key = random.choice(all_keys)
    print(search_key)
    actions.send_keys(search_key)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    prev_search_key = search_key
    time.sleep(4)

    # TODO: Click the search request to make it more human

    sel = Selector(text=driver.page_source)
    link = sel.xpath('//h3/a/@href').extract()[0]
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    time.sleep(10)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])


# driver.find_element_by_id("token-animation").click()
# print(driver.find_element_by_xpath("//button[@type='submit']"))
# driver.find_element_by_xpath("//input[@type='submit']").click();
# print(input("Enter your Username and Password Menually then enter 1: "))

# driver.execute_script("window.open('https://engine.presearch.org');")
# driver.close()
# driver.get("https://presearch.org")
# driver.find_element_by_id("search").send_keys("username")
# driver.find_element_by_id("search").send_keys(Keys.ENTER)

time.sleep(5)

driver.close()
driver.quit()
