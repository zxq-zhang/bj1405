from v4.page.page_address import PageAddress
from v4.page.page_login import PageLogin
from v4.page.page_order import PageOrder
from v4.tool.get_driver import GetDriver


class PageIn:

    def __init__(self):
        self.driver = GetDriver.get_driver()

    # 获取PageLoin对象
    def page_get_pagelogin(self):
        return PageLogin(self.driver)

    # 获取PageOrder对象
    def page_get_pageorder(self):
        return PageOrder(self.driver)

    # 获取PageAddress对象
    def page_get_pageaddress(self):
        return PageAddress(self.driver)