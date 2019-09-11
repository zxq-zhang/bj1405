import pytest


class Test02:
    """函数级别开始"""
    def setup(self):
        print("setup开始")

    def teardown(self):
        """函数级别结束"""
        print("teardown结束")

    def setup_class(self):
        """类级别开始"""
        print("setup_class开始")

    def teardown_class(self):
        """类级别结束"""
        print("teardown_class结束")

    def test02(self):
        """测试方法1"""
        print("test02被执行")

    def test03(self):
        """测试方法2"""
        print("test03被执行")


pytest.main("-s test02.py")
