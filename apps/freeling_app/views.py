from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
import freeling
from freeling_variables import *
from django.views.decorators.csrf import csrf_exempt

def morphological_analysis(text):
    analyzed_lines = []
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
        dict_ = {}
        for word in words:
            dict_[str(word.get_form())] = {
                'lemma': str(word.get_lemma()),
                'tag': str(word.get_tag()),
                'analysis': [],
            }
            word_analysis = word.get_analysis()
            for an in word_analysis:
                dict_[word.get_form()]['analysis'].append({'tag': str(an.get_tag()),
                                                           'prob': an.get_prob()})
        analyzed_lines.append(dict_)
    print "analyzed lines =", analyzed_lines
    return analyzed_lines

@csrf_exempt
def freeling_view(request):
    output = {}
    print "==> request received in server"
    if request.method == 'POST':
        print "the request method is POST"
        try:
            text = request.POST['text'].decode('utf-8')
            print 'the text is ' + text
            output['data'] = morphological_analysis(text)
        except Exception as err:
            output['data'] = 'Bad parameters ' + str(err)
    print "==> response sent to client"
    return JsonResponse(output)

def home_view(request):
    return render(request, 'index.html')

def hello_world(request):
    return render(request, 'index.html', {'output':'Hola mundo'})
