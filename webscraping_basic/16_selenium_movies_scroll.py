# 동적페이지 크롤링 처리 -> 네이버 쇼핑 처리하려면 필요
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url ="https://play.google.com/store/movies/top?hl=ko&gl=US"
browser.get(url) # 셀레늄을 통해 페이지 정보를 가져올때는 헤더정보가 필요없음

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # x, y 좌표

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

print("스크롤 완료")

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"WHE7ib mpg5gc"})
# movies = soup.find_all("div", attrs={"class":["WHE7ib mpg5gc", "Vpfmgd"]}) # 클래스가 리스트안에 있는것중 하나라도 일치하는걸 전부 가져오기 위해서 쓰이는 로직
print(len(movies))

for movie in movies:
    # title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"})["title"]
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, " <할인하지 않는 영화는 제외>")
        continue
    # 할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    print(price)

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 :  https://play.google.com/ + link
    print(f"제목 :{title}")
    print(f"할인 전 가격 : {original_price}")
    print(f"할인 후 가격 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 120)

browser.quit()