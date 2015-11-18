import sys

from PyQt5.QtWidgets import QApplication

from textparser.textparser import *
from ui.testqt import MainApplication

test_functions = True

# setup nltk text parsing
textp = TextParser()
standford_parser = Stanford()

# function tests
if test_functions:
    test_sentence = "Why is the rum gone?"
    print(test_sentence)
    textp.get_sent_length(test_sentence)
    textp.get_word_length(test_sentence)
    standford_parser.get_sent_depth(test_sentence, False)

# setup qt app
app = QApplication(sys.argv)
frame = MainApplication(textp.output())
frame.show()
app.exec_()
