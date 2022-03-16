import requests
from bs4 import BeautifulSoup


for year in range(2017, 2022):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})
    for idx, img in enumerate(images):
        # print(img["src"])
        img_url = img["src"]
        if img_url.startswith("//"):
            img_url = "https://" + img_url
        print(img_url)
        img_res = requests.get(img_url)
        img_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(img_res.content)
        
        # 상위 5개의 이미지만 받겠음
        if idx >= 4:
            break


# 2:31:47 부터