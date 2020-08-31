import smtplib

#recipent 
to = input("Enter the email of receipent:\n")

#message
content = input("Enter content of email:\n")

#mainFunction
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',578) 
    server.ehlo()
    server.starttls()
    server.login('senderEmail@gmail.com','1234')
    server.sendmail('recipentemail@gmail.com',to,content)
    server.close()

sendEmail(to,content)    