import requests
from selenium import webdriver

#rowser = webdriver.Chrome()
fire = webdriver.PhantomJS()
fire.get('http://www.baidu.com')
print(fire.current_url)