import requests
import requests
from bs4 import BeautifulSoup

req = requests.get('https://beomi.github.io/beomi.github.io_old/')
html = req.text
header = req.headers
status = req.status_code
is_ok=req.ok

soup=BeautifulSoup(html,'html.parser')

titles = soup.select(

'body > h3:nth-child(4) > a'

)

print(titles)

# https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/