
"""


"""
# 导包

from appium import webdriver
import time
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

# swipe 滑动
driver.swipe(1111,2046,1111,949,duration=3000)



time.sleep(5)
driver.quit()
