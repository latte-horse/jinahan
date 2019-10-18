from konlpy.tag import Komoran
import os
import re
import string
import konlpy
from collections import Counter
import pandas as pd

komoran = Komoran(userdic = './user_dic.txt')


############형태소분석 저장


filelist ='C:/Users/student/Documents/jinahan/형태소분석/코모란/sample_analysis/*.txt'
try:
    doc = open(filelist , encoding = 'UTF8').read().replace('\n' , '')
    testr =  komoran.nouns(doc)



    #경로에 있는 파일을 저장.
    count =Counter(testr)
    # 참고: https://excelsior-cjh.tistory.com/94
    return_list=[]
    for n,c in count.most_common(20):
        temp = {'tag':n.replace("\n",""),'count':c}
        return_list.append(temp)
except Exception as e:    
    print(e)
    print(return_list)

