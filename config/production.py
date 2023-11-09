from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x0c\xf63\x86\xd3E\x04\xd2\xed\x1a{T]V\xc0\x1e'

# STMP 서버의 url과 port 번호
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
EMAIL_ADDR = 'm23235180@gmail.com'
EMAIL_PASSWORD = 'bpzwmnstpwrxmevk'

API_KEY = "17e8c69b251581aa18fe957963b434a4"
CITY_NAME = "Seoul"
