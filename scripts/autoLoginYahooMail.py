from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

email_forward = 'rimalisa2019@gmail.com'


# timer define : start thread
def timer1(delay, repeat):
	while repeat < 2:
		time.sleep(delay)
		repeat += 1
		thread_one()
	print("First thread" + "completeed")
def timer2(delay, repeat):
	while repeat < 2:
		time.sleep(delay)
		repeat += 1
		thread_two()
	print("Second thread" + "completeed")


# auto login and setting forward emailing
def login(email,password):

	fp = webdriver.FirefoxProfile()
	fp.set_preference("http.response.timeout", 5)
	fp.set_preference("dom.max_script_run_time", 5)
	driver = webdriver.Firefox(firefox_profile=fp)
	driver.delete_all_cookies()
	#driver.get("http://login.yahoo.com/")
	driver.get(
		'https://login.yahoo.com/?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.src%3Dfp')

	driver.set_page_load_timeout(5)

	driver.maximize_window()


	email_input = driver.find_element_by_name("username")

	email_input.send_keys(email)

	next_btn = driver.find_element_by_name("signin")

	next_btn.send_keys(Keys.RETURN)

	driver.set_page_load_timeout(5)

	time.sleep(5)

	password_input = driver.find_element_by_name("password")

	password_input.send_keys(password)

	next_btn1 = driver.find_element_by_xpath("//button[contains(@id,'login-signin') and contains(@name,'verifyPassword')]")

	next_btn1.send_keys(Keys.RETURN)
# Setting on HomePage
	driver.set_page_load_timeout(15)
	time.sleep(15)
	setting_link = driver.find_element_by_xpath("//span[contains(@data-test-id,'settings-link-label')]")
	setting_link.click()
	time.sleep(5)
	more_setting = driver.find_element_by_xpath("//a[contains(@data-test-id,'more-settings')]")
	more_setting.click()
# mailboxes on Setting
	driver.set_page_load_timeout(5)
	time.sleep(5)

	mailboxes = driver.find_element_by_xpath("//a[contains(@data-test-id,'settings-tab-1')]")
	mailboxes.click()

	time.sleep(5)
	mailboxes_list = driver.find_element_by_xpath("//li[contains(@data-test-id,'accounts-list-item')]")
	mailboxes_list.click()

	time.sleep(5)

	email_input_forward = driver.find_element_by_name("stateForwardEmail")
	email_input_forward.clear()
	email_input_forward.send_keys(email_forward)
	time.sleep(5)
	verify_bt = driver.find_element_by_xpath("//button[contains(@data-test-id,'accounts-verify-forwarding-btn')]")
	verify_bt.send_keys(Keys.RETURN)

# Save Button

	time.sleep(5)
	save_bt = driver.find_element_by_xpath("//button[contains(@data-test-id,'edit-save-btn')]")
	save_bt.send_keys(Keys.RETURN)



# First thread
def thread_one():

		email = "comptamarsi8520@yahoo.com "

		password ="zMLO5Qne"

		login(email,password)


def thread_two():
	email = "terpdecroebu7793@yahoo.com "

	password = "O0VuIRxjx"

	login(email, password)


def main():
	email_number = 1
	t1 = Thread(target=timer1, args=(5, email_number))
	t2 = Thread(target=timer2, args=(5, email_number))
	t1.start()
	t2.start()

main()

