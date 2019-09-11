"""
    目标：获取元素在屏幕中位置
    方法：location
    需求：
      1.进入设置页面
      2.获取搜索按钮在屏幕的坐标位置
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

location = driver.find_element_by_id("com.android.settings:id/search").location
print("搜索按钮位置：", location)

# 获取包名
package = driver.current_package
print("当前App应用包名为：", package)
# 获取启动名
activity = driver.current_activity
print("当前App应用启动名为：", activity)
# 暂停3秒
sleep(3)
# 关闭driver
driver.quit()
