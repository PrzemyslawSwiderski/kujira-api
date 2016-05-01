'''
Created on 29 kwi 2016

@author: PrzemyslawSwiderski
'''
from graphite_fetcher import GraphiteFetcher
from store.events_queue import Redis


class GraphiteCacher(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.fetcher = GraphiteFetcher()
        self.redis = Redis()
        self.redis.connect()

    def get_metric_and_push_to_redis(self, target, from_param):
        """Get metric from GraphiteFetcher and push to redis"""
        data = self.fetcher.get_data_json(target, from_param)
        self.redis.push(data)
        return data

    def pop_metric_from_redis(self):
        """Pop last metric from Redis"""
        return self.redis.pop()
