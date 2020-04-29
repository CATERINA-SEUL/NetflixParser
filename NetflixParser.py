
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

class NetflixParser:

    def __init__(self, datetime, login_id, login_pw):
        self.login_id = login_id
        self.login_pw = login_pw
        self.driver = self.login()
        self.scan(self.driver)
        
        df = pd.DataFrame(self.items_list)
        df = df.drop_duplicates(keep='last').set_index('rank')
        df['Date'] = datetime
        self.df = df.sort_index()

        self.driver.quit()

    def login(self):
        driver = webdriver.Chrome()
        driver.set_window_size(1080,800)
        url = 'https://www.netflix.com/kr/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse%2Fgenre%2F83'
        driver.get(url)
        driver.implicitly_wait(1)
        #로그인
        driver.find_element_by_css_selector('#id_userLoginId').send_keys(self.login_id)
        driver.find_element_by_css_selector('#id_password').send_keys(self.login_pw)
        driver.find_element_by_css_selector('.btn').click()
        driver.implicitly_wait(3)
        # driver.find_element_by_css_selector('#appMountPoint > div > div > div:nth-child(1) > div.bd.dark-background > div.profiles-gate-container > div > div > ul > li:nth-child(1) > div > a > div > div').click()
        driver.find_element_by_css_selector('#appMountPoint > div > div > div:nth-child(1) > div.bd.dark-background > div.profiles-gate-container > div > div > ul > li:nth-child(2) > div > a > div > div').click()

        return driver

    def scan(self, driver):
        import time

        self.items_list = []
        items_get = self.driver.find_element_by_xpath('//div[@data-list-context="mostWatched"]')

        if items_get:
            items = items_get.find_element_by_css_selector('.rowContent .slider .sliderContent')
            items.text.strip()
            items_get.find_element_by_css_selector('.handle').click()
            time.sleep(2)
            items_get.find_element_by_css_selector('.handle').click()
            items_2 = items_get.find_elements_by_css_selector("div.ptrack-content a")

        for item in items_2:
            title = item.get_attribute("aria-label")
            rank = item.find_elements_by_css_selector("div > svg > use")[0].get_attribute("xlink:href")
            rank = int(rank.split('-')[1])
            self.items_list.append({"title" : title, "rank" : rank})

        return self.items_list
