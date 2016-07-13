import sys
import os
from helpers.freeling_variables import *

def add_feature():
    arg = sys.argv[1]
    dir_path = os.getcwd()
    path_to_train_file = dir_path + "/train_files/esp_" + arg + ".train"
    path_to_test_file = dir_path + "/test_files/esp_" + arg + ".test"
    path_to_model_file = dir_path + "/models_files/model_" + arg

def add_feature_to_files(path_to_train_file, path_to_test_file):
    train_file = open(path_to_train_file, 'r+')
    test_file = open(path_to_train_file, 'r+')
    train_lines = train_file.readlines()
    test_lines = test_file.readlines()
    txt = ""
    for line in train_lines:
        train_txt += line.split()[0] + " "
    for line in test_lines:
        test_txt += line.split()[0] + " "
    tokens = tokenizer.tokenize(train_txt)
    splitted_text = splitter.split(sid, tokens, False)
    mf_analysis = morfo.analyze(splitted_text)
    mf_analysis = tagger.analyze(mf_analysis)
    mf_analysis = parser.analyze(mf_analysis)
    tags = []
    for item in mf_analysis:
        words = item.get_words()
        for word in words:
            tags.append(str(word.get_tag()))
    for i in range(len(train_lines)):
        train_lines[i] = train_lines[i][:-2] + tags[i] + train_lines[i][-2:]
    train_file.close()
