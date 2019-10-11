from selenium import webdriver
import bs4 
import requests
import pandas
import parser
from bs4 import BeautifulSoup

#def gglist(Key_Word):
browser = webdriver.Firefox(executable_path='C:/Users/student/Documents/jinahan/googlecroll/geckodriver.exe')
RealPage = ["https://www.google.com/search?q="+"이다희"+"&sxsrf=ACYBGNSRzU3ufdsJK1P8V79WyrsOnA4NIg:1570437429290&source=lnms&tbm=nws",
            "https://www.google.com/search?q="+"이다희"+"&tbm=nws&ei=Ez6cXcfoJ62ymAX-goLACw&start=10&sa=N",
            "https://www.google.com/search?q="+"이다희"+"&tbm=nws&sxsrf=ACYBGNRHe5rC4V-P1kvtVm1bO_pnY56IrA:1570522095629&ei=70OcXcaGJqyymAW73L8Y&start=20"]

for page in RealPage:
    Next_page = browser.get(page)
    hrefs = []
    titles = []

    for i in range(0,10):
        results = browser.find_elements_by_css_selector('div.g')
        link = results[i].find_element_by_tag_name("a.lLrAF")
        hrefs.append(link.get_attribute("href"))
        titles.append(link.text)

for whole in range(0,3):
    for list_up in range(0,10):
        print(hrefs[list_up])
        print(titles[list_up])


browser.close()          