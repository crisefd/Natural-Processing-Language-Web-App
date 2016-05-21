from django.shortcuts import render
from django.template import Template, Context
# from django.http import HttResponse
import freeling
# code extracted from https://gist.github.com/arademaker/dffb8de093502b153e85#file-processing-py-L50
FREELINGDIR = '/usr/local'
DATA = FREELINGDIR + '/share/freeling/'
LANGUAGE = 'es'

# Analyzer variables
morfo = None
tokenizer = None
splitter = None
tagger = None
parser = None
sid = None

def setting_freeling():
    freeling.util_init_locale('default')
    option = freeling.maco_options(LANGUAGE)
    option.set_data_files( "", 
                           DATA + "common/punct.dat",
                           DATA + LANGUAGE + "/dicc.src",
                           DATA + LANGUAGE + "/afixos.dat",
                           "",
                           DATA + LANGUAGE + "/locucions.dat", 
                           DATA + LANGUAGE + "/np.dat",
                           DATA + LANGUAGE + "/quantities.dat",
                           DATA + LANGUAGE + "/probabilitats.dat")
    morfo = freeling.maco(option)
    tokenizer = freeling.tokenizer(DATA + LANGUAGE + '/tokenizer.dat')
    splitter = freeling.splitter(DATA + LANGUAGE + '/splitter.dat')
    sid = splitter.open_session()
    tagger = freeling.hmm_tagger(DATA + LANGUAGE + '/tagger.dat', True, 2)
    # senses = freeling.senses(DATA + LANGUAGE + '/senses.dat')
    parser = freeling.chart_parser(DATA + LANGUAGE + '/chunker/grammar-chunk.dat')
    morfo.set_active_options(False, True, True, True,
                             True, True, False, True,
                             True, True, True, True )

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

    return render(request, 'index.html', {'output': output})

def home_view(request):
    return render(request, 'index.html', {'output': output})

def hello_world(request):
    return render(request, 'index.html', {'output':'Hola mundo'})
