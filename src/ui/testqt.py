import sys
from PyQt5.QtWidgets import QDialog, QFileDialog, QLabel, QApplication
from PyQt5.QtCore import QTextStream, QFile, QIODevice
from PyQt5.QtGui import QImageReader, QImage, QPalette, QPixmap
from PyQt5 import QtCore, QtGui
from ui.ui_dialog import Ui_Dialog


class MainApplication(QDialog, Ui_Dialog):
    def __init__(self, tagged_data):
        super(MainApplication, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        self.tag = tagged_data
        self.pushButton.clicked.connect(self.show_tagged)

        self.Datei_btn.clicked.connect(self.open_text)

    def show_tagged(self):
        self.plainTextEdit.setPlainText(self.tag)

    def open_text(self):
        dialog = QFileDialog(self)
        dialog.setNameFilters([self.tr('Text Files (*.txt)'), self.tr('All Files (*)')])
        dialog.setDefaultSuffix('.txt')
        file_name = dialog.getOpenFileName(self, 'Open file')
        #file = QFile(file_name[0])
        #if not file.open(QIODevice.ReadOnly):
        #    QtGui.QMessageBox.information(None, 'info', file.errorString())
        #stream = QtCore.QTextStream(file)
        self.tag = open(file_name[0]).read()



