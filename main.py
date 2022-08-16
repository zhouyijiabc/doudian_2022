from selenium import webdriver
from selenium.webdriver import ChromeOptions
from helium import *
from time import sleep


class DouDian:
    def __init__(self):
        self.url = 'https://buyin.jinritemai.com/mpa/account/login?log_out=1&type=24'
        self.option = ChromeOptions()
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.option.add_argument('--start-maximized')
        # self.option.opt_binary_location=r"D:\RunningCheeseChrome_V96.0_XiTongZhiJia\RunningCheeseChrome\App\chrome.exe"
        self.option.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.option, executable_path='./chromedriver.exe')
        set_driver(self.driver)

    def open_live_central(self):
        go_to(self.url)
        sleep(60)

    def


if __name__ == '__main__':
    aa = DouDian()
    aa.open_live_central()