from appium.webdriver import webdriver


class GetDriver:
    driver = None
    # 获取driver对象
    @classmethod
    def get_driver(cls):
        if cls.get_driver is None:
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
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # 重点：重点：不能缩进，必须和if判断持平
        return cls.driver

    # 关闭driver对象
    @classmethod
    def quit_driver(cls):
        ...

