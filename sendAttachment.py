# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:48:18 2018

@author: Ray
"""

# Python code to illustrate Sending mail with attachments
# from your Gmail account 
 
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# email variables
smtp_server = "smtp.gmail.com"
port = 587
from_email = "sender's email address"
password = 12345 # gmail account password
to_email = "recepient's email address"
subject = "Test email from Python"
content = "Hello there ! I am coming from Python."

print(">>> Preaparing to send email.")
# setting up the multipart email
msg = MIMEMultipart()  
msg['From'] = from_email 
msg['To'] = to_email
msg['Subject'] = subject
body = content
 
# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

print(">>> Opening file to be attached...")
# open the file to be sent 
filename = "test.png"
attachment = open("E:/Pics/test.png", "rb")
mb = MIMEBase('application', 'octet-stream')
# To change the payload into encoded form
mb.set_payload((attachment).read())
# encode into base64
encoders.encode_base64(mb)
mb.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(mb)
print(">>> File attached.")
# creates SMTP session
s = smtplib.SMTP(smtp_server, port)

# start TLS for security
s.starttls()
 
# Authentication
s.login(from_email, password)

# Converts the Multipart msg into a string
text = msg.as_string()
 
# sending the mail
s.sendmail(from_email, to_email, text)

print(">>> Email sent successfully!") 
# terminating the session
s.quit()