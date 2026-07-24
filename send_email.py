
import smtplib, ssl
import os


port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL') 
PASSWORD = os.environ.get('USER_PASSWORD')
message = """\
Subject: Github Email Report

Weekly email report.
"""

 # Create connection to SMTP server
context = ssl.create_default_context()                               
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)      # Sending from myself
    server.sendmail(USERNAME, USERNAME, message)   # Sending to myself
