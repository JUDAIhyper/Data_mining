# 批量按时间爬取多家公司多页的百度新闻
import requests
import re
import time
import pymysql

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}


def baidu(company, page):
    num = (page - 1) * 10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + \
        company + '&pn=' + str(num)
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

    # 数据清洗
    source = []
    date = []
    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])
        info[i] = re.sub('<.*?>', '', info[i])
        source.append(info[i].split('&nbsp;&nbsp;')[0])
        date.append(info[i].split('&nbsp;&nbsp;')[1])
        source[i] = source[i].strip()
        date[i] = date[i].strip()

        # 统一日期格式
        date[i] = date[i].split(' ')[0]
        date[i] = re.sub('年', '-', date[i])
        date[i] = re.sub('月', '-', date[i])
        date[i] = re.sub('日', '', date[i])
        if('小时' in date[i]) or ('分钟' in date[i]):
            date[i] = time.strftime("%Y-%m-%d")
        else:
            date[i] = date[i]

    # 舆情数据评分系统版本4级数据深度清洗
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
        # 数据深度清洗
        company_re = company[0] + '.{0,5}' + company[-1]
        if len(re.findall(company_re, article)) < 1:
            title[i] = ''
            source[i] = ''
            href[i] = ''
            date[i] = ''
            score[i] = ''
    while '' in title:
        title.remove('')
    while '' in href:
        href.remove('')
    while '' in date:
        date.remove('')
    while '' in source:
        source.remove('')
    while '' in score:
        score.remove('')

    # 打印清洗后的数据
    for i in range(len(title)):
        print(str(i + 1) + '.' + title[i] +
              '(' + date[i] + '-' + source[i] + ')')
        print(href[i])
        print(company + '该条新闻的舆情评分为' + str(score[i]))

    # 将数据存入数据库并去重
    for i in range(len(title)):
        db = pymysql.connect(host='localhost', port=3306, user='root',
                             password='root', database='pachong', charset='utf8')
        # 引入会话指针,调用sql语句
        cur = db.cursor()

        # 查询数据，为之后的数据去重做准备
        sql_1 = 'SELECT * FROM article WHERE company=%s'
        cur.execute(sql_1, company)
        data_all = cur.fetchall()
        title_all = []
        for j in range(len(data_all)):
            title_all.append(data_all[j][1])

        # 判断爬取的数据是否在数据库中，不在的话才存入
        if title[i] not in title_all:
            sql_2 = 'INSERT INTO article(company,title,date,source,href,score) VALUES (%s,%s,%s,%s,%s,%s)'
            cur.execute(sql_2, (company, title[i], date[
                        i], source[i], href[i], score[i]))
            db.commit()
        cur.close()
        db.close()
    print('-----------------------------------')

# 添加永久循环
# while True:
# 批量调用函数
companys = ['万科集团', '华能信托', '阿里巴巴', '百度集团', '腾讯', '京东', '网易']
# 加入异常处理，令程序一直运行
for company in companys:
    for i in range(20):
        try:
            baidu(company, i + 1)
            print(company + '第' + str(i + 1) + '页爬取成功')
        except:
            print(company + '第' + str(i + 1) + '页爬取失败')
    # time.sleep(10800)
    # baidu(company)
