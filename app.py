import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.google.com/")
time.sleep(2)
search_box = driver.find_element_by_name("q")
search_box.send_keys("qasim shareh")
time.sleep(2)
search_box.send_keys(Keys.RETURN)
time.sleep(2)
try:
    link = driver.find_element_by_xpath('(//h3)[2]/a')
    link.click()
except NoSuchElementException:
    print("failed to find link")
driver.Close()
