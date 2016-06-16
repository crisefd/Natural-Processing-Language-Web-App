from nltk.tag import StanfordPOSTagger
st = StanfordPOSTagger('stanford-postagger/models/english-left3words-distsim.tagger', path_to_jar='/home/crisefd/stanford-postagger/stanford-postagger.jar')
#tagged_text = st.tag("Brett Smith's friend had committed suicide, his parents divorced and his dad lost his job. With a hug from John Kasich at a rally, he became the face of more gentle emotions among GOP voters.".split())
#print tagged_text
#import os
#print os.environ['CLASSPATH']
def pos(txt):
    return st.tag(txt.split())

def to_bikel_format(input_array):
    # input_array = map(lambda tup: '(' + tup[1] + ')', input_array)
    bikel_txt = "("
    for item in input_array:
        item_1 = "(" + item[1] + ")"
        bikel_txt += "(" + item[0] + " " + item_1 + ")"
    return bikel_txt + ")"

def print_to_file(bikel_txt):
    f = open('bikel-output.txt', 'w')
    f.write(bikel_txt)
    f.close()


tagged_text = pos("Brett Smith's friend had committed suicide, his parents divorced and his dad lost his job. With a hug from John Kasich at a rally, he became the face of more gentle emotions among GOP voters.")
bikel_txt = to_bikel_format(tagged_text)
print_to_file(bikel_txt)
