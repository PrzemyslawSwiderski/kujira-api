'''
Created on 30 kwi 2016

@author: PrzemyslawSwiderski
'''
import sys
import time
from daemon import Daemon
from graphite_cacher import GraphiteCacher


class GraphiteDaemon(Daemon):
    '''
    classdocs
    '''

    def __init__(self, pidfile):
        '''
        Constructor
        '''
        Daemon.__init__(self, pidfile)
        self.cacher = GraphiteCacher()

        print("__________________\n")
        print("Popped old metric:\n")
        print(self.cacher.get_metric_and_push_to_redis(
            'servers.localhost_localdomain.cpu.cpu0.system', '-1hours'))

    def run(self):
        '''
        run method
        '''
        while True:
            time.sleep(5)
            print("__________________\n")
            print("Popped old metric:\n")
            print(self.cacher.pop_metric_from_redis())
            print("__________________\n")
            print("Pushed new metric:\n")
            print(self.cacher.get_metric_and_push_to_redis(
                'servers.localhost_localdomain.cpu.cpu0.system', '-1hours'))

if __name__ == "__main__":
    daemon = GraphiteDaemon('/tmp/graphite_daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
