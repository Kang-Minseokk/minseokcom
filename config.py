import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'mysql://user1:Minseok0920#@127.0.0.1/pybo_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# STMP 서버의 url과 port 번호
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
EMAIL_ADDR = 'm23235180@gmail.com'
EMAIL_PASSWORD = 'bpzwmnstpwrxmevk'

API_KEY = "17e8c69b251581aa18fe957963b434a4"
CITY_NAME = "Seoul"