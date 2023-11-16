from config.default import *
from logging.config import dictConfig

SQLALCHEMY_DATABASE_URI = 'mysql://root:minseok0920#@localhost/pybo_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x0c\xf63\x86\xd3E\x04\xd2\xed\x1a{T]V\xc0\x1e'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(client_ip)s - %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})

