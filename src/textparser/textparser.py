import codecs
import os
import string
from os.path import expanduser

import nltk
from nltk.parse.stanford import StanfordParser
from nltk.tokenize import RegexpTokenizer

home = expanduser("~")


class TextParser:
    def __init__(self):
        # default common words list
        self.common_words = set()

        self.noun_tags = {'NN', 'NNS', 'NNP', 'NNPS'}
        self.verb_tags = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

        self.tokenizer = RegexpTokenizer(r'\w+')

    def purify(self, polluted_text):
        """ remove non-printable chars but keep umlauts """
        purified_text = polluted_text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
        purified_text = ''.join(filter(lambda x: x in string.printable, purified_text))
        return purified_text

    def set_common_words(self, path_to_file):
        """ add a domain specific list of common words """
        if path_to_file != "":
            text = codecs.open(path_to_file, "r", "utf-8").read()
            tokenizer = RegexpTokenizer(r'\w+')

            self.common_words = set(tokenizer.tokenize(self.purify(text).lower()))

    def get_sent_length(self, s):
        length = len(self.tokenizer.tokenize(s))

        sent_length_feature_value = (length - 2) / 27

        if sent_length_feature_value < 0: return 0
        if sent_length_feature_value > 1: return 1
        return round(sent_length_feature_value, 2)

    def get_word_length(self, s):
        tokens = self.tokenizer.tokenize(s)
        length_sum = 0
        for word in tokens:
            length_sum += len(word)

        if length_sum > 0:
            average_length = length_sum / len(tokens)
        else:
            average_length = 0

        word_length_feature_value = (average_length - 2) / 4

        if word_length_feature_value < 0: return 0
        if word_length_feature_value > 1: return 1
        return round(word_length_feature_value, 2)

    def get_sent_voc_complexity(self, s):
        tokens = self.tokenizer.tokenize(s.lower())
        length = len(tokens)
        if length > 0:
            word_matches = 0
            for word in self.common_words:
                for token in tokens:
                    if token.lower() == word:
                        word_matches += 1
            complex_word_count = length - word_matches

            complexity = complex_word_count / length
        else:
            complexity = 1

        if complexity < 0: return 0
        if complexity > 1: return 1
        return round(complexity, 2)

    def get_sent_nomins(self, s):
        verb_count = 0
        noun_count = 0
        nomin_count = 0

        tokens = nltk.word_tokenize(s)
        tags = nltk.pos_tag(tokens)

        for word, tag in tags:
            if tag in self.verb_tags:
                verb_count += 1
            elif tag in self.noun_tags:
                noun_count += 1
                # count potential nominalized nouns via possible endings of nominalized words
                if word.endswith(('tion', 'sion', 'ment', 'ity', 'ness', 'cy')) \
                        and len(word) > 4:  # make sure short words are ignored, e.g. 'pity'
                    nomin_count += 1

        # add number of potential nominalizations to noun count, giving them more weight, so bigger is better
        nomin_compl = 4 if noun_count == 0 else (verb_count / (noun_count + nomin_count))

        nomin_compl_feature_value = 1 - (0.25 * nomin_compl)

        if nomin_compl_feature_value < 0: return 0
        if nomin_compl_feature_value > 1: return 1
        return round(nomin_compl_feature_value, 2)


class Stanford:
    def __init__(self):
        """ The Stanford Parser is required, download from http://nlp.stanford.edu/software/lex-parser.shtml and unpack somewhere """
        # insert path to java home
        if os.name == "nt":
            os.environ['JAVAHOME'] = 'C:\Program Files\Java\jdk1.8.0_66\bin\java.exe'
            # insert path to the directory containing stanford-parser.jar and stanford-parser-3.5.2-models.jar
            self.english_parser = StanfordParser(
                'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser.jar',
                'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar')
        elif os.name != "posix":
            os.environ['JAVAHOME'] = 'C:/Program Files (x86)/Java/jdk1.8.0_65/bin/java.exe'
            # insert path to the directory containing stanford-parser.jar and stanford-parser-3.5.2-models.jar
            self.english_parser = StanfordParser(
                'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser.jar',
                'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar')
        else:
            os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-1.8.0-openjdk-amd64'
            # insert path to the directory containing stanford-parser.ja and stanford-parser-3.5.2-models.jar
            self.english_parser = StanfordParser(
                expanduser("~") + '/lib/stanford-parser-full-2015-04-20/stanford-parser.jar',
                expanduser("~") + '/lib/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar')

    def get_sent_depth(self, s):
        # remove linebreaks for syntax tree
        s = s.replace('\n', ' ').replace('\r', ' ')

        sentence = self.english_parser.raw_parse(s)
        current_tree = None
        depth = 0

        for line in sentence:
            current_tree = line
            depth = line.height() - 1

        sent_depth_feature_value = (depth - 4) / 20

        if sent_depth_feature_value < 0: return current_tree, 0
        if sent_depth_feature_value > 1: return current_tree, 1
        return current_tree, round(sent_depth_feature_value, 2)
