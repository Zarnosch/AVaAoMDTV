import os
from os.path import expanduser
import nltk
from nltk.corpus import brown
from nltk.parse.stanford import StanfordParser
from nltk.tokenize import RegexpTokenizer

home = expanduser("~")


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
        # print("The sentence has ", length, "words.")

        sent_length_feature_value = length / 100

        if sent_length_feature_value < 0: return 0
        if sent_length_feature_value > 1: return 1
        return round(sent_length_feature_value, 2)

    def get_word_length(self, s):
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(s)
        length_sum = 0
        for word in tokens:
            length_sum += len(word)
        average_length = length_sum / len(tokens)
        # print("The average word length is ", average_length, ".")

        word_length_feature_value = (average_length - 2) / 6

        if word_length_feature_value < 0: return 0
        if word_length_feature_value > 1: return 1
        return round(word_length_feature_value, 2)

    def get_sent_voc_complexity(selfself, s):
        file = open("textparser/wordlist.txt").read()
        common_words = nltk.word_tokenize(file)
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(s)
        length = len(tokens)
        word_matches = 0
        for word in common_words:
            for token in tokens:
                if token.lower() == word:
                    word_matches += 1
        complex_word_count = length - word_matches

        complexity = complex_word_count / length

        # print(complex_word_count, " of ", length, " words in this sentence are not common, so the vocabular complexity is ", complexity, ".")

        if complexity < 0: return 0
        if complexity > 1: return 1
        return round(complexity, 2)

    def get_sent_nomins(self, s):
        verb_count = 0
        noun_count = 0
        nomin_count = 0

        noun_tags = {'NN', 'NNS', 'NNP', 'NNPS'}
        verb_tags = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
        tokens = nltk.word_tokenize(s)
        tags = nltk.pos_tag(tokens)

        for word, tag in tags:
            if tag in verb_tags:
                verb_count += 1
            elif tag in noun_tags:
                noun_count += 1
                # count potential nominalized nouns via possible endings of nominalized words
                # TODO: research most common nominalization endings
                if word.endswith(('tion', 'sion', 'ment', 'ity', 'ness', 'cy')) \
                        and len(word) > 4:  # make sure short words are ignored, e.g. 'pity'
                    nomin_count += 1

        # add number of potential nominalizations to noun count, giving them more weight, so bigger is better
        nomin_compl = 5 if noun_count == 0 else (verb_count / (noun_count + nomin_count))

        # print("The sentence has", verb_count, "verb(s) and", noun_count, "noun(s), \nverb/noun ratio: ",
        #       verb_noun_ratio, ", \nnominalizations: ", nomin_count)

        nomin_compl_feature_value = 1 - (0.2 * nomin_compl)

        if nomin_compl_feature_value < 0: return 0
        if nomin_compl_feature_value > 1: return 1
        return round(nomin_compl_feature_value, 2)

    def output(self):
        # Warum wurde das als String zurueck gegeben????
        # YOLO
        # return str(self.bigram_tagger.tag(self.tokens)).strip('[]')
        return self.bigram_tagger.tag(self.tokens)


class Stanford():
    def __init__(self):
        # The Stanford Parser is required, download from http://nlp.stanford.edu/software/lex-parser.shtml and unpack somewhere
        # insert path to java home
        if os.name != "posix":
            os.environ['JAVAHOME'] = 'C:/Program Files (x86)/Java/jdk1.8.0_65/bin/java.exe'
            # insert path to the directory containing stanford-parser.jar and stanford-parser-3.5.2-models.jar
            self.english_parser = StanfordParser(
                'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser.jar',
                'C:/Python34/Lib/site-packages/stanford-parser-full-2015-04-20/stanford-parser-3.5.2-models.jar')
        else:
            os.environ['JAVA_HOME'] = '/usr/lib/jvm/java-1.8.0-openjdk-amd64'
            # insert path to the directory containing stanford-parser.ja and stanford-parser-3.5.2-models.jar
            self.english_parser = StanfordParser(
                expanduser("~") + '/lib/stanford-parser-full-2015-12-09/stanford-parser.jar',
                expanduser("~") + '/lib/stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar')

    def get_sent_depth(self, s, draw_tree):
        sentence = self.english_parser.raw_parse(s)
        depth = 0
        for i in sentence:
            depth = i.height() - 1
            # print('The depth of the parse tree is ' + depth + '.')

            if draw_tree:
                i.draw()

        sent_depth_feature_value = (depth - 3) / 23

        if sent_depth_feature_value < 0: return 0
        if sent_depth_feature_value > 1: return 1
        return round(sent_depth_feature_value, 2)