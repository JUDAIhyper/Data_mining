import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}


def sina(company):
    url = 'https://search.sina.com.cn/?q=' + \
        company + '&c=news&from=channel&ie=utf-8'
    res = requests.get(url, headers=headers, timeout=10).text
    # 正则表达式
    p_title = '<h2><a href=".*?" target="_blank">(.*?)</a>'
    p_href = '<h2><a href="(.*?)" target="_blank">'
    p_info = '<span class="fgray_time">(.*?)</span>'
    title = re.findall(p_title, res, re.S)
    href = re.findall(p_href, res, re.S)
    info = re.findall(p_info, res, re.S)
    # 数据清洗
    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        info[i] = re.sub('<.*?>', '', info[i]).strip()
        print(str(i + 1) + '.' + title[i] + '-' + info[i])
        print(href[i])

# 批量调用函数
companys = ['阿里巴巴', '百度集团', '腾讯', '京东', '网易']
# 加入异常处理，令程序一直运行
for i in companys:
    try:
        sina(i)
        print(i + 'finish')
    except:
        print(i + 'fail')
