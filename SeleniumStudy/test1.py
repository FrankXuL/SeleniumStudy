# encoding=utf-8
from selenium import webdriver
import time

# 获得浏览器驱动
driver = webdriver.Chrome()
# 打开需要访问的页面
driver.get("https://www.baidu.com/")
# 用id定位
# driver.find_element_by_id("kw" ).send_keys("六一儿童节")
# driver.find_element_by_id("su").click()
# driver.quit()
# 用classname定位
# driver.find_element_by_class_name("").send_keys("六一儿童节")
# driver.quit()
# link text 适用于可点击的链接
# driver.find_element_by_link_text("新闻").click()
# partial link text 用部分内容去定位元素
driver.find_element_by_partial_link_text("hao").click()
time.sleep(3)
# tag name
# driver.find_element_by_tag_name("input").send_keys("西安")
# driver.find_element_by_tag_name().click()
# xpath
