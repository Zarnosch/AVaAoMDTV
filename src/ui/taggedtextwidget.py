from PyQt5 import QtCore, QtWidgets, QtWebKitWidgets
from PyQt5.QtWebKit import QWebSettings
from ui.htmlgen.generator import ViewGenerator
from textparser.textutil.structures import *

import os

import time

class MQTaggedTextWidget(QtWebKitWidgets.QWebView):

    def __init__(self, parent, app):
        self.taggedData = None
        self.app = app

        super().__init__(parent)
        self.initUI()

    # Erstellt das TextEdit
    def initUI(self):
        self.setMinimumSize(300, 300)

        #  self.TextEdit = QtWidgets.QTextEdit(self)
        # self.TextEdit.setMinimumSize(300, 300)
        # self.TextEdit.setReadOnly(True)

        # self.load(QtCore.QUrl('file:///'+os.getcwd()+"/generated_html/index.html"))

        QWebSettings.setMaximumPagesInCache(0)
        QWebSettings.setObjectCacheCapacities(0, 0, 0)

    def showData(self, data):
        QWebSettings.clearMemoryCaches()
        QWebSettings.clearIconDatabase()            
 
        ViewGenerator.generate_document_view(data, self.app)

        time.sleep(2)

        self.load(QtCore.QUrl('file:///'+os.getcwd()+"/generated_html/document_view.html"))

    def showDataNoGeneration(self, data):
        QWebSettings.clearMemoryCaches()
        QWebSettings.clearIconDatabase()

        ViewGenerator.generate_css(data)
        ViewGenerator.generate_html(data)

        time.sleep(2)

        self.load(QtCore.QUrl('file:///'+os.getcwd()+"/generated_html/index.html"))

    def showLoading(self):
        QWebSettings.clearMemoryCaches()
        QWebSettings.clearIconDatabase()

        self.load(QtCore.QUrl('file:///'+os.getcwd()+"/resources/loading.html"))

    def showDataNoWait(self, data):
        QWebSettings.clearMemoryCaches()
        QWebSettings.clearIconDatabase()

        ViewGenerator.generate_document_view(data, self.app)
        self.reload()
