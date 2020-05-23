
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

chrome_options = Options()

#
chrome_options.add_argument("--enable-popup-blocking")

class InstaBot:

    def __init__(self, username, pw):

        self.driver = webdriver.Chrome("R:\InstagramBot\chromedriver.exe", chrome_options=chrome_options)
        self.username = username


        self.driver.get("https://cas.ucalgary.ca/cas/login?service=https://my.ucalgary.ca/psp/paprd/?cmd=start&ca.ucalgary.authent.ucid=true")
        #self.driver.get("https://instagram.com")
        time.sleep(2)
        #self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()

        #time.sleep(1)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)

        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)

        self.driver.find_element_by_xpath('//input[@type="submit"]').click()

        time.sleep(2)

        #self.driver.get("https://cas.ucalgary.ca/cas/")
        self.driver.find_element_by_partial_link_text("myUofC Login").click()

        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)

        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)

        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        time.sleep(4  )
        self.driver.find_element_by_xpath("//button[contains(text(), 'Schedule Builder')]").click()

        time.sleep(1)

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        #self.driver.find_element_by_xpath("//button[contains(text(), 'Schedule Builder')]").click()
        self.driver.find_element_by_xpath('//input[@value=\"Continue\"]').click()
        #self.driver.find_element_by_xpath("//button[contains(text(), 'Continue')]").click()
        #self.driver.find_element_by_xpath("//a[contains(text(), '/'+username)]").click()
        #self.driver.find_element_by_partial_link_text(username).click()
        #self.driver.find_element_by_partial_link_text(username).click()
        time.sleep(1)
        #self.driver.find_element_by_partial_link_text('/'+username+'/following').click()

        #Finding the term radio button by id and clicking it
        self.driver.find_element_by_xpath("//input[@id='term_32203']").click()

        time.sleep(5)
        #soup = BeautifulSoup(term_element, 'html.parser')
        #self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"code_number\"]").send_keys('CPSC 457')
        self.driver.find_element_by_xpath('//input[@name=\"add_course\"]').click()
        time.sleep(4)

        data = self.driver.find_element_by_class_name('requirementDiv requirementMargin')
        print(data)
        #dataList = self.driver.find_element_by_class_name('class_code')

        for item in dataList:
            text = item.text
            print(text)

        #div = self.driver.find_element_by_css_selector('_2dbep qNELH kIKUG').get_attribute('href')
        #div = self.driver.find_element_by_class_name('_2dbep qNELH kIKUG')
        #div = div.find_element_by_css_selector('a').get_attribute('href')
        #print(div)
        time.sleep(400)


InstaBot('rashikhassan.md', 'Tasnim123@')

"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Interview questions")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
lists= driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists)) + " searches:")

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem.get_attribute("innerHTML"))
   i=i+1
   if(i>10):
      break

# close the browser window
driver.quit()
"""
