import unittest

from case import TestLogin
from htmltestreport import HTMLTestReport
suite= unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
HTMLTestReport('report.html','登陆数据测试报告').run(suite)