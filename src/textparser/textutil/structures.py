from nltk.tokenize import PunktSentenceTokenizer

from textparser.textparser import *


class Sentence(object):
    """Describes one sentence.
    Args:
        one sentence
    """

    def __init__(self, textpart, my_id, parser, s_parser):
        self.id = my_id
        self.Text = textpart

        # nasty umlaut workaround
        self.Text = self.Text.encode('latin-1').decode('utf-8')
        self.Text = self.Text.replace("ä", "ae")
        self.Text = self.Text.replace("ö", "oe")
        self.Text = self.Text.replace("ü", "ue")

        """features"""
        self.sent_len = parser.get_sent_length(self.Text)
        self.avg_word_len = parser.get_word_length(self.Text)
        self.voc_complexity = parser.get_sent_voc_complexity(self.Text)
        self.nominals = parser.get_sent_nomins(self.Text)

        self.stanford_result = s_parser.get_sent_depth(self.Text)
        self.syntax_tree = self.stanford_result[0]
        # draw some happy trees with the following line
        # self.syntax_tree.draw()
        self.depth = self.stanford_result[1]


class Text(object):
    """Describes the whole text."""

    def __init__(self, text):
        # train PunktSentenceTokenizer to recognize abbreviations
        self.punkt = PunktSentenceTokenizer()
        abbrevs = "i.e., e.g., etc., Mr., Mrs.,"
        self.punkt.train(abbrevs)

        self.Parser = TextParser()
        self.StanfordParser = Stanford()
        # self.Sentences = self.split_text_and_work(text)
        self.Tokens = self.split_text(text)

        self.ProcessedTokens = 0
        self.TokensCount = len(self.Tokens)

        self.WordCount = 0

        self.Sentences = []

    def split_text_and_work(self, text):
        tokens = self.punkt.sentences_from_text(text)

        sentences = []

        count = 0

        for token in tokens:
            sentences.append(Sentence(token, count, self.Parser, self.StanfordParser))
            count += 1

        return sentences

    def split_text(self, text):
        tokens = self.punkt.sentences_from_text(text)

        return tokens

    def process_next_token(self):
        if self.TokensCount > (self.ProcessedTokens):
            self.Sentences.append(Sentence(self.Tokens[self.ProcessedTokens], self.ProcessedTokens,
                                           self.Parser, self.StanfordParser))

            self.WordCount += len(self.Parser.tokenizer.tokenize(self.Tokens[self.ProcessedTokens]))

            self.ProcessedTokens += 1
        else:
            return False

        return True
