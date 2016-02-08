#import sys
#from PyQt5.QtWidgets import QApplication, QDialog
#from Form import Ui_Dialog
#
#app = QApplication(sys.argv)
#window = QDialog()
#ui = Ui_Dialog()
#ui.setupUi(window)
#
#window.show()
#sys.exit(app.exec_())

#or

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Form import Ui_Dialog

class ImageDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(ImageDialog, self).__init__()
        
        # Set up the user interface from Designer.
        self.setupUi(self)


app = QApplication(sys.argv)
window = ImageDialog()
ui = Ui_Dialog()

window.show()
sys.exit(app.exec_())
