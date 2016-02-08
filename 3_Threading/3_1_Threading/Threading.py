from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import sys

class Ui(QtWidgets.QDialog):
	def __init__(self):
		super(Ui, self).__init__()
		uic.loadUi('Threading.ui', self)

		# this will call the fun function
		self.pushMe.clicked.connect(self.fun)

		# instantiating class
		self.threading = Threading()

		# showing the app gui to user
		self.show()

	def fun(self):
		self.threading.start()
		QMessageBox.information(self, "Done!", "Done.")


# adding QThread class to this class
class Threading(QThread):
	def __init__(self):
		super(Threading, self).__init__()

	def run(self):
		# tem terminating the program
		time.sleep(6)
		print("sleep done")
		self.quit()  # quitting thread
		self.terminate()  # terminating th connection to threading

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Ui()
	sys.exit(app.exec_())
