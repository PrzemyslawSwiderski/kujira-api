"""
Created on 29 kwi 2016

@author: PrzemyslawSwiderski
"""
import time
from graphite_fetcher import GraphiteFetcher
from store.events_queue import Redis


class GraphiteCacher(object):
    """
    Class connecting Redis and graphite-api
    """

    def __init__(self, target_metric):
        """
        Constructor
        """
        self.target_metric = target_metric
        self.fetcher = GraphiteFetcher()
        self.redis = Redis()
        self.redis.connect()
        self.timestamp = int(round(time.time()))

    def get_metric_and_push_to_redis(self):
        """Get metric from GraphiteFetcher and push to redis"""
        data = self.fetcher.get_data_json(self.target_metric, '-30minutes')

        self.redis.append_metric(data[0]['target'], "{'datapoints': [")

        for index, d in enumerate(data[0]['datapoints']):
            if index == 0:
                d_string = str(d)
                self.redis.append_metric(data[0]['target'], d_string)
                self.timestamp = d[1]

            if d[0] is not None and index != 0:
                d_string = str(d)
                self.redis.append_metric(data[0]['target'], ", " + d_string)
                self.timestamp = d[1]

        return data

    def get_metric_and_append_to_redis(self):
        """Get metric from GraphiteFetcher and append to redis"""
        data = self.fetcher.get_data_json(self.target_metric, '-' + str(self.get_time_diff()) + 's')

        for d in data[0]['datapoints']:
            if d[0] is not None and d[1] > self.timestamp:
                d_string = str(d)
                self.redis.append_metric(data[0]['target'], ", " + d_string)
                self.timestamp = d[1]

        return data

    def get_time_diff(self):
        """Get time difference between current time and timestamp"""
        current_time = int(round(time.time())) + 15
        # print("CURRENT TIME: " + str(current_time))
        # print("TIMESTAMP: " + str(self.timestamp))
        return current_time - self.timestamp

    def get_metric_from_redis(self):
        """Get target metric from Redis"""
        return self.redis.get_metric(self.target_metric)
