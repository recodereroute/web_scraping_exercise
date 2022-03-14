import requests
res = requests.get("http://google.com")
res.raise_for_status() # 문제가 생긴경우 바로 에러를 내뱉고 프로그램 종료

# res = requests.get("http://nadocoding.tistory.com")
# print("응답코드 : ", res.status_code) # 200 : 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)