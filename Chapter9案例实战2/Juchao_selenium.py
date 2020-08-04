from selenium import webdriver
import re
import time


def juchao(keyword):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--headless')
    url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=' + keyword
    browser = webdriver.Chrome(options=chrome_option)
    browser.maximize_window()
    browser.get(url)
    data = browser.page_source

    # 抽取正则
    p_title = '<span title="" class="r-title">(.*?)</span>'
    p_href = '<a target="_blank" href="(.*?)" data-id=.*? class="ahover"><span title="" class="r-title">'
    # div.tab-content td > div > span.time
    title = re.findall(p_title, data)
    href = re.findall(p_href, data)
    date = browser.find_elements_by_css_selector(
        'div.tab-content td > div > span.time')
    # print(date)
    # 数据清洗
    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        href[i] = 'http://www.cninfo.com.cn/' + href[i]
        href[i] = re.sub('amp;', '', href[i])
        # date[i] = date[i].text
        print(str(i + 1) + '.' + title[i] + '-' + date[i].text)
        print(href[i])
    browser.quit()


keywords = ['理财', '现金管理', '纾困']
for i in keywords:
    juchao(i)
