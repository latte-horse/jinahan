
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path='C:/Users/student/Documents/jinahan/googlecroll/geckodriver.exe')
# 실행을 하기 위해서는 https://github.com/mozilla/geckodriver/releases 로들어가서 드라이버 다운해야 합니다.
browser.get("https://www.google.com/search?q="+"엄마부대"+"&sxsrf=ACYBGNSRzU3ufdsJK1P8V79WyrsOnA4NIg:1570437429290&source=lnms&tbm=nws")

results = browser.find_elements_by_css_selector('div.g')

hrefs = []

for i in range(0,10):
    link = results[i].find_element_by_tag_name("a")
    hrefs.append(link.get_attribute("href"))

for href in hrefs:
    print(href)

#from furl import furl
#f = furl(href)


   # browser.execute_script('window.open("'+ href +'","_blank");')

# print(f.args['url'])

#html = urllib.request.urlopen(results).read()
#soup = BeautifulSoup(html,'html.parser')

#table = soup.find('a aria-label',{'class': 'f1'})

#print(soup)

browser.get("https://www.google.com/search?q="+"엄마부대"+"&tbm=nws&ei=Ez6cXcfoJ62ymAX-goLACw&start=10&sa=N")
results = browser.find_elements_by_css_selector('div.g')


hrefs = []

for i in range(0,10):
    link = results[i].find_element_by_tag_name("a")
    hrefs.append(link.get_attribute("href"))

for href in hrefs:
    print(href)

#from furl import furl
#f = furl(href)


   # browser.execute_script('window.open("'+ href +'","_blank");')
  
# print(f.args['url'])

#html = urllib.request.urlopen(results).read()
#soup = BeautifulSoup(html,'html.parser')

#table = soup.find('a aria-label',{'class': 'f1'})
#print(soup)
browser.get("https://www.google.com/search?q="+"엄마부대"+"&tbm=nws&sxsrf=ACYBGNRHe5rC4V-P1kvtVm1bO_pnY56IrA:1570522095629&ei=70OcXcaGJqyymAW73L8Y&start=20")
results = browser.find_elements_by_css_selector('div.g')


hrefs = []

for i in range(0,10):
    link = results[i].find_element_by_tag_name("a")
    hrefs.append(link.get_attribute("href"))

for href in hrefs:
    print(href)

#from furl import furl
#f = furl(href)


  #  browser.execute_script('window.open("'+ href +'","_blank");')

    