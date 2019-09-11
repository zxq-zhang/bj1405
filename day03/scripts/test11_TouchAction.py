"""
    业务场景：
        1.进入设置
        2.向上滑动屏幕到可见"安全"选项
        3.进入到安全
        4.点击屏幕锁定方式
        5.点击图案
        6.绘制图案
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

# 第一个坑：
driver.implicitly_wait(10)

# 定位存储
save = driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 定位WLAN
wlan = driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
# 滑动 存储->wlan
driver.drag_and_drop(save, wlan)
# 点击安全
driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
# 点击 屏幕锁定方式
driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定方式')]").click()
# 点击 图案
driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()

# 第二个坑 强制性等待
sleep(2)

# 绘制
""" 
    1. 234,837  2.719,837    3. 1199,837
                4.719,1326 
    5.234,1811 6.719,1811, 7.1199,1811
"""
TouchAction(driver).press(x=234,y=837).wait(500).move_to(x=719-234,y=0).wait(500).\
    move_to(x=1199-719,y=0).wait(500).move_to(x=719-1199,y=1326-837).wait(500).\
    move_to(x=234-719,y=1811-1326).wait(300).move_to(x=719-234,y=0).wait(500).\
    move_to(x=1199-719,y=0).wait(500).release().perform()

# 暂停3秒
sleep(10)
# 关闭driver
driver.quit()