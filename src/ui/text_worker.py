from PyQt5 import QtCore

from textparser.textutil.structures import Text


# import random

class TextWorker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    updated = QtCore.pyqtSignal(float)
    common_words_file = "textparser/wordlist.txt"
    TextToParse = None
    FinishedText = None

    def __init__(self):
        super(TextWorker, self).__init__()

    def longRunning(self):
        self.FinishedText = Text(self.TextToParse)  # SampleText()
        self.FinishedText.Parser.set_common_words(self.common_words_file)

        while self.FinishedText.process_next_token():
            self.updated.emit(self.FinishedText.ProcessedTokens / self.FinishedText.TokensCount)

        self.finished.emit()

# class SampleText(object):
# 	def __init__(self):
# 		self.Tokens = random.randrange(5,30)
# 		self.Sentences = []
# 		for id in range(0,10):
# 			self.Sentences.append(SampleSent(id))
#
# class SampleSent(object):
#     def __init__(self, id):
#         self.id = id
#         self.Text = "Construction started in 1963, and the freeway opened on December 18, 1970."
#         self.sent_len = round(random.random(),2)
#         self.avg_word_len = round(random.random(),2)
#         self.voc_complexity = round(random.random(),2)
#         self.depth = round(random.random(),2)
#         self.nominals = round(random.random(),2)
