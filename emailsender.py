import smtplib

#recipent 
to = input("Enter the email of receipient:\n")

#message
content = input("Enter content of email:\n")

#mainFunction
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',578) 
    server.ehlo()
    server.starttls()
    server.login('senderEmail@gmail.com','1234')
    server.sendmail('recipientemail@gmail.com',to,content)
    server.close()

sendEmail(to,content)    
