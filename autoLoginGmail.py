from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

def login(email,password):

	# Telling the script which driver to pick, Chrome driver in this case
	driver = webdriver.Chrome();

	# Opening the specified URL
	driver.get("http://gmail.com")

	# Giving time to the browser to load the page
	driver.set_page_load_timeout(10)

	# Maximizing browser window
	driver.maximize_window()

	# Right click on the Email input field and click on inspect. Copy the name of the element. Now we have extracted the element and we can use it
	email_input = driver.find_element_by_name("identifier")

	# Populate the Email field to fill in the email address passed in to this function 
	email_input.send_keys(email)

	# Right click on the "Next" button and click on inspect. Here we use find_element_by_xpath to pass in multiple elements and extract the button
	next_btn = driver.find_element_by_xpath("//div[contains(@id,'identifierNext') and contains(@tabindex,'0')]") 

	# Basically pressing enter 
	next_btn.send_keys(Keys.RETURN)

	# Giving time for the page to load
	driver.set_page_load_timeout(5)

	time.sleep(2)

	# Following the same steps to input the password and pressing "Next"
	password_input = driver.find_element_by_name("password");

	password_input.send_keys(password);

	next_btn1 = driver.find_element_by_xpath("//div[contains(@id,'passwordNext')]")

	next_btn1.send_keys(Keys.RETURN)

	# Copies this block of code from StackOverflow to prevent closing of the script, and making it close only when enter is pressed
	user_choice = raw_input('Please click ENTER button to close script')
	if not user_choice:
		print("\n**** Thank You for using autoLogin ****\n")
		quit()


def main():

	if (len(sys.argv)!=3):

		print("Please provide Email and Password as arguments")

	else:

		print("\n**** Login Initiated ****\n")

		email = sys.argv[1]

		password = sys.argv[2]

		login(email,password)

main()