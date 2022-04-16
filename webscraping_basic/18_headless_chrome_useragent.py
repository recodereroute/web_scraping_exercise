import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True # 크롬을 띄우지 않고 작업진행
options.add_argument("window-size=1920x1080") # 본인 화면 사이즈
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
# headlessChrome 사용하면 원래의 user-agent 정보가 날아가고 headlessChrome 정보가 들어가있음(차단의 원인이 될수있음) -> 전처리 필요
print(detected_value.text)
browser.quit()