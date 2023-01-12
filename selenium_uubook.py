from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

# 问题基本解决，ending不完美，但无伤大雅

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable‐gpu')
chrome_options.add_argument("--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'")
#自己的Chrome浏览器文件路径
path = r'C:/webdriver/chromedriver.exe'
service = Service(path)
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
# 主页： ‘https://www.uukanshu.com/’
url = 'https://www.uukanshu.com/b/197887/178474.html'           # 起始章节
driver.get(url)

with open('../陈医生，别怂.txt', 'a', encoding='utf-8') as fp:
    while True:
        a = driver.find_element(By.ID, 'timu')
        fp.write(a.text + '\n' + '\n')
        t = time.perf_counter()
        if t >60:
            minutes = t//60
            second = t % 60
            use = ' {:.0f} 分{:.0f} 秒'.format(minutes, second)
        else:
            use = ' {:.0f} 秒'.format(t)
        print(a.text + use)
        b = driver.find_elements(By.TAG_NAME, 'p')
        for i in b:
            fp.write(i.text + '\n' + '\n')
        try:
            js_bottom = 'document.documentElement.scrollTop=100000'
            driver.execute_script(js_bottom)
            AC(driver).move_by_offset(2, 10).click().perform()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(('id', 'next')))
            time.sleep(1)
            driver.find_element(By.ID, 'next').click()
        except:
            c = driver.find_element(By.CSS_SELECTOR, '#next').get_attribute('href')
            driver.get(c)




driver.quit()
