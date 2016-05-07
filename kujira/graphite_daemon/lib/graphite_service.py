"""
Created on 30 kwi 2016

@author: PrzemyslawSwiderski

"""

#!/usr/bin/python

from graphite_daemon import GraphiteDaemon

if __name__ == '__main__':
    dm = GraphiteDaemon()
    dm.run()

