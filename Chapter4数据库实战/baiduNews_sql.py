# 爬取百度新闻存入数据库
import requests
import re
import pymysql

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
    # 存入数据库
    for i in range(len(title)):
        db = pymysql.connect(host='localhost', port=3306, user='root',
                             password='root', database='pachong', charset='utf8')
        # 引入会话指针,调用sql语句
        cur = db.cursor()
        sql = 'INSERT INTO test(company,title,href,date,source) VALUES(%s,%s,%s,%s,%s)'
        cur.execute(sql, (company, title[i], href[
                    i], date[i], source[i]))  # 执行sql语句
        db.commit()  # 更新数据表
        cur.close()  # 关闭会话指针
        db.close()  # 关闭数据库连接

# 批量调用函数
companys = ['阿里巴巴', '百度集团', '腾讯', '京东', '网易']
# 加入异常处理，令程序一直运行
for i in companys:
    try:
        baidu(i)
        print(i + 'finish')
    except:
        print(i + 'fail')
