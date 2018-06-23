import os
import sys
import ttk
import sched
import time
import csv
import os.path
import threading
from threading import Thread
from threading import Timer
from Tkinter import *
from sys import argv
from tkFileDialog import askopenfilename 

window = Tk()
window.geometry('680x680')
window.title('Email Scheduler App')
window.resizable(width=False, height=False)

def browse_user():
    global user_name
    user_name = str(askopenfilename())
    file = open('scripts/user_file_path.txt', 'w')
    file.write(user_name)
    file.close()
    if(user_name != ''):
    	#status.config(text='File Uploaded')
	msg1.config(text=user_name)
    

def browse_mail_1():
    global mail_path
    mail_path = str(askopenfilename())
    file = open('scripts/mail_path_1.txt', 'w')
    file.write(mail_path)
    file.close()
    if(mail_path != ''):
	msg4.config(text=mail_path)

def browse_mail_2():
    global mail_path
    mail_path = str(askopenfilename())
    file = open('scripts/mail_path_2.txt', 'w')
    file.write(mail_path)
    file.close()
    if(mail_path != ''):
	msg8.config(text=mail_path)
    
def createuserthread(event):
	Thread(target=create_user,args=(event,)).start()

def create_user(event):
    os.system('python scripts\Load_User.py')
    with open ('scripts/Users_Created.txt','r') as f:
    	for line in f:
        	count = line.rstrip()
    if(count > 0):
    	msg2.config(text=count+' number of user(s) created')	
    else:      
    	msg2.config(text=count+' number of user(s) created')

def create_user1(event):
	msg2.config(text='Please wait user creation In Progress')

def schedule_delay():
        import Tkinter as tk
		
	class SampleApp1(tk.Tk):
		def __init__(self):
                    tk.Tk.__init__(self)
                    self.entry = tk.Entry(self)
                    label = Label(self, text="Enter the delay time (Seconds) to send mail")
                    self.button = tk.Button(self, text="OK", command=self.on_button)
		    
                    label.pack()
                    self.entry.pack()
                    self.button.pack()
		
		def on_button(self):
		    a = self.entry.get()
		    if a.isdigit():
		    	msg10.config(text=self.entry.get()+' seconds')
			msg11.config(text='Date and Delay set')
	            	file = open('scripts/delay_time.txt', 'w')
    		    	file.write(self.entry.get())
    		    	file.close()
		    	app1.destroy() 
                    else:
			msg10.config(text=self.entry.get())
			msg11.config(text='Oops! Provide valid input to set Delay')
			file = open('scripts/delay_time.txt', 'w')
    		    	file.write(self.entry.get())
		     	app1.destroy()

	app1 = SampleApp1()
	app1.mainloop()

def get_time_1():
	from datetime import datetime
	import Tkinter as tk
		
	class SampleApp(tk.Tk):
		def __init__(self):
                    tk.Tk.__init__(self)
                    self.entry = tk.Entry(self)
                    label = Label(self, text="Enter Date & Time: mm/dd/yy hh:mm(Military Time)")
                    self.button = tk.Button(self, text="OK", command=self.on_button)
		    
                    label.pack()
                    self.entry.pack()
                    self.button.pack()
		
		def on_button(self):
		    d1 = datetime.strptime(self.entry.get(), "%m/%d/%y %H:%M")
	            t = (d1-datetime.now()).total_seconds()
	            if(t>0):
		    	msg5.config(text=self.entry.get())
			msg6.config(text='Date Set')
		    	d1 = datetime.strptime(self.entry.get(), "%m/%d/%y %H:%M")
	            	t = (d1-datetime.now()).total_seconds()
		    	file = open('scripts/datetime1.txt', 'w')
    		    	file.write(str(t))
    		    	file.close()
		    	file1 = open('scripts/time1.txt', 'w')
    		    	file1.write(str(d1))
    		    	file1.close()
		    	app.destroy()
                    else:
		    	msg5.config(text=self.entry.get())
			msg6.config(text='Oops! Please provide valid Date/Time to schedule Email')
			d1 = datetime.strptime(self.entry.get(), "%m/%d/%y %H:%M")
	            	t = (d1-datetime.now()).total_seconds()
		    	file = open('scripts/datetime1.txt', 'w')
    		    	file.write(str(t))
    		    	file.close()
		    	file1 = open('scripts/time1.txt', 'w')
    		    	file1.write(str(d1))
    		    	file1.close()		
		     	app.destroy()

	app = SampleApp()
	app.mainloop()

