import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# browser.find_element_by_link_text("가는 날").click()
# browser.find_element_by_css_selector('div.button#tabContent_option__2y4c6 select_Date__1aF7Y').click()
# browser.find_elements_by_class_name("tabContent_option__2y4c6")[0].click()

# 이번달 27일, 28일 선택
print(len(browser.find_elements_by_link_text("27")))
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

# 호눌룰루 선택
browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[6]/div/div[2]/div/ul/li[1]").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[10]/div[2]/div[1]/div[2]/ul/li[1]")))
    # 첫번째 결과출력
    print(elem.text)
    # 성공했을 때 동작 수행
finally:
    browser.quit()