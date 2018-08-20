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

	def wait_text(self, text):
		"""
		method responsible for waiting until an asset loads by link_text
		"""
		wait = WebDriverWait(self.driver, 20)
		return wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))


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
		# self.driver.get("https://www.google.com/recaptcha/api2/demo")

	def add_item(self, name, size, category, index):
		"""
		method responsible for going to clothing category link, clicking clothing, selecting size, and adding to cart
		"""
		self.driver.get("https://www.supremenewyork.com/shop/all/"+category)
		link = self.wait_text(name)
		link.click()
		if index != 1:
			colour = self.wait_xpath('//*[@id="details"]/ul/li[{}]'.format(index))
			colour.click()
		# checks to see if size selection is necessary, waits for dropdown to load, selects size, and adds to cart
		if size != "OS":
			dropdown = self.wait_xpath('//*[@id="s"]')
			select = Select(dropdown)
			select.select_by_visible_text(size)
			add_to_cart = self.wait_xpath('//*[@id="add-remove-buttons"]/input')
		else:
			add_to_cart = self.wait_xpath('//*[@id="add-remove-buttons"]/input')
		# adds item to cart after selection has been made
		add_to_cart.click()

	def checkout(self):
		"""
		method responsible for going to checkout page and entering all info
		"""
		# finds first info box and sends all keys
		info = self.wait_xpath('//*[@id="order_billing_name"]')
		info.send_keys(self.shipping["name"] + Keys.TAB + \
						self.google["email"] + Keys.TAB + \
						self.shipping["phone"] + Keys.TAB + \
						self.shipping["street"] + Keys.TAB + Keys.TAB + \
						self.shipping["zip"] + Keys.TAB*5 + \
						self.billing["number"] + Keys.TAB + \
						self.billing["expiration_month"] + Keys.TAB + \
						self.billing["expiration_year"] + Keys.TAB + \
						self.billing["cvv"])
		# finds accept checkbox and clicks
		accept = self.driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins')
		accept.click()

	def run(self):
		"""
		method which runs all parts of program together
		"""
		self.google_sign_in()
		self.wait_until(10, 59, 57, False)
		self.driver.get("https://www.supremenewyork.com/shop/all")
		self.wait_until(11, 00, 00, True)
		start_time = time()
		for name, [size, category, index] in self.clothing.items():
			self.add_item(name, size, category, index)
		sleep(1)
		self.driver.get("https://www.supremenewyork.com/checkout")
		self.checkout()
		print("~~~~~ Finished in {0:.2f} seconds ~~~~~"
        .format(time() - start_time))
		sleep(60)


if __name__ == "__main__":
	Application().run()
