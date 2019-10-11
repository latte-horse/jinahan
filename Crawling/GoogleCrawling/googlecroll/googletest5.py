import requests
import bs4
import pandas as pd

url = 'https://news.google.com/search?q=%EB%8C%80%ED%95%9C%ED%95%AD%EA%B3%B5&hl=ko&gl=KR&ceid=KR%3Ako'

resp = requests.get(url)
soup = bs4.BeautifulSoup(resp,'lxml')

items = soup.select('h3>a')