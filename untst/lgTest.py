import unittest

class loginTest(unittest.TestCase):
    # 类方法，只执行一次
    @classmethod
    def setUpClass(cls) -> None:
        print("1.打开浏览器")
    @classmethod
    def tearDownClass(cls) -> None:
        print("5.关闭浏览器")
    # 每个方法执行一次
    def setUp(self)->None:
        print("2.打开页面")
    def tearDown(self)->None:
        print("4.关闭页面")
    # 测试用例
    def test1(self):
        print("3.点击登陆_1")
    def test2(self):
        print("3.点击登陆_2")
    def test3(self):
        print("3.点击登陆_3")