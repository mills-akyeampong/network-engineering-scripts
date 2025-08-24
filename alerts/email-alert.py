
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