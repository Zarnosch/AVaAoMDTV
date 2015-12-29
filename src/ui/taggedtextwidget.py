from PyQt5 import QtCore, QtWidgets, QtWebKitWidgets
from ui.htmlgen.generator import ViewGenerator
from textparser.textutil.structures import *

import os

import time

class MQTaggedTextWidget(QtWebKitWidgets.QWebView):

    def __init__(self, parent):
        self.taggedData = None

        super().__init__(parent)
        self.initUI()

    # Erstellt das TextEdit
    def initUI(self):
        self.setMinimumSize(300, 300)

        #  self.TextEdit = QtWidgets.QTextEdit(self)
        # self.TextEdit.setMinimumSize(300, 300)
        # self.TextEdit.setReadOnly(True)

        # self.load(QtCore.QUrl('file:///'+os.getcwd()+"/generated_html/index.html"))

    def showData(self, data):
        ViewGenerator.generate_css(data)
        ViewGenerator.generate_html(data)

        time.sleep(2)

        self.load(QtCore.QUrl('file:///'+os.getcwd()+"/generated_html/index.html"))

    def showDataNoGeneration(self, data):
        time.sleep(2)
          
        self.load(QtCore.QUrl('file:///'+os.getcwd()+"/generated_html/index.html"))

    def showLoading(self):
        self.load(QtCore.QUrl('file:///'+os.getcwd()+"/resources/loading.html"))
