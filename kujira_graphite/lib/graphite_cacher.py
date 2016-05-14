"""
Created on 29 kwi 2016

@author: PrzemyslawSwiderski
"""
import time
import ConfigParser

from redis_connection import RedisConnection
from graphite_fetcher import GraphiteFetcher


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
        self.redis = RedisConnection()
        self.timestamp = int(round(time.time()))
        self.config = ConfigParser.RawConfigParser()
        self.config.read('/etc/kujira-graphite.cfg')

    def get_metric_and_push_to_redis(self):
        """Get metric from GraphiteFetcher and push to redis"""
        how_old_fetch_from_start = self.config.get('Metrics', 'how_old')

        data = self.fetcher.get_data_json(self.target_metric, how_old_fetch_from_start)

        redis_metrics = self.redis.get_metric(self.target_metric)

        if redis_metrics is None:
            d_string = str(data[0]['datapoints'][0])
            self.redis.append_metric(data[0]['target'], d_string)
            self.timestamp = data[0]['datapoints'][1]

        for index, d in enumerate(data[0]['datapoints']):
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

        return current_time - self.timestamp

    def delete_metric_from_redis(self):
        """Remove metric from Redis"""
        self.redis.delete_metric(self.target_metric)
