from selenium import webdriver
import bs4 
import requests
import pandas
import parser
from bs4 import BeautifulSoup


browser = webdriver.Firefox(executable_path='C:/Users/student/Documents/jinahan/googlecroll/geckodriver.exe')
#Key_Word = [naver, daum 에서 가지고 오기로 함.]
#for 변수명 in Key_Word
#def getNewList(Key_Word, cnt):
RealPage = ["https://www.google.com/search?q="+"엄마부대"+"&sxsrf=ACYBGNSRzU3ufdsJK1P8V79WyrsOnA4NIg:1570437429290&source=lnms&tbm=nws",
                "https://www.google.com/search?q="+"엄마부대"+"&tbm=nws&ei=Ez6cXcfoJ62ymAX-goLACw&start=10&sa=N",
                "https://www.google.com/search?q="+"엄마부대"+"&tbm=nws&sxsrf=ACYBGNRHe5rC4V-P1kvtVm1bO_pnY56IrA:1570522095629&ei=70OcXcaGJqyymAW73L8Y&start=20"]

    #엄마의 부대라는 수동적 키워드 대신에 Key_Word변수가 들어가야함.

    #페이지넘기고 30개의 html 열어주는 코드

for page in RealPage:
    Next_page = browser.get(page)
    #여기서부터 제목 가지고 오는 코드
    hrefs = []
    titles = []
    for i in range(0,10):
        #페이지넘기고 30개의 html 열어주는 코드
        results = browser.find_elements_by_css_selector('div.g')
        link = results[i].find_element_by_tag_name("a.lLrAF")
        
        hrefs.append(link.get_attribute("href"))
        titles.append(link.text)
        # print(type(link))
        # print(link)
        # for href in hrefs:
        #     resp = requests.get(href)
        #     soup = bs4.BeautifulSoup(resp,'html.parser')
        #     title_area = soup.select('.lLrAF')
        #     title=[title_area]
        #     print(href)


        #여기서부터 제목 가지고 오는 코드
            # resp = requests.get(href)
            # soup = bs4.BeautifulSoup(resp.text,'lxml')
            # title_area = soup.select('.lLrAF')
            
            # for t in title_area:
            #     text= []
            #     text.append(t.text)

    print(hrefs)
    print(titles)       
            

        
                
                

        
