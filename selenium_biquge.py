from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
import time


path = 'C:/webdriver/chromedriver.exe'
driver = webdriver.Chrome(path)

# 访问网站，使用 笔趣阁       https://www.xbiquge.so/
url = 'https://www.xbiquge.so/book/54523/38644956.html'           # 小说起始章节
driver.get(url)
with open('../宇宙职业选手.txt', 'a', encoding='utf-8') as fp:
    while True:
        a = driver.find_element(By.TAG_NAME, 'h1')
        fp.write(a.text + '\n' + '\n')
        # print(a.text)
        b = driver.find_elements(By.ID, 'content')
        for i in b:
            fp.write(i.text + '\n' + '\n')
        try:
            js_bottom = 'document.documentElement.scrollTop=100000'
            driver.execute_script(js_bottom)
            AC(driver).move_by_offset(2, 10).click().perform()
            c = driver.find_element(By.LINK_TEXT, '下一章').click()
        except:
            js_bottom = 'document.documentElement.scrollTop=100000'
            driver.execute_script(js_bottom)
            AC(driver).move_by_offset(2, 10).click().perform()
            c = driver.find_element(By.LINK_TEXT, '下一章').click()


# driver.quit()
