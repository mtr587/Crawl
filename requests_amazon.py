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
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'cookie':'session-id=145-0030061-2482421; ubid-main=134-3550000-0012952; s_nr=1653590556418-New; s_dslv=1653590556420; s_vnum=2085590556419%26vn%3D1; lc-main=en_US; x-main="23ln3Z2jiE?wWkGEwaoRyNcYAHHAPtQXVczovos9ljt6MjMGc1cYlCTYRw6QQJ8B"; at-main=Atza|IwEBINLVo5yg7zXIJLI85AKHiPjs0qS8JVX1mFUZ1zvaZxVXyHdOkRa_50--h_Vfkt4Fjc0PdMhoJ1J5j1PD6qSb2P8s9XZ2MmMr_3DTnF7KCJmXUvsYlvZysytvbKKtNhi5C7I01B6esoqPUUvgRjj2ttzALfpmvtWVi52R1_cdeeVJmcFk6sHqB_56aKJPuOxUMv7JEwjZrQqG5ZoG1Z44XlFc; sess-at-main="wWGb5J3EbJNvmBlIGdbLVjwh/v6zwP2tRM5ZOzZdMsY="; sst-main=Sst1|PQEPWXJsLNdoqsKzuOqH08joCUS7uIJctlFetWWAjxgBoXnQUggmn9OBwdBvJK2KFVf2GSmEbu4GYYxlaMiWUv4Ia1tQkXo3HqgkqIPF2lcFsAevasp4Oxza_Pe1qakkN5Mjq2CxrRlcp0uCmVttZMuOE-tMfixn2EF-UGlcFt9UFnu7w1FBNpgdYmynTqkVe-L5qJzEda8tWpY9PnH17W0djOR7TpX7P1TaSnN6TVDSViRc5las51k1ZtsGsC-8FS8bdwvuEd2jXUDnbPVszdFNWDyWVvIouQ1oH0bA9Y5Ga6Q; session-id-time=2082787201l; i18n-prefs=USD; csd-key=eyJ3YXNtVGVzdGVkIjp0cnVlLCJ3YXNtQ29tcGF0aWJsZSI6dHJ1ZSwid2ViQ3J5cHRvVGVzdGVkIjpmYWxzZSwidiI6MSwia2lkIjoiMDkzYzFlIiwia2V5IjoiTnVsNktrTXdZT0UwM25tOXZqcHlCckVzMlZrU09zcnZXQUE1Kys1dWlIU3IyK2pOWTcyVGR2YTFqVmV2V0pVQ05wNWdHbytodm1VNmMwcWJsV25ISzBVbjMyeDlHeHg5eUd3VmhuRGh3NW01RTdPQjlKMHExK2dUN2pNalMzcCtVcW80NzdMWEdmOTF3dmdjQ203QUphUlRyRE8zRFZaSVpiR1JnUnhPY25CUDZ1elNQN1dkZ1FwVS82UVlQMFdJN1dPYnl2aTBXbVU4T0RuTVl5QS9HdGxUVjVDN0IzY3p2TlgveVN3cWQrTUJLRXBqeDNTdjhJZXdtQU5nNGsvOU42UkI2OGJoTWJiN1J0cEs5Mk9DOE1QT0h4THZoSDVjWjViNVZjcVF3STJuYmdraFhNOWFwKzREOWtNbXdSRkFYWmd0aStINTdVMkVDTVpNYkE2dWd3PT0ifQ==; skin=noskin; session-token=VBMuZGx6HM57IQVw/mkq8uyToQVWwQtOUhpu8c7pzF3+a6DSszTq6tN3JkiJrSrHTwGpw98/PnsweQEqs3QRulkPMjtOCuysxV2NaTB7xLMyosHX0BlYjT8vwUmSgAKMfp4et54v7iloj+L9bN1KV6OeYS4mc0QW31ZlyVy9bj3gWyJhH+291gKo4oIWpfW8oM2UIAhlKsnPCeqcMbuCCXZ7X2cgrSH6Bh+y0482P1JABqjXnaBY/MS4wempzX2r; csm-hit=tb:8SJX38N7WAKZPZ8SE689+s-GKC005F7PQB3QEABMPG3|1673143988753&t:1673143988753&adb:adblk_yes'
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






