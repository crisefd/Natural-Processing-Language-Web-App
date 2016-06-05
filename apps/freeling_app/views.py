from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
import freeling
from helpers.freeling_variables import *
from django.views.decorators.csrf import csrf_exempt
import subprocess
import os

def morphological_analysis(text):
    analyzed_lines = []
    lines_forms = []
    tokens = tokenizer.tokenize(text)
    splitted_text = splitter.split(sid, tokens, False)
    mf_analysis = morfo.analyze(splitted_text)
    mf_analysis = tagger.analyze(mf_analysis)
    mf_analysis = parser.analyze(mf_analysis)
    for item in mf_analysis:
        words = item.get_words()
        list_ = []
        k = 0
        line_forms = []
        for word in words:
            list_.append( {
                'lemma': '',
                'tag': str(word.get_tag()),
                'analysis': [],
                'form': str(word.get_form()),
                'stemm': ''
            })
            line_forms.append(str(word.get_form()))
            word_analysis = word.get_analysis()
            for an in word_analysis:
                list_[k]['analysis'].append({'tag': str(an.get_tag()),
                                             'prob': an.get_prob()})
            k += 1
        lines_forms.append(line_forms)
        analyzed_lines.append(list_)
    return (lines_forms, analyzed_lines)

def lemmatized(lines_forms, analyzed_lines):
    command = 'Rscript'
    path_to_script = os.getcwd() + '/apps/freeling_app/helpers/script.r'
    # path_to_script = '/srv/npl_project/apps/freeling_app/helpers/script.r'
    k = 0
    print "len analyzed_lines ", len(analyzed_lines)
    for line in lines_forms:
        cmd = [command, path_to_script] + line
        print "CMD: ", cmd
        line_lemma = subprocess.check_output(cmd, universal_newlines=True).split(',')
        print "line lemma ", line_lemma
        print "line ", k
        j = 0
        for lemma in line_lemma:
            print "lemma ", j
            analyzed_lines[k][j]['lemma'] = str(lemma)
            j += 1
        k += 1

def stemming(lines_forms, analyzed_lines):
    command = 'php'
    path_to_script = os.getcwd() + '/apps/freeling_app/helpers/script.php'
    # path_to_script = '/srv/npl_project/apps/freeling_app/helpers/script.php'
    k = 0
    for line in lines_forms:
        cmd = [command, path_to_script] + line
        line_stemm = subprocess.check_output(cmd, universal_newlines=True).split()
        j = 0
        for stemm in line_stemm:
            analyzed_lines[k][j]['stemm'] = str(stemm)
            j += 1
        k += 1


@csrf_exempt
def freeling_view(request):
    output = {}
    print "==> request received in server"
    if request.method == 'POST':
        print "the request method is POST"
        try:
            text = request.POST['text'].decode('utf-8')
            print 'the text is ' + text
            lines_forms, analyzed_lines = morphological_analysis(text)
            print "morpho analysis"
            lemmatized(lines_forms, analyzed_lines)
            print "lemmatized"
            stemming(lines_forms, analyzed_lines)
            print "stemming"
            output['data'] = analyzed_lines
            print "adding data"
        except Exception as err:
            print("Error: "+ str(err))
            output['data'] = 'Error ' + str(err)
    print "==> response sent to client"
    return JsonResponse(output)

def home_view(request):
    return render(request, 'index.html')

def hello_world(request):
    return render(request, 'index.html', {'output':'Hola mundo'})
