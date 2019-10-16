import konlpy
from collections import Counter

# 저는 이미 khaiii로 형태소 분석이 끝났기 때문에 불필요 할 것 같습니다.
# 대신에 collections 의 counter 함수를 이용해서 빈도수만 채크

def get_key(text, ntags=30):
    nouns = "파일 경로"
    #경로에 있는 파일을 저장.
    count =Counter(nouns)
    # 참고: https://excelsior-cjh.tistory.com/94
    return_list=[]
    for n,c in count.most_common(ntags):
        temp = {'tag':n,'count':c}
        return_list.append(temp)

    return return_list


text_file="형태소 분석이 끝난 파일경로"
#형태소 분석이 끝난 파일
noun_count = 20
#빈도수 20개의 명사
output_file = "count.txt"
#빈도수 측정
open_text = open("형태소 분석이 끝난 파일경로",'r',-1,"utf-8")
#파일을 가지고옴.
text = open_text.read()
#파일을 읽어들임
keys = get_key(text, ntags=30)

for key in range(keys):
    noun = tag['tag']