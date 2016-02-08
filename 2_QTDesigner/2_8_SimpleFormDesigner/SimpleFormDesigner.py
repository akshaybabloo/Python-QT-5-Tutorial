# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimpleFormDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 249)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(150, 80, 401, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.edit = QtWidgets.QLineEdit(self.widget)
        self.edit.setObjectName("edit")
        self.horizontalLayout.addWidget(self.edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.change = QtWidgets.QLabel(self.widget)
        self.change.setObjectName("change")
        self.verticalLayout.addWidget(self.change)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Full Name"))
        self.change.setText(_translate("Dialog", "TextLabel"))

