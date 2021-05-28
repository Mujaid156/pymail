import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'mujaid.kariem22@gmail.com'
receiver_email_id = 'thabosetsubi3@gmail.com'
password = input("Enter senders email password: ")

s.starttls()
s.login(sender_email_id, password)
message = "Hi, how are you doing today\n"
message = message + "What are you doing this weekend"
s.sendmail(sender_email_id, receiver_email_id, message)
s.quit()
