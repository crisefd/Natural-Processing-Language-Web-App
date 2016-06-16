from django.conf import settings
from nltk.tag import StanfordPOSTagger

stanford_postagger = StanfordPOSTagger(settings.BASE_DIR + '/static/stanford-postagger/models/english-left3words-distsim.tagger',
                                       path_to_jar=settings.BASE_DIR + '/static/stanford-postagger/stanford-postagger.jar')
