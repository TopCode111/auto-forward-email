# Main Logic - If the script is run for the first time, create a text file "credentials.txt" and save the emailID and password 
# in it based on the input of the user. If the file already exists, parse the file to extract the email and password and call
# the main login script based on chosen service - Google/Yahoo

import os
import time
import getpass

def set_email(f):

	email = raw_input("Please enter your E-mail ID: ")

	time.sleep(1)

	email_confirm = raw_input('Please confirm your E-mail ID: ')

	if (email == email_confirm):

		print("\n**** E-mail ID Confirmed ****\n")
		time.sleep(2)
		f.write(email+"\n")
		return 1

	else:

		print("\n!!!! E-mail did not match. Please try again !!!!\n")
		return 0


def set_password(f):

	password = getpass.getpass('Please enter your Password (Nothing will appear on-screen when you type, for privacy reasons) : ')

	time.sleep(1)

	password_confirm = getpass.getpass('Please confirm your Password: ')

	if (password == password_confirm):

		print("\n**** Password Confirmed ****\n")
		time.sleep(2)
		f.write(password)
		return 1

	else:

		print("\n!!!! Password did not match. Please try again !!!!\n")
		return 0


def email_service():

	print("**** Please press 1 if you use Gmail or press 2 if you use Yahoo Mail ****\n")

	response = raw_input("Enter Response : ")

	if(int(response) == 1):

		print("\n**** You have selected Gmail!! ****\n")
		f = open("credentials.txt","w+")
		f.write("Gmail\n")
		f.close()

	else:

		if(int(response) == 2):

			print("\n**** You have selected Yahoo Mail!! ****\n")
			f = open("credentials.txt","w+")
			f.write("Yahoo\n")
			f.close()

	return int(response)


def login():

	f = open("credentials.txt","r+")
	service = f.readline().strip()
	email = f.readline().strip()
	password = f.readline()

	if(service=="Gmail"):
		run_string = "python autoLoginGmail.py " + email + " " + password

	else:
		run_string = "python autoLoginYahooMail.py " + email + " " + password


	os.system(run_string)


def main():

	if os.path.isfile("credentials.txt"):

		print("\n**** Welcome to Auto-Login! Your credentials are already set ****\n")
		time.sleep(2)
		login()

	else:

		print("\n**** Welcome to Auto-Login! This is a one time set-up for your Email Credentials ****\n")

		time.sleep(2)

		email_return_code = email_service()

		while email_return_code not in [1, 2] :

			print("\n**** Wrong Option. Please try again ****\n")
			email_return_code = email_service()

		f = open("credentials.txt","a+")

		time.sleep(2)

		return_code = set_email(f)

		while(return_code != 1):

			return_code = set_email(f)

		return_code1 = set_password(f)

		while(return_code1 != 1):

			return_code1 = set_password(f)

		f.close()

		print("\n**** Credentials set successfully !! Preparing to log you in ****")

		time.sleep(2)

		login()

main()