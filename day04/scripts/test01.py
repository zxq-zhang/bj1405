import pytest


class Test01:
    def test01(self):
        """测试方法"""
        print("test01被执行")

    def tpshop_login(self):
        print("登陆成功")

    def test02(self):
        print("test02被执行")



pytest.main("-s test01.py")

