
import smtplib
from email.mime.text import MIMEText

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Network Alert'
    msg['From'] = 'you@example.com'
    msg['To'] = 'admin@example.com'

    s = smtplib.SMTP('smtp.example.com', 587)
    s.starttls()
    s.login('you@example.com', 'yourpassword')
    s.sendmail('you@example.com', ['admin@example.com'], msg.as_string())
    s.quit()

send_alert("Interface Gi0/1 is DOWN on Switch1.")



#📬 4. Email Alert When Interface Goes Down
#📜 Script Summary

#Sends an email using SMTP if something like an interface failure is detected.

#🔍 Explanation

#smtplib: Sends email through an SMTP server.

#MIMEText: Formats plain-text email.

#starttls(): Secures the connection with encryption.

#Used to notify admins about outages.