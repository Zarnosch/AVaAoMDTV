from PyQt5 import QtCore, QtWidgets
import re # Just for testing at the moment

class MQTaggedTextWidget(QtWidgets.QWidget):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.initUI()
    
    # Erstellt das TextEdit
    def initUI(self):
        
        self.setMinimumSize(300, 300)
        
        self.TextEdit = QtWidgets.QTextEdit(self)
        self.TextEdit.setMinimumSize(300, 300)
        self.TextEdit.setReadOnly(True)

    #Einfach nur stur Textausgabe
    def setPlainText(self, text):
        self.TextEdit.setHtml(text)
        
    #Wie sehen denn die Daten aus, die ich bekomme, anscheind ein string -.-
    def setTaggedData(self, data):
        list_of_tags = data
        self.setPlainText(str(list_of_tags))
         

