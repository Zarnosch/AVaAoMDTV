import nltk
from nltk.corpus import brown

class TextParser():
    def __init__(self):
        sent = "Thist is a sample sentence, nothing important here."
        self.tokens = nltk.word_tokenize(sent)

        brown_tagged_sents = brown.tagged_sents(categories="news")

        self.unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
        self.bigram_tagger = nltk.BigramTagger(brown_tagged_sents, backoff=self.unigram_tagger)

    def output(self):
        return str(self.bigram_tagger.tag(self.tokens)).strip('[]')