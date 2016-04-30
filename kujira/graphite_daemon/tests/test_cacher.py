'''
Created on 30 kwi 2016

@author: PrzemyslawSwiderski
'''
import unittest
from graphite_daemon.lib.graphite_cacher import GraphiteCacher

class Test(unittest.TestCase):


    def setUp(self):
        self.cacher = GraphiteCacher()
        pass


    def tearDown(self):
        pass


    def testCacherPush(self):
        self.cacher.get_metric_and_push_to_redis('servers.localhost_localdomain.cpu.cpu0.system','-1hours')
        self.assertIsNotNone(self.cacher)
        pass
        
    def testCacherPop(self):
        print self.cacher.pop_metric_from_redis()
        self.assertIsNotNone(self.cacher)
        pass
        
if __name__ == "__main__":
    unittest.main()