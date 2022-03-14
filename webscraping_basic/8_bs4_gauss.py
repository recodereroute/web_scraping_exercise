import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print("https://comic.naver.com"+link)

# 만화제목 + 링크가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 계산하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    # rate = cartoon.strong.get_text()
    print(rate)
    total_rates += float(rate)
    print(total_rates)
print("전체 점수: ", total_rates) # 숫자 튀는 이유 : 파이썬은 계산시 2진수로 바꾸고 출력할때 다시 10진수로 바꿈 -> 이러한 과정에서 소숫점 계산시 튀는 상황 발생
print("평균 점수: ", total_rates/len(cartoons))