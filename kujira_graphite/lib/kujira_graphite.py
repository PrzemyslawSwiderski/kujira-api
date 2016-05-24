"""
Created on 30 kwi 2016

@author: PrzemyslawSwiderski

"""
import time
import ConfigParser
import ast
from graphite_cacher import GraphiteCacher


class KujiraGraphite(object):
    """
    Instance to run in service
    """

    def __init__(self):
        """
        Constructor
        """
        kujira_graphite_config_file_location = '/etc/kujira-graphite.cfg'
        config = ConfigParser.RawConfigParser()
        config.read(kujira_graphite_config_file_location)
        self.metrics_to_watch = ast.literal_eval(config.get('Metrics', 'metrics'))

        self.cachers = []

        for m in self.metrics_to_watch:
            self.cachers.append(GraphiteCacher(m))

        for c in self.cachers:
            c.get_metric_and_push_to_redis()

    def run(self):
        """
        run method
        """
        while True:
            time.sleep(61)
            for c in self.cachers:
                c.get_metric_and_append_to_redis()