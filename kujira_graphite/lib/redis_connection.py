import redis
import ConfigParser


class RedisConnection(object):
    def __init__(self):
        config = ConfigParser.RawConfigParser()
        kujira_graphite_config_file_location = '/etc/kujira-graphite.cfg'
        config.read(kujira_graphite_config_file_location)
        self.POOL = redis.ConnectionPool(host=config.get('Redis', 'redis_url'), port=config.get('Redis', 'redis_port'), db=config.get('Redis', 'redis_db'))

    def get_metric(self, metric_name):
        """function getting metric by name"""
        my_server = redis.Redis(connection_pool=self.POOL)
        response = my_server.get(metric_name)
        return response

    def append_metric(self, metric_name, metric_value):
        """function appending value to key"""
        my_server = redis.Redis(connection_pool=self.POOL)
        my_server.append(metric_name, metric_value)

    def delete_metric(self, metric_name):
        """function deleting metric value"""
        my_server = redis.Redis(connection_pool=self.POOL)
        my_server.delete(metric_name)
