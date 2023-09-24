from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/')
accept = driver.find_element('xpath', '//*[@id="accept-choices"]')
accept.click()
menu_html = driver.find_element('xpath', '//*[@id="main"]/div[2]/div/div[1]/a[1]')
menu_html.click()
forms = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[39]')
forms.click()
time.sleep(5)


