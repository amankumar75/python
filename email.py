import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "amankumar919921@gmail.com"       # your gmail
APP_PASSWORD = "xwwrobytbnmrlvnv"         # your app password
RECEIVER = "pushkarmkr9128@gmail.com"     # receiver email

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello Dalla"
msg.set_content("This email was sent using Python SMTP...")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)

print("Email sent successfully!")
import smtplib
import ssl
from email.message import EmailMessage

EMAIL = "amankumar919921@gmail.com"       # your gmail
APP_PASSWORD = "xwwrobytbnmrlvnv"         # your app password
RECEIVER = "pushkarmkr9128@gmail.com"     # receiver email

msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello Dalla"
msg.set_content("This email was sent using Python SMTP...")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)

print("Email sent successfully!")
