# Email Sender

from email.message import EmailMessage
import ssl
import smtplib 


email_sender = 'otamendi1606@gmail.com'
email_password = 'ztmp ozyv qpsz cxsi'

email_receiver = "jaboyav342@othao.com"

subject = "Python Test Emails"
body = """
    When you watch a video, please hit subscribe and support the mission 
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

