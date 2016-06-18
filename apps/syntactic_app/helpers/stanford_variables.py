from django.conf import settings
from nltk.tag import StanfordPOSTagger
from nltk.parse.stanford import StanfordParser


stanford_postagger = StanfordPOSTagger(settings.BASE_DIR + '/static/stanford-postagger/models/english-left3words-distsim.tagger',
                                       path_to_jar=settings.BASE_DIR + '/static/stanford-postagger/stanford-postagger.jar')

stanford_parser = StanfordParser(path_to_models_jar=settings.BASE_DIR + "/static/stanford-parser/stanford-parser-3.6.0-models.jar",
                                 model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz",
                                 path_to_jar=settings.BASE_DIR + '/static/stanford-parser/stanford-parser.jar')
