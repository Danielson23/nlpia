from __future__ import print_function, unicode_literals, division, absolute_import
from future import standard_library
standard_library.install_aliases()  # noqa: Counter, OrderedDict, 
from builtins import *  # noqa

import logging
import logging.config
import os

import configparser


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'django': {
            'format': 'django: %(message)s',
        },
        'basic': {
            'format': '%(asctime)s %(levelname)7s:%(name)15s:%(lineno)3s:%(funcName)20s %(message)s',
        },
        'short': {
            'format': '%(asctime)s %(levelname)s:%(name)s:%(message)s'
        },
    },

    'handlers': {
        'logging.handlers.SysLogHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'facility': 'local7',
            'formatter': 'django',
            'address': '/dev/log',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'basic',
            'stream': 'ext://sys.stdout',
        },
    },

    'loggers': {
        'loggly': {
            'handlers': ['console', 'logging.handlers.SysLogHandler'],
            'propagate': True,
            'format': 'django: %(message)s',
            'level': 'DEBUG',
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

USER_HOME = os.path.expanduser("~")
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
BIGDATA_PATH = os.path.join(os.path.dirname(__file__), 'bigdata')

secrets = configparser.RawConfigParser()
secrets.read(os.path.join(PROJECT_PATH, 'secrets.cfg'))

locals().update(secrets.__dict__)