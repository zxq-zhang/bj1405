from appium.webdriver import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self):
        # 准备启动参数
        caps = {}
        # 必填-且正确
        caps['platformName'] = 'Android'
        # 必填-且正确
        caps['platformVersion'] = '5.1'
        # 必填
        caps['deviceName'] = '192.168.56.101:5555'
        # APP包名 /
        caps['appPackage'] = 'com.vcooline.aike'
        # 启动名
        caps['appActivity'] = '.umanager.LoginActivity'
        # 获取driver
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        return (WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)).until(lambda x: x.find_element(*loc))

    # 输入 方法
    def base_inpute(self, loc, values):
        # 获取
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(values)

    # 点击 方法
    def base_click(self, loc):
        self.base_find(loc).click()
