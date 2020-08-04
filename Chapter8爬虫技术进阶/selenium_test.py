# 使用selenium库
from selenium import webdriver
import time


def sina_test():
    # 无界面访问
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(
        'https://finance.sina.com.cn/realstock/company/sh000001/nc.shtml')
    data = browser.page_source
    print(data)


def baidu_test():
    # 基础网页访问
    browser = webdriver.Chrome()
    # 网页最大化
    browser.maximize_window()
    browser.get('https://www.baidu.com')

    # 查找元素模拟器和鼠标键盘操作
    # 1.xpath
    browser.find_element_by_xpath('//*[@id="kw"]').clear()  # 清空搜索框文字
    browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python')  # 传入输入值
    browser.find_element_by_xpath('//*[@id="su"]').click()  # 模拟鼠标单击
    time.sleep(3)
    # 2.css方法
    # browser.find_element_by_css_selector('#kw').send_keys('python')

    # 获取网页真正的源代码
    data = browser.page_source  # 通过F12看到的渲染后的代码
    print(data)
    # 关闭浏览器
    # browser.quit()
if __name__ == '__main__':
    sina_test()
