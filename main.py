from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import random

all_keys = ["make money fast today",
"how to make money online for beginners",
"how to make money online for free",
"how to make quick money in one day",
"creative ways to make money",
"real ways to make money from home",
"ideas to make money",
"how to make money in life",
"most viewed youtube video in 24 hours",
"what is the most viewed video on tiktok",
"most viewed youtube video 2019",
"most viewed youtube channel",
"most viewed youtube video not music",
"most viewed video on youtube in india",
"top 50 most viewed youtube videos of all time",
"Md Jawad Hossain",
"Tech Teach Pro",
"fanyconda",
"Hollow Block Bd"]
rand_time= [5, 9, 16, 6, 12, 10, 8, 7, 11, 13, 14, 15]
email = os.environ.get('email')
password = os.environ.get('password')

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
actions = ActionChains(driver)
driver.get('https://engine.presearch.org/')



def login():
    window_before = driver.window_handles[0]
    driver.find_element_by_xpath('//*[@id="Home"]/div[1]/div/div[2]/a').click() #Register or Login
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    driver.find_element_by_name('email').send_keys(email) #email
    driver.find_element_by_name('password').send_keys(password) #password
    driver.find_element_by_name('remember').click() #Remember Me
    input('Verify the reCAPTCHS and press 1 :  ')
    driver.find_element_by_xpath('//*[@id="login-form"]/form/div[3]/div[3]/button').click()
    time.sleep(2)
    driver.switch_to_window(window_before)
    time.sleep(2)
    driver.get('https://engine.presearch.org/')
    time.sleep(3)
    driver.set_page_load_timeout(7)


def search1():
    random_time = random.choice(rand_time)
    actions.send_keys(Keys.TAB * 10)
    search_key = random.choice(all_keys)
    actions.send_keys(search_key, Keys.ENTER)
    actions.perform()
    time.sleep(random_time)
    prev_search_key = search_key

    while True:
        for i in range(len(prev_search_key)):
            actions.send_keys(Keys.BACK_SPACE)

        time.sleep(4)
        search_key = random.choice(all_keys)
        print(search_key)
        actions.send_keys(search_key, Keys.ENTER)
        actions.perform()
        prev_search_key = search_key
        time.sleep(4)

try:
    login()

except:
    pass

search1()
