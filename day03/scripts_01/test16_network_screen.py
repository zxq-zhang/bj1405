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

# 获取当前手机网络
print("当前网络类型为：", driver.network_connection)
# 设置当前手机网络 为 wifi
driver.set_network_connection(1)
# 查看设置后的数据类型
print("设置之后网络类型为：",driver.set_network_connection(4))
# 截图
driver.get_screenshot_as_file("../img/img.png")

# 暂停5秒
time.sleep(5)
driver.quit()
