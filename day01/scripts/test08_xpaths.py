"""
    目标：
        1. 安装 install_app()
        2. 卸载 remove_app()
        3. 是否安装 is_app_installed()  ->True 安装
    需求：
        爱客为例，
            如果安装，进行卸载，
            否则，进行安装
"""
# 导包
import os
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
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 查找wlan 并点击
# 精准定位 使用等号=
driver.find_element_by_xpath("//*[@text='WLAN']").click()

# 模糊定位
# driver.find_element_by_xpath("//*[contains(@text,'LAN')]").click()

# 错误的写法
# driver.find_element_by_xpath("//*[@text()='WLAN']").click()


time.sleep(5)
driver.quit()
