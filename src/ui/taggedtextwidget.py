from PyQt5 import QtCore, QtWidgets
import re # Just for testing at the moment

class MQTaggedTextWidget(QtWidgets.QTextEdit):
    
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
        self.setReadOnly(True)

    #Einfach nur stur Textausgabe
    def setPlainText(self, text):
        # self.TextEdit.setHtml(text)
        self.setHtml(text)   
     
    #Wie sehen denn die Daten aus, die ich bekomme, anscheind ein string -.-
    def setTaggedData(self, data):
        text = ""
        for (token, tag) in data: 
            if tag == '.' or tag == ',' or tag == '!':
                text = text[:-1]
                text += token+" "
            else:
                text += token + " "
       
        self.setPlainText(text)
    
    def setTaggedData(self, data, tagvalue):
        text = ""
        for (token, tag) in data:
            if tag == '.' or tag == ',' or tag == '!':
                text = text[:-1]
                text += token+" "
            elif tagvalue == tag and (tag == '.' or tag == ',' or tag == '!'):
                text = text[:1]
                text += "<b>"+token+"</b> "
            elif tagvalue == tag:
                text += "<b>"+token+"</b> "
            else:
                text += token + " "

            self.setPlainText(text)
