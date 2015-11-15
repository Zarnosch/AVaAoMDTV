# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\test02.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.taggedtextwidget import MQTaggedTextWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Datei_btn = QtWidgets.QPushButton(Dialog)
        self.Datei_btn.setObjectName("Datei_btn")
        self.horizontalLayout.addWidget(self.Datei_btn)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        #self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        #self.plainTextEdit.setObjectName("plainTextEdit")
        self.taggedTextWidget = MQTaggedTextWidget(Dialog)
        self.taggedTextWidget.setObjectName("taggedTextWidget")
        #self.verticalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout.addWidget(self.taggedTextWidget)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Datei_btn.setText(_translate("Dialog", "Datei"))
        self.pushButton_3.setText(_translate("Dialog", "PushButton"))
        self.pushButton.setText(_translate("Dialog", "show tagged"))

