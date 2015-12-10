import sys
import time

from PyQt5.QtWidgets import QApplication

from textparser.textparser import *
from ui.testqt import MainApplication

# turn feature tests on/off
test_features = True

# setup nltk text parsing
textp = TextParser()
stanford_parser = Stanford()

# function tests
if test_features:
    t = time.time()

    # text = open('../kindertexte/en/it_could_happen.txt').read()
    # text = open('../kindertexte/en/the_halloween_house.txt').read()
    # text = open('../kindertexte/en/the_little_gingerbread_man.txt').read()
    text = open('../kindertexte/en/who_did_patricks_homework.txt').read()

    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences_ntlk = sent_detector.tokenize(text.strip())

    slength_lst = []
    wlength_lst = []
    compl_lst = []
    depth_lst = []

    for sentence in sentences_ntlk:
        slength_lst.append(textp.get_sent_length(sentence))
        wlength_lst.append(textp.get_word_length(sentence))
        if textp.get_sent_voc_complexity(sentence) < 0:
            print(sentence)
        compl_lst.append(textp.get_sent_voc_complexity(sentence))
        depth_lst.append(stanford_parser.get_sent_depth(sentence, False))

        # test_sentence = "The use of drugs is dangerous."
        # print("Test sentence: \"", test_sentence, "\"\n")

        # textp.get_sent_length(test_sentence)
        # textp.get_word_length(test_sentence)
        # textp.get_sent_voc_complexity(test_sentence)
        # stanford_parser.get_sent_depth(test_sentence, False)
        # stanford_parser.get_sent_nomins(test_sentence)

    min_wlength = min(wlength_lst)
    max_wlength = max(wlength_lst)
    avg_wlength = sum(wlength_lst) / float(len(wlength_lst))
    print('The min word length of the texttext is ' + str(min_wlength) + '.')
    print('The max word length of the texttext is ' + str(max_wlength) + '.')
    print('The avg word length of the texttext is ' + str(avg_wlength) + '.')

    min_compl = min(compl_lst)
    max_compl = max(compl_lst)
    avg_compl = sum(compl_lst) / float(len(compl_lst))
    print('The min complexity of the text is ' + str(min_compl) + '.')
    print('The max complexity of the text is ' + str(max_compl) + '.')
    print('The avg complexity of the text is ' + str(avg_compl) + '.')

    min_slength = min(slength_lst)
    max_slength = max(slength_lst)
    avg_slength = sum(slength_lst) / float(len(compl_lst))
    print('The min sentence length of the text is ' + str(min_slength) + '.')
    print('The max sentence length of the text is ' + str(max_slength) + '.')
    print('The avg sentence length of the text is ' + str(avg_slength) + '.')

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
