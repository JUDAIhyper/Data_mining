from selenium import webdriver
import re
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://wenshu.court.gov.cn/')
browser.find_element_by_xpath(
    '//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input').clear()
browser.find_element_by_xpath(
    '//*[@id="_view_1540966814000"]/div/div[1]/div[2]/input').send_keys('房地产')
browser.find_element_by_xpath(
    '// *[@id="_view_1540966814000"]/div/div[1]/div[3]').click()
time.sleep(30)
data = browser.page_source
browser.quit()
print(data)
