import re
from nltk.tokenize import sent_tokenize
from textparser.textparser import *

class Sentence(object):
    """Describes one sentence.
    Args:
        one sentence
    """

    def __init__(self, textpart, my_id, parser, s_parser):
        self.id = my_id
        self.Text = textpart

        """features"""
        self.sent_len = parser.get_sent_length(self.Text)
        self.avg_word_len = parser.get_word_length(self.Text)
        self.voc_complexity = parser.get_sent_voc_complexity(self.Text)
        self.depth = s_parser.get_sent_depth(self.Text, False)
        self.nominals = parser.get_sent_nomins(self.Text)

class Text(object):
    """Describes the whole text."""

    def __init__(self, text):
        self.Parser = TextParser()
        self.StanfordParser = Stanford()

        self.Sentences = self.split_text(text)

    def split_text(self, text):
        tokens = sent_tokenize(text)

        sentences = []
	
        count = 0

        for token in tokens:
            sentences.append(Sentence(token, count, self.Parser, self.StanfordParser))
            count += 1

        return sentences
