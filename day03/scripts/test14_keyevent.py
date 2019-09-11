"""
    目标：向手机发送按键
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

# 音量 24为增加 25为减小
for i in range(4):
    sleep(1)
    driver.keyevent(25)
for n in range(4):
    sleep(1)
    driver.keyevent(24)


# 暂停3秒
sleep(3)
# 关闭driver
driver.quit()