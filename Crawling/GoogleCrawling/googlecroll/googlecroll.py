import requests
from bs4 import BeautifulSoup

def spider(max_pages):
	 page = 1
	 while page < max_pages:
		 url = 'http://creativeworks.tistory.com/' +str(page)
		 source_code = requests.get(url)
		 plain_text = source_code.text
		 soup = BeautifulSoup(plain_text,'lxml')
		 for link in soup.select('h2>a'):
			 href = 'http://creativeworks.tistory.com/' + link.get('herf')
			 title=link.string
			 print(href)
			 print(title)
	 page += 1

def get_single_article(item_url):
    source_code = requests.get(item_url)
	plain_text = source_code.text


spider(2)