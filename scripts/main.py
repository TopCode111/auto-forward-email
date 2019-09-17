import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

fp = webdriver.FirefoxProfile()
fp.set_preference("http.response.timeout", 5)
fp.set_preference("dom.max_script_run_time", 5)
driver = webdriver.Firefox(firefox_profile=fp)

#wait = WebDriverWait(driver, 10)
#wait.until(lambda driver: driver.current_url == "https://mail.yahoo.com")
driver.get('https://login.yahoo.com/?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.src%3Dfp')

driver.find_element_by_id('login-username').click()
driver.find_element_by_id('login-username').clear()
driver.find_element_by_id('login-username').send_keys("inafonar7721@yahoo.com")

#driver.find_element_by_name('browser-fp-data').send_keys("")

driver.find_element_by_id('login-signin').click()

#wait = WebDriverWait(driver, 1000)
#driver.get('https://login.yahoo.com/account/challenge/password?.src=ym&.lang=en-US&.intl=us&authMechanism=primary&display=login&done=https%3A%2F%2Fmail.yahoo.com%2Fd%3F.src%3Dfp&sessionIndex=QQ--&acrumb=YM4ilVw9')
driver.set_page_load_timeout(5)
time.sleep(5)
driver.find_element_by_id('login-passwd').click()
driver.find_element_by_id('login-passwd').clear()

driver.find_element_by_id('login-passwd').send_keys("VoCw0eecmjV")
next_btn1 = driver.find_element_by_xpath("//button[contains(@id,'login-signin') and contains(@name,'verifyPassword')]")
next_btn1.send_keys(Keys.RETURN)

driver.set_page_load_timeout(15)
time.sleep(15)
next_btn11 = driver.find_element_by_xpath("//span[contains(@data-test-id,'settings-link-label')]")
next_btn11.click()
time.sleep(5)
next_btn2 = driver.find_element_by_xpath("//a[contains(@data-test-id,'more-settings')]")
next_btn2.click()

driver.set_page_load_timeout(5)
time.sleep(5)

mailboxes = driver.find_element_by_xpath("//a[contains(@data-test-id,'settings-tab-1')]")
mailboxes.click()

time.sleep(5)
mailboxes_list = driver.find_element_by_xpath("//li[contains(@data-test-id,'accounts-list-item')]")
mailboxes_list.click()