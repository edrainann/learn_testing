#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('3.10frame.html')
driver.get(file_path)

driver.implicitly_wait(30)

#先找到ifromel(id=f1)
driver.switch_to_frame('f1')

#再找到其下面的ifrome2(id=f2)
driver.switch_to_frame('f2')

#下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys('selenium')
driver.find_element_by_id("su").click()
time.sleep(3)

# driver.quit()
