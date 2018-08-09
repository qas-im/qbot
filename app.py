from time import sleep,time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("/usr/local/bin/chromedriver")    # starting chrome driver
driver.get("https://thechinatownmarket.com/")               # loading up chinatown website
wait = WebDriverWait(driver, 20)                            # wait used for timing out loading


"""current_time = datetime.now()                               # getting current time
while current_time.second != 15:                              # wait for time to hit exactly 11:00
    driver.refresh()                                        # refresh page
    current_time = datetime.now()"""                           # get current time again
start_time = time()                                         # get start time once bot moves through site

# waits for item to load and clicks item
link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='hat']")))
link.click()

# close driver when done and print time
driver.close()                                              # closes driver at the end
print("~~~~~ Finished in {0:.2f} seconds ~~~~~"             # print out time elapsed
      .format(time() - start_time))                         # subtract current time from starting time
