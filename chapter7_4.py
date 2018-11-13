# --*-- coding:utf-8 --*--

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Taobao(object):
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")

        self.browser = webdriver.Chrome(chrome_options=chrome_options)




    def run(self):
        """
        the start function
        :return:
        """
        self.browser.get("https://www.baidu.com/s?ie=UTF-8&wd=%E6%B7%98%E5%AE%9D&tn=39042058_1_oem_dg&ch=1")
        print(self.browser.page_source)

        self.browser.quit()

if __name__ == '__main__':
    spider = Taobao()
    spider.run()