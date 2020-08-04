# 批量按时间爬取多家公司多页的百度新闻
import requests
import re
import time

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
        # 输出
        # print(str(i + 1) + '.' + title[i] +
        #       '(' + date[i] + '-' + source[i] + ')')
        # print(href[i])
    # 将数据写入文件
    file1 = open(r"多页数据挖掘报告.txt", 'a', encoding='utf-8')
    file1.write(company + '数据挖掘completed!' + '\n' + '\n')
    for i in range(len(title)):
        file1.write(str(i + 1) + '.' + title[i] +
                    '(' + date[i] + '-' + source[i] + ')' + '\n')
        file1.write(href[i] + '\n')
    file1.write('-----------------------' + '\n')
    file1.close()

# 添加永久循环
# while True:
# 批量调用函数
companys = ['华能信托', '阿里巴巴', '百度集团', '腾讯', '京东', '网易']
# 加入异常处理，令程序一直运行
for company in companys:
    for i in range(20):
        try:
            baidu(company, i + 1)
            print(company + '第' + str(i + 1) + '页爬取成功')
        except:
            print(company + '第' + str(i + 1) + '页爬取失败')
# time.sleep(10800)
