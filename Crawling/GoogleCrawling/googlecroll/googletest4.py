from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:/Users/student/Documents/jinahan/googlecroll/chromedriver.exe')

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

r = soup.select('.r')

for i in r:
    print

