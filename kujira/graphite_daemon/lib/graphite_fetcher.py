'''
Created on 29 kwi 2016

@author: PrzemyslawSwiderski
'''

import requests  
import json

class GraphiteFetcher(object):
    '''
    classdocs
    '''
    def __init__(self, redisUrl='http://127.0.0.1:8013/render'):
        '''
        Constructor
        '''
        self.redisUrl = redisUrl
        
    def get_data_json(self, target, fromParam, format='json'):
        """Collect data from Graphite-api in json format"""
        
        payload = {'target': target, 'from': fromParam, 'format':format}
        
        resp = requests.get(self.redisUrl, params=payload)

        data = resp.json()
         
        return data
        
    def get_data_raw_csv(self, target, fromParam, format='csv'):
        """Collect data from Graphite-api in csv format"""
        
        payload = {'target': target, 'from': fromParam, 'format':format}
        
        resp = requests.get(self.redisUrl, params=payload)

        data = resp.text
         
        return data





