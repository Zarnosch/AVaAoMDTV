from PyQt5.QtWidgets import QDialog, QFileDialog, QLabel
from PyQt5.QtGui import QImageReader, QImage, QPalette, QPixmap
from ui.ui_dialog import Ui_Dialog


class MainApplication(QDialog, Ui_Dialog):
    def __init__(self, tagged_data):
        super(MainApplication, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        self.tag = tagged_data
        self.pushButton.clicked.connect(self.show_tagged)

    def show_tagged(self):
        self.plainTextEdit.setPlainText(self.tag)
