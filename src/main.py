import sys
import time

from PyQt5.QtWidgets import QApplication

from textparser.textparser import *
from ui.testqt import MainApplication

test_functions = True

# setup nltk text parsing
textp = TextParser()
standford_parser = Stanford()

# function tests
if test_functions:
    test_sentence = "The use of drugs is dangerous."
    print("Test sentence: \"", test_sentence, "\"\n")
    t = time.time()

    textp.get_sent_length(test_sentence)
    textp.get_word_length(test_sentence)
    textp.get_sent_voc_complexity(test_sentence)
    standford_parser.get_sent_depth(test_sentence, False)
    standford_parser.get_sent_nomins(test_sentence)

    print("\nAnalyzing the sentence took", time.time() - t,
          "seconds.")  # should be < 1 second for now, to be optimized later

# setup qt app
app = QApplication(sys.argv)
frame = MainApplication(textp.output())
frame.show()
app.exec_()
