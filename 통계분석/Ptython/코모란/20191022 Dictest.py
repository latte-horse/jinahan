from konlpy.tag import Komoran

komoran=Komoran(userdic='C:/Users/student/Documents/jinahan/통계분석/명단/user_dic_fix.txt') 
#komoran=Komoran()
sentence = '자유한국당이나 더불어민주당이나.'

komoran.pos(sentence)
print(komoran.pos(sentence))