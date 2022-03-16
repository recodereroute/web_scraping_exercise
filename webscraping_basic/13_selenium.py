# 셀레늄 사용하려면 웹 드라이버 다운로드해야함 (일단 크롬기준)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()#현재폴더에 크롬드라이버가 있어서 경로를 안적음
# 경로가 다른곳에 크롬이 있다면 아래와 같이 경로 적어줘야함
# browser = webdriver.Chrome("C:\Users\이근호\Desktop\NadoCoding\chromedriver.exe")
browser.get("http://naver.com")

# 3:13:50 부터