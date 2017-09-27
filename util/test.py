#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Firefox()

driver.get("https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_0b250a12ee4642208fd202ea59ded6ea")

ui_areamini_text = driver.find_element_by_class_name("dorpdown")

time.sleep(2)

# 浮动
ActionChains(driver).move_to_element(ui_areamini_text).perform()

# 获取内容
address = driver.find_element_by_xpath("//*[@id='ttbar-mycity']/div[2]/div[2]/div/div/div[2]/a")

# 查找一组
addresses = driver.find_elements_by_xpath("//div[@class = 'item']/a")

print len(addresses)

for index in addresses:

    print index.text

print address.text


# 休眠五秒
time.sleep(5)

# 关闭浏览器
driver.quit()

