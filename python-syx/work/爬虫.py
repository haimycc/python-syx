import os
from selenium import webdriver

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器