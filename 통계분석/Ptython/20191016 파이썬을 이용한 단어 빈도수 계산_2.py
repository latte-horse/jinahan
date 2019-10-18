import konlpy
from collections import Counter

# 저는 이미 khaiii로 형태소 분석이 끝났기 때문에 불필요 할 것 같습니다.
# 대신에 collections 의 counter 함수를 이용해서 빈도수만 채크

# def get_key(text, ntags=30):
nouns = open("C:/Users/student/Documents/jinahan/통계분석/sample_file/words.txt",encoding='utf-8')
#경로에 있는 파일을 저장.
noun_count = 20
count =Counter(nouns)
# 참고: https://excelsior-cjh.tistory.com/94
return_list=[]
for n,c in count.most_common(noun_count):
    temp = {'key':n.replace("\n",""),'count':c}
    return_list.append(temp)

output_file = "C:/Users/student/Documents/jinahan/통계분석/sample_file/count.txt"
keys = return_list
for key in range(len(keys)):
    noun = key
    count = key
    output_file.write('{} {}\n'.format(noun,count))
    # 결과 저장 , 참고: .forat https://programmers.co.kr/learn/courses/2/lessons/63 
output_file.close()