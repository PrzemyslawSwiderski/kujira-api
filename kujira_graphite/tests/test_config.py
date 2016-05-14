import os
import sys
import unittest
import ConfigParser
import ast
import logging

logging.basicConfig(level=logging.INFO)

sys.path.append(os.path.realpath('..'))


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRead(self):
        config = ConfigParser.RawConfigParser()
        config.read('/etc/kujira-graphite.cfg')
        metrics_to_watch = ast.literal_eval(config.get('Metrics', 'metrics'))
        logging.info("dsadsad")
        for c in metrics_to_watch:
            logging.info(c)

        how_old_fetch_from_start = config.get('Metrics', 'how_old')
        logging.info(how_old_fetch_from_start)

        pass

    def testReadRedisSection(self):
        config = ConfigParser.RawConfigParser()
        config.read('/etc/kujira-graphite.cfg')
        host = config.get('Redis', 'redis_url')
        port = config.get('Redis', 'redis_port')
        db = config.get('Redis', 'redis_db')
        logging.info(host)
        logging.info(port)
        logging.info(db)
        pass

if __name__ == "__main__":
    unittest.main()
