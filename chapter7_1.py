# --*-- coding:utf-8 --*--

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("https://www.baidu.com/")

input_block = browser.find_element_by_name("wd")
input_block.send_keys("2005")
time.sleep(3)
input_block.clear()

input_block.send_keys("anthony")
time.sleep(3)

submit_button = browser.find_element(By.ID, "su")
submit_button.click()

time.sleep(3)
browser.close()









browser.close()



