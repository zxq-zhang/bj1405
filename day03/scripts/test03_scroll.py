"""
    目标：获取元素在屏幕中位置
    方法：scroll
    业务场景：
      1.进入设置页
      2.模拟手指从存储菜单位置 到 WLAN菜单位置的上滑操作
    特色：基于两个元素，自动停止
"""
from time import sleep

from appium import webdriver

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# udid区分设备
# desired_caps['udid'] = '192.168.86.101:5555'
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 存储
save = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# WLAN
wlan = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")

# 从存储滚动WLAN
driver.scroll(save,wlan)




# 暂停3秒
sleep(3)
# 关闭driver
driver.quit()