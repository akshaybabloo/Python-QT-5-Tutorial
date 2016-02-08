import sys
from PyQt5.QtWidgets import QDialog, QApplication
from SimpleFormDesigner import Ui_Dialog

class Simple(QDialog, Ui_Dialog):
	def __init__(self):
		super(Simple, self).__init__()

		self.setupUi(self)

		# this will connect the text box to label
		self.edit.textEdited['QString'].connect(self.change.setText)

app = QApplication(sys.argv)
window = Simple()
ui = Ui_Dialog()

window.show()
sys.exit(app.exec_())
