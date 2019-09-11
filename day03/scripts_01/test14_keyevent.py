"""


"""
# 导包
from platform import release

from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
# 声明driver对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 音量24为增加  25为减小
for i in range(4):
    time.sleep(1)
    driver.keyevent(25)

for i in range(4):
    time.sleep(1)
    driver.keyevent(24)

# 暂停5秒
time.sleep(5)
driver.quit()
