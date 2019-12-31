# coding=utf-8

import os
import redis


# redis配置
redis_options = {
    'host': "127.0.0.1",
    'password': "zhidu12345",
    'port': 6379,
    'max_conn': 10
}
# redis连接池
redis_pool = redis.ConnectionPool(
    host=redis_options['host'],
    port=redis_options["port"],
    password=redis_options["password"],
    max_connections=redis_options["max_conn"]
)

# app配置
settings = {
    'template_path': os.path.join(os.path.dirname(__file__), "template"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'xsrf_cookies': True,
    'cookie_secret': 'wX8y3pkxSTak4R+v79jZiTZCYfFRL0gpoDDkYgkyJHk=',
    'login_url': '/login',
    'debug': True
}

# 日志
log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
