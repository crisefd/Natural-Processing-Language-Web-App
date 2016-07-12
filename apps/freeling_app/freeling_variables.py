import freeling
# code extracted from https://gist.github.com/arademaker/dffb8de093502b153e85#file-processing-py-L50
FREELINGDIR = '/usr/local'
DATA = FREELINGDIR + '/share/freeling/'
LANGUAGE = 'es'

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
parser = freeling.chart_parser(DATA + LANGUAGE + '/chunker/grammar-chunk.dat')
morfo.set_active_options(False, True, True, True,
                         True, True, False, True,
                         True, True, True, True )
