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
all_keys = ["python for kinds", "american legends", "wikipedia people ranking in a country", "funny videos", "machine learning"
            "facebook api", "twitter api", "instagram api", "linkedin api", "github", "github api", "git lab",
            "git lab api", "most popular programming language", "socket programming", "socket programming python"
            "data science", "python data science", "docker", "nodejs", "advanced javascript", "django ajax",
            "artificial intelligence", "best movies list 2020", "top movie ratting imdb", "harry potter",
            "game of thrones", "michael jackson", "abraham lincoln vampire hunter", "hide and seek", "the rock"]


chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")

# driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
driver = webdriver.Chrome()
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

    # Scrolling up-down
    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(random.randint(1, 5))
    driver.execute_script("window.scrollBy(0, -800);")
    time.sleep(random.randint(1, 5))

    # TODO: Click the search request to make it more human
    links = driver.find_elements_by_xpath('//h3/a[@href]')
    link = driver.find_elements_by_xpath('//h3/a[@href]')[0]
    url = link.get_attribute('href')
    driver.execute_script("window.open('about:blank', 'tab2');")
    driver.switch_to.window("tab2")
    driver.get(url)
    time.sleep(10)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(random.randint(5, 35))

    '''
    # Using parsel library
    sel = Selector(text=driver.page_source)
    link = sel.xpath('//h3/a/@href').extract()[0]
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    time.sleep(10)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(random.randint(5, 35))
    '''


time.sleep(5)
driver.close()
driver.quit()
