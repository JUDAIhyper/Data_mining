from selenium import webdriver
import re

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_option)
browser.get('https://finance.sina.com.cn/realstock/company/sh000001/nc.shtml')
data = browser.page_source
browser.quit()
# 数据提取
p_price = '<div id="price" class=".*?">(.*?)</div>'
price = re.findall(p_price, data)
print(price)
