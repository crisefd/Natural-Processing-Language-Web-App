from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
from django.conf import settings
from helpers.stanford_variables import stanford_postagger
from helpers.parseval import parseval
from django.views.decorators.csrf import csrf_exempt
import os

def pos_tag(txt):
    return stanford_postagger.tag(txt.split())

def to_bikel_format(input_array):
    bikel_txt = "("
    for item in input_array:
        item_1 = "(" + item[1] + ")"
        bikel_txt += "(" + item[0] + " " + item_1 + ")"
    return bikel_txt + ")"

def print_to_file(txt, name=''):
    f = open(settings.BASE_DIR + '/syn_ana_files/' + name, 'w')
    f.write(txt)
    f.close()

def dan_bikel_parser():
    os.system("{0}/static/dbparser/bin/parse 1000 {0}/static/dbparser/settings/collins.properties {0}/static/wsj/wsj-02-21.obj.gz {0}/syn_ana_files/bikel-pos.txt".format(settings.BASE_DIR))

@csrf_exempt
def analysis_view(request):
    output = {}
    print "==> request received in server"
    if request.method == 'POST':
        print "the request method is POST"
        try:
            text = request.POST['text'].decode('utf-8')
            #print 'the text is ' + text
            tagged_text = pos_tag(text)
            print "text tagged"
            bikel_txt = to_bikel_format(tagged_text)
            print "bikel formatted text"
            print_to_file(bikel_txt, name='bikel-pos.txt')
            dan_bikel_parser()
            parse_eval_output = parseval(settings.BASE_DIR + '/syn_ana_files/bikel-pos.txt.parsed',
                                         settings.BASE_DIR + '/static/wsj/wsj_0001.mrg')

            print "parse evaluation"
        except Exception as err:
            print "Error: "+ str(err)
            output['data'] = 'Error ' + str(err)
    print "==> response sent to client"
    return JsonResponse(output)


def syntactic_ana_view(request):
    return render(request, 'index_syntactic.html')
