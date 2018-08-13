import json
from time import sleep,time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("/usr/local/bin/chromedriver")    # starting chrome driver
wait = WebDriverWait(driver, 20)                            # wait used for timing out loading
with open("./config.json","r") as configuration:            # opening config.json
    info = json.load(configuration)                        # loading data into info dict
    configuration.close()                                   # closing config.json to avoid corruption

# goes to google sign in, waits for email entry to load, enters email address, and clicks next
driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
email = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]')))
email.send_keys(info["google"]["email"])
driver.find_element_by_xpath('//*[@id="identifierNext"]/content').click()


# waits for password entry to load, enters password, and clicks next
password = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
password.send_keys(info["google"]["password"])
driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()


# goes to captcha practive and waits to load supreme page 30 seconds before drop
driver.get("https://www.google.com/recaptcha/api2/demo")
"""current_time = datetime.now()
while current_time.minute != 59 or current_time.second != 40:
    current_time = datetime.now()"""

# temporary sleep for testing
sleep(30)

# loads website and waits for a certain time before starting
driver.get("https://thechinatownmarket.com/")
"""current_time = datetime.now()                               # getting current time
while current_time.hour != 11:                              # wait for time to hit exactly 11:00
    driver.refresh()                                        # refresh page
    current_time = datetime.now()"""                           # get current time again
start_time = time()                                         # get start time once bot moves through site


# waits for item to load and clicks item
link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="ctm-l-s"]')))
link.click()


# waits for dropdown to load, selects size, and adds to cart
dropdown = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="SingleOptionSelector-0"]')))
select = Select(dropdown)
select.select_by_visible_text("LARGE")
driver.find_element_by_xpath('//*[@id="shopify-section-product"]/div/div/div[2]/form/div/button/span').click()


# waits for checkout button to load and clicks it
checkout = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MainContent"]/div/div/form/div[3]/input[2]')))
checkout.click()


# waits for first box to load, enters information, and clicks to shipping info
info = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_email"]')))
info.send_keys("johndoe@gmail.com" + Keys.TAB + Keys.TAB + \
               "John" + Keys.TAB + \
               "Doe" + Keys.TAB + \
               "1234 California St" + Keys.TAB + Keys.TAB + \
               "San Ramon" + Keys.TAB + Keys.TAB + \
               "C" + Keys.TAB + \
               "94582")
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button').click()


# close driver when done and print time
driver.close()                                              # closes driver at the end
print("~~~~~ Finished in {0:.2f} seconds ~~~~~"             # print out time elapsed
      .format(time() - start_time))                         # subtract current time from starting time
