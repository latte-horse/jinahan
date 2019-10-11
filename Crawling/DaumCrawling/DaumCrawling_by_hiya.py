import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib
from datetime import datetime
import lxml
import json
import pathlib

###########################################키워드 뽑아오기
html=requests.get("https://www.daum.net").text
soup=BeautifulSoup(html,'html.parser')

title_list=soup.select(".list_mini .rank_cont .link_issue")
ranking=soup.select(".list_mini .rank_cont .ir_wa")
#키워드 저장 장소 선언
htmllist=[]
del htmllist[:]
for top in title_list:
    #하나씩 저장 
    htmllist.append(top.text)

#키워드 뽑히나 확인!
print(htmllist)

###########################################키워드로 뉴스 검색
#url를 나눈다(page 1,2,3 넣고 keyword넣기 위해서)
furl="https://search.daum.net/search?w=news&sort=recency&q="
surl="&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p="
lurl="&rc=1&at=more&sd=&ed=&period="

daumlist = []
del daumlist[:]
i=0
for keyword in htmllist:
    #데이터 초기화를 위해 for문 안에 daumitem배열 선언을 한다.
    daumitem=[]
    #한페이지당 10개의 뉴스가 있으므로 30개를 가지기 위해서 3까지
    for i in range(3):
        i+=1
        #검색할 주소 를 다 더해준다.
        url = requests.get(furl + keyword + surl + str(i) + lurl).text
        #검색
        soup = BeautifulSoup(url,'html.parser')
        #뉴스의 url주소를 가져온다.
        urllink = soup.select("a[class*=f_link_b]")
        #뉴스의 제목을 가져온다.
        urlname = soup.select(".f_link_b")
        #각각을 딕셔너리에 추가한다.
        for list,list2 in zip(urllink,urlname):
            daumitem.append({"title":list2.text,"link":list.get('href')})
    daumlist.append({"keyword":keyword,"items":daumitem})


#############################################파일 저장       
#json으로저장 
with open('C:/Users/student/Documents/jinahan/Crawling/DaumCrawling/results/result.json','w',encoding = "utf-8") as make_file:
    json.dump(daumlist,make_file,ensure_ascii = False,indent="\t")