def schedule_mail(event):
	import sched
    	import time
	import csv
	global t
	global date
	global time
	global count	
        with open('scripts/datetime1.txt','r') as f:
		for line in f:
    			t = float(line)
	if (t>0):

        	def job():
    			os.system('python scripts\Mail_CSV.py')
    			os.system('python scripts\Spring_Automail.py')
		
			count = 0

			with open('scripts/time1.txt','r') as f1:
				for line in f1:
					date, time = line.split()

			with open('scripts/Spring_User.csv','r') as f1:
				read_csv = csv.DictReader(f1)
				for line in read_csv:
					count = count + 1
			msg6.config(text= str(count) + ' number of Emails sent at '+ time + ' military time')

		Timer(t,job, ()).start()
		time.sleep(t)
	else:
		msg6.config(text= 'Sorry, you cannot schedule Email for the given Date/Time')

def schedule_time1(event):
	with open('scripts/datetime1.txt','r') as f:
		for line in f:
			time = line
	if (time > 0):
		with open('scripts/time1.txt','r') as f1:
			for line1 in f1:
				date, time1 = line1.split()
		msg6.config(text= 'Email(s) scheduled to send at '+ time1 + ' military time')
	else:
		pass

def schedule_time2(event):
	with open('scripts/datetime2.txt','r') as f:
		for line in f:
			time = line
	if(time>0):
		with open('scripts/time2.txt','r') as f:
			for line1 in f:
				date, time1 = line1.split()
		with open('scripts/delay_time.txt','r') as f1:
			for line2 in f1:
				delay = line2
		if delay.isdigit():
			msg11.config(text= 'Email(s) scheduled to send at '+ time1 + ' military time with '+delay+' seconds delay')	 
		else:
			pass
	else:
		pass

def get_time_2():
	from datetime import datetime
	import Tkinter as tk
		
	class SampleApp(tk.Tk):
		def __init__(self):
                    tk.Tk.__init__(self)
                    self.entry = tk.Entry(self)
                    label = Label(self, text="Enter Date & Time: mm/dd/yy hh:mm(Military Time)")
                    self.button = tk.Button(self, text="OK", command=self.on_button)
		    
                    label.pack()
                    self.entry.pack()
                    self.button.pack()
		
		def on_button(self):
		    d1 = datetime.strptime(self.entry.get(), "%m/%d/%y %H:%M")
	            t = (d1-datetime.now()).total_seconds()
	            if(t>0):
		    	msg9.config(text=self.entry.get())
			msg11.config(text='Date Set')
			d1 = datetime.strptime(self.entry.get(), "%m/%d/%y %H:%M")
	            	t = (d1-datetime.now()).total_seconds()
		    	file = open('scripts/datetime2.txt', 'w')
    		    	file.write(str(t))
    		    	file.close()
		    	file1 = open('scripts/time2.txt', 'w')
    		    	file1.write(str(d1))
    		    	file1.close()
		    	app.destroy()
		    else:
			msg9.config(text=self.entry.get())
			msg11.config(text='Oops! Please provide valid Date/Time to schedule Email')
		    	d1 = datetime.strptime(self.entry.get(), "%m/%d/%y %H:%M")
	            	t = (d1-datetime.now()).total_seconds()
		    	file = open('scripts/datetime2.txt', 'w')
    		    	file.write(str(t))
    		    	file.close()
		    	file1 = open('scripts/time2.txt', 'w')
    		    	file1.write(str(d1))
    		    	file1.close()
		    	app.destroy()              
		     
	app = SampleApp()
	app.mainloop()
	
def send_mail(event):
	import sched
    	import time
	import csv	
	global t
	global date
	global time1
	
    	with open('scripts/datetime2.txt','r') as f:
    		for line in f:
    			t = float(line)
	if(t>0):
		with open('scripts/delay_time.txt','r') as f2:
			for line in f2:
				delay = line
		if delay.isdigit():
    			
    			def job():
				count = 0
	    			os.system('python scripts/Mail_CSV_1.py')
    	    			os.system('python scripts/Spring_Automail1.py')
				with open('scripts/delay_time.txt','r') as f2:
					for line in f2:
						delay = line
				with open('scripts/Spring_User1.csv','r') as f1:
					read_csv = csv.DictReader(f1)
					for line in read_csv:
						count = count + 1
				
				with open('scripts/time2.txt','r') as f1:
					for line in f1:
						date, time1 = line.split()

				msg11.config(text= str(count) + ' number of Emails sent at '+ time1 + ' military time with'+delay+' seconds delay')
					

			Timer(t,job, ()).start()
			time.sleep(t)
			

		else:
			msg11.config(text= 'Sorry, you cannot schedule Email for this delay')
	else:
		msg11.config(text= 'Sorry, you cannot schedule Email for the given Date/Time')

