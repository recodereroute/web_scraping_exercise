import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

for i in range(1,6):
    # 1 ~ 5 페이지내의
    print("페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=노트북&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:
        # 광고제품은 제외
        ad_badge = item.find("span", attrs = {"class":"ad-badge-text"})
        if ad_badge:
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()
        # 애플 제품 제외
        if "Apple" in name:
            continue

        # 가격
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        # 평점 -> 평점이 없는 상품이 있음 -> 에러발생(예외처리 분기해줘야 함)
        # 리뷰 100개 이상, 평정 4.5이상 되는것만 조회
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점 없음"
            continue
        # 평점 수
        rate_count = item.find("span", attrs={"class":"rating-total-count"})
        if rate_count:
            rate_count = rate_count.get_text()[1:-1]
        else:
            rate_count = "평점 수 없음"
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_count) >= 100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_count}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100) # 줄 긋기

# 2:22:45 부터