import smtplib
from email.message import EmailMessage

def send_progress_update(to_email, message):
    sender = "youremail@gmail.com"
    password = "yourpassword"

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = "AYUSH - User Emotional Progress"
    msg['From'] = sender
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
        print("Progress update sent.")
    except Exception as e:
        print("Error sending email:", e)