def select_users():
	import ttk
	root = Tk()
	root.title('Choose User')
	root.geometry("+50+150")
	lines = []
	sum = 0
	with open ('scripts/Available_Users.txt','r') as f:
		for line in f:
			line = line.strip()
			lines.append(line)
			sum += 1
	yscroll = Scrollbar(root)
	yscroll.pack(side=RIGHT, fill=Y)
	lstbox = Listbox(root, selectmode=MULTIPLE,yscrollcommand=yscroll.set)	
	for i in range (0,sum):
		lstbox.insert(i,lines[i])
	lstbox.pack()
	yscroll.config(command=lstbox.yview)

	def select():
		if (os.path.isfile('scripts/Mail_User.txt')==TRUE):
			os.remove('scripts/Mail_User.txt')
    		else:
			pass
		res_list = list()
    		selection = lstbox.curselection()
    		for i in selection:
        		entry = lstbox.get(i)
			
        		res_list.append(entry)
    		for val in res_list:
        		with open ('scripts/Mail_User.txt','a') as file:
				file.write(val+ '\n')
		msg3.config(text=res_list)
		root.destroy()	
		
	btn = Button(root, text='OK', command=select)
	btn.pack()
	
	root.mainloop()

def select_users_1():
	import ttk
	root = Tk()
	root.title('Choose User')
	root.geometry("+50+150")
	lines = []
	sum = 0
	with open ('scripts/Available_Users.txt','r') as f:
		for line in f:
			line = line.strip()
			lines.append(line)
			sum += 1

	yscroll = Scrollbar(root)
	yscroll.pack(side=RIGHT, fill=Y)
	lstbox = Listbox(root, selectmode=MULTIPLE,yscrollcommand=yscroll.set)	
	for i in range (0,sum):
		lstbox.insert(i,lines[i])
	lstbox.pack()
	yscroll.config(command=lstbox.yview)

	def select():
		if (os.path.isfile('scripts/Mail_User1.txt')==TRUE):
			os.remove('scripts/Mail_User1.txt')
    		else:
			pass
		res_list = list()
    		selection = lstbox.curselection()
    		for i in selection:
        		entry = lstbox.get(i)
			
        		res_list.append(entry)
    		for val in res_list:
        		with open ('scripts/Mail_User1.txt','a') as file:
				file.write(val+ '\n')
		msg7.config(text=res_list)
		root.destroy()	
		
	btn = Button(root, text='OK', command=select)
	btn.pack()
	
	root.mainloop()

#Create User Account frame  
label1 = Label(window, text='CREATE USER ACCOUNTS', font='bold', bg='light blue', fg='black')
label2 = Label(window, text='File Path:')
label3 = Label(window, text='Status:')
msg1 = Label(window,text=' ')
msg2 = Label(window,text='No New Users Created')
button1 = Button(window, text='Select File', command=browse_user)
button2 = Button(window, text='Create Accounts')
button2.bind('<Button-1>',create_user1)
button2.bind('<ButtonRelease-1>',createuserthread)

#Initial E-Mails frame
label4 = Label(window, text='INITIAL EMAIL SETUP', font='bold', bg='light blue', fg='black')
label5 = Label(window, text='Selected Accounts:')
label6 = Label(window, text='Selected Email Script:')
label7 = Label(window, text='Initial Email Scheduled Date:')
label8 = Label(window, text='Status:')
msg3 = Label(window,text=' ')
msg4 = Label(window,text=' ')
msg5 = Label(window,text=' ')
msg6 = Label(window,text='No Emails Scheduled')
button3 = Button(window, text='Select Accounts', command=select_users)
button4 = Button(window, text='Select Email Script', command=browse_mail_1)
button5 = Button(window, text='Set Date', command=get_time_1)
button6 = Button(window, text='Schedule')
button6.bind('<Button-1>',schedule_time1)
button6.bind('<ButtonRelease-1>',schedule_mail)
label9 = Label(window, text='ONCE EMAIL SCHEDULED THE ACTION CANNOT BE UNDONE', fg='black', bg='yellow')

#Session E-Mail frame
label10 = Label(window, text='SESSION EMAIL SETUP',font='bold', bg='light blue', fg='black')
label11 = Label(window, text='Selected Accounts:')
label12 = Label(window, text='Selected Email Script:')
label13 = Label(window, text='Session Email Schedule Date:')
label14 = Label(window, text='Delay:')
label15 = Label(window, text='Status:')
msg7 = Label(window,text=' ')
msg8 = Label(window,text=' ')
msg9 = Label(window,text=' ')
msg10 = Label(window,text=' ')
msg11 = Label(window,text='No Emails Scheduled')
button7 = Button(window, text='Select Accounts', command=select_users_1)
button8 = Button(window, text='Select Email Script', command=browse_mail_2)
button9 = Button(window, text='Set Date', command=get_time_2)
button10 = Button(window, text='Set Delay', command=schedule_delay)
button11 = Button(window, text='Schedule')
button11.bind('<Button-1>',schedule_time2)
button11.bind('<ButtonRelease-1>',send_mail)
label16 = Label(window, text='ONCE EMAIL SCHEDULED THE ACTION CANNOT BE UNDONE', fg='black', bg='yellow')


