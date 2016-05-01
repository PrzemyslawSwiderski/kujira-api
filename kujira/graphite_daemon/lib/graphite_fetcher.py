'''
Created on 29 kwi 2016

@author: PrzemyslawSwiderski
'''

import requests


class GraphiteFetcher(object):
    '''
    classdocs
    '''

    def __init__(self, redis_url='http://127.0.0.1:8013/render'):
        '''
        Constructor
        '''
        self.redis_url = redis_url

    def get_data_json(self, target, from_param, out_format='json'):
        """Collect data from Graphite-api in json format"""

        payload = {'target': target, 'from': from_param, 'format': out_format}

        resp = requests.get(self.redis_url, params=payload)

        data = resp.json()

        return data

    def get_data_raw_csv(self, target, from_param, out_format='csv'):
        """Collect data from Graphite-api in csv format"""

        payload = {'target': target, 'from': from_param, 'format': out_format}

        resp = requests.get(self.redis_url, params=payload)

        data = resp.text

        return data
