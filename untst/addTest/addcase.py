import unittest
from parameterized import parameterized

from untst.addTest import tools
from untst.addTest.readjson import readjson


class addcase(unittest.TestCase):
    @parameterized.expand(readjson)
    def test1(self,a,b,expect):
        print(f"a={a},b={b},expect={expect}")
        self.assertEqual(expect, tools.add(a,b))


