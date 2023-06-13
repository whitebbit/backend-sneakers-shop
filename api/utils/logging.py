import logging
import logstash
import sys

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logstash_handler = logstash.TCPLogstashHandler('localhost', 5959, version=1)
logger.addHandler(logstash_handler)

