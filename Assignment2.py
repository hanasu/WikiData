import codecs
import string
import re
from nltk import word_tokenize

f = codecs.open("smallcleaned.txt", encoding="UTF-8")
contents = f.read()
contents = re.sub(r'\{\{(.*?)\}\}', "", contents)
tokens = word_tokenize(contents)

small = codecs.open('smalltokens.txt', 'w', 'utf8')
tokens = filter(lambda word: word not in ',-.:;()', tokens)
for ele in tokens:
    #ele.encode('utf-8').translate(None, string.punctuation)
    small.write(ele+'\n')
small.close()
