import sys
from PyQt5.QtWidgets import QDialog, QFileDialog, QLabel, QApplication, QMainWindow, QSizePolicy
from PyQt5.QtCore import QTextStream, QFile, QIODevice
from PyQt5.QtGui import QImageReader, QImage, QPalette, QPixmap
from PyQt5 import QtCore, QtGui
from ui.ui_dialog import Ui_MainWindow
from textparser.textparser import TextParser
from textparser.textutil.structures import Text
from ui.taggedtextwidget import MQTaggedTextWidget


class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, tagged_data):
        super(MainApplication, self).__init__()

        # Load TextParser
        self.textParser = TextParser()

        # Set up the user interface from Designer.
        self.setupUi(self)

        #remove qttextWidget and setup own textwidget (detailview)
        self.verticalLayout.removeWidget(self.plainTextEdit)
        self.plainTextEdit.close()
        self.taggedTextWidget = MQTaggedTextWidget(self.centralwidget)
        self.taggedTextWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.verticalLayout.addWidget(self.taggedTextWidget)
        self.verticalLayout.update()

        #remove qttextWidget and setup own textwidget (documentview)
        self.gridLayout_9.removeWidget(self.textBrowser)
        self.textBrowser.close()
        self.taggedDocumentWidget = MQTaggedTextWidget(self.centralwidget)
        self.taggedDocumentWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout_9.addWidget(self.taggedDocumentWidget)
        self.gridLayout_9.update()

        #setup the slider
        #self.ViewSlider.setMaximum(1)
        #self.ViewSlider.actionTriggered.connect(self.updateView)


        self.tag = tagged_data

        self.actionText_ffnen.triggered.connect(self.open_text)

        # initilize features
        self.kompVokIsActive = False
        self.wlengthIsActive = False
        self.nomIsActive = False
        self.slenghtIsActive = False
        self.kompSatzIsActive = False

        self.kompVokWeight = 0
        self.wlengthWeight = 0
        self.nomWeight = 0
        self.slenghtWeight = 0
        self.kompSatzWeight = 0

        self.checkBoxKompVok.clicked.connect(self.updateFeatureWeights)
        self.checkBoxWortlaenge.clicked.connect(self.updateFeatureWeights)
        self.checkBoxSatzlaenge.clicked.connect(self.updateFeatureWeights)
        self.checkBoxNom.clicked.connect(self.updateFeatureWeights)
        self.checkBoxKompSatz.clicked.connect(self.updateFeatureWeights)

        self.sliderKompVok.actionTriggered.connect(self.updateFeatureWeights)
        self.sliderWortlaenge.actionTriggered.connect(self.updateFeatureWeights)
        self.sliderSatzlaenge.actionTriggered.connect(self.updateFeatureWeights)
        self.sliderKompSatz.actionTriggered.connect(self.updateFeatureWeights)
        self.sliderNom.actionTriggered.connect(self.updateFeatureWeights)

        self.updateFeatureWeights()

    def show_data(self):
        self.taggedTextWidget.showData(self.tag)

    def open_text(self):
        dialog = QFileDialog(self)
        dialog.setNameFilters([self.tr('Text Files (*.txt)'), self.tr('All Files (*)')])
        dialog.setDefaultSuffix('.txt')
        file_name = dialog.getOpenFileName(self, 'Open file')
        self.tag = Text(open(file_name[0]).read())
        self.show_data()

    def updateView(self):
        v = self.ViewSlider.sliderPosition()
        if v == 0:
            self.ActiveViewText.setText("Document")
        elif v == 1:
            self.ActiveViewText.setText("Words - Details")
        else:
            self.ActiveViewText.setText("No View available")

    def updateFeatureWeights(self):
        if self.checkBoxKompVok.isChecked():
            self.checkBoxKompVok.setText(str(self.sliderKompVok.sliderPosition()) + "%")
            self.kompVokIsActive = True
            self.kompVokWeight = self.sliderKompVok.sliderPosition()
        else:
            self.checkBoxKompVok.setText("-")
            self.kompVokIsActive = False
            self.kompVokWeight = 0

        if self.checkBoxKompSatz.isChecked():
            self.checkBoxKompSatz.setText(str(self.sliderKompSatz.sliderPosition()) + "%")
            self.kompSatzIsActive = True
            self.kompSatzWeight = self.sliderKompSatz.sliderPosition()
        else:
            self.checkBoxKompSatz.setText("-")
            self.kompSatzIsActive = False
            self.kompSatzWeight = 0

        if self.checkBoxNom.isChecked():
            self.checkBoxNom.setText(str(self.sliderNom.sliderPosition()) + "%")
            self.nomIsActive = True
            self.nomWeight = self.sliderNom.sliderPosition()
        else:
            self.checkBoxNom.setText("-")
            self.nomIsActive = False
            self.nomWeight = 0

        if self.checkBoxSatzlaenge.isChecked():
            self.checkBoxSatzlaenge.setText(str(self.sliderSatzlaenge.sliderPosition()) + "%")
            self.slenghtIsActive = True
            self.slenghtWeight = self.sliderSatzlaenge.sliderPosition()
        else:
            self.checkBoxSatzlaenge.setText("-")
            self.slenghtIsActive = False
            self.slenghtWeight = 0

        if self.checkBoxWortlaenge.isChecked():
            self.checkBoxWortlaenge.setText(str(self.sliderWortlaenge.sliderPosition()) + "%")
            self.wlengthIsActive = True
            self.wlengthWeight = self.sliderWortlaenge.sliderPosition()
        else:
            self.checkBoxWortlaenge.setText("-")
            self.wlengthIsActive = False
            self.wlengthWeight = 0




