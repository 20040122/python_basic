import unittest

from untst.testAssert import TestAssert

sui = unittest.TestSuite()
sui.addTest(unittest.makeSuite(TestAssert))
unittest.TextTestRunner().run(sui)