# sends 2 mails from isenbergtest to isenbergtest with a gap of 120 seconds
import csv
import time 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

#username_password = {'CEO@ou.edu' : 'YsH1OGITM' ,
#                     'CIO@ou.edu' : '9wNvMocwo' ,
#                     'COO@ou.edu' : '8Bqx9S5AX' }

with open('scripts/username.txt') as f1:
		for line1 in f1:
			uname = line1
	

input_file = csv.DictReader(open('scripts/Spring_User.csv'))
row_count = sum(1 for rows in input_file)
print row_count

input_file = csv.DictReader(open('scripts/Spring_User.csv'))
userID = []
body = []
subject = []
receive = []


for row in input_file:
    #print row['From Email']
    userID.append(row['From Email'])
    body.append(row['Body'])
    subject.append(row['Subject'])
    receive.append(row['Receiver'])


for i in range(row_count):
    print userID[i]
    
    msg = MIMEMultipart('')  
    receiver = receive[i]
    sender = userID[i]
    email_subject = subject[i]
    email_body = body[i]
    print email_subject
    print receiver
    print "START"
    msg['From'] = sender
    msg['To'] = receiver
    #','.join(address_book)
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_body, 'html'))
    text=msg.as_string()
   
#'Emailspam12'

# Send the message via our SMTP server
    s = smtplib.SMTP(uname)
    		#adminserverexc.ou.edu:2525') #465 #25 #587
    s.ehlo()
    s.starttls()
    s.sendmail(sender,receiver,text)
    print "END"
    s.quit()
    print "sleeping.."
    #time.sleep(10)




