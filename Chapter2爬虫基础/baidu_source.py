import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}
url = 'https://baijiahao.baidu.com/s?id=1673178924816631259&wfr=spider&for=pc'
res = requests.get(url, headers=headers).text
p_title = '<div class="article-title">.*?>(.*?)</h2>'
title = re.findall(p_title, res)
print(title)
