import redis

POOL = redis.ConnectionPool(host='localhost', port=6379, db=0)


def get_metric(metric_name):
    """function getting metric by name"""
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.get(metric_name)
    return response


def append_metric(metric_name, metric_value):
    """function appending value to key"""
    my_server = redis.Redis(connection_pool=POOL)
    my_server.append(metric_name, metric_value)


def delete_metric(metric_name):
    """function deleting metric value"""
    my_server = redis.Redis(connection_pool=POOL)
    my_server.delete(metric_name)
