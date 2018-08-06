import time
from selenium import webdriver

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("http://www.google.com/")
time.sleep(5)
