import os
from builtins import print

import nltk
from nltk.corpus import brown
from nltk.parse.stanford import StanfordParser
from nltk.tokenize import RegexpTokenizer

class TextParser():
    def __init__(self):
        sent = "This is a sample sentence, nothing important here."
        self.tokens = nltk.word_tokenize(sent)
        brown_tagged_sents = brown.tagged_sents(categories="news")

        self.unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
        self.bigram_tagger = nltk.BigramTagger(brown_tagged_sents, backoff=self.unigram_tagger)

    def get_sent_length(self, s):
        tokenizer = RegexpTokenizer(r'\w+')
        length = len(tokenizer.tokenize(s))
        print("The sentence has ", length, "words.")
        return (s, length)
    
    def tagText(self, text):
        tokens = nltk.word_tokenize(text)
        
        return self.bigram_tagger.tag(tokens)

    def output(self):
        # Warum wurde das als String zurueck gegeben????
        # return str(self.bigram_tagger.tag(self.tokens)).strip('[]')
        return self.bigram_tagger.tag(self.tokens)


class Stanford():
    def __init__(self):
        # The Stanford Parser is required, download from http://nlp.stanford.edu/software/lex-parser.shtml and unpack somewhere
        # insert path to java home
        if os.name != "posix":
            os.environ['JAVAHOME'] = 'C:/Program Files (x86)/Java/jdk1.8.0_60/bin/java.exe'
            # insert path to the directory containing stanford-parser.jar and stanford-parser-3.5.2-models.jar
            self.english_parser = StanfordParser(
                'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser.jar',
                'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar')
        else:
            os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-1.8.0-openjdk-amd64'
            # insert path to the directory containing stanford-parser.ja and stanford-parser-3.5.2-models.jar
            self.english_parser = StanfordParser(
                '/lib/stanford-parser-full-2015-04-20/stanford-parser.jar',
                '/lib/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar')

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

    def get_sent_nomins(self, s):

        return
