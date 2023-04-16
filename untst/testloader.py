import unittest


suite=unittest.TestLoader().discover('case','test*.py')
unittest.TextTestRunner().run(suite)