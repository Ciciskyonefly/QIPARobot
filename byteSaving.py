#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import pynlpir

pynlpir.open()

s = '怎么才能把电脑里的垃圾文件删除'

segments = pynlpir.get_key_words(s,weighted=True)

for segment in segments:
    print segment[0],'\t',segment[1]

pynlpir.close()