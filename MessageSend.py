import smtplib
#I know I should import it as "import tkinter as tk" but I will work on that next.
from tkinter import *
# Establishing connection with gmail server
server = smtplib.SMTP( "smtp.gmail.com", 587)
server.starttls()
server.ehlo()
#Sending login info to connect
server.login( "bigdniquette@gmail.com", "---------" )
#GUI class 
class Email(Tk):

	def __init__(self, master):
		#Initialize all buttons with placements, sizes, and commands for button
		self.root = root
		self.root.title("Danny's Email Program")
		self.root.geometry("890x535")
		self.Label1 = Label(root, text="To: ")
		self.Label1.grid(row=0, column=1)
		self.Label2 = Label(root, text= "Subject: ")
		self.Label2.grid(row=1, column=1)
		self.Sendy = Entry(root)
		self.Sendy.grid(row=0, column=2, ipadx=300, sticky=W)
		self.Subject = Entry(root)
		self.Subject.grid(row=1, column=2, ipadx=300, sticky=W)
		self.Body = Text(root, relief="groove", bd=4, highlightcolor='DeepSkyBlue2')
		self.Body.grid(row=3, column=2, ipadx=4, ipady=40, sticky=W+E)
		self.Send = Button(root, text="Send", command = self.doEmail)
		self.Send.grid(row=5, column=2, ipadx=4)

	def doEmail(self):
		#Fetch text that is currently located in Entries and Text location
		Recipient = self.Sendy.get()
		SubjectLine = self.Subject.get()
		#Format string so that subject will appear in proper spot
		EmailBody = "Subject: {}\n\n{}".format(SubjectLine, self.Body.get("1.0", "end-1c"))
		from1 = "Danny Niquette"
		#send mail
		server.sendmail( from1 , [Recipient], EmailBody)
		#close GUI
		self.root.destroy()
		#quit server use
		server.quit()


root = Tk()
email_gui = Email(root)
root.mainloop()
