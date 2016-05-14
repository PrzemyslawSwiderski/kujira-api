"""
Created on 30 kwi 2016

@author: PrzemyslawSwiderski
"""
import os
import sys
import time
import unittest

sys.path.append(os.path.realpath('..'))

from lib.graphite_cacher import GraphiteCacher


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

    def testCacherDelete(self):
        print("Before delete ->")
        print(self.cacher.get_metric_from_redis())
        self.cacher.delete_metric_from_redis()
        print("After delete ->")
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
