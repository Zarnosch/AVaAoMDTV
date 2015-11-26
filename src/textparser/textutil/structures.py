import re

class Word(object):
    """Describes a word.
    Args:
        one word
    """

    """this variable is shared across all instaces"""
    all_words

    def __init__(self, word):
        if all_words is None:
            all_words = 0
        else:
            all_words += 1

        self.id = all_words
        self.value = word
        self.word_length = len(word)
        self.tag = ""

    def __len__(self):
        return self.word_length

class Sent(object):
    """Describes one sentence.
    Args:
        one sentence
    """

    all_sents

    def __init__(self, sent):
        if all_sents is None:
            all_sents = 0
        else:
            all_sents += 1

        self.id = all_sents
        self.words = []
        self.syntax_trees = []

        """features"""
        self.sent_len = 0
        self.avg_word_len = 0
        self.voc_complexity = 0
        self.depth = 0
        self.nominals = 0

class Block(object):
    """Describes one block."""

    all_blocks

    def __init__(self):
        if all_blocks is None:
            all_blocks = 0
        else:
            all_blocks += 1

        self.id = all_blocks
        self.sents = []

class Text(object):
    """Describes the whole text."""

    def __init__(self, text):
        self.blocks = split_text(text)

    def split_text(self, text):
        return re.split(r"\.\s", text)
