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

driver.close_app()

# 判断爱客是否安装 传入包名
if driver.is_app_installed("com.vcooline.aike"):
    # 卸载
    driver.remove_app("com.vcooline.aike")
    print("卸载成功！")
# 否则
else:
    # 安装
    # driver.install_app(os.getcwd()+os.sep+"AK_CRM.apk")
    driver.install_app("F:\\移动环境\\apk\\AK_CRM.apk")
    print("安装成功！")

time.sleep(5)
driver.quit()
