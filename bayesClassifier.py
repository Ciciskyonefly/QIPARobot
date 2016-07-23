
# coding:utf-8

# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import nltk

my_train_set = [
        ({'feature1':u'a'},'1'),
        ({'feature1':u'a'},'2'),
        ({'feature1':u'a'},'3'),
        ({'feature1':u'a'},'3'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ]
classifier = nltk.NaiveBayesClassifier.train(my_train_set)
print classifier.classify({'feature1':u'a'})
print classifier.classify({'feature1':u'b'})




#
# 文档注释文件
# from nltk.corpus import movie_reviews
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = all_words.keys()[:2000]
# def document_features(document):
# 	for word in word_features:
# 		features['contains(%s)' % word] = (word in document_words)
# 	return features