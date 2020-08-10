from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



def SendEmail(senderEmail, senderPassword, recipientEmail, emailSubject, emailText):
#Must be a Gmail sender email
    fromaddr = senderEmail
    toaddr = recipientEmail
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = emailSubject
    
    body = emailText
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(senderEmail, senderPassword)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    
    
