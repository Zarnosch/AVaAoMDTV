import codecs

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QSizePolicy, QWidget, QMessageBox, QColorDialog

from ui.taggedtextwidget import MQTaggedTextWidget
from ui.text_worker import TextWorker
from ui.ui_dialog import Ui_MainWindow


class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()

        # Load TextParser
        # self.textParser = TextParser()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # connect Textedit buttons
        self.textEditApply.clicked.connect(self.applyAllText)
        self.textEditSave.clicked.connect(self.saveTextEdit)
        self.textEditApplyMarked.clicked.connect(self.applyChoosenText)
        self.spinBox.valueChanged.connect(self.setTextSize)
        self.setTextSize()

        # set default colors
        self.worstColor = QColor(173, 50, 31)
        self.neutralColor = QColor(255, 255, 255)
        self.bestColor = QColor(51, 71, 153)
        self.setWorstColorButton(self.worstColor)
        self.setNeutralColorButton(self.neutralColor)
        self.setBestColorButton(self.bestColor)

        # colorwidget
        self.colorDia = QColorDialog(self.neutralColor, self.centralwidget)
        # connect widget with buttons
        self.bestColorButton.clicked.connect(self.chooseBestColor)
        self.neutralColorButton.clicked.connect(self.chooseNeutralColor)
        self.worstColorButton.clicked.connect(self.chooseWorstColor)

        # open Buttons
        self.openButton_1.clicked.connect(self.open_text)
        self.openButton_2.clicked.connect(self.open_text)
        # progressBar
        self.progress = 0
        self.progressBar.setValue(self.progress)
        self.progressBar_2.setValue(self.progress)
        self.progressBar_3.setValue(self.progress)
        self.progressBar.setVisible(False)
        self.progressBar_2.setVisible(False)
        self.progressBar_3.setVisible(False)
        # print(self.progressBar.value)

        # numWords
        self.numWords.setText("0")

        # numSent
        self.numSent.setText("0")

        # Corpora
        # self.CorporaBox.addItem("Thriller")  # 0
        # self.CorporaBox.addItem("Kindertext")  # 1
        # self.CorporaBox.addItem("Nachrichten")  # 2
        # self.CorporaBox.addItem("Gesetzestexte")  # 3
        # self.activeCorporaIndex = 0
        # self.CorporaBox.activated.connect(self.updateCorpora)

        # remove qttextWidget and setup own textwidget (detailview)
        self.verticalLayout.removeWidget(self.plainTextEdit)
        self.plainTextEdit.close()
        self.taggedTextWidget = MQTaggedTextWidget(self.centralwidget, self)
        self.taggedTextWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.verticalLayout.addWidget(self.taggedTextWidget)
        self.verticalLayout.update()

        # remove qttextWidget and setup own textwidget (documentview)
        self.verticalLayout_3.removeWidget(self.plainTextEdit_2)
        self.plainTextEdit_2.close()
        self.taggedDocumentWidget = MQTaggedTextWidget(self.centralwidget, self)
        self.taggedDocumentWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout_9.addWidget(self.taggedDocumentWidget)
        self.gridLayout_9.update()

        # setup the slider
        # self.ViewSlider.setMaximum(1)
        # self.ViewSlider.actionTriggered.connect(self.updateView)

        # menue actions
        self.actionText_ffnen.triggered.connect(self.open_text)
        self.action_ber.triggered.connect(self.showAbout)
        self.actionDocumentView.triggered.connect(self.setActiveTabDocumentView)
        self.actionDetailView.triggered.connect(self.setActiveTabDetailView)
        self.actionChangeView.triggered.connect(self.changeView)
        self.actionSave.triggered.connect(self.saveTextEdit)

        # statusbar

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
        self.openButton_1.setEnabled(True)
        self.openButton_2.setEnabled(True)
        self.actionText_ffnen.setEnabled(True)
        self.textEditApply.setEnabled(True)
        self.textEditApplyMarked.setEnabled(True)
        self.textEditSave.setEnabled(True)
        self.progressBar.setVisible(False)
        self.progressBar_2.setVisible(False)
        self.progressBar_3.setVisible(False)

        self.tag = self.tag[0].FinishedText
        self.show_data()

        self.updateNumSent(len(self.tag.Sentences))
        self.updateNumWords(self.tag.WordCount)

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
        self.progressBar.setVisible(True)
        self.progressBar_2.setVisible(True)
        self.progressBar_3.setVisible(True)
        if file_name[0] != '':
            text = codecs.open(file_name[0], "r", "utf-8").read()
            # We need to create new TextWorker
            self.tag = (TextWorker(), QtCore.QThread())

            # prompt for custom common words list
            msg = QMessageBox()
            question = "Do you want to choose a custom list of domain specific common words?"
            reply = msg.question(self, 'Message', question, msg.Yes, msg.No)
            if reply == msg.Yes:
                dialog = QFileDialog(self)
                dialog.setNameFilters([self.tr('Text Files (*.txt)'), self.tr('All Files (*)')])
                dialog.setDefaultSuffix('.txt')
                file_name = dialog.getOpenFileName(self, 'Open file')
                self.tag[0].common_words_file = file_name[0]

            self.tag[0].TextToParse = text
            self.textEdit.setText(text)
            # Gray out all buttons
            self.openButton_1.setEnabled(False)
            self.openButton_2.setEnabled(False)
            self.actionText_ffnen.setEnabled(False)
            self.textEditApply.setEnabled(False)
            self.textEditApplyMarked.setEnabled(False)
            self.textEditSave.setEnabled(False)

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
        self.progressBar_3.setValue(int_value)

    def updateNumSent(self, int_value):
        self.numSent.setText(str(int_value))

    def updateNumWords(self, int_value):
        self.numWords.setText(str(int_value))

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
        # print(self.tabWidget.currentIndex())
        if self.tabWidget.currentIndex() == 0:
            self.tabWidget.setCurrentIndex(1)
        elif self.tabWidget.currentIndex() == 1:
            self.tabWidget.setCurrentIndex(0)

    def showAbout(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # msg.setTextFormat(QLabel.openExternalLinks);   #this is what makes the links clickable
        msg.setText("Applied Visualization and Analysis of Multivariate Datasets - Text Visualization")
        msg.setInformativeText("Git repository: " + "https://github.com/Zarnosch/AVaAoMDTV")
        msg.setWindowTitle("About")
        msg.setDetailedText(
            "Version: " + "0.1.0" + "\n \n" + "This Project is done in the context of Applied Visualization and Analysis of Multivariate Datasets at the"
                                              "OVGU University." + "\n \n" + "This tool can load .txt files and shows the readability difficulty.")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def setBestColorButton(self, color):
        r = str(color.red())
        g = str(color.green())
        b = str(color.blue())
        self.bestColorButton.setStyleSheet(
            "background-color: rgb(" + r + ", " + g + ", " + b + "); border: 1px dashed black; padding: 2px;")
        # self.bestColorButton.setStyleSheet("border: 1px solid black")

    def setNeutralColorButton(self, color):
        r = str(color.red())
        g = str(color.green())
        b = str(color.blue())
        self.neutralColorButton.setStyleSheet(
            "background-color: rgb(" + r + ", " + g + ", " + b + "); border: 1px dashed black; padding: 2px;")
        # self.neutralColorButton.setStyleSheet("border: 1px solid black")

    def setWorstColorButton(self, color):
        r = str(color.red())
        g = str(color.green())
        b = str(color.blue())
        self.worstColorButton.setStyleSheet(
            "background-color: rgb(" + r + ", " + g + ", " + b + "); border: 1px dashed black; padding: 2px;")
        # self.worstColorButton.setStyleSheet("border: 1px solid black")

    def chooseWorstColor(self):
        self.worstColor = QColorDialog.getColor(self.worstColor)
        self.setWorstColorButton(self.worstColor)
        self.taggedTextWidget.showDataNoWait(self.tag)
        self.taggedDocumentWidget.showDateNoWaitDetails(self.tag)

    def chooseNeutralColor(self):
        self.neutralColor = QColorDialog.getColor(self.neutralColor)
        self.setNeutralColorButton(self.neutralColor)
        self.taggedTextWidget.showDataNoWait(self.tag)
        self.taggedDocumentWidget.showDateNoWaitDetails(self.tag)

    def chooseBestColor(self):
        self.bestColor = QColorDialog.getColor(self.bestColor)
        self.setBestColorButton(self.bestColor)
        self.taggedTextWidget.showDataNoWait(self.tag)
        self.taggedDocumentWidget.showDateNoWaitDetails(self.tag)

    def getWorstColorHSL(self):
        return self.worstColor.getHsl()

    def getNeutralColorHSL(self):
        return self.neutralColor.getHsl()

    def getBestColorHSL(self):
        return self.bestColor.getHsl()

    def applyChoosenText(self):
        cursor = self.textEdit.textCursor()
        # cursor = QTextCursor()
        stext = cursor.selection()
        mtext = stext.toPlainText()
        self.applyTextEdit(mtext)

    def applyAllText(self):
        self.applyTextEdit(self.textEdit.toPlainText())

    def applyTextEdit(self, text):
        # Show loading page
        self.taggedTextWidget.stop()
        self.taggedTextWidget.showLoading()

        self.progressBar.setVisible(True)
        self.progressBar_2.setVisible(True)
        self.progressBar_3.setVisible(True)

        self.taggedDocumentWidget.stop()
        self.taggedDocumentWidget.showLoading()

        # We need to create new TextWorker
        self.tag = (TextWorker(), QtCore.QThread())

        # prompt for custom common words list
        msg = QMessageBox()
        question = "Do you want to choose a custom list of domain specific common words?"
        reply = msg.question(self, 'Message', question, msg.Yes, msg.No)
        if reply == msg.Yes:
            dialog = QFileDialog(self)
            dialog.setNameFilters([self.tr('Text Files (*.txt)'), self.tr('All Files (*)')])
            dialog.setDefaultSuffix('.txt')
            file_name = dialog.getOpenFileName(self, 'Open file')
            self.tag[0].common_words_file = file_name[0]

        self.tag[0].TextToParse = text
        # self.textEdit.setText(text)
        # Gray out all buttons
        self.openButton_1.setEnabled(False)
        self.openButton_2.setEnabled(False)
        self.actionText_ffnen.setEnabled(False)
        self.textEditApply.setEnabled(False)
        self.textEditApplyMarked.setEnabled(False)
        self.textEditSave.setEnabled(False)

        # Create Thread
        self.tag[1].objThread = QtCore.QThread()
        self.tag[0].moveToThread(self.tag[1])
        self.tag[0].finished.connect(self.tag[1].quit)
        self.tag[0].updated.connect(self.updateWorkerInfo);
        # self.tag[0].finished.connect(self.finishOpen)
        self.tag[1].started.connect(self.tag[0].longRunning)
        self.tag[1].finished.connect(self.finishOpen)

        self.tag[1].start()

    def saveTextEdit(self):
        filename = ""
        dialog = QFileDialog(self, 'Save File')
        dialog.setNameFilters([self.tr('Text Files (*.txt)'), self.tr('All Files (*)')])
        dialog.setDefaultSuffix('.txt')
        filename = dialog.getSaveFileName()
        file = filename[0]
        if not file.endswith('.txt'):
            file += ".txt"
        f = open(file, 'w')
        filedata = self.textEdit.toPlainText()
        f.write(filedata)
        f.close()

    def setTextSize(self):
        self.textEdit.setAcceptRichText(True)
        font = QFont()
        font.setPixelSize(self.spinBox.value())
        self.textEdit.setFont(font)


class CorpusChooser(QMessageBox, QWidget):
    def __init__(self):
        super(CorpusChooser, self).__init__()
        self.centralwidget = QtWidgets.QWidget(CorpusChooser)
        self.setIcon(QMessageBox.Information)
        self.setWindowTitle("Choose a Corpus")
        self.setText("Please choose a Corpus, which is needed to calculate the complexity of the Words in your text")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        print("1")
        # self.gridLayout.setObjectName("gridLayout")
        self.CorporaBox = QtWidgets.QComboBox(self.gridLayout)
        print("Fu")
        self.CorporaBox.setCurrentText("")
        self.CorporaBox.setObjectName("CorporaBox")
