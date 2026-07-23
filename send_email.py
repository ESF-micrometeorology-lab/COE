
import smtplib, ssl
import os


port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL') 
PASSWORD = os.environ.get('USER_PASSWORD')
message = """\
Subject: Github Email REport

Weekly email report.
"""

contect = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)      # Sending from myself
    server.sendmail(USERNAME, USERNAME)   # Sending to myself
