import os
from builtins import print

import nltk
from nltk.corpus import brown
from nltk.parse.stanford import StanfordParser


class TextParser():
    def __init__(self):
        sent = "This is a sample sentence, nothing important here."
        self.tokens = nltk.word_tokenize(sent)

        brown_tagged_sents = brown.tagged_sents(categories="news")

        self.unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
        self.bigram_tagger = nltk.BigramTagger(brown_tagged_sents, backoff=self.unigram_tagger)

    def output(self):
        return str(self.bigram_tagger.tag(self.tokens)).strip('[]')


class Stanford():
    def __init__(self):
        # The Stanford Parser is required, download from http://nlp.stanford.edu/software/lex-parser.shtml and unpack somewhere
        # insert path to java.exe
        os.environ['JAVAHOME'] = 'C:/Program Files (x86)/Java/jdk1.8.0_60/bin/java.exe'
        # insert path to the directory containing stanford-parser.jar and stanford-parser-3.5.2-models.jar
        self.english_parser = StanfordParser(
            'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser.jar',
            'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar')

    def get_sent_depth(self, s, draw_tree):
        sentences = self.english_parser.raw_parse_sents((s,))
        # print(sentences)  # only prints <listiterator object> in this version

        # display the tree

        for line in sentences:
            for sentence in line:
                depth = str(sentence.height() - 1)
                print('The depth of the parse tree is ' + depth + '.')
                if draw_tree:
                    sentence.draw()

