# 20191011 Naver Crawling  소스 해석



### UrlLib 라이브러리를 활용한 크롤링

------



```python
import urllib.request
import json

client_key = '클라이언트 키'
client_secret = '시크릿 키'

# 한글등 non-ASCII text를 URL에 넣을 수 있도록 "%" followed by hexadecimal digits 로 변경
# URL은 ASCII 인코딩셋만 지원하기 때문임
encText = urllib.parse.quote_plus("스마트폰")
# print(encText)

naver_url = 'https://openapi.naver.com/v1/search/news.json?query=' + encText

# urllib.request.Request()는 HTTP Header 변경시에 사용함
# 네이버에서도 다음 HTTP Header 키를 변경해야하기 때문에 사용함
# HTTP Header 변경이 필요없다면, 바로 urllib.request.urlopen()함수만 사용해도 됩
request = urllib.request.Request(naver_url)
request.add_header("X-Naver-Client-Id",client_key)
request.add_header("X-Naver-Client-Secret",client_secret)

# urllib.request.urlopen 메세드로 크롤링할 웹페이지를 가져옴
response = urllib.request.urlopen(request)


# getcode() 메서드로 HTTP 응답 상태 코드를 가져올 수 있음
rescode = response.getcode()

# HTTP 요청 응답이 정상적일 경우, 해당 HTML 데이터를 수신되었기 때문에 필요한 데이터 추출이 가능함
# HTTP 요청에 대한 정상응답일 경우, HTTP 응답 상태 코드 값이 200이 됩니다.
if(rescode == 200):
    # response.read() 메서드로 수신된 HTML 데이터를 가져올 수 있음
    response_body = response.read()
    # 네이버 Open API를 통해서 수신된 데이터가 JSON 포멧이기 때문에, 
    # JSON 포멧 데이터를 파싱해서 사전데이터로 만들어주는 json 라이브러라를 사용
    data = json.loads(response_body)
    # json.loads() 메서드를 사용해서 data 에 수신된 데이터를 사전 데이터로 분석해서 자동으로 만들어줌
    print (data['items'][0]['title'])
    print (data['items'][0]['description'])
else:
    print("Error Code:" + rescode)
    
    출처:https://www.fun-coding.org/crawl_basic3.html
```



#### 딕셔너리 구조

------



>  JSON 포멧 예
> { "id":"01", "language": "Java", "edition": "third", "author": "Herbert Schildt" }



### Requests 라이브러리를 활용한 크롤링

------

```python
mport requests

client_key = 'CsODwdUTyG9vOI1uIeIf'
client_secret = 'YmIx0GW8JG'
# 별도 quote_plus() 메서드등 처리할 필요 없음. requests 객체가 알아서 해줌
naver_url = 'https://openapi.naver.com/v1/search/news.json?query=스마트폰'

header_params = {"X-Naver-Client-Id":client_key, "X-Naver-Client-Secret":client_secret}
# headers= header_params 는 header 변경시에만 필요하고, 그렇지 않으면, requests.get(원하는 URL) 만 해도 됨
response = requests.get(naver_url, headers = header_params)
# 별도 json.loads() 라이브러리 메서드 사용하지 않아도, reqeusts 라이브러리에 있는 json() 메서드로 간단히 처리 가능함
# print(response.json())
# print(response.text)

# HTTP 응답 코드는 status_code 에 저장됨
if(response.status_code == 200):
    data = response.json()
    print(data['items'][0]['title'])
    print(data['items'][0]['description'])
else:
    print("Error Code:" + response.status_code)
    
     출처:https://www.fun-coding.org/crawl_basic3.html
```

