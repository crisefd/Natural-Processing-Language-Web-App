from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
from django.conf import settings
from helpers.stanford_variables import *
from helpers.parseval import parseval
from django.views.decorators.csrf import csrf_exempt
import os
import traceback

def print_to_file(txt, name=''):
    f = open(settings.BASE_DIR + '/syn_ana_files/' + name, 'w')
    f.write(txt)
    f.close()

###### Bikel pre-processing ############

def pos_tag(txt):
    return stanford_postagger.tag(txt.split())

def to_bikel_format(input_array):
    bikel_txt = "("
    for item in input_array:
        item_1 = "(" + item[1] + ")"
        bikel_txt += "(" + item[0] + " " + item_1 + ")"
    return bikel_txt + ")"

############ Stanford pre-processing ################

def change_stanford_format(txt):
    txt = txt[6:(len(txt) - 1)]
    return txt


################## Parsers ##############################

def dan_bikel_parse(txt, output_tree):
    tagged_text = pos_tag(txt)
    bikel_txt = to_bikel_format(tagged_text)
    print_to_file(bikel_txt, name='bikel-pos.txt')
    os.system("{0}/static/dbparser/bin/parse 1000 {0}/static/dbparser/settings/collins.properties {0}/static/wsj/wsj-02-21.obj.gz {0}/syn_ana_files/bikel-pos.txt".format(settings.BASE_DIR))
    f = open("{0}/syn_ana_files/bikel-pos.txt.parsed".format(settings.BASE_DIR))
    output_tree.append(f.read())

def stanford_parse(txt, output_tree):
    tree = stanford_parser.raw_parse(txt)
    print "parsed"
    parsed_txt = str(tree.next())
    parsed_txt = change_stanford_format(parsed_txt)
    print "formatted"
    output_tree.append(parsed_txt)
    print 'output-tree', output_tree[0]
    print_to_file(parsed_txt, name='stanford-pos.txt.parsed')

@csrf_exempt
def analysis_view(request):
    output = {}
    print "==> request received in server"
    if request.method == 'POST':
        print "the request method is POST", request.POST
        try:
            text = request.POST['text'].decode('utf-8')
            analyzer = request.POST['analyzer'].decode('utf-8')
            print 'analyzer ', analyzer
            parse_eval_output = {}
            output_tree = []
            if analyzer == 'Bikel':
                dan_bikel_parse(text, output_tree)
                parse_eval_output = parseval(settings.BASE_DIR + '/syn_ana_files/bikel-pos.txt.parsed',
                                             settings.BASE_DIR + '/static/wsj/gold_standard_tree/wsj_0001.mrg')
            elif analyzer == 'Stanford':
                stanford_parse(text, output_tree)
                parse_eval_output = parseval(settings.BASE_DIR + '/syn_ana_files/bikel-pos.txt.parsed',
                                             settings.BASE_DIR + '/static/wsj/gold_standard_tree/wsj_0001.mrg')
            #print 'output-tree', output_tree[0]
            output['data'] = {
                'output_tree': output_tree[0],
                'parse_eval_output': parse_eval_output,
            }
            print "parse evaluation"
        except Exception as err:
            print "Error: "+ str(err) + str(type(err))
            traceback.print_exc()
            output['data'] = 'Error ' + str(err)
    print "==> response sent to client"
    return JsonResponse(output)


def syntactic_ana_view(request):
    return render(request, 'index_syntactic.html')
