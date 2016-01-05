import sys
from PyQt5.QtWidgets import QDialog, QFileDialog, QLabel, QApplication, QMainWindow, QSizePolicy, QWidget, QMessageBox, QComboBox, QAbstractButton, QRadioButton, QBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTextStream, QFile, QIODevice, QThread
from PyQt5.QtGui import QImageReader, QImage, QPalette, QPixmap
from PyQt5 import QtCore, QtGui
from ui.ui_dialog import Ui_MainWindow
from textparser.textparser import TextParser
from textparser.textutil.structures import Text
from ui.taggedtextwidget import MQTaggedTextWidget
from ui.text_worker import TextWorker
import pkg_resources


class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()

        # Load TextParser
        self.textParser = TextParser()

        # Set up the user interface from Designer.
        self.setupUi(self)
        # open Buttons
        self.openButton_1.clicked.connect(self.open_text)
        self.openButton_2.clicked.connect(self.open_text)

        #progressBar
        self.progress = 100
        self.progressBar.setValue(self.progress)
        self.progressBar_2.setValue(self.progress)
        #print(self.progressBar.value)

        #numWords
        self.numWords.setText("0")

        #numSent
        self.numSent.setText("0")

        #Corpora
        self.CorporaBox.addItem("Thriller") #0
        self.CorporaBox.addItem("Kindertext") #1
        self.CorporaBox.addItem("Nachrichten") #2
        self.CorporaBox.addItem("Gesetzestexte") #3
        self.activeCorporaIndex = 0
        self.CorporaBox.activated.connect(self.updateCorpora)

        #remove qttextWidget and setup own textwidget (detailview)
        self.verticalLayout.removeWidget(self.plainTextEdit)
        self.plainTextEdit.close()
        self.taggedTextWidget = MQTaggedTextWidget(self.centralwidget, self)
        self.taggedTextWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.verticalLayout.addWidget(self.taggedTextWidget)
        self.verticalLayout.update()

        #remove qttextWidget and setup own textwidget (documentview)
        self.verticalLayout_3.removeWidget(self.plainTextEdit_2)
        self.plainTextEdit_2.close()
        self.taggedDocumentWidget = MQTaggedTextWidget(self.centralwidget, self)
        self.taggedDocumentWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout_9.addWidget(self.taggedDocumentWidget)
        self.gridLayout_9.update()

        #setup the slider
        #self.ViewSlider.setMaximum(1)
        #self.ViewSlider.actionTriggered.connect(self.updateView)

        # menue actions
        self.actionText_ffnen.triggered.connect(self.open_text)
        self.action_ber.triggered.connect(self.showAbout)
        self.actionDocumentView.triggered.connect(self.setActiveTabDocumentView)
        self.actionDetailView.triggered.connect(self.setActiveTabDetailView)
        self.actionChangeView.triggered.connect(self.changeView)

        #statusbar

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

        # updating the css
        self.checkBoxKompVok.clicked.connect(self.sliderChanged)
        self.checkBoxWortlaenge.clicked.connect(self.sliderChanged)
        self.checkBoxSatzlaenge.clicked.connect(self.sliderChanged)
        self.checkBoxNom.clicked.connect(self.sliderChanged)
        self.checkBoxKompSatz.clicked.connect(self.sliderChanged)

        self.sliderKompVok.sliderReleased.connect(self.sliderChanged)
        self.sliderWortlaenge.sliderReleased.connect(self.sliderChanged)
        self.sliderSatzlaenge.sliderReleased.connect(self.sliderChanged)
        self.sliderKompSatz.sliderReleased.connect(self.sliderChanged)
        self.sliderNom.sliderReleased.connect(self.sliderChanged)

        self.setAllWeights(100)

    def show_data(self):
        self.taggedTextWidget.stop()
        self.taggedTextWidget.showData(self.tag)

        self.taggedDocumentWidget.stop()
        self.taggedDocumentWidget.showDataNoGeneration(self.tag)

    def finishOpen(self):
        self.tag = self.tag[0].FinishedText
        self.show_data()

    def updateWorkerInfo(self, value):
        self.updateProgressBar(value * 100.0)

    def open_text(self):
        # Show loading page
        self.taggedTextWidget.stop()
        self.taggedTextWidget.showLoading()

        self.taggedDocumentWidget.stop()
        self.taggedDocumentWidget.showLoading()

        dialog = QFileDialog(self)
        dialog.setNameFilters([self.tr('Text Files (*.txt)'), self.tr('All Files (*)')])
        dialog.setDefaultSuffix('.txt')
        file_name = dialog.getOpenFileName(self, 'Open file')
        if file_name[0] != '':
            text = open(file_name[0]).read()
            self.chooseCorpus()
            # We need to create new TextWorker
            self.tag = (TextWorker(), QtCore.QThread())
            self.tag[0].TextToParse = text

            # Create Thread
            self.tag[1].objThread = QtCore.QThread()
            self.tag[0].moveToThread(self.tag[1])
            self.tag[0].finished.connect(self.tag[1].quit)
            self.tag[0].updated.connect(self.updateWorkerInfo);
            # self.tag[0].finished.connect(self.finishOpen)
            self.tag[1].started.connect(self.tag[0].longRunning)
            self.tag[1].finished.connect(self.finishOpen)

            self.tag[1].start()

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



    def updateProgressBar(self, int_value):
        self.progressBar.setValue(int_value)
        self.progressBar_2.setValue(int_value)

    def updateNumSent(self, int_value):
        self.numSent.setText(str(int_value))

    def updateNumWords(self, int_value):
        self.numWords.sentText(str(int_value))

    def updateCorpora(self):
        self.activeCorporaIndex = self.CorporaBox.currentIndex()

    def setAllWeights(self, int_weight):
        if int_weight > 100 or int_weight < 0:
            int_weight = 0
        self.checkBoxKompVok.setChecked(True)
        self.checkBoxWortlaenge.setChecked(True)
        self.checkBoxSatzlaenge.setChecked(True)
        self.checkBoxNom.setChecked(True)
        self.checkBoxKompSatz.setChecked(True)

        self.sliderKompVok.setValue(int_weight)
        self.sliderWortlaenge.setValue(int_weight)
        self.sliderSatzlaenge.setValue(int_weight)
        self.sliderKompSatz.setValue(int_weight)
        self.sliderNom.setValue(int_weight)

        self.updateFeatureWeights()

    def sliderChanged(self):
        self.taggedTextWidget.showDataNoWait(self.tag)

    def setActiveTabDocumentView(self):
        self.tabWidget.setCurrentIndex(1)

    def setActiveTabDetailView(self):
        self.tabWidget.setCurrentIndex(0)

    def changeView(self):
        #print(self.tabWidget.currentIndex())
        if self.tabWidget.currentIndex() == 0:
            self.tabWidget.setCurrentIndex(1)
        elif self.tabWidget.currentIndex() == 1:
            self.tabWidget.setCurrentIndex(0)


    def showAbout(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        #msg.setTextFormat(QLabel.openExternalLinks);   #this is what makes the links clickable
        msg.setText("Applied Visualization and Analysis of Multivariate Datasets - Text Visualization")
        msg.setInformativeText("Git repository: " + "https://github.com/Zarnosch/AVaAoMDTV")
        msg.setWindowTitle("About")
        msg.setDetailedText("Version: " + "0.1.0" +"\n \n" + "This Project is done in the context of Applied Visualization and Analysis of Multivariate Datasets at the"
                                                    "OVGU University." + "\n \n" + "This tool can load .txt files and shows the readability difficulty.")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def chooseCorpus(self):
        #msg = CorpusChooser()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Choose a Corpus")
        msg.setText("Please choose a Corpus, which is needed to calculate the complexity of the Words in your text")
        #msg.addButton(QMessageBox.Accepted())

        retval = msg.exec_()

class CorpusChooser(QMessageBox,QWidget):
    def __init__(self):
        super(CorpusChooser, self).__init__()
        self.centralwidget = QtWidgets.QWidget(CorpusChooser)
        self.setIcon(QMessageBox.Information)
        self.setWindowTitle("Choose a Corpus")
        self.setText("Please choose a Corpus, which is needed to calculate the complexity of the Words in your text")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        print("1")
        #self.gridLayout.setObjectName("gridLayout")
        self.CorporaBox = QtWidgets.QComboBox(self.gridLayout)
        print("Fu")
        self.CorporaBox.setCurrentText("")
        self.CorporaBox.setObjectName("CorporaBox")






