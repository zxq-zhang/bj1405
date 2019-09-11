"""
    目标：获取元素在屏幕中位置
    类：TouchAciton
    业务场景：
      1.进入设置页
      2.从存储移动到更多
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
# driver.implicitly_wait(10)

# 存储
# save = driver.find_element_by_xpath("//*[contains(@text,'存储')]")

# 更多
# more = driver.find_element_by_xpath("//*[contains(@text,'更多')]")

# 长按 基于元素实现
# 注意事项：按下之后必须添加等待时长 移动之后不用添加时长
# TouchAction(driver).press(save).wait(500).move_to(more).release().perform()

# 基于坐标点移动
"""
    1. appium1.8以下不含1.8,move_to使用的坐标的偏移量
        偏移量：10,20 x向右偏移 x=5  
    2. appium1.8(含)以上，使用的是坐标点  x=15
"""
# 存储 357,2329  更多：357,1238
TouchAction(driver).press(x=357, y=2329).wait(500).move_to(x=357, y=1238).release().perform()

# 暂停3秒
sleep(10)
# 关闭driver
driver.quit()