# 批量爬取多家公司的百度新闻
# 根据标题进行评分
import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}


def baidu(company):
    url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=' + company
    res = requests.get(url, headers=headers).text
    # 提取链接
    p_href = '<h3 class="c-title">.*?<a href="(.*?)"'
    # 提取标题
    p_title = '<h3 class="c-title">.*?>(.*?)</a>'
    # 提取新闻来源和日期
    p_info = '<p class="c-author">(.*?)</p>'
    # 匹配正则
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    info = re.findall(p_info, res, re.S)
    # print(info)

    # 舆情数据评分系统版本1----根据新闻标题中是否出现特定的负面词来打分
    score = []
    keywords = ['违约', '诉讼', '兑付', '阿里', '百度', '京东', '互联网']
    for i in range(len(title)):
        num = 0
        for k in keywords:
            if k in title[i]:
                num -= 5
        score.append(num)

    # 数据清洗及舆情数据评分打印
    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])
        print(str(i + 1) + '.' + title[i])
        print(href[i])
        print(company + '该条舆情评分为' + str(score[i]))


# 批量调用函数
companys = ['万科集团', '阿里巴巴', '百度', '腾讯', '京东']
for i in companys:
    try:
        baidu(i)
        print(i + 'finish')
    except:
        print(i + 'fail')
