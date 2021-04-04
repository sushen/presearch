from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from parsel import Selector

# TODO: Make a Long List of keyword
all_keys = ["american legends", "income", "funny videos", "python for kids"]


driver = webdriver.Chrome()
driver.implicitly_wait(5)

print(input("Enter your Username and Password Menually then enter 1: "))
driver.get("https://engine.presearch.org")
sleep(2)

search_query = driver.find_element_by_name('q')
search_query.send_keys(random.choice(all_keys))
search_query.send_keys(Keys.RETURN)
sleep(5)

sel = Selector(text=driver.page_source)
link = sel.xpath('//h3/a/@href').extract()[0]
driver.execute_script("window.open(link);")
window_name = driver.current_url[1]
driver.switch_to.window(window_name=window_name)
sleep(5)
driver.close()

window_name = driver.window_handles[0]
driver.switch_to.window(window_name=window_name)
