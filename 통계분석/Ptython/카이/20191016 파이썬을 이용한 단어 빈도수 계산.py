import konlpy
from collections import Counter

# 저는 이미 khaiii로 형태소 분석이 끝났기 때문에 불필요 할 것 같습니다.
# 대신에 collections 의 counter 함수를 이용해서 빈도수만 채크

# def get_key(text, ntags=30):
nouns = open("C:/Users/student/Documents/jinahan/형태소분석/코모란/komoran.txt")
#경로에 있는 파일을 저장.
count =Counter(nouns)
# 참고: https://excelsior-cjh.tistory.com/94
return_list=[]
for n,c in count.most_common(20):
    temp = {'tag':n,'count':c}
    return_list.append(temp)

print(return_list)

# text_file="C:/Users/student/Documents/jinahan/통계분석/sample_file/words.txt"
# #형태소 분석이 끝난 파일
# noun_count = 20
# #빈도수 20개의 명사
# output_file = "C:/Users/student/Documents/jinahan/통계분석/sample_file/count.txt"
# #빈도수 측정
# open_text = open(text_file,'r',-1,"utf-8")
# #파일을 가지고옴.
# text = open_text.read()
# #파일을 읽어들임
# keys = get_key(text, ntags=30)
# open_ouput_file =open(output_file)
# for key in range(keys):
#     noun = key['key']
#     count = key['count']
#     open_ouput_file.write('{} {}\n'.format(noun,count))
#     # 결과 저장 , 참고: .forat https://programmers.co.kr/learn/courses/2/lessons/63 
# open_ouput_file.close()