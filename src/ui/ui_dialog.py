# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\testview2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 859)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.colorBar = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorBar.sizePolicy().hasHeightForWidth())
        self.colorBar.setSizePolicy(sizePolicy)
        self.colorBar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.colorBar.setObjectName("colorBar")
        self.gridLayout_2.addWidget(self.colorBar, 0, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_13.setHorizontalSpacing(6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridWidget_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget_2.sizePolicy().hasHeightForWidth())
        self.gridWidget_2.setSizePolicy(sizePolicy)
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit_2 = QtWidgets.QTextBrowser(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_3.addWidget(self.plainTextEdit_2)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.progressBar_2 = QtWidgets.QProgressBar(self.gridWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy)
        self.progressBar_2.setMinimumSize(QtCore.QSize(250, 0))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_12.addWidget(self.progressBar_2, 0, 1, 1, 1)
        self.openButton_2 = QtWidgets.QPushButton(self.gridWidget_2)
        self.openButton_2.setObjectName("openButton_2")
        self.gridLayout_12.addWidget(self.openButton_2, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_12)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_10.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_4.addLayout(self.gridLayout_10)
        self.gridLayout_9.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_13.addWidget(self.gridWidget_2, 0, 0, 2, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridWidget = QtWidgets.QWidget(self.tab_2)
        self.gridWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.openButton_1 = QtWidgets.QPushButton(self.gridWidget)
        self.openButton_1.setObjectName("openButton_1")
        self.gridLayout_11.addWidget(self.openButton_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_11.addWidget(self.label_2, 1, 0, 1, 1)
        self.numSent = QtWidgets.QLabel(self.gridWidget)
        self.numSent.setObjectName("numSent")
        self.gridLayout_11.addWidget(self.numSent, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_11.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.worstColorButton = QtWidgets.QPushButton(self.gridWidget)
        self.worstColorButton.setObjectName("worstColorButton")
        self.gridLayout_3.addWidget(self.worstColorButton, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_3, 3, 1, 1, 1)
        self.numWords = QtWidgets.QLabel(self.gridWidget)
        self.numWords.setObjectName("numWords")
        self.gridLayout_11.addWidget(self.numWords, 1, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(250, 0))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_11.addWidget(self.progressBar, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_11.addWidget(self.label_4, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridWidget)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_11.addWidget(self.label_6, 5, 0, 1, 1)
        self.bestColorButton = QtWidgets.QPushButton(self.gridWidget)
        self.bestColorButton.setObjectName("bestColorButton")
        self.gridLayout_11.addWidget(self.bestColorButton, 5, 1, 1, 1)
        self.neutralColorButton = QtWidgets.QPushButton(self.gridWidget)
        self.neutralColorButton.setObjectName("neutralColorButton")
        self.gridLayout_11.addWidget(self.neutralColorButton, 4, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_11)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBoxKompVok = QtWidgets.QCheckBox(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxKompVok.sizePolicy().hasHeightForWidth())
        self.checkBoxKompVok.setSizePolicy(sizePolicy)
        self.checkBoxKompVok.setText("")
        self.checkBoxKompVok.setChecked(False)
        self.checkBoxKompVok.setObjectName("checkBoxKompVok")
        self.gridLayout.addWidget(self.checkBoxKompVok, 1, 2, 1, 1)
        self.checkBoxWortlaenge = QtWidgets.QCheckBox(self.gridWidget)
        self.checkBoxWortlaenge.setText("")
        self.checkBoxWortlaenge.setChecked(False)
        self.checkBoxWortlaenge.setObjectName("checkBoxWortlaenge")
        self.gridLayout.addWidget(self.checkBoxWortlaenge, 1, 4, 1, 1)
        self.sliderWortlaenge = QtWidgets.QSlider(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderWortlaenge.sizePolicy().hasHeightForWidth())
        self.sliderWortlaenge.setSizePolicy(sizePolicy)
        self.sliderWortlaenge.setMaximum(100)
        self.sliderWortlaenge.setOrientation(QtCore.Qt.Vertical)
        self.sliderWortlaenge.setObjectName("sliderWortlaenge")
        self.gridLayout.addWidget(self.sliderWortlaenge, 2, 4, 1, 1)
        self.labelSatzlaenge = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSatzlaenge.sizePolicy().hasHeightForWidth())
        self.labelSatzlaenge.setSizePolicy(sizePolicy)
        self.labelSatzlaenge.setMinimumSize(QtCore.QSize(85, 0))
        self.labelSatzlaenge.setObjectName("labelSatzlaenge")
        self.gridLayout.addWidget(self.labelSatzlaenge, 0, 6, 1, 1)
        self.labelNom = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNom.sizePolicy().hasHeightForWidth())
        self.labelNom.setSizePolicy(sizePolicy)
        self.labelNom.setMinimumSize(QtCore.QSize(85, 0))
        self.labelNom.setObjectName("labelNom")
        self.gridLayout.addWidget(self.labelNom, 0, 5, 1, 1)
        self.sliderNom = QtWidgets.QSlider(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderNom.sizePolicy().hasHeightForWidth())
        self.sliderNom.setSizePolicy(sizePolicy)
        self.sliderNom.setMaximum(100)
        self.sliderNom.setOrientation(QtCore.Qt.Vertical)
        self.sliderNom.setObjectName("sliderNom")
        self.gridLayout.addWidget(self.sliderNom, 2, 5, 1, 1)
        self.labelKompVok = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelKompVok.sizePolicy().hasHeightForWidth())
        self.labelKompVok.setSizePolicy(sizePolicy)
        self.labelKompVok.setMinimumSize(QtCore.QSize(85, 0))
        self.labelKompVok.setObjectName("labelKompVok")
        self.gridLayout.addWidget(self.labelKompVok, 0, 2, 1, 1)
        self.labelKompSatz = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelKompSatz.sizePolicy().hasHeightForWidth())
        self.labelKompSatz.setSizePolicy(sizePolicy)
        self.labelKompSatz.setMinimumSize(QtCore.QSize(85, 0))
        self.labelKompSatz.setObjectName("labelKompSatz")
        self.gridLayout.addWidget(self.labelKompSatz, 0, 7, 1, 1)
        self.checkBoxKompSatz = QtWidgets.QCheckBox(self.gridWidget)
        self.checkBoxKompSatz.setText("")
        self.checkBoxKompSatz.setChecked(False)
        self.checkBoxKompSatz.setObjectName("checkBoxKompSatz")
        self.gridLayout.addWidget(self.checkBoxKompSatz, 1, 7, 1, 1)
        self.checkBoxNom = QtWidgets.QCheckBox(self.gridWidget)
        self.checkBoxNom.setText("")
        self.checkBoxNom.setChecked(False)
        self.checkBoxNom.setObjectName("checkBoxNom")
        self.gridLayout.addWidget(self.checkBoxNom, 1, 5, 1, 1)
        self.checkBoxSatzlaenge = QtWidgets.QCheckBox(self.gridWidget)
        self.checkBoxSatzlaenge.setText("")
        self.checkBoxSatzlaenge.setChecked(False)
        self.checkBoxSatzlaenge.setObjectName("checkBoxSatzlaenge")
        self.gridLayout.addWidget(self.checkBoxSatzlaenge, 1, 6, 1, 1)
        self.sliderSatzlaenge = QtWidgets.QSlider(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderSatzlaenge.sizePolicy().hasHeightForWidth())
        self.sliderSatzlaenge.setSizePolicy(sizePolicy)
        self.sliderSatzlaenge.setMaximum(100)
        self.sliderSatzlaenge.setOrientation(QtCore.Qt.Vertical)
        self.sliderSatzlaenge.setObjectName("sliderSatzlaenge")
        self.gridLayout.addWidget(self.sliderSatzlaenge, 2, 6, 1, 1)
        self.sliderKompSatz = QtWidgets.QSlider(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderKompSatz.sizePolicy().hasHeightForWidth())
        self.sliderKompSatz.setSizePolicy(sizePolicy)
        self.sliderKompSatz.setMaximum(100)
        self.sliderKompSatz.setOrientation(QtCore.Qt.Vertical)
        self.sliderKompSatz.setObjectName("sliderKompSatz")
        self.gridLayout.addWidget(self.sliderKompSatz, 2, 7, 1, 1)
        self.labelWortlaenge = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelWortlaenge.sizePolicy().hasHeightForWidth())
        self.labelWortlaenge.setSizePolicy(sizePolicy)
        self.labelWortlaenge.setMinimumSize(QtCore.QSize(85, 0))
        self.labelWortlaenge.setObjectName("labelWortlaenge")
        self.gridLayout.addWidget(self.labelWortlaenge, 0, 4, 1, 1)
        self.sliderKompVok = QtWidgets.QSlider(self.gridWidget)
        self.sliderKompVok.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderKompVok.sizePolicy().hasHeightForWidth())
        self.sliderKompVok.setSizePolicy(sizePolicy)
        self.sliderKompVok.setMaximum(100)
        self.sliderKompVok.setOrientation(QtCore.Qt.Vertical)
        self.sliderKompVok.setObjectName("sliderKompVok")
        self.gridLayout.addWidget(self.sliderKompVok, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QTextBrowser(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.gridLayout_4.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.gridLayout_8.addWidget(self.gridWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEditSave = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditSave.sizePolicy().hasHeightForWidth())
        self.textEditSave.setSizePolicy(sizePolicy)
        self.textEditSave.setObjectName("textEditSave")
        self.horizontalLayout_3.addWidget(self.textEditSave)
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy)
        self.progressBar_3.setMinimumSize(QtCore.QSize(250, 0))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_3.addWidget(self.progressBar_3)
        self.textEditApply = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditApply.sizePolicy().hasHeightForWidth())
        self.textEditApply.setSizePolicy(sizePolicy)
        self.textEditApply.setObjectName("textEditApply")
        self.horizontalLayout_3.addWidget(self.textEditApply)
        self.textEditApplyMarked = QtWidgets.QPushButton(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditApplyMarked.sizePolicy().hasHeightForWidth())
        self.textEditApplyMarked.setSizePolicy(sizePolicy)
        self.textEditApplyMarked.setObjectName("textEditApplyMarked")
        self.horizontalLayout_3.addWidget(self.textEditApplyMarked)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setProperty("value", 20)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 21))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuHilfe = QtWidgets.QMenu(self.menubar)
        self.menuHilfe.setObjectName("menuHilfe")
        self.menuAnsicht = QtWidgets.QMenu(self.menubar)
        self.menuAnsicht.setObjectName("menuAnsicht")
        MainWindow.setMenuBar(self.menubar)
        self.actionText_ffnen = QtWidgets.QAction(MainWindow)
        self.actionText_ffnen.setObjectName("actionText_ffnen")
        self.actionBlock = QtWidgets.QAction(MainWindow)
        self.actionBlock.setObjectName("actionBlock")
        self.actionDetail = QtWidgets.QAction(MainWindow)
        self.actionDetail.setObjectName("actionDetail")
        self.actionDocument = QtWidgets.QAction(MainWindow)
        self.actionDocument.setObjectName("actionDocument")
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionCorpus_2 = QtWidgets.QAction(MainWindow)
        self.actionCorpus_2.setObjectName("actionCorpus_2")
        self.actionKinderb_cher = QtWidgets.QAction(MainWindow)
        self.actionKinderb_cher.setObjectName("actionKinderb_cher")
        self.actionThriller = QtWidgets.QAction(MainWindow)
        self.actionThriller.setObjectName("actionThriller")
        self.actionGesetzestexte = QtWidgets.QAction(MainWindow)
        self.actionGesetzestexte.setObjectName("actionGesetzestexte")
        self.actionNachrichten = QtWidgets.QAction(MainWindow)
        self.actionNachrichten.setObjectName("actionNachrichten")
        self.actionKeine_Hilfe_f_r_dich_Swag = QtWidgets.QAction(MainWindow)
        self.actionKeine_Hilfe_f_r_dich_Swag.setObjectName("actionKeine_Hilfe_f_r_dich_Swag")
        self.action_ber = QtWidgets.QAction(MainWindow)
        self.action_ber.setObjectName("action_ber")
        self.actionDocumentView = QtWidgets.QAction(MainWindow)
        self.actionDocumentView.setObjectName("actionDocumentView")
        self.actionDetailView = QtWidgets.QAction(MainWindow)
        self.actionDetailView.setObjectName("actionDetailView")
        self.actionChangeView = QtWidgets.QAction(MainWindow)
        self.actionChangeView.setObjectName("actionChangeView")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuDatei.addAction(self.actionText_ffnen)
        self.menuDatei.addAction(self.actionSave)
        self.menuHilfe.addAction(self.action_ber)
        self.menuAnsicht.addAction(self.actionDocumentView)
        self.menuAnsicht.addAction(self.actionDetailView)
        self.menuAnsicht.addAction(self.actionChangeView)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuAnsicht.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Not Our Tool"))
        self.openButton_2.setText(_translate("MainWindow", "Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Detail View"))
        self.openButton_1.setText(_translate("MainWindow", "Open"))
        self.label_2.setText(_translate("MainWindow", "Words:"))
        self.numSent.setText(_translate("MainWindow", "output NumSent"))
        self.label_3.setText(_translate("MainWindow", "Sentences:"))
        self.worstColorButton.setText(_translate("MainWindow", "change Color"))
        self.numWords.setText(_translate("MainWindow", "output NumWords"))
        self.label_4.setText(_translate("MainWindow", "neutral Color:"))
        self.label.setText(_translate("MainWindow", "worst Color:"))
        self.label_6.setText(_translate("MainWindow", "best Color:"))
        self.bestColorButton.setText(_translate("MainWindow", "change Color"))
        self.neutralColorButton.setText(_translate("MainWindow", "change Color"))
        self.labelSatzlaenge.setText(_translate("MainWindow", "Sentencelength"))
        self.labelNom.setText(_translate("MainWindow", "Nominalization"))
        self.labelKompVok.setText(_translate("MainWindow", "Comp. Word"))
        self.labelKompSatz.setText(_translate("MainWindow", "Comp. Sentence"))
        self.labelWortlaenge.setText(_translate("MainWindow", "Wordlength"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Document View"))
        self.textEditSave.setText(_translate("MainWindow", "Save"))
        self.textEditApply.setText(_translate("MainWindow", "Apply"))
        self.textEditApplyMarked.setText(_translate("MainWindow", "Apply on marked"))
        self.label_7.setText(_translate("MainWindow", "Fontsize:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Editor"))
        self.menuDatei.setTitle(_translate("MainWindow", "File"))
        self.menuHilfe.setTitle(_translate("MainWindow", "Help"))
        self.menuAnsicht.setTitle(_translate("MainWindow", "View"))
        self.actionText_ffnen.setText(_translate("MainWindow", "Open"))
        self.actionText_ffnen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionBlock.setText(_translate("MainWindow", "Block"))
        self.actionDetail.setText(_translate("MainWindow", "Detail"))
        self.actionDocument.setText(_translate("MainWindow", "Document"))
        self.actionTest.setText(_translate("MainWindow", "Test"))
        self.actionCorpus_2.setText(_translate("MainWindow", "Corpus"))
        self.actionKinderb_cher.setText(_translate("MainWindow", "Kinderbücher"))
        self.actionThriller.setText(_translate("MainWindow", "Thriller"))
        self.actionGesetzestexte.setText(_translate("MainWindow", "Gesetzestexte"))
        self.actionNachrichten.setText(_translate("MainWindow", "Nachrichten"))
        self.actionKeine_Hilfe_f_r_dich_Swag.setText(_translate("MainWindow", "Keine Hilfe für dich! Swag!"))
        self.action_ber.setText(_translate("MainWindow", "About"))
        self.action_ber.setShortcut(_translate("MainWindow", "F12"))
        self.actionDocumentView.setText(_translate("MainWindow", "Document View"))
        self.actionDocumentView.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionDetailView.setText(_translate("MainWindow", "Detail View"))
        self.actionDetailView.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.actionChangeView.setText(_translate("MainWindow", "ChangeView"))
        self.actionChangeView.setShortcut(_translate("MainWindow", "Ctrl+Tab"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

