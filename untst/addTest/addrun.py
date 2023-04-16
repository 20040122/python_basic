import unittest
from htmltestreport import HTMLTestReport
from untst.addTest.addcase import addcase

s=unittest.TestSuite()
s.addTest(unittest.makeSuite(addcase))
HTMLTestReport('report.html','测试报告').run(s)