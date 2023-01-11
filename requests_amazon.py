import time

import requests
import parsel
import urllib.request
import re


product = input('Enter what you want: ')
for i in range(1, 21):
    print(f'page {i}')
    base_url = 'https://www.amazon.com/s?'
    url = base_url + 'k=' + str(product) + f'&page={i}'

    headers = {
        'user-agent':'YOUR UA',
        'cookie':'YOUR COOKIE'
    }

    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    content = response.text

    a = parsel.Selector(content)
    li = a.xpath('//div/img[@class="s-image"]')
    for i in li:
        name = i.xpath('./@alt').get()
        img = i.xpath('./@src').get()
        if name.startswith('Sponsored') or name == '':
            continue
        mode = re.compile(r'[\\\/\:\*\?\<\>\"\|]')
        name = re.sub(mode, '_', name)
        urllib.request.urlretrieve(url=img, filename=name + '.jpg')
        # print(name, img)






