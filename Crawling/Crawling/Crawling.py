import codecs
import requests
import os
import sys
import shutil
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import urllib
from datetime import datetime
import lxml
import json
import pathlib
import time
import datetime



#################다음키워드 뽑아오기############################
def DaumCrawling():
    html=requests.get("https://www.daum.net").text
    soup=BeautifulSoup(html,'html.parser')

    title_list=soup.select(".list_mini .rank_cont .link_issue")
    ranking=soup.select(".list_mini .rank_cont .ir_wa")
    htmllist=[]
    del htmllist[:]
    for top in title_list:

        htmllist.append(top.text)

    ################키워드로 뉴스 검색 ############################
    #url를 나눈다(page 1,2,3 넣고 keyword넣기 위해서)
    furl="https://search.daum.net/search?w=news&sort=recency&q="
    surl="&cluster=n&DA=STC&s=NS&a=STCF&dc=STC&pg=1&r=1&p="
    lurl="&rc=1&at=more&sd=&ed=&period="

    daumlist = []
    del daumlist[:]
    i=0
    for keyword in htmllist:
        daumitem=[]
        for i in range(3):
            i+=1
            url = requests.get(furl + keyword + surl + str(i) + lurl).text
            
            soup = BeautifulSoup(url,'html.parser')
            urllink = soup.select("a[class*=f_link_b]")
            urlname = soup.select(".f_link_b")
            for list,list2 in zip(urllink,urlname):
                daumitem.append({"title":list2.text,"link":list.get('href')})
        daumlist.append({"keyword":keyword,"items":daumitem})

    ################파일 저장###########################
        
    #json으로저장 
    with open('C:/Users/user/Documents/jinahan/Crawling/Crawling/results/DCrawling.json','w',encoding = "utf-8") as make_file:
        json.dump(daumlist,make_file,ensure_ascii = False,indent="\t")



########### 네이버 검색어 가져오기 ######################################
def NaverCrawling():
    html = requests.get('https://www.naver.com/').text
    soup = BeautifulSoup(html, 'html.parser')
    title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

    info = []
    for a in title_list :
        info.append(a.get_text())
    N_title = info[:10]

    client_id = "AcSs8vk1vXfmzpFkSX4h"
    client_secret = "WBwj2IuI0D"
    ranlist = N_title

    for i in range(len(ranlist)) :  
        encText = urllib.parse.quote(ranlist[i]) 
        url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=30&start=1&sort=sim" #display값이 뉴스갯수

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        

        if(rescode==200):
            response_body = response.read()      
            file = codecs.open('C:/Users/user/Documents/jinahan/Crawling/Crawling/results/NCrawling.json', 'a', 'utf8')
            file.write(response_body.decode('utf-8'))
            file.close() 
        else:
            print("Error Code:" + rescode)
            
##############폴더 만들기####################

def get_today() :
    now = time.localtime()
    s = "%04d-%02d-%02d" % (now.tm_year,now.tm_mon,now.tm_mday)
    return s

def get_time() :
    now = time.localtime()
    now_time = time.localtime()
    t = "%02d%02d" %(now.tm_hour,now.tm_min)
    return t

def make_folder(folder_name) :
    if not os.path.isdir(folder_name) :
        os.mkdir(folder_name)


root_dir="C:/Users/user/Documents/jinahan/Crawling/etc"
today = get_today()
work_dir = root_dir + "/" + today

make_folder(work_dir)        

root_dir_2 = work_dir
time = get_time()
work_dir_2 = root_dir_2+"/"+time

make_folder(work_dir_2)

# ####### 데이터 프레임 구조 #########
totalKey_word = [htmllist,N_title]

df1 = pd.DataFrame({'Data':pd.Timestamp('20191014'),
                    'KeyWord':totalKey_word,
                    'URL':3,
                    'Description': 2})