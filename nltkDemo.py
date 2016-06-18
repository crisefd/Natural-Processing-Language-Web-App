from nltk.parse.stanford import StanfordParser
stanford_parser = StanfordParser(path_to_models_jar="static/stanford-parser/stanford-parser-3.6.0-models.jar",
                                 model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz",
                                 path_to_jar='static/stanford-parser/stanford-parser.jar')

tree = stanford_parser.raw_parse("The cat eats food in the house.")
#f = open('syn_ana_files/stanford-post.txt', 'w')
#f.write(str(tree.next()))
txt = str(tree.next())
print txt
print "=========================="
txt = txt[6:(len(txt) - 1)]
print txt
