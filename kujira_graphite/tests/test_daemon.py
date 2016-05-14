"""
Created on 30 kwi 2016

@author: PrzemyslawSwiderski
"""
import os
import sys
import unittest

sys.path.append(os.path.realpath('..'))

from lib.kujira_graphite import KujiraGraphite

class Test(unittest.TestCase):
    def setUp(self):
        self.daemon = KujiraGraphite()
        pass

    def tearDown(self):
        pass

    def testRun(self):
        self.daemon.run()
        self.assertFalse(False)
        pass


if __name__ == "__main__":
    unittest.main()
