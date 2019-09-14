from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

def login(email,password):

	driver = webdriver.Chrome();

	driver.get("http://login.yahoo.com")

	driver.set_page_load_timeout(10)

	driver.maximize_window()

	email_input = driver.find_element_by_name("username")

	email_input.send_keys(email)

	next_btn = driver.find_element_by_name("signin")

	next_btn.send_keys(Keys.RETURN)

	driver.set_page_load_timeout(5)

	time.sleep(2)

	password_input = driver.find_element_by_name("password");

	password_input.send_keys(password);

	next_btn1 = driver.find_element_by_xpath("//button[contains(@id,'login-signin') and contains(@name,'verifyPassword')]")

	next_btn1.send_keys(Keys.RETURN)

	user_choice = raw_input('Please click ENTER button to close script')
	if not user_choice:
		print("\n**** Thank You for using autoLogin ****\n")
		quit()


def main():

	#print("\n**** Login Initiated ****\n")

	email = "inafonar7721@yahoo.com"
	password = "VoCw0eecmjV"
	login(email,password)

main()

