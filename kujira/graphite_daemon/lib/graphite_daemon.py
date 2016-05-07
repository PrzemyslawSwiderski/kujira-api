"""
Created on 30 kwi 2016

@author: PrzemyslawSwiderski

"""
import time
from graphite_cacher import GraphiteCacher


class GraphiteDaemon(object):
    """
    Instance to run in service
    """

    def __init__(self):
        """
        Constructor
        """
        self.cachers = []
        self.cachers.append(GraphiteCacher('servers.localhost_localdomain.cpu.cpu0.system'))
        for c in self.cachers:
            print("__________________\n")
            print("Metric named: " + c.target_metric + "\n")
            print("Metric pushed to redis:\n")
            print(c.get_metric_and_push_to_redis())

    def run(self):
        """
        run method
        """
        while True:
            time.sleep(61)
            for c in self.cachers:
                print("__________________\n")
                print("Metric named: " + c.target_metric + "\n")
                print("All Dataponits in redis:\n")
                print(c.get_metric_from_redis())
                print("__________________\n")
                print("Last datapoints:\n")
                print(c.get_metric_and_append_to_redis())

    def add_metric(self, target_metric):
        """
        run method
        """
        self.cachers.append(GraphiteCacher(target_metric))
