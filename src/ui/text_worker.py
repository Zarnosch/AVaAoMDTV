from PyQt5 import QtCore
from textparser.textutil.structures import Text

class TextWorker(QtCore.QObject):
	finished = QtCore.pyqtSignal()
	updated = QtCore.pyqtSignal(float)

	TextToParse = None
	FinishedText = None

	def __init__(self):
		super(TextWorker, self).__init__()		

	def longRunning(self):
		self.FinishedText = Text(self.TextToParse)

		while self.FinishedText.process_next_token():
			self.updated.emit(self.FinishedText.ProcessedTokens / self.FinishedText.TokensCount)

		self.finished.emit()
