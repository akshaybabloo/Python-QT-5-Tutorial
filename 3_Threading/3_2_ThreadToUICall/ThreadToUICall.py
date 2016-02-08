from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import sys
from Threading import Ui_Dialog



class Ui(QtWidgets.QDialog, Ui_Dialog):
	def __init__(self):
		super(Ui, self).__init__()
		self.setupUi(self)

		self.pushMe.clicked.connect(self.fun)

		self.threading = ThreadingIt()

		# self.connect(self.threading, self.signalCalled, Qt.DirectConnection)

		self.show()

	def fun(self):
		self.threading.start()
		QMessageBox.information(self, "Done!", "Done.")

	def signalCalled(self):
		QMessageBox.information(self, "yo!", "yo")


# adding QThread class to this class
class ThreadingIt(QThread):

	def __init__(self):
		super(ThreadingIt, self).__init__()

	def run(self):
		time.sleep(6)
		self.trigger.connect(name='signalCalled')
		self.trigger.emit()



if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Ui()
	sys.exit(app.exec_())
