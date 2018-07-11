#! python3
# sendEmailService.py

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import const
import codecs

def createMessage(from_addr, to_addrs,bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addrs
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg

def prepareSender(from_addr, my_password, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(from_addr, my_password)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

def sendEmail(TO_ADDRESS, SUBJECT, BODY):
    FROM_ADDRESS = 'xxx@gmail.com'
    MY_PASSWORD = 'XXXXXXX'
    BCC = 'xxx@gmail.com'
    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY

    msg = createMessage(FROM_ADDRESS, to_addr, BCC,subject, body)
    send(FROM_ADDRESS, MY_PASSWORD, to_addr, msg)


def sendEmailMock(TO_ADDRESS, SUBJECT, BODY):
    content = """TO_ADDRESS: {} 
    \nSUBJECT: {}  
    \nBODY: {}
    """.format(TO_ADDRESS,SUBJECT,BODY)
    file = codecs.open("../emailOutPutSample/emailOutPut.txt", "w", "utf_8_sig")
    file.write(content)
    file.close()
    return True
    
