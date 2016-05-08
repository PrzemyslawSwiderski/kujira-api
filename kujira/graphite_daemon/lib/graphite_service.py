#!/usr/bin/python

"""
Created on 30 kwi 2016

@author: PrzemyslawSwiderski

"""
from kujira.graphite_daemon.lib.graphite_daemon import GraphiteDaemon

if __name__ == '__main__':
    dm = GraphiteDaemon()
    dm.run()

