# 웹 사이트에서 html을 읽어와 필요한 데이터를 긁어오는 것을 말함
# 기본적으로 제공하는 urllib, urllib2을 사용하건 편리한 HTTP라이브러리로 많이 쓰이고 있는 requests를 설치해 사용할 수 있다
# 만약 기존 코드를 유지 보수하는 일이 아니라면 requests를 사용할 것을 권장한다

# requests 웹 페이지 읽어오기
import requests

# GET
resp = requests.get('http://httpbin.org/get')
print(resp.text)

# POST
dic = {"id": 1, "name": "Kim", "age": 10}
resp = requests.post('http://httpbin.org/post', data=dic)
print(resp.text)

resp = requests.put('http://httpbin.org/put')
resp = requests.delete('http://httpbin.org/delete')
# requests.get(url) 함수를 사용하면 해당 웹 페이지 호출 결과를 가진 Response 객체를 리턴

import requests

resp = requests.get('http://daum.net')
# resp.raise_for_status()

if (resp.status_code == requests.codes.ok):
    html = resp.text
    print(html)

# 한글 깨짐 문제
# text의 속성은 str 클래스 타입
# 보통 requests 모듈에서 자동으로 데이터를 인코딩해줌
# 즉, requests는 HTTP헤더를 통해 결과 데이터의 인코딩 방식을 추측하여 Response 객체의 encoding 속성에 그 값을 지정하고, text 속성을 엑세스할 때 이 encoding 속성을 사용함
# 만약 인코딩 방식을 변경해야 한다면, text 속성을 읽기 전에 Response의 encoding 속성을 변경하면 된다.
# 인코딩 문제를 처리한 코드
import requests

resp = requests.get('http:..finance.naver.com/')
resp.raise_for_status()

resp.encoding=None
# resp.encoding='euc-kr' 한글 인코딩
html = resp.text
print(html)

# BeautifulSoup - 웹 페이지 파싱
# 웹 페이지 HTML 문서를 파싱(Parsing)하기 위해서는 BeautifulSoup 라는 모듈을 사용할 수 있다.
import bs4

html = "<html><body>...생략...</body></html>"
bs = bs4.BeautifulSoup(html, 'html.parser')

# BeautifulSoup 객체에서 특정 HTML 태그를 찾기 위해 select() 매소드를 사용
# 어떤 태그를 찾을지는 CSS 스타일의 Selector로 지정하면 된다.
import requests, bs4

resp = requests.get('http://finance.naver.com/')
resp.raise_for_status()

resp.encoding='euc-kr'
html = resp.text

bs = bs4.BeautifulSoup(html, 'html.parser')
tags = bs.select('div.news_area h2 a') # 네이버 증권사이트 주요 Top 뉴스 제목 발췌
title = tags[0].getText()
print(title)