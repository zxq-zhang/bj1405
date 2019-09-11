"""
    目标：获取元素在屏幕中位置
    方法：back_ground_app(s)
    业务场景：
      1. 将设置APP置于后台10秒，在置于前台
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

# 将设置app置于后台 10秒
driver.background_app(10)

# 暂停3秒
sleep(3)
# 关闭driver
driver.quit()