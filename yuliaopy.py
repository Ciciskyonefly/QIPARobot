# encoding: utf-8

import sys

from nltk.corpus import brown

reload(sys)
sys.setdefaultencoding("utf-8")
import nltk
default_tagger = nltk.DefaultTagger("NN")
raw = '我 累 个 去'
tokens = nltk.word_tokenize(raw)
tags = default_tagger.tag(tokens)
print tags

pattern = [(r'.*们$','PRO')]
tagger = nltk.RegexpTagger(pattern)
print tagger.tag(nltk.word_tokenize('我们 累 个 去 你们 和 他们 啊'))

tagged_sents = [[(u'我', u'PRO'), (u'小兔', u'NN')]]
unigram_tagger = nltk.UnigramTagger(tagged_sents)
sents = brown.sents(categories='news')
sents = [[u'我', u'你', u'小兔']]
tags = unigram_tagger.tag(sents[0])
print tags