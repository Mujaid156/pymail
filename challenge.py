import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'mujaid.kariem22@gmail.com'
receiver_email_id = 'thabosetsubi3@gmail.com, tashwilla27@gmail.com, lizzystrachan99@gmail.com, thapelo@lifechoices.co.za'
password = input("Enter senders email password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = receiver_email_id
msg['Subject'] = subject
body = "Hi, how are you doing today\n"
body = body + "What are you doing this weekend"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

s.starttls()
s.login(sender_email_id, password)

s.sendmail(sender_email_id, receiver_email_id, text)
s.quit()
