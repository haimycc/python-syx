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
driver.get(
    "https://account.xiaomi.com/pass/serviceLogin?callback=https%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252Findex.html%26sign%3DMjM0MWU0NjBlOTU1YzY4NGQzOTc3MDk4N2M2MjQ5Y2ZiZTMxNTFlZQ%2C%2C&sid=mi_eshop&_bannerBiz=mistore&_qrsize=180")
driver.maximize_window()  # 窗口最大化（无关紧要哈）
# driver.find_element_by_link_text("扫码登陆").click()
click = driver.find_element_by_css_selector("[data-tab='qr']").click()
print(click)


def login():
    # driver.maximize_window()
    # 打开淘宝登录页，并进行扫码登录
    # driver.get("https://www.taobao.com")
    time.sleep(3)
    wait = True
    while wait:
        try:
            time.sleep(2)
            selector = driver.find_element_by_css_selector("[data-tab='qr']")
        except:
            wait = False
    driver.get("https://www.mi.com/seckill/")
    # 点击购物车里全选按钮
    # if driver.find_element_by_id("J_SelectAll1"):
    #     driver.find_element_by_id("J_SelectAll1").click()
    # now = datetime.datetime.now()
    # print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_css_selector("[data-id='2164900010']"):
                    print(driver.find_element_by_css_selector("[data-id='2164900010']"))
                    driver.find_element_by_css_selector("[data-id='2164900010']").click()
                    driver.find_element_by_link_text("立即抢购").click()
                driver.find_element_by_link_text('去结算').click()
                driver.find_element_by_class_name("J_addressItem").click()
                driver.find_element_by_link_text('去结算').click()
            except:
                pass
        print(now)
        time.sleep(0.1)


if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    buy("2018-10-15 18:00:00.000000")
