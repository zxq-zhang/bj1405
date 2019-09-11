"""
    目标：获取元素在屏幕中位置
    方法：swipe
    需求：1111,2046  1111,949
"""
from time import sleep

from appium import webdriver

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# swipe 滑动
driver.swipe(1111,2046, 1111,949, duration=3000)




# 暂停3秒
sleep(3)
# 关闭driver
driver.quit()