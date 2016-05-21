from django.shortcuts import render
from django.template import Template, Context
from django.http import JsonResponse
import freeling
from freeling_variables import *

def morphological_analysis(text):
    analyzed_lines = []
    tokens = tokenizer.tokenize(text)
    splitted_text = splitter.split(sid, tokens, False)
    mf_analysis = morfo.analyze(splitted_text)
    mf_analysis = tagger.analyze(mf_analysis)
    mf_analysis = parser.analyze(mf_analysis)
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
    return analyzed_lines

def freeling_view(request):
    output = ''
    if request.method == 'POST':
        try:
            text = str(request['POST'])
            output = morphological_analysis(text)
        except Exception as err:
            output = 'Bad parameters ' + str(err)

    return JsonResponse(output)

def home_view(request):
    return render(request, 'index.html')

def hello_world(request):
    return render(request, 'index.html', {'output':'Hola mundo'})
