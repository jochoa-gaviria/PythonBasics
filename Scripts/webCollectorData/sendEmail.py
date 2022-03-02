from email.mime.text import MIMEText
import smtplib

from cv2 import meanStdDev


def sendEmail(email, height, averageHeight):
    fromEmail = "pythont82@gmail.com"
    fromPassword = "python82prueba"
    toEmail = email

    subject = "Heigt data"
    message = "Hey there, your height is <strong>%s.</strong> and the height average of all is %s" %(height, averageHeight)
    try:
        msg = MIMEText(message, 'html')
        msg['Subject'] = subject
        msg['To']=toEmail
        msg['From']=fromEmail
        gmail=smtplib.SMTP('smtp.gmail.com', 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(fromEmail, fromPassword)
        gmail.send_message(msg)
    except:
        print('Err')
