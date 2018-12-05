#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018/09/05
# 淘宝秒杀脚本，扫码登录版
import os
from selenium import webdriver
import datetime
import time

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
driver.get("https://order.mi.com/buy/checkout?r=97961.1539596799")


def buy(buytime):
    while True:
        time.sleep(20)
        # print(driver.find_element_by_id("立即抢购"))
        # print(driver.find_element_by_css_selector("[data-id='2183700046']"))
        print(driver.find_element_by_class_name("J_addressItem"))
        driver.find_element_by_class_name("J_addressItem").click()


if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    buy("2018-10-15 17:00:00.000000")
