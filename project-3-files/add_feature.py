#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import io
from helpers.freeling_variables import *
import traceback
import codecs
# reload(sys)
# sys.setdefaultencoding('utf8')

def add_feature():
    arg = sys.argv[1]
    dir_path = os.getcwd()
    path_to_new_train_file = dir_path + "/train_files/esp_" + arg + ".train"
    path_to_new_test_file = dir_path + "/test_files/esp_" + arg + ".test"
    path_to_new_model_file = dir_path + "/models_files/model_" + arg
    path_to_train_file = dir_path + "/train_files/esp_" + str(int(arg) -1) + ".train"
    path_to_test_file = dir_path + "/test_files/esp_" + str(int(arg) -1) + ".test"
    path_to_model_file = dir_path + "/models_files/model_" + str(int(arg) -1)
    # print path_to_model_file
    # print path_to_train_file
    # print path_to_test_file
    add_feature_to_files(path_to_train_file, path_to_test_file, path_to_new_train_file, path_to_new_test_file, arg)

def add_feature_to_files(path_to_train_file, path_to_test_file, path_to_new_train_file, path_to_new_test_file, arg):
    train_file = open(path_to_train_file, 'r')
    test_file = open(path_to_train_file, 'r')
    # new_train_file = open(path_to_new_train_file, 'w')
    # new_test_file = open(path_to_new_test_file, 'w')
    train_lines = train_file.readlines()
    test_lines = test_file.readlines()
    train_txt = ""
    test_txt = ""
    #for line in train_lines:
    #    try:
    #        train_txt += line.split()[0] + ".\n"
    #    except IndexError:
    #        continue
    for line in test_lines:
        spl_line = line.split()
        if len(spl_line) == 0:
            continue
        elif spl_line[0][-1] == ",":
            spl_line[0].replace(',', '')
            test_txt += spl_line[0] + " ,\n"
        else:
            test_txt += spl_line[0] + " .\n"
    if arg != "1":
        temp_test = codecs.open('salida.txt', 'w', "utf-8")
        temp_test.write(test_txt.decode('ISO-8859-1'))
        temp_test.close()
        os.system("analyze -f myconfig.es --output conll --outlv tagged <salida.txt >salida.tag ")
        # tokens = tokenizer.tokenize(train_txt)
        # splitted_text = splitter.split(sid, tokens, False)
        # mf_analysis = morfo.analyze(splitted_text)
        # mf_analysis = tagger.analyze(mf_analysis)
        # mf_analysis = parser.analyze(mf_analysis)
        # tags = []
        # for item in mf_analysis:
        #     words = item.get_words()
        #     for word in words:
        #         tags.append(str(word.get_tag()))
        #
        # tokens = tokenizer.tokenize(test_txt)
        # splitted_text = splitter.split(sid, tokens, False)
        # mf_analysis = morfo.analyze(splitted_text)
        # mf_analysis = tagger.analyze(mf_analysis)
        # mf_analysis = parser.analyze(mf_analysis)
        # tags = []
        # for item in mf_analysis:
        #     words = item.get_words()
        #     for word in words:
        #         tags.append(str(word.get_tag()))
        #
        # for i in range(len(train_lines)):
        #     splitted_line = train_lines[i].split()
        #     train_lines[i] = " ".join(splitted_line.insert(-1, tags[i]))
        # for i in range(len(test_lines)):
        #     splitted_line = test_lines[i].split()
        #     test_lines[i] = " ".join(splitted_line.insert(-1, tags[i]))

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
    #new_train_file.write("\n".join(train_lines))
    #new_test_file.write("\n".join(test_lines))
    test_file.close()
    train_file.close()
    #new_test_file.close()
    #new_train_file.close()

# quita puntos
def bar(name):
    f = open(name, 'r')
    lines = f.readlines()
    f.close
    lines_to_be_kept = []
    size = len(lines)
    for i in range(0, size-1):
        spl_line1 = lines[i].split()
        spl_line2 = lines[i + 1].split()
        if i%1000 == 0: print "iter =", i
        #print spl_line1
        if len(spl_line1) == 0 or len(spl_line2) == 0:
            continue
        spl_line2 = lines[i + 1].split()
        #print "2=", spl_line2[0], " 1 ", spl_line1[0]
        if (spl_line2[1] == "." and spl_line1[1] != "."):
            lines_to_be_kept.append(i)
        elif (spl_line2[1] == "." and spl_line1[1] == "."):
            lines_to_be_kept.append(i + 1)
    new_lines = []
    f = open(name, 'w')
    print "appending"
    for j in lines_to_be_kept:
        new_lines.append(lines[j])
    print "writing to file ", len(new_lines)
    f.write("\n".join(new_lines))
    f.close()

# quita espacios
def foo(name):
    f = open(name, 'r')

    lines = f.readlines()
    f.close()
    lines_to_be_kept = []
    k = 0
    for line in lines:
        spl_line = line.split()
        if len(spl_line) == 0:
            k += 1
            continue
        lines_to_be_kept.append(line.replace('\n', ''))
        k += 1
    f = open(name, 'w')
    f.write("\n".join(lines_to_be_kept))
    f.close()

# separa puntos de palabras
def paar(name):
    f = open(name, 'r')
    lines = f.readlines()
    f.close()
    i = 0
    while True:
        if i == len(lines): break
        spl_line1 = lines[i].split()
        # spl_line2 = lines[i].split()
        if spl_line1[1][-1] == '.':
            spl_line1[1].replace('.', '')
            lines[i] = spl_line1[0] + " " + spl_line1[1]  + " ".join(spl_line1[2:])
            lines.insert(i + 1, ".         .         Fp      Fp  pos=punctuation|type=period                         - - - - - - -")
            i += 1
        i += 1
    f = open(name, 'w')
    f.write("\n".join(lines))
    f.close




def comp():
    f1 = open('salida.tag', 'r')
    f2 = open('test_files/new_esp_1.test', 'r')
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    f1.close()
    f2.close()
    i = 0
    while True:
        try:
            spl_line1 = lines1[i].split()
        except IndexError:
            print "lines1 ", i
            sys.exit()
        try:
            spl_line2 = lines2[i].split()
        except IndexError:
            print "lines2 ", i
            sys.exit()
        if spl_line1[1] != spl_line2[0]:
            print "i = ", i
            print ".tag => ", spl_line1[1]
            print ".test => ", spl_line2[0]
            r = raw_input("Enter something")
        i += 1



if __name__ == "__main__":
    #add_feature()
    bar("salida.tag")
    foo("salida.tag")
    #paar("salida.tag")
