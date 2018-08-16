import json
from time import sleep,time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Application:
	
	def __init__(self):
		"""
		initializes driver
		loads configuration into self.info
		separates info into self. google, clothing, shipping, and billing
		"""
		self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
		self.info = self.load_configuration()
		self.google = self.info["google"]
		self.clothing = self.info["clothing"]
		self.shipping = self.info["shipping"]
		self.billing = self.info["billing"]


	@staticmethod
	def load_configuration():
		"""
		static method for efficiency
		loads json file into a dictionary used to separate all info
		"""
		with open("./config.json","r") as configuration:
			info = json.load(configuration)
			configuration.close()
		return info


	def wait_xpath(self, xpath):
		"""
		method responsible for waiting until an asset loads by xpath
		"""
		wait = WebDriverWait(self.driver, 20)
		return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


	def wait_css(self, css):
		"""
		method responsible for waiting until an asset loads by css_selector
		"""
		wait = WebDriverWait(self.driver, 20)
		return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))


	def wait_until(self, hour, minute, second, refresh=True):
		"""
		method responsible for waiting until a certain time
		if refresh is true, method will refresh driver for every iteration waited
		refresh is defaulted to True
		"""
		current_time = datetime.now()
		while current_time.hour != hour or current_time.minute != minute or current_time.second != second:
			if refresh:
				self.driver.refresh()
			current_time = datetime.now()


	def google_sign_in(self, email=None, password=None):
		"""
		method responsible for signing into google and loading captcha site
		email and password defaulted to None, in which case method gets from self.google
		loads each page, waits for elements to load, enters information, and goes to next page
		"""
		# enters email
		self.driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
		email_box = self.wait_xpath('//*[@id="identifierId"]')
		if email == None:
			email_box.send_keys(self.google["email"])
		else:
			email_box.send_keys(email)
		self.driver.find_element_by_xpath('//*[@id="identifierNext"]/content').click()
		# enters password
		password_box = self.wait_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
		if password == None:
			password_box.send_keys(self.google["password"])
		else:
			password_box.send_keys(password)
		self.driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
		# loads captcha site
		self.driver.get("https://www.google.com/recaptcha/api2/demo")


	def add_item(self, name, size, category):
		pass


	def checkout(self, shipping, billing):
		pass


	def run(self):
		"""
		method which runs all parts of program together
		"""
		self.google_sign_in()
		self.wait_until(18,12,20,False)
		self.driver.get("https://www.supremenewyork.com")
		self.wait_until(18,12,25)
		self.driver.close()


# driver = webdriver.Chrome("/usr/local/bin/chromedriver")    # starting chrome driver
# wait = WebDriverWait(driver, 20)                            # wait used for timing out loading
# with open("./config.json","r") as configuration:            # opening config.json
#     info = json.load(configuration)                        # loading data into info dict
#     configuration.close()                                   # closing config.json to avoid corruption

# # goes to google sign in, waits for email entry to load, enters email address, and clicks next
# driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
# email = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]')))
# email.send_keys(info["google"]["email"])
# driver.find_element_by_xpath('//*[@id="identifierNext"]/content').click()


# # waits for password entry to load, enters password, and clicks next
# password = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
# password.send_keys(info["google"]["password"])
# driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()


# # goes to captcha practive and waits to load supreme page 30 seconds before drop
# driver.get("https://www.google.com/recaptcha/api2/demo")
# """current_time = datetime.now()
# while current_time.minute != 59 or current_time.second != 40:
#     current_time = datetime.now()"""

# # temporary sleep for testing
# #sleep(5)

# # loads website and waits for a certain time before starting
# """current_time = datetime.now()                               # getting current time
# while current_time.hour != 11:                              # wait for time to hit exactly 11:00
#     driver.refresh()                                        # refresh page
#     current_time = datetime.now()"""                           # get current time again
# start_time = time()                                         # get start time once bot moves through site


# # iterates through clothing list in info dict; separates all variables by name, size, and category
# for name,[size,category] in info["clothing"].items():
#     # first goes to category page, then finds clothing with name in link and clicks it
#     driver.get("https://thechinatownmarket.com/collections/"+category)
#     link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="{}"]'.format(name))))
#     link.click()
#     # checks to see if size selection is necessary, waits for dropdown to load, selects size, and adds to cart
#     if size != "OS":
#         dropdown = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="SingleOptionSelector-0"]')))
#         select = Select(dropdown)
#         select.select_by_visible_text(size)
#         driver.find_element_by_xpath('//*[@id="shopify-section-product"]/div/div/div[2]/form/div/button/span').click()
#     else:
#         add_to_cart = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="shopify-section-product"]/div/div[1]/div[2]/form/button')))
#         add_to_cart.click()

# # waits for checkout button to load and clicks it
# checkout = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="MainContent"]/div/div/form/div[3]/input[2]')))
# checkout.click()


# # waits for first box to load, enters information, and clicks to shipping info
# shipping = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_email"]')))
# shipping.send_keys(info["google"]["email"] + Keys.TAB + Keys.TAB + \
#                info["shipping"]["first"] + Keys.TAB + \
#                info["shipping"]["last"] + Keys.TAB + \
#                info["shipping"]["street"] + Keys.TAB + Keys.TAB + \
#                info["shipping"]["city"] + Keys.TAB + Keys.TAB + \
#                info["shipping"]["state"] + Keys.TAB + \
#                info["shipping"]["zip"])
# driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button').click()


# # waits for continue to shipping button to load and clicks it
# continue_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/form/div[2]/button')))
# continue_button.click()


# # waits for payment info to load, enters information and clicks submit
# payment = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-header"]')))
# payment.send_keys(Keys.TAB + Keys.TAB + \
#                     info["billing"]["number"] + Keys.TAB + \
#                     info["shipping"]["first"] + " " + info["shipping"]["last"] + Keys.TAB + \
#                     info["billing"]["expiration"] + Keys.TAB + \
#                     info["billing"]["cvv"])
# submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/div/form/div[4]/div[1]/button')
# #submit.click() # uncomment to actually make purchase


# # close driver when done and print time
# driver.close()                                              # closes driver at the end
# print("~~~~~ Finished in {0:.2f} seconds ~~~~~"             # print out time elapsed
#       .format(time() - start_time))                         # subtract current time from starting time


if __name__ == "__main__":
	Application().run()
