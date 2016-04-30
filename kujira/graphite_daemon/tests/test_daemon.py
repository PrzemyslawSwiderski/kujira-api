'''
Created on 30 kwi 2016

@author: PrzemyslawSwiderski
'''
import unittest
from graphite_daemon.lib.graphite_daemon import GraphiteDaemon

class Test(unittest.TestCase):


    def setUp(self):
        self.daemon = GraphiteDaemon('/tmp/graphite_daemon.pid')
        print "CTRL + C to stop daemon"
        pass


    def tearDown(self):
        pass


    def testRun(self):
        self.daemon.run()
        self.assertFalse(False)
        pass


if __name__ == "__main__":
    unittest.main()