import sys
import time
from PyQt5.QtWidgets import QApplication
from textparser.textparser import *
from ui.testqt import MainApplication

# turn feature tests on/off
test_features = False

test_wlength = False
test_compl = False
test_nomi = True
test_slength = False
test_depth = False

# setup nltk text parsing
textp = TextParser()
stanford_parser = Stanford()

# function tests
if test_features:
    t = time.time()

    # easy texts
    text = open('../texts/easy/it_could_happen.txt').read()
    # text = open('../texts/easy/the_halloween_house.txt').read()
    # text = open('../texts/easy/the_little_gingerbread_man.txt').read()
    # text = open('../texts/easy/who_did_patricks_homework.txt').read()

    # hard texts
    # text = open('../texts/hard/black_and_white_and_everything_in_between.txt').read()
    # text = open('../texts/hard/fight_terrorism.txt').read()
    # text = open('../texts/hard/jura_paper.txt').read()
    # text = open('../texts/hard/paper_medicine.txt').read()
    # text = open('../texts/hard/poems.txt').read()
    # text = open('../texts/hard/political_english_text.txt').read()



    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences_ntlk = sent_detector.tokenize(text.strip())

    wlength_lst = []
    compl_lst = []
    nomi_lst = []
    slength_lst = []
    depth_lst = []

    for sentence in sentences_ntlk:
        if test_wlength: wlength_lst.append(textp.get_word_length(sentence))
        if test_compl: compl_lst.append(textp.get_sent_voc_complexity(sentence))
        if test_nomi: nomi_lst.append(stanford_parser.get_sent_nomins(sentence))
        if test_slength: slength_lst.append(textp.get_sent_length(sentence))
        if test_depth: depth_lst.append(stanford_parser.get_sent_depth(sentence, False))

        # test_sentence = "The use of drugs is dangerous."
        # print("Test sentence: \"", test_sentence, "\"\n")

        # textp.get_sent_length(test_sentence)
        # textp.get_word_length(test_sentence)
        # textp.get_sent_voc_complexity(test_sentence)
        # stanford_parser.get_sent_depth(test_sentence, False)
        # stanford_parser.get_sent_nomins(test_sentence)

    if test_wlength:
        min_wlength = min(wlength_lst)
        max_wlength = max(wlength_lst)
        avg_wlength = sum(wlength_lst) / float(len(wlength_lst))
        print('The min word length of the texttext is ' + str(min_wlength) + '.')
        print('The max word length of the texttext is ' + str(max_wlength) + '.')
        print('The avg word length of the texttext is ' + str(avg_wlength) + '.')
    if test_compl:
        min_compl = min(compl_lst)
        max_compl = max(compl_lst)
        avg_compl = sum(compl_lst) / float(len(compl_lst))
        print('The min complexity of the text is ' + str(min_compl) + '.')
        print('The max complexity of the text is ' + str(max_compl) + '.')
        print('The avg complexity of the text is ' + str(avg_compl) + '.')
    if test_nomi:
        min_nomi = min(nomi_lst)
        max_nomi = max(nomi_lst)
        avg_nomi = sum(nomi_lst) / float(len(nomi_lst))
        print('The min nominal form complexity of the text is ' + str(min_nomi) + '.')
        print('The max nominal form complexity of the text is ' + str(max_nomi) + '.')
        print('The avg nominal form complexity of the text is ' + str(avg_nomi) + '.')
    if test_slength:
        min_slength = min(slength_lst)
        max_slength = max(slength_lst)
        avg_slength = sum(slength_lst) / float(len(slength_lst))
        print('The min sentence length of the text is ' + str(min_slength) + '.')
        print('The max sentence length of the text is ' + str(max_slength) + '.')
        print('The avg sentence length of the text is ' + str(avg_slength) + '.')
    if test_depth:
        min_depth = min(depth_lst)
        max_depth = max(depth_lst)
        avg_depth = sum(depth_lst) / float(len(depth_lst))
        print('The min depth of the parse tree is ' + str(min_depth) + '.')
        print('The max depth of the parse tree is ' + str(max_depth) + '.')
        print('The avg depth of the parse tree is ' + str(avg_depth) + '.')

    print("\nAnalyzing the text took", time.time() - t, "seconds.")

# setup qt app
app = QApplication(sys.argv)
frame = MainApplication(textp.output())
frame.show()
app.exec_()
