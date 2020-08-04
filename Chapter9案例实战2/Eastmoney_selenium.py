from selenium import webdriver
import re


def dongfang(company):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_option)
    url = 'http://so.eastmoney.com/news/s?keyword=' + company
    browser.get(url)
    data = browser.page_source
    browser.quit()
    # print(data)
    # 提取各项数据
    p_title = '<div class="news-item"><h3><a href=".*?">(.*?)</a>'
    p_href = '<div class="news-item"><h3><a href="(.*?)">.*?</a>'
    p_date = '<p class="news-desc">(.*?)</p>'
    title = re.findall(p_title, data)
    href = re.findall(p_href, data)
    date = re.findall(p_date, data, re.S)
    # 数据清洗
    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        date[i] = date[i].split(' ')[0]
        print(str(i + 1) + '.' + title[i] + '-' + date[i])
        print(href[i])

companys = ['华能信托', '阿里巴巴', '腾讯', '京东', '网易']
for i in companys:
    try:
        dongfang(i)
        print(i + 'finish')
    except:
        print(i + 'fail')
