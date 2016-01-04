from PyQt5 import QtCore
from textparser.textutil.structures import Text
import random

class TextWorker(QtCore.QObject):
	finished = QtCore.pyqtSignal()
	updated = QtCore.pyqtSignal(float)

	TextToParse = None
	FinishedText = None

	def __init__(self):
		super(TextWorker, self).__init__()

	def longRunning(self):
		self.FinishedText = SampleText() #Text(self.TextToParse)

		# while self.FinishedText.process_next_token():
		# 	self.updated.emit(self.FinishedText.ProcessedTokens / self.FinishedText.TokensCount)

		self.finished.emit()

class SampleText(object):
    def __init__(self):
        self.Sentences = [SampleSent(0), SampleSent(1), SampleSent(2), SampleSent(3)]


class SampleSent(object):
    def __init__(self, id):
        self.id = id
        self.Text = "Construction started in 1963, and the freeway opened on December 18, 1970."
        self.sent_len = round(random.random(),2)
        self.avg_word_len = round(random.random(),2)
        self.voc_complexity = round(random.random(),2)
        self.depth = round(random.random(),2)
        self.nominals = round(random.random(),2)
