import sys
from PyQt5.QtWidgets import QDialog, QFileDialog, QLabel, QApplication, QMainWindow
from PyQt5.QtCore import QTextStream, QFile, QIODevice
from PyQt5.QtGui import QImageReader, QImage, QPalette, QPixmap
from PyQt5 import QtCore, QtGui
from ui.ui_dialog import Ui_MainWindow
from textparser.textparser import TextParser
from ui.taggedtextwidget import MQTaggedTextWidget

class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, tagged_data):
        super(MainApplication, self).__init__()

        # Load TextParser
        self.textParser = TextParser()

        # Set up the user interface from Designer.
        self.setupUi(self)

        #remove qttextWidget and setup own textwidget
        self.verticalLayout.removeWidget(self.plainTextEdit)
        self.plainTextEdit.close()
        self.taggedTextWidget = MQTaggedTextWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.taggedTextWidget)
        self.verticalLayout.update()


        self.tag = tagged_data
        self.updateBtn.clicked.connect(self.show_tagged)

        self.actionText_ffnen.triggered.connect(self.open_text)

    def show_tagged(self):
        self.taggedTextWidget.setTaggedData(self.tag, 'NN')

    def open_text(self):
        dialog = QFileDialog(self)
        dialog.setNameFilters([self.tr('Text Files (*.txt)'), self.tr('All Files (*)')])
        dialog.setDefaultSuffix('.txt')
        file_name = dialog.getOpenFileName(self, 'Open file')
        #file = QFile(file_name[0])
        #if not file.open(QIODevice.ReadOnly):
        #    QtGui.QMessageBox.information(None, 'info', file.errorString())
        #stream = QtCore.QTextStream(file)
        self.tag = self.textParser.tagText(open(file_name[0]).read())
        self.show_tagged()



