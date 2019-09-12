import smtplib

sender = ""
recipient = ""
password = ""
subject = "Test email from Python"
text = "Hello from Python!\n How are you today?"

use_ssl=True
smtp_server = smtplib.SMTP_SSL("smtp.gmail.com",465)
print smtp_server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
smtp_server.sendmail(sender, recipient, message)
smtp_server.close()
