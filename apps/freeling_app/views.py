from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
import freeling
from helpers.freeling_variables import *
from django.views.decorators.csrf import csrf_exempt
import subprocess

def morphological_analysis(text):
    analyzed_lines = []
    lines_forms = []
    #print "tokenizer =", tokenizer
    #print "splitter = ", splitter
    #print "morfo = ", morfo
    #print "tagger = ", tagger
    #print "parser = ", parser
    #print "sid = ", sid
    tokens = tokenizer.tokenize(text)
    #print "tokens size = ", len(tokens)
    splitted_text = splitter.split(sid, tokens, False)
    #print "splitted text = ", splitted_text
    mf_analysis = morfo.analyze(splitted_text)
    mf_analysis = tagger.analyze(mf_analysis)
    mf_analysis = parser.analyze(mf_analysis)
    #print "mf_analysis size is " + str(len(mf_analysis))
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
                'form': str(word.get_form())
            })
            line_forms.append(str(word.get_form()))
            word_analysis = word.get_analysis()
            for an in word_analysis:
                list_[k]['analysis'].append({'tag': str(an.get_tag()),
                                             'prob': an.get_prob()})
            k += 1
        lines_forms.append(line_forms)
        analyzed_lines.append(list_)
    # print "analyzed lines =", analyzed_lines
    return (lines_forms, analyzed_lines)

def lemmatized(lines_forms, analyzed_lines):
    command = 'Rscript'
    path_to_script = 'helpers/script.r'
    k = 0
    for line in lines_forms:
        cmd = [command, path_to_script] + line
        line_lemma = subprocess.check_output(cmd, universal_newlines=True)
        j = 0
        for lemma in line_lemma:
            analyzed_lines[k][j]['lemma'] = str(lemma)
            j += 1
        k += 1



def create_lines_forms(analyzed_lines):
    lines_forms = []
    for line in analyzed_lines:
        for dic in line:
            lines_forms.append(dic['form'])
    return lines_forms

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
            output['data'] = analyzed_lines
            print "adding data"
        except Exception as err:
            output['data'] = 'Bad parameters ' + str(err)
    print "==> response sent to client"
    return JsonResponse(output)

def home_view(request):
    return render(request, 'index.html')

def hello_world(request):
    return render(request, 'index.html', {'output':'Hola mundo'})
