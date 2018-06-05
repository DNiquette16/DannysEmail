import sys
import os.path
import smtplib
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title = "Danny's First Window"
		self.top = 100
		self.left = 500
		self.height = 680
		self.width = 600
		self.InitWindow()

	def __init__(self, Uname, Pword, email):
		super().__init__()

		self.title = "Danny's First Window"
		self.top = 100
		self.left = 100
		self.height = 680
		self.width = 600
		self.Uname = Uname
		self.Pword = Pword
		self.email = email
		self.InitWindow()

	def InitWindow(self):

		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		button = QPushButton('Send', self)
		button.move(80, 500)
		button.setFixedWidth(130)
		button.clicked.connect(self.send_click)
    
		self.To = QLineEdit(self)
		self.To.move(80, 45)
		self.To.resize(500, 20)

		self.Subject = QLineEdit(self)
		self.Subject.move(80, 70)
		self.Subject.resize(500, 20)

		ToLabel = QLabel(self)
		ToLabel.setText("To:")
		ToLabel.move(15, 40)

		SubjectLabel = QLabel(self)
		SubjectLabel.setText("Subject:")
		SubjectLabel.move(15, 63)

		self.Body = QPlainTextEdit(self)
		self.Body.move(80, 100)
		self.Body.resize(500, 350)

		self.show()

	def send_click(self):
    #Retrieve info from lineedits
		Recipient = self.To.text()
		SubjectLine = self.Subject.text()
		self.close()
    #determine which email server to send login info too
		if self.email == "gmail":
			self.server = smtplib.SMTP( "smtp.gmail.com", 587)
		elif self.email == "aol":
			self.server = smtplib.SMTP( "smtp.aol.com", 465)
		elif self.email== "yahoo":
			self.server = smtplib.SMTP( "smtp.mail.yahoo.com", 587)
    #finish sending email after we know which provider it is
		self.server.ehlo()
		self.server.starttls()
		self.server.ehlo()
		self.server.login(self.Uname, self.Pword)
		#format email body to be sent
		EmailBody = "Subject: {}\n\n{}".format(SubjectLine, self.Body.toPlainText())
		self.server.sendmail(self.Uname, [Recipient], EmailBody)
		self.server.quit()

#Login page before actual email editor
class Login(QDialog):
	def __init__(self):
		super().__init__()

		self.title = "Email Login"
		self.top = 500
		self.left = 100
		self.height = 200
		self.width = 350
		self.InitLogin()
#Initialize GUI for main page
	def InitLogin(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
    
    #Login button to check validity of user info
		Login = QPushButton('Login', self)
		Login.clicked.connect(self.login_click)
		Login.move(115, 130)
		Login.setFixedWidth(139)
    
		UsernameLabel = QLabel(self)
		UsernameLabel.setText("Username")
		UsernameLabel.move(50, 50)
   
		PasswordLabel = QLabel(self)
		PasswordLabel.setText("Password")
		PasswordLabel.move(50, 75)
    #Username entry
		self.Username = QLineEdit(self)
		self.Username.move(120, 50)
		self.Username.setFixedWidth(130)
    #Password Entry
		self.Password = QLineEdit(self)
		self.Password.move(120, 75)
		self.Password.setFixedWidth(130)
		self.Password.setEchoMode(QLineEdit.Password)
    #Checkbox to allow seeing your password
		self.ShowPword = QCheckBox("Show Password", self)
		self.ShowPword.move(120, 100)
		self.ShowPword.stateChanged.connect(self.showP)
    
		self.show()
  
  #Protocol for after login button is pushed
	def login_click(self):
    #Retrieving login info from entry boxes
		Uname = self.Username.text()
		Pword = self.Password.text()
    #Parsing username to find the email supplier and determine server name
		email = Uname.split('@')[1].split('.')[0]
    #3 cases so far for different email servers
		if email == "gmail":
			try: 
				self.server = smtplib.SMTP( "smtp.gmail.com", 587)
				self.server.ehlo()
				self.server.starttls()
				self.server.ehlo()
				self.server.login(Uname, Pword)
				self.window = Window(Uname, Pword, email)
				self.close()
			except:
				label1 = QLabel(self)
				label1.move(60, 170)
				label1.setText("Error: Incorrect Username or Password")
				label1.show()

		elif email == "yahoo":
			try:
				self.server = smtplib.SMTP( "smtp.mail.yahoo.com", 587)
				self.server.ehlo()
				self.server.starttls()
				self.server.ehlo()
				self.server.login(Uname, Pword)
				self.window = Window(Uname, Pword, email)
				self.close()
			except:
				label1 = QLabel(self)
				label1.move(60, 170)
				label1.setText("Error: Incorrect Username or Password")
				label1.show()
        
		elif email == "aol":
			try:
				self.server = smtplib.SMTP( "smtp.aol.com", 465)
				self.server.ehlo()
				self.server.starttls()
				self.server.ehlo()
				self.server.login(Uname, Pword)
				self.window = Window(Uname, Pword, email)
				self.close()
			except:
				label1 = QLabel(self)
				label1.move(60, 170)
				label1.setText("Error: Incorrect Username or Password")
				label1.show()
  #check if checkbox is checked and if it is, then show text and if not, then hide password
	def showP(self):

		if self.ShowPword.isChecked():
			self.Password.setEchoMode(QLineEdit.Normal)
		elif not self.ShowPword.isChecked():
			self.Password.setEchoMode(QLineEdit.Password)


App = QApplication(sys.argv)
login = Login()
sys.exit(App.exec())
