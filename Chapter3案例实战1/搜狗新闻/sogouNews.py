import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}


def sogou(company):
    url = 'https://news.sogou.com/news?mod=1&sort=0&fixrank=1&query=' + company + '&shid=djt1'
    #<a href="http://www.sohu.com/a/410111862_115865" id="uigs_0" target="_blank"><em><!--red_beg-->阿里巴巴<!--red_end--></em>零售通20万小店转型便利店</a>
    res = requests.get(url, headers=headers).text
    p_href = '<a href="(.*?)" id="uigs_.*?" target="_blank">'
    p_title = '<a href=".*?" id="uigs_.*?" target="_blank">(.*?)</a>'
    p_info = '<p class="news-from">.*?&nbsp;(.*?)</p>'
    title = re.findall(p_title, res)
    href = re.findall(p_href, res)
    info = re.findall(p_info, res)
    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        title[i] = re.sub('&.*?;', '', title[i])
        info[i] = re.sub('<.*?>', '', info[i])
        print(str(i + 1) + '.' + title[i] + '-' + info[i])
        print(href[i])
# 批量调用函数
companys = ['华能信托', '阿里巴巴', '百度集团', '腾讯', '京东', '网易']
# 加入异常处理，令程序一直运行
for i in companys:
    try:
        sogou(i)
        print(i + 'finish')
    except:
        print(i + 'fail')
