from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
from django.conf import settings
from helpers.stanford_variables import *
from helpers.parseval import parseval
from django.views.decorators.csrf import csrf_exempt
import os
import traceback
import re


raw_file_name = ''

def print_to_file(txt, name=''):
    f = open(settings.BASE_DIR + '/syn_ana_files/' + name, 'w')
    f.write(txt)
    f.close()

###### Bikel pre-processing ############

def pos_tag(txt):
    #txt = txt.split('\n')
    sentences = txt.split('\n')
    output = []
    for sentence in sentences:
        output.append(stanford_postagger.tag(sentence.split()))
    return output

def to_bikel_format(output_tagged_txt):
    output_bikel_format = ""
    for input_array in output_tagged_txt:
        if len(input_array) > 0:
            bikel_txt = "("
            for item in input_array:
                item_1 = "(" + item[1] + ")"
                item_0 = item[0]
                punc = ""
                if re.search(r"\w+.(\.|\,|:|!|\?|\'s|\'|;)", item_0):
                    if item_0[-1] == "'":
                        punc = "({0} (POS))".format(item_0[-1])
                        item_0 = item_0[:-1]
                    elif item_0[-2:] == "'s":
                        punc = "({0} (POS))".format(item_0[-2:])
                        item_0 = item_0[:-2]
                    else:
                        punc = "({0} ({0}))".format(item_0[-1])
                        item_0 = item_0[:-1]
                bikel_txt += "(" + item_0 + " " + item_1 + ")" + punc
            bikel_txt += ")"
            output_bikel_format += bikel_txt + '\n'
    return output_bikel_format

############ Stanford pre-processing ################

def change_stanford_format(txt):
    print "parsed ==> ", txt
    txt = txt[6:(len(txt) - 1)]
    return "(" + txt + ")"
    # return txt


################## Parsers ##############################

def dan_bikel_parse(txt, output_tree):
    output_tagged_txt = pos_tag(txt)
    output_bikel_format = to_bikel_format(output_tagged_txt)
    print_to_file("".join(output_bikel_format), name='bikel-pos.txt')
    os.system("{0}/static/dbparser/bin/parse 1000 {0}/static/dbparser/settings/collins.properties {0}/static/wsj/wsj-02-21.obj.gz {0}/syn_ana_files/bikel-pos.txt".format(settings.BASE_DIR))
    f = open("{0}/syn_ana_files/bikel-pos.txt.parsed".format(settings.BASE_DIR))
    output_tree.append("\n".join(f.readlines()))

def stanford_parse(txt, output_tree):
    txt = txt.split("\n")
    trees = stanford_parser.raw_parse_sents(txt)

    parsed_txt = ""
    #for tree in list(trees):
    #    parsed_txt += change_stanford_format(str(tree)) + "\n"
    while True:
        try:
            tree = trees.next()
            while True:
                try:
                    parsed_txt += change_stanford_format(str(tree.next())) + "\n"
                except StopIteration:
                    break
        except StopIteration:
            break;
    # parsed_txt = change_stanford_format(parsed_txt)
    print "formatted"
    output_tree.append(parsed_txt)
    print 'output-tree', output_tree[0]
    print_to_file(parsed_txt, name='stanford-pos.txt.parsed')

@csrf_exempt
def analysis_view(request):
    output = {}
    global raw_file_name
    print "==> request received in server"
    if request.method == 'POST':
        print "the request method is POST", request.POST

        try:
            text = request.POST['text'].decode('utf-8')
            analyzer = request.POST['analyzer'].decode('utf-8')
            parseval_flag = request.POST['parseval'].decode('utf-8')
            parse_eval_output = {}
            output_tree = []
            if analyzer == 'Bikel':
                dan_bikel_parse(text, output_tree)
                if parseval_flag == "true":
                    parse_eval_output = parseval(settings.BASE_DIR + '/syn_ana_files/bikel-pos.txt.parsed',
                                                 settings.BASE_DIR + '/static/wsj/gold_standard_tree/{0}.mrg'.format(raw_file_name))
            elif analyzer == 'Stanford':
                stanford_parse(text, output_tree)
                if parseval_flag == "true":
                    parse_eval_output = parseval(settings.BASE_DIR + '/syn_ana_files/bikel-pos.txt.parsed',
                                                 settings.BASE_DIR + '/static/wsj/gold_standard_tree/{0}.mrg'.format(raw_file_name))
            #print 'output-tree', output_tree[0]
            output['data'] = {
                'output_tree': output_tree[0],
                'parse_eval_output': parse_eval_output,
            }
            print "parse evaluation"
        except IndexError as ierr:
            print "Error: "+ str(ierr) + str(type(ierr))
            traceback.print_exc()
            output['data'] = {
                'output_tree': output_tree[0],
            }
        except Exception as err:
            print "Error: "+ str(err) + str(type(err))
            traceback.print_exc()
            output['data'] = 'Error ' + str(err)
    print "==> response sent to client"
    return JsonResponse(output)


def get_raw_text_view(request):
    global raw_file_name
    output = {}
    content = ''
    if request.method == 'GET':
        try:
            print "request method is GET", request.GET
            raw_file_name = request.GET['name'].decode('utf-8')
            print "file_name=", raw_file_name
            f = open(settings.BASE_DIR + '/static/wsj/raw_text/' + raw_file_name)
            content = "".join(f.readlines()[2:])
            #print "raw text sent ==> ", content
        except Exception as err:
            print "Error: "+ str(err) + str(type(err))
            traceback.print_exc()
            output['data'] = 'Error ' + str(err)
    output['data'] = { 'text': content }
    return JsonResponse(output)




def syntactic_ana_view(request):
    return render(request, 'index_syntactic.html')
