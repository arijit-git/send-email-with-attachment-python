# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:47:23 2018

@author: Ray
"""

import smtplib

print(">>> Setting up email parameters...")
smtp_server = "smtp.gmail.com"
port = 587
from_email = "sender's email address"
to_email = "recipient's email address"
subject = "Test email from Python"
content = "Hello there ! I am coming from Python."
message = 'Subject: {}\n\n{}'.format(subject, content)
print(">>> Sending email now...")
mail = smtplib.SMTP(smtp_server,port)
mail.ehlo()
mail.starttls()
mail.login(from_email,"your gmail account password")
mail.sendmail(from_email, to_email, message)
print(">>> Email sent successfully!")
mail.quit()