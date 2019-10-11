from bs4 import BeautifulSoup as BS
import ssl
import urllib
import traceback
import requests

base_url = 'https://www.google.co.kr/search'

values = {
    'q' : '조국', 
    'aqs' : 'chrome..69i57.35694j0j7',
    'sourceid' : 'chrome',
    'ie': 'UTF-8'
} 

hdr = {'User-Agent': 'Mozilla/5.0'}

query_string = urllib.parse.urlencode(values)
req = urllib.request.Request(base_url + '?' + query_string, headers=hdr)
context = ssl._create_unverified_context()
try:
    res = urllib.request.urlopen(req,context=context)
except:
    html_data = BS(res.read(),'html.parser')

    g_list = html_data.find_all('div',attrs={'class':'g'})

try:
    for g in g_list:
        ahref = g.find('a')['href']
        ahref = 'https://www.google.co.kr'+ ahref

        span = g.find('span',attrs = {'class':'st'})
        if span:
            span_text = span.get_text()
            span_text = span_text.replace(' ','')
            span_text = span_text.replace('\n','')
except:
    traceback.print_exc()



