# 셀레늄 사용하려면 웹 드라이버 다운로드해야함 (일단 크롬기준)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()#현재폴더에 크롬드라이버가 있어서 경로를 안적음
# 경로가 다른곳에 크롬이 있다면 아래와 같이 경로 적어줘야함
# browser = webdriver.Chrome("C:\Users\이근호\Desktop\NadoCoding\chromedriver.exe")

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id") # 실제 id를 입력하면 됨
browser.find_element_by_id("pw").send_keys("naver_pw") # 실제 pw 입력 

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id 를 새로입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료

# 3:21:31 부터