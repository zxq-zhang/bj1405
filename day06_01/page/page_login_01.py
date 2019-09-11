"""
    编写：
        0. 模块名：page_页面/模块
        1. 类名将模块名以大驼峰形式抄进来，有下划线去掉下划线；
        2. 方法：将操作步骤，每一步单独封装成一个方法
        3. 根据需求组合业务方法；
"""
from day05.v4.base.base_01 import Base


class PageLogin(Base):
    # 输入用户名
    def page_input_username(self):
        ...
    # 输入密码
    def page_input_pwd(self):
        ...
    # 点击登录
    def page_click_login(self):
        ...
    # 组合业务方法
    def page_login(self):
        ...