import sys

from PyQt5.QtWidgets import QApplication

from textparser.textparser import *
from ui.testqt import MainApplication

# setup nltk text parsing
textp = TextParser()

standford_parser = Stanford()
standford_parser.get_sent_depth("I don't even know why this is so deep.", False)

# setup qt app
app = QApplication(sys.argv)
frame = MainApplication(textp.output())
frame.show()
app.exec_()
