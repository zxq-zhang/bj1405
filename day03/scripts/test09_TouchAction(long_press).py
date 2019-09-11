"""
    目标：获取元素在屏幕中位置
    类：TouchAciton
    业务场景：
      1.进入设置页
      2.轻敲wlan
      3.长按无线名称 1秒
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
driver.implicitly_wait(10)

# WLAN
wlan = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")

# 轻敲wlan
TouchAction(driver).tap(wlan).perform()

# name
name = driver.find_element_by_xpath("//*[contains(@text,'486')]")

# 长按
TouchAction(driver).long_press(el=name, duration=1000).release().perform()

# 暂停3秒
sleep(10)
# 关闭driver
driver.quit()