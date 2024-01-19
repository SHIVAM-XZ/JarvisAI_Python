import smtplib
from email.mime.text import MIMEText # text to MIMEText object is then used as the body of the email.
from email.mime.multipart import MIMEMultipart

def Send_email(to_id,subject,message):
    sender_mail = "enter your email"
    sender_app_pass = "enter app password"
    receiver_mail = to_id

    try:
        msg = MIMEMultipart() # it is act as a container to hold a data
        msg['From'] = sender_mail
        msg['To'] = receiver_mail
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:# Python's built-in smtplib module to establish a connection with Gmail's SMTP server. We're doing this using the "with" statement, which automatically takes care of closing the connection when we're done with it.
        # 587 is commonly used as the default submission port for sending e-mail messages from a client to a server.
           server.starttls()
           server.login(sender_mail, sender_app_pass)
           server.sendmail(sender_mail, receiver_mail, msg.as_string())
           print("email sent successfully")

    except:
        print("error")
