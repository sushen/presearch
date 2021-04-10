#   Copyright (c) 2021.
#   Version : 1.0.2
#   Script Author : Sushen Biswas
#   Script Author : morsalin
#
#   Sushen Biswas Github Link : https://github.com/sushen
#   morsalin Github Link : https://github.com/pip-pipo
#
#   coding: utf-8


# ================= read this first ===================

#make .env file with EMAIL and PASSWORD  of your Presearch 
# $ make .env file ./.env 

# install requirements.txt
# $ pip install -r requirements.txt

# Run the project
# $ python Main.py

# for unix or linux
# $ python3 Main.py

#================== end of read this first =============

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import random
import time
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())


class Presearch:
    def __init__(self):
        # firefox driver if you want to use
        # self.driver = webdriver.Firefox(executable_path='./geckodriver.exe')
        # chrome driver
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=/tmp/chrome2/")
        # chrome_options.add_argument("--user-data-dir=chrome-data")
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver.exe', options=chrome_options)
        # is browser new tab Open
        self.isNewTabOpen = False
        # count How Many Times Searched
        # currently count not work todo make count 
        self.count = 0
        # keywords list
        self.keyWords = ['dhaka',
                         'Islamabad', 'Bangladesh',
                         'Pakista','karachi',
                         'ISS', 'WEB DEVELOPMENT', 'amazing', 'beautiful', 'adventure', 'photography', 'nofilter',
                         'newyork', 'artsy', 'alumni', 'lion', 'best', 'fun', 'happy',
                         'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema',
                         'love', 'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy',
                         'street', 'canon', 'beauty', 'studio', 'pretty', 'vintage', 'fierce']

    def openPresearch(self):
        driver = self.driver
        driver.get("https://presearch.org")
        driver.implicitly_wait(10)
        driver.maximize_window()

        # validate is user already logged
        isUserLogged = driver.find_element(
            By.XPATH, "//*[@id='user-menu-toggle']")
        # print(not isUserLogged) False means user already not logged
        if not isUserLogged:
            self.MakeRegisterOrLogIn()
        else:
            self.runProcessInfiniteTimes()

    def MakeRegisterOrLogIn(self):

        driver = self.driver
        # user EMAIL AND PASSWORD FROM .env file
        Email = os.environ.get("EMAIL")
        Password = os.environ.get("PASSWORD")

        # click loginOrRegisterButton
        time.sleep(4)
        elm = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[1]/header/nav/div/div[2]/ul/li[5]/a")
        elm.click()

        # fill Email Input
        time.sleep(4)
        emailInput = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[3]/div[1]/form/div[1]/input")
        emailInput.clear()
        emailInput.send_keys(Email)

        # fill password Input
        time.sleep(4)
        passwordInput = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[3]/div[1]/form/div[2]/div/input")
        passwordInput.clear()
        passwordInput.send_keys(Password)

        # captha Validation Manual

        print("Please fill the captha manually")

        WaitUntillUserNotClickToLoginButton = driver.find_element(
            By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[3]/div[1]/form/div[3]/div[3]/button")

        WebDriverWait(driver, timeout=500).until(
            EC.staleness_of(WaitUntillUserNotClickToLoginButton))

        time.sleep(4)
        self.runProcessInfiniteTimes()

    def SearchWithKeyWords(self):
        for i in range(10):
            self.OpenNewTab()
        time.sleep(4)
        self.driver.close()
        self.driver.quite()

    def OpenNewTab(self):
        self.isNewTabOpen == True
        self.count += 1
        driver = self.driver
        keyWords = self.keyWords
        time.sleep(4)

        driver.get("https://presearch.org")

        # click the search input element
        searchInput = driver.find_element(By.XPATH, "//*[@id='search']")
        searchInput.clear()

        # use random keywords
        searchInput.send_keys(random.choice(keyWords))
        searchInput.send_keys(Keys.ENTER)
        time.sleep(7)

        # scroll 0,scrollHeight
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(4)

        # make like human

        # goto search releted next page
        clickGotoPage1 = driver.find_element(
            By.XPATH, "/html/body/div/div/div[3]/div[3]/div[1]/a")
        time.sleep(4)
        clickGotoPage1.click()

        time.sleep(8)
        driver.get("https://presearch.org")

        # repeate Task 
        # Todo ::: Make SomeThing InterActive or make some task 
        searchInput = driver.find_element(By.XPATH, "//*[@id='search']")
        searchInput.clear()
        time.sleep(2)
        searchInput.send_keys(random.choice(keyWords))
        time.sleep(4)
        # WebDriverWait(driver,timeout=500).until(EC.staleness_of(
        searchInput.send_keys(Keys.ENTER)
        # ))
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(4)
        clickGotoPage1 = driver.find_element(
            By.XPATH, "/html/body/div/div/div[3]/div[3]/div[1]/a")
        time.sleep(2)
        clickGotoPage1.click()
        # end Todo

    def runProcessInfiniteTimes(self):
        # use loop for making infinite
        self.SearchWithKeyWords()


runPresearch = Presearch()
runPresearch.openPresearch()


