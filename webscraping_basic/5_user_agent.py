import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status() # 문제가 생긴경우 바로 에러를 내뱉고 프로그램 종료

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)