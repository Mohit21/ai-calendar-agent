
import smtplib
from email.mime.text import MIMEText

def send_email(body):
    msg = MIMEText(body)
    msg["Subject"] = "Today's Calendar Summary"
    msg["From"] = "mohitkumra95@gmail.com"
    msg["To"] = "mohitkumra95@gmail.com"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("mohitkumra95@gmail.com", "abpk fqfn itpf ryty")
    server.send_message(msg)
    server.quit()

