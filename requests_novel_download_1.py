import requests
import time
import re
import parsel

# 已成熟
# 主页1：https://www.xbiquge.tw/
# 主页2：https://www.ptzw.com/
base_url = 'https://www.xbiquge.bz/book/7888/'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
response = requests.get(url=base_url, headers=headers)
response.encoding = 'utf-8'
content = response.text

start_time = time.time()

"""下面输入获取方法跟保存"""

a = parsel.Selector(content)            # 或者用re，用re就可以注释这一行
# all_novels = a.xpath('//div[@id="list"]/dl/dd//@href')          # so的
all_novels = a.xpath('//div/dl/dd/a/@href')
# all_novels = a.xpath('//*[@id="catalog"]/ul/li/a/@href')
full_all_novels = []
for i in all_novels:
    b = base_url + i.get()
    full_all_novels.append(b)

print(full_all_novels)
n = 1
key_words = ['PS:', '幕山', '正版', '订阅', '月票', '推荐', '收藏']

with open('请公子斩妖.txt', 'a', encoding='utf-8') as f:
    for i in full_all_novels[12:]:
        response = requests.get(url=i, headers=headers)
        response.encoding = 'gbk'
        info = response.text
        b = parsel.Selector(info)
        title = b.xpath('//h1/text()').extract_first()
        f.write(title + '\n')
        # y = '第' + str(n) + '章' + title[title.rfind(' '):]  # 这三行是针对奇怪标题使用的，否则使用上一行的注释
        # f.write(title + '\n')
        n += 1
        print(title)                                            # 如果不是奇怪的标题就使用print(title)
        read = b.xpath('//div[@id="content"]/text()').extract()
        # read = b.xpath('//div/div/div/text()').extract()
        for i in read[1:]:
            if i.__contains__('ps:'):
                continue
            f.write(i.replace('\\\\', '') + '\n')
        # print(read)

end_time = time.time()

use_time = end_time - start_time
print(use_time)

# break是直接下载下一章
# continue是跳过该行去下一行