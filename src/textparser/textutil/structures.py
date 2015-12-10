import re
from nltk.tokenize import sent_tokenize
from textparser.textparser import *

class Sentence(object):
    """Describes one sentence.
    Args:
        one sentence
    """

    def __init__(self, textpart, my_id):
        self.id = my_id
        self.Text = textpart

        self.Parser = TextParser()
        self.StanfordParser = Stanford()

        """features"""
        self.sent_len = self.Parser.get_sent_length(self.Text)
        self.avg_word_len = self.Parser.get_word_length(self.Text)
        self.voc_complexity = self.Parser.get_sent_voc_complexity(self.Text)
        self.depth = 0.0 # self.StanfordParser.get_sent_depth(self.Text, False)
        self.nominals = self.StanfordParser.get_sent_nomins(self.Text)

class Text(object):
    """Describes the whole text."""

    def __init__(self, text):
        self.Sentences = self.split_text(text)

    def split_text(self, text):
        tokens = sent_tokenize(text)

        sentences = []
	
        count = 0

        for token in tokens:
            sentences.append(Sentence(token, count))
            count += 1

        return sentences
