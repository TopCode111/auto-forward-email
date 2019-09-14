import yagmail
import smtplib
yag_smtp_connection = yagmail.SMTP(user="inafonar7721@yahoo.com", password = "VoCwOeecmjV", host ='smtp.mail.yahoo.com')

subject = "hello from richard"

contents = ['Hello tom this is', 'An image file is attached']

yag_smtp_connection.send('rimalisa2019@gmail.com', subject, contents)