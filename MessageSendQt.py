import sys
import smtplib
from PyQt5 import QtGui
from PyQt5.QtWidgets import *


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title = "Danny's First Window"
		self.top = 100
		self.left = 100
		self.height = 680
		self.width = 600
		self.InitWindow()


	def InitWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top, self.left, self.width, self.height)
		
		button = QPushButton('Push this button', self)
		button.move(80, 500)
		button.setFixedWidth(130)
		button.clicked.connect(self.send_click)

		self.From = QLineEdit(self)
		self.From.move(80, 20)
		self.From.resize(500, 20)

		self.To = QLineEdit(self)
		self.To.move(80, 45)
		self.To.resize(500, 20)

		self.Subject = QLineEdit(self)
		self.Subject.move(80, 70)
		self.Subject.resize(500, 20)
		
		self.Body = QPlainTextEdit(self)
		self.Body.move(80, 100)
		self.Body.resize(500, 350)

		FromLabel = QLabel(self)
		FromLabel.setText("From:")
		FromLabel.move(15,15)

		ToLabel = QLabel(self)
		ToLabel.setText("To:")
		ToLabel.move(15, 40)

		SubjectLabel = QLabel(self)
		SubjectLabel.setText("Subject:")
		SubjectLabel.move(15, 63)
		
		self.show()

	def send_click(self):
		Sender = self.From.text()
		Recipient = self.To.text()
		SubjectLine = self.Subject.text()
		self.close()
		server = smtplib.SMTP( "smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(Sender, "Nighthawk16")
		EmailBody = "Subject: {}\n\n{}".format(SubjectLine, self.Body.toPlainText())
		server.sendmail(Sender, [Recipient], EmailBody)
		server.quit()




App = QApplication(sys.argv)

window = Window()
sys.exit(App.exec())
