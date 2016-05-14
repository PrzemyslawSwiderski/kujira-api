"""
Created on 29 kwi 2016

@author: PrzemyslawSwiderski
"""

import requests
import ConfigParser


class GraphiteFetcher(object):
    """
    Fetches metrics from graphite-api
    """

    def __init__(self):
        """
        Constructor
        """
        kujira_graphite_config_file_location = '/etc/kujira-graphite.cfg'
        self.config = ConfigParser.RawConfigParser()
        self.config.read(kujira_graphite_config_file_location)
        self.graphite_api_url = self.config.get('Metrics', 'graphite-api_url')

    def get_data_json(self, target, from_param, out_format='json'):
        """Collect data from Graphite-api in json format"""

        payload = {'target': target, 'from': from_param, 'format': out_format}

        resp = requests.get(url=self.graphite_api_url, params=payload)

        data = resp.json()

        return data

    def get_data_raw_csv(self, target, from_param, out_format='csv'):
        """Collect data from Graphite-api in csv format"""

        payload = {'target': target, 'from': from_param, 'format': out_format}

        resp = requests.get(url=self.graphite_api_url, params=payload)

        data = resp.text

        return data
