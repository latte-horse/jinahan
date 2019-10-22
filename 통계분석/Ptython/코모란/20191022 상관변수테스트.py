from konlpy.tag import Komoran
import os
from gensim.models import Word2Vec
import tensorflow as tf
import gensim
import re
import string
import konlpy
from collections import Counter
import pandas as pd
import numpy as np

komoran = Komoran(userdic ='C:/Users/student/Documents/jinahan/통계분석/명단/names.txt')


def allfiles(path):
    res = []

    for root, dirs, files in os.walk(path):
        rootpath = os.path.join(os.path.abspath(path), root)

        for file in files:
            filepath = os.path.join(rootpath, file)
            res.append(filepath)

    return res

result = allfiles("C:/Users/student/Documents/jinahan/통계분석/명단/1450/D_K_05")

koko1 = []
del koko1[:]
nounsresult = []
del nounsresult[:]   

for filelist in result:
    try:
        doc = open(filelist , encoding = 'UTF8').read().replace('\n' , '')
        nounsresult += komoran.nouns(doc)
        testr =  komoran.nouns(doc) 
        kkk = []
        for i in range(len(testr)):
            
            if(len(testr[i]) >= 2):
                kkk.append(testr[i])
        koko1.append(kkk)

    except Exception as e:
        print(e)
        
#print(kkk)
return_list=[]
del return_list[:]
count = Counter(nounsresult)
#print(count)
for n , c in count.most_common(20):
    temp = {'tag':n,'count':c}
    return_list.append(temp)

print(return_list)


# for col in return_list:
#     print(col)
    
#return_Clist=list(map(int,return_list))

df = pd.DataFrame(return_list).T
print(df)
# .T는 세로의 데이터르 가로로 나타내줌.
corr =df.corr(method='pearson')
#print(df)

print(corr)
print(corr.dropna())
#corr=return_list.corr(method = 'pearson')


#model1 = Word2Vec(koko1 , size = 200 ,  window = 2 , iter = 100 , sg = 1 , workers = 3 )
#model11 = Word2Vec(koko1 , size = 200 ,  window = 2 , iter = 100 , sg = 0 , workers = 3)


#kokoresult1 = model1.most_similar(positive = ["이승우"] ,  topn = 20 )
#kokoresult11 = model11.most_similar(positive = ["이승우"] ,  topn = 20 )

# print(kokoresult1)
# print(kokoresult11)

#model1.save('model1')
#model11.save('model11')

#df = pd.DataFrame(kokoresult1)
#df2 = pd.DataFrame(kokoresult11)





