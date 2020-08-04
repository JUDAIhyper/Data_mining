# 批量爬取多家公司的百度新闻
# 根据标题和正文内容进行评分
# 解决乱码
# 处理非相关信息
import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}


def baidu(company):
    url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=' + company
    res = requests.get(url, headers=headers, timeout=10).text
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
        # 爬取正文
        try:
            article = requests.get(href[i], headers=headers, timeout=10).text
        except:
            article = '单个新闻爬取失败'

        try:
            article = article.encode('ISO-8859-1').decode('utf-8')
        except:
            try:
                article = article.encode('ISO-8859-1').decode('gbk')
            except:
                article = article

        # 筛选有效信息
        p_article = '<p>(.*?)</p>'
        article_main = re.findall(p_article, article)
        article = ''.join(article_main)

        # 根据正文和标题进行评分
        for k in keywords:
            if (k in title[i]) or (k in article):
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
