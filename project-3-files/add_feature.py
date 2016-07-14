import sys
import os
from helpers.freeling_variables import *
import traceback

def add_feature():
    arg = sys.argv[1]
    dir_path = os.getcwd()
    path_to_new_train_file = dir_path + "/train_files/esp_" + arg + ".train"
    path_to_new_test_file = dir_path + "/test_files/esp_" + arg + ".test"
    path_to_new_model_file = dir_path + "/models_files/model_" + arg
    path_to_train_file = dir_path + "/train_files/esp_" + str(int(arg) -1) + ".train"
    path_to_test_file = dir_path + "/test_files/esp_" + str(int(arg) -1) + ".test"
    path_to_model_file = dir_path + "/models_files/model_" + str(int(arg) -1)
    print path_to_model_file
    print path_to_train_file
    print path_to_test_file
    add_feature_to_files(path_to_train_file, path_to_test_file, path_to_new_train_file, path_to_new_test_file, arg)

def add_feature_to_files(path_to_train_file, path_to_test_file, path_to_new_train_file, path_to_new_test_file, arg):
    print "XX"
    train_file = open(path_to_train_file, 'r')
    test_file = open(path_to_train_file, 'r')
    new_train_file = open(path_to_new_train_file, 'w')
    new_test_file = open(path_to_new_test_file, 'w')
    train_lines = train_file.readlines()
    test_lines = test_file.readlines()
    train_txt = ""
    test_txt = ""
    for line in train_lines:
        try:
            train_txt += line.split()[0] + " "
        except IndexError:
            continue
    for line in test_lines:
        try:
            test_txt += line.split()[0] + " "
        except IndexError:
            continue
    if arg != "1":
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

        tokens = tokenizer.tokenize(test_txt)
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
            splitted_line = train_lines[i].split()
            train_lines[i] = " ".join(splitted_line.insert(-1, tags[i]))
        for i in range(len(test_lines)):
            splitted_line = test_lines[i].split()
            test_lines[i] = " ".join(splitted_line.insert(-1, tags[i]))

    else:
        for i in range(len(train_lines)):
            try:
                splitted_line = train_lines[i].split()
                bin_str = "1" if splitted_line[0].isupper() else "0"
                splitted_line.insert(-1, bin_str)
                train_lines[i] = " ".join(splitted_line)
            except IndexError:
                continue
        for i in range(len(test_lines)):
            try:
                splitted_line = test_lines[i].split()
                bin_str = "1" if splitted_line[0].isupper() else "0"
                splitted_line.insert(-1, bin_str)
                test_lines[i] = " ".join(splitted_line)
            except IndexError:
                continue
    new_train_file.write("\n".join(train_lines))
    new_test_file.write("\n".join(test_lines))
    test_file.close()
    train_file.close()
    new_test_file.close()
    new_train_file.close()

if __name__ == "__main__":
    add_feature()
