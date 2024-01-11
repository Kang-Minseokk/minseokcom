import os
from datetime import timedelta
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# STMP 서버의 url과 port 번호
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
EMAIL_ADDR = 'm23235180@gmail.com'
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
UPLOADED_PHOTOS_DEST = 'pybo/static/image/image_content'
UPLOADS_DEFAULT_URL = 'pybo/static/image/image_content/'
