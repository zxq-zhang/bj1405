import pytest


class Test02:
    """测试方法"""
    @pytest.mark.run(order=2)
    def test02(self):
        """测试方法1"""
        print("test02被执行")

    @pytest.mark.run(order=3)
    def test03(self):
        """测试方法2"""
        print("test03被执行")

    @pytest.mark.run(order=1)
    def test01(self):
        """测试方法2"""
        print("test01被执行")


pytest.main("-s test02.py")
