import os

RABBITMQ_CONFIG = {
    'host': os.environ.get('RABBITMQ_HOST', 'localhost'),
    'port': int(os.environ.get('RABBITMQ_PORT', 5672)),
    'virtual_host': os.environ.get('RABBITMQ_DEFAULT_VHOST', '/'),
    'login': os.environ.get('RABBITMQ_DEFAULT_USER', 'root'),
    'password': os.environ.get('RABBITMQ_DEFAULT_PASS', 'root')
}

RABBITMQ_QUEUES = {
    'to_main': 'MEDIA_MAIN',
    'from_main': 'MAIN_MEDIA'
}