#Status Bar frame
#status = Label(window, text='No File Chosen',bd=1,relief=SUNKEN,anchor=W)

#Create user account grid
label1.grid(row=0, column=1, sticky=W+E,pady=30)
label2.grid(row=1, sticky=W+E,pady=2)
label3.grid(row=2, sticky=W+E,pady=2)
msg1.grid(row=1, column=1,pady=2)
msg2.grid(row=2, column=1,pady=2)
button1.grid(row=1, column=2, sticky=W,pady=2)
button2.grid(row=2, column=2, sticky=W,pady=2)

#Initial E-Mails grid
label4.grid(row=3, column=1, sticky=W+E,pady=30)
label5.grid(row=4, sticky=W+E,pady=2)
label6.grid(row=5, sticky=W+E,pady=2)
label7.grid(row=6, sticky=W+E,pady=2)
label8.grid(row=7, sticky=W+E,pady=2)
msg3.grid(row=4, column=1,pady=2)
msg4.grid(row=5, column=1,pady=2)
msg5.grid(row=6, column=1,pady=2)
msg6.grid(row=7, column=1,pady=2)
button3.grid(row=4, column=2, sticky=W,pady=2)
button4.grid(row=5, column=2, sticky=W,pady=2)
button5.grid(row=6, column=2, sticky=W,pady=2)
button6.grid(row=7, column=2, sticky=W,pady=2)
label9.grid(row=8, column=1, sticky=W+E,pady=15)

#Session E-Mail grid
label10.grid(row=9, column=1, sticky=W+E, pady=30)
label11.grid(row=10, sticky=W+E,pady=2)
label12.grid(row=11, sticky=W+E,pady=2)
label13.grid(row=12, sticky=W+E,pady=2)
label14.grid(row=13, sticky=W+E,pady=2)
label15.grid(row=14, sticky=W+E,pady=2)
msg7.grid(row=10, column=1,pady=2)
msg8.grid(row=11, column=1,pady=2)
msg9.grid(row=12, column=1,pady=2)
msg10.grid(row=13, column=1,pady=2)
msg11.grid(row=14, column=1,pady=2)
button7.grid(row=10, column=2, sticky=W,pady=2)
button8.grid(row=11, column=2, sticky=W,pady=2)
button9.grid(row=12, column=2, sticky=W,pady=2)
button10.grid(row=13, column=2, sticky=W,pady=2)
button11.grid(row=14, column=2, sticky=W,pady=2)
label16.grid(row=15, column=1, sticky=W+E,pady=15)


#Configuring Buttons

button1.config(width=15, height=1)
button2.config(width=15, height=1)
button3.config(width=15, height=1)
button4.config(width=15, height=1)
button5.config(width=15, height=1)
button6.config(width=15, height=1)
button7.config(width=15, height=1)
button8.config(width=15, height=1)
button9.config(width=15, height=1)
button10.config(width=15, height=1)
button11.config(width=15, height=1)

#Column Color
row0column0 = Label(window, text='s', font='bold', fg='lightblue', bg='light blue')
row0column0.grid(row=0,column=0, sticky=W+E,pady=30)
row0column2 = Label(window, text='s', font='bold', fg='lightblue', bg='light blue')
row0column2.grid(row=0,column=2, sticky=W+E,pady=30)
row3column0 = Label(window, text='s', font='bold', fg='lightblue', bg='light blue')
row3column0.grid(row=3,column=0, sticky=W+E,pady=30)
row3column2 = Label(window, text='s', font='bold', fg='lightblue', bg='light blue')
row3column2.grid(row=3,column=2, sticky=W+E,pady=30)
row8column0 = Label(window, text='s', fg='yellow', bg='yellow')
row8column0.grid(row=8,column=0, sticky=W+E,pady=15)
row8column2 = Label(window, text='s',fg='yellow', bg='yellow')
row8column2.grid(row=8,column=2, sticky=W+E,pady=15)
row9column0 = Label(window, text='s', font='bold', fg='lightblue', bg='light blue')
row9column0.grid(row=9,column=0, sticky=W+E,pady=30)
row9column2 = Label(window, text='s', font='bold', fg='lightblue', bg='light blue')
row9column2.grid(row=9,column=2, sticky=W+E,pady=30)
row15column0 = Label(window, text='s', fg='yellow', bg='yellow')
row15column0.grid(row=15,column=0, sticky=W+E,pady=15)
row15column2 = Label(window, text='s',fg='yellow', bg='yellow')
row15column2.grid(row=15,column=2, sticky=W+E,pady=15)

#Status Bar grid
#status.grid(sticky=W)

window.grid_columnconfigure(0,weight=1)
window.grid_columnconfigure(1,weight=15)
window.grid_columnconfigure(2,weight=1)


window.mainloop()

