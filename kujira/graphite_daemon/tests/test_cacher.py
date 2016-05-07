"""
Created on 30 kwi 2016

@author: PrzemyslawSwiderski
"""
import unittest
import time
from graphite_daemon.lib.graphite_cacher import GraphiteCacher


class Test(unittest.TestCase):
    def setUp(self):
        self.cacher = GraphiteCacher('servers.localhost_localdomain.cpu.cpu0.system')
        pass

    def tearDown(self):
        pass

    def testCacherPush(self):
        self.cacher.get_metric_and_push_to_redis()
        self.assertIsNotNone(self.cacher)
        pass

    def testCacherGet(self):
        print(self.cacher.get_metric_from_redis())
        self.assertIsNotNone(self.cacher)
        pass

    def testCacherAppend(self):
        self.cacher.get_metric_and_append_to_redis()
        self.assertIsNotNone(self.cacher)
        pass

    def testCacherPushAndAppend(self):
        self.cacher.get_metric_and_push_to_redis()
        time.sleep(6)
        print(self.cacher.get_time_diff())
        self.cacher.get_metric_and_append_to_redis()

        self.assertIsNotNone(self.cacher)
        pass

    def testGetTimeDiff(self):
        time.sleep(6)
        print(self.cacher.get_time_diff())
        self.assertIsNotNone(self.cacher)
        pass


if __name__ == "__main__":
    unittest.main()