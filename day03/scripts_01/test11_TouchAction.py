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

# 定位wlan
wlan = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
TouchAction(driver).press(wlan).release().perform()

name = driver.find_element_by_xpath("//*[contains(@text,'486')]")
TouchAction(driver).press(name).wait(1000).release().perform()


#  强制性等待
time.sleep(2)
# 绘制
"""
 1、239,851      2、718,851         3、1200,851
                 4、718，1330
 5、239，1809    6、718，1809                 7、1200，1809
"""
TouchAction(driver).press(x=239, y=851).wait(500).move_to(x=718, y=851).wait(500). \
    move_to(x=1200, y=851).wait(500).move_to(x=718, y=1330).wait(500).\
    move_to(x=239, y=1809).wait(500).move_to(x=718,y=1809).wait(500).\
    move_to(x=1200, y=1809)

# 暂停5秒
time.sleep(5)
driver.quit()
