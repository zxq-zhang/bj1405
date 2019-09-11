"""
    目标：获取元素在屏幕中位置
    类：TouchAciton
    业务场景：
      1.进入设置页
      2.轻敲Wlan
"""
from time import sleep

from appium import webdriver

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

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

# WLAN 372,655   更多：372,1218
driver.tap([(372, 655), (372, 1218)], 500)

# 暂停3秒
sleep(3)
# 关闭driver
driver.quit()