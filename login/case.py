import unittest
from login import tools
from parameterized import parameterized
from readjson import readjson
class TestLogin(unittest.TestCase):
    @parameterized.expand(readjson())
    def test_login(self,a,b):
        self.assertEqual(tools.login(a,b),'登陆成功')
