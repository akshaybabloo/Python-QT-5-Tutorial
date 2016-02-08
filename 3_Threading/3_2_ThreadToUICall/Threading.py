# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Threading.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(163, 61)
        self.pushMe = QtWidgets.QPushButton(Dialog)
        self.pushMe.setGeometry(QtCore.QRect(20, 20, 115, 32))
        self.pushMe.setObjectName("pushMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushMe.setText(_translate("Dialog", "PushButton"))

