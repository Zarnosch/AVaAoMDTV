import sys
from PyQt5.QtWidgets import QApplication
from ui.testqt import MainApplication
from textparser.textparser import TextParser

# setup nltk text parsing
textp = TextParser()

# setup qt app
app = QApplication(sys.argv)
frame = MainApplication(textp.output())
frame.show()
app.exec_()

