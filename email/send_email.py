

import smtplib
#SERVER = "localhost"

FROM = 'asabeneh@gmail.com'

TO = ["washeraacademy@gmail.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

message = f"""\
From: {FROM}
To: {TO}
Subject:{SUBJECT}

{TEXT}
"""

# Send the mail

server = smtplib.SMTP('local')
server.sendmail(FROM, TO, message)
server.quit()
