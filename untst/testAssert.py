import unittest

class TestAssert(unittest.TestCase):
    def testAssert_1(self):
        self.assertEqual(1, 1)
    def testAssert_2(self):
        self.assertEqual(1, 2)

    def astin(self):
        self.assertIn('admin','欢迎admin登录')
        