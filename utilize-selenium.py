# Selenium
# 웹 브라우저를 컨트롤하여 윕 UI를 Automation 하는 도구 중의 하나

from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://python.org")

# 예제: python.org 윕 사이트를 방문해서 상단 메인 메뉴 문자열을 출력하고, PyPI 메뉴를 클릭한 후 5초 후에 브라우저를 종료
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://python.org")

menus = browser.find_element_by_css_selector('#top ul.menu li')

pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.text)

pypi.click()

time.sleep(5)
browser.quit()
