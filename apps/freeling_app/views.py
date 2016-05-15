from django.shortcuts import render
from django.template import Template, Context
# from django.http import HttResponse
import freeling
import json
# code extracted from https://gist.github.com/arademaker/dffb8de093502b153e85#file-processing-py-L50
FREELINGDIR = '/usr/local'
DATA = FREELINGDIR + '/share/freeling'
LANGUAGE = 'es'

freeling.util_init_locale('default')
opt = freeling.maco_options(LANGUAGE)
opt.set_active_modules(1,1,1,1,1,1,1,1,1,1,0)
opt.set_data_files("usermap.dat",
                                    DATA+LANGUAGE+"/locucions.dat", 
                                    DATA+LANGUAGE+"/quantities.dat", 
                                    DATA+LANGUAGE+"/afixos.dat",
                                    DATA+LANGUAGE+"/probabilitats.dat", 
                                    DATA+LANGUAGE+"/dicc.src", 
                                    DATA+LANGUAGE+"/np.dat",  
                                    DATA+"common/punct.dat", 
                                    "")
opt.set_retok_contractions(False)

lg  = freeling.lang_ident(DATA+"common/lang_ident/ident-few.dat")
mf  = freeling.maco(op)
tk  = freeling.tokenizer(DATA+LANGUAGE+"/tokenizer.dat")
sp  = freeling.splitter(DATA+LANGUAGE+"/splitter.dat")
tg  = freeling.hmm_tagger(DATA+LANGUAGE+"/tagger.dat",1,2)
sen = freeling.senses(DATA+LANGUAGE+"/senses.dat");
ukb = freeling.ukb(DATA+LANGUAGE+"/ukb.dat")

def tag(obj):
    sent = obj['text']
    out = obj
    lang = lg.identify_language(sent)
    l = tk.tokenize(sent)
    ls = sp.split(l, 1) # old value 0
    ls = mf.analyze(ls)
    ls = tg.analize(ls)
    ze(ls)
    wss = []
    for s in ls:
        ws = s.get_words()
        for w in ws:
            an = w.get_analysis()
            a = an[0]
            wse = dict(wordform = w.get_form(),
                       lemma = a.get_lemma(),
                       tag = a.get_tag(),
                       prob = a.get_prob(),
                       analysis = len(an))
            wss.append(wse)
        out['words'] = wss
        out['lang'] = lang
        return out

def freeling_view(request):
    phrase = "hola, me llamo cristhian"
    tweets = []
    for s in phrase:
        tweets.append(tag(s))
    context = {'output':tweets}
    return render(request, 'index.html', context)

def hello_world(request):
    return render(request, 'index.html', {'output':'Hola mundo'})
