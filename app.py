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
		"""
		CAN'T FINISH UNTIL OFFICIAL SITE POSTED
		method responsible for going to clothing category link, clicking clothing, selecting size, and adding to cart
		"""
		self.driver.get("https://supremenewyork.com/shop/"+category)
		link = self.wait_css('a[href*="{}"]'.format(name))
		link.click()
		# checks to see if size selection is necessary, waits for dropdown to load, selects size, and adds to cart
		if size != "OS":
			# CAN'T FINISH UNTIL SUPREME POSTS SITE; NEED XPATH
			dropdown = self.wait_xpath('//*[@id="SingleOptionSelector-0"]')
			select = Select(dropdown)
			select.select_by_visible_text(size)
			# CAN'T FINISH UNTIL SUPREME POSTS SITE; NEED XPATH
			driver.find_element_by_xpath('//*[@id="shopify-section-product"]/div/div/div[2]/form/div/button/span').click()
		else:
			# CAN'T FINISH UNTIL SUPREME POSTS SITE; NEED XPATH
			add_to_cart = self.wait_xpath('//*[@id="shopify-section-product"]/div/div[1]/div[2]/form/button')
			add_to_cart.click()

	def checkout(self, shipping, billing):
		"""
		CAN'T START UNTIL OFFICIAL SITE POSTED
		method responsible for going to checkout page and entering all info
		"""
		# self.driver.get(LINK_TO_SUPREME_CHECKOUT)
		# info = self.wait_xpath(XPATH_TO_FIRST_INFO_BOX)
		# info.send_keys(self.shipping["name"] + Keys.TAB + \
		# 				self.google["email"] + Keys.TAB + \
		# 				self.shipping["address"] + Keys.TAB + Keys.TAB + \
		# 				self.shipping["zip"] + Keys.TAB + \
		# 				self.shipping["city"] + Keys.TAB + \
		# 				self.shipping["state"] + Keys.TAB + \
		# 				"USA" + Keys.TAB + Keys.TAB + Keys.TAB \
		# 				self.billing["number"] + Keys.TAB + \
		# 				self.billing["expiration_month"] + Keys.TAB + \
		# 				self.billing["expiration_year"] + Keys.TAB + \
		# 				self.billing["cvv"])
		# accept = self.driver.find_element_by_xpath(XPATH_TO_TERMS_AND_SERVICES_BOX)
		# accpet.click()
		# checkout = self.driver.find_element_by_xpath(PATH_TO_CHECKOUT)
		# # checkout.click()

	def run(self):
		"""
		method which runs all parts of program together
		"""
		self.google_sign_in()
		self.wait_until(10, 59, 40, False)
		self.driver.get("https://www.supremenewyork.com/shop")
		self.wait_until(11, 00, 00, True)
		start_time = time()
		for name, [size, category] in self.clothing.items():
			self.add_item(name, size, category)
		self.driver.close()
		print("~~~~~ Finished in {0:.2f} seconds ~~~~~"
        .format(time() - start_time))


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

if __name__ == "__main__":
	Application().run()
