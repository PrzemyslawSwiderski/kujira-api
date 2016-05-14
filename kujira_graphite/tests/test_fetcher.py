"""
Created on 29 kwi 2016

@author: PrzemyslawSwiderski
"""
import os
import sys
import unittest

sys.path.append(os.path.realpath('..'))

from lib.graphite_fetcher import GraphiteFetcher


class Test(unittest.TestCase):
    def setUp(self):
        self.fetcher = GraphiteFetcher()

    def tearDown(self):
        pass

    def testGetData(self):
        print(self.fetcher.get_data_json('servers.localhost_localdomain.cpu.cpu0.system', '-1hours')[0]['target'])

    def testGetDataJson1(self):
        print(self.fetcher.get_data_json('servers.localhost_localdomain.cpu.cpu0.system', '-1hours')[0]['target'])
        self.assertIsNotNone(self.fetcher.get_data_json('servers.localhost_localdomain.cpu.cpu0.system', '-1hours')[0]['target'])

    def testGetDataJsonTimestamp(self):
        timestamp = self.fetcher.get_data_json('servers.localhost_localdomain.cpu.cpu0.system', '-1hours')[0]['datapoints'][-1][1]
        print(timestamp)
        self.assertIsNotNone(self.fetcher.get_data_json('servers.localhost_localdomain.cpu.cpu0.system', '-1hours')[0]['datapoints'])

    def testGetDataCsv1(self):
        print(self.fetcher.get_data_raw_csv('servers.localhost_localdomain.cpu.cpu0.system', '-1hours'))
        self.assertIsNotNone(self.fetcher.get_data_raw_csv('servers.localhost_localdomain.cpu.cpu0.system', '-1hours'))

    def testGetDataCsv2(self):
        print(self.fetcher.get_data_raw_csv('servers.localhost_localdomain.cpu.cpu0.system', '-1hours'))
        self.assertIsNotNone(self.fetcher.get_data_raw_csv('servers.localhost_localdomain.cpu.cpu0.system', '-1hours'))


if __name__ == "__main__":
    unittest.main()
