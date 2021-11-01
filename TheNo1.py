#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/10/12 0:31 
# @Author : liuguoliang

from selenium import webdriver
from time import sleep

driver = webdriver.Edge(".././msedgedriver.exe")
# driver = webdriver.Firefox(".././geckodriver.exe")
# dirver = webdriver.Chrome("./")

driver.get("https://www.baidu.com")
sleep(1)

kw= driver.find_element_by_id("kw").is_displayed()
sleep(1)
print(kw)





driver.quit()
