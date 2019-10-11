import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib
from datetime import datetime
import lxml
import json
import pathlib

########## 다음 키워드 뽑아오기 ##########
dlist = [] ## 다음 키워드 저장
html = requests.get("https://www.daum.net").text
soup = BeautifulSoup(html,'html.parser')
title_list = soup.select(".list_mini .rank_cont .link_issue")
ranking = soup.select(".list_mini .rank_cont .ir_wa")
del dlist[:]
for top in title_list:    
    dlist.append(top.text)
#print(dlist)

########### 네이버 키워드 뽑아오기 ##########
nlist20 = [] ## 네이버 키워드 저장
html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')
title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
for a in title_list :
    nlist20.append(a.get_text())
nlist = nlist20[:10]
#print(nlist)

########## 키워드 합침##########
tlist = dlist + nlist
#print(NaverDaumList)


##################################################################################

########## 다음 뉴스 검색하기 ##########
listdgo = tlist
DaumList = [] ## 다음 뉴스 저장
furl = "https://search.daum.net/search?w=news&sort=recency&q=" #url를 나눈다(page 1,2,3 넣고 keyword넣기 위해서)
surl = "&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p="
lurl = "&rc=1&at=more&sd=&ed=&period="
del DaumList[:]
for keyword in listdgo:
    #데이터 초기화를 위해 for문 안에 daumitem배열 선언을 한다.
    daumitem=[]
    #한페이지당 10개의 뉴스가 있으므로 30개를 가지기 위해서 3까지
    for i in range(3):
        #검색할 주소 를 다 더해준다.
        url = requests.get(furl + keyword + surl + str(i) + lurl).text
        #검색
        soup = BeautifulSoup(url,'html.parser')
        #뉴스의 url주소를 가져온다.
        urllink = soup.select("a[class *= f_link_b]")
        #뉴스의 제목을 가져온다.
        urlname = soup.select(".f_link_b")
        #각각을 딕셔너리에 추가한다.
        for list,list2 in zip(urllink,urlname):
            daumitem.append({"title" : list2.text , "link" : list.get('href')})
    DaumList.append({"keyword" : keyword , "items" : daumitem})


########## 네이버 뉴스 검색하기 ##########
import os
import sys
import urllib.request
client_id = "AcSs8vk1vXfmzpFkSX4h" ## 네이버 API id
client_secret = "WBwj2IuI0D"       ## 네이버 API secret

listngo = tlist
NaverList = []
for i in range(len(listngo)) :  ##len뒤에 값을 나중에 total_title로 가주자고
    Keyword = []
    Keyword.append(listngo[i])
    encText = urllib.parse.quote(listngo[i]) ##len뒤에 값을 나중에 total_title로 가주자고
    url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=30&start=1&sort=sim" #display값이 뉴스갯수   
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):  
        response_body = response.read()        
        jsonlist = json.loads(response_body.decode('utf-8'))['items']        
        TitleLink = []
        for i in jsonlist:
            TitleLink.append( {'title' : i['title'], 'link' : i['link']} )    
    else:
        print("Error Code:" + rescode)
    NaverList.append({"keyword" : Keyword , "items" : TitleLink})    

########## 뉴스 합침 ##########
TotalList = DaumList + NaverList
#print(TotalList)


########## 파일 저장 ##########    

PrintList = TotalList
with open('C:/after/out','w',encoding = "utf-8") as make_file:
    json.dump(PrintList,make_file,ensure_ascii = False,indent="\t")