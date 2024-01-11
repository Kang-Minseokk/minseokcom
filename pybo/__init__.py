import datetime
import os

from flask_uploads import configure_uploads, UploadSet, IMAGES

from config.default import SMTP_SERVER, SMTP_PORT, EMAIL_ADDR, EMAIL_PASSWORD, BASE_DIR
from flask_cors import CORS
import pymysql
import time
import apscheduler.schedulers.background
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests



pymysql.install_as_MySQLdb()
db = SQLAlchemy()
migrate = Migrate()


def page_not_found(e):
    return render_template('404.html'), 404


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')
    CORS(app)

    # photos = UploadSet('photos', IMAGES)
    # configure_uploads(app, photos)

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("mysql"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import (main_views, question_views, answer_views, auth_views, comment_views, vote_views, home_views,
                        goal_views, calendar_views, statistic_views)
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)
    app.register_blueprint(goal_views.bp)
    app.register_blueprint(calendar_views.bp)
    app.register_blueprint(statistic_views.bp)
    app.register_error_handler(404, page_not_found)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    from .functions import get_redirect_url, login_time_management

    scheduler = apscheduler.schedulers.background.BackgroundScheduler()
    scheduler.add_job(
        job2,
        'cron',
        hour=8,
        minute=00,
        id='calendar_alarm'
    )
    scheduler.add_job(
        get_weather_data,
        'cron',
        minute=0,
        id='weather_update'
    )
    scheduler.add_job(
        news_crawl,
        'cron',
        hour=8,
        minute=30,
        id='am_news_crawl'
    )
    scheduler.add_job(
        news_crawl,
        'cron',
        hour=19,
        minute=00,
        id='pm_news_crawl'
    )
    print('sched before~')
    scheduler.start()
    print('sched after~')

    return app


def news_crawl():
    url = "https://tilnote.io/news"
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('lang=ko')
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(1)
    html_content = driver.page_source

    news_list = []
    news_link_list = []
    soup = BeautifulSoup(html_content, features="html.parser")
    news_content = soup.find_all(class_='news-link')

    for news_link in soup.find_all(class_='News_curated-news__meta__WvGmE'):
        span_tag = news_link.find_all('span')[1]
        a_tag = span_tag.find('a')
        news_link_list.append(a_tag.get('href'))

    url_path = os.path.join(BASE_DIR, "pybo/static/statistic_data/news_letter.txt")
    for news in news_content:
        news_list.append(news.text.replace("'", "\""))
    news_list = str(news_list).strip('[]')
    news_link_list = str(news_link_list).strip('[]')
    with open(url_path, 'a') as f:
        f.write(f'[{datetime.datetime.now()}]' + news_link_list + '\n')
        f.write(f'[{datetime.datetime.now()}]' + news_list + '\n')


def job2():
    print(f'이메일 송신 완료.. : {time.strftime("%H:%M:%S")}')

    import smtplib
    from datetime import datetime
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import pymysql

    con = pymysql.connect(host='localhost', user='root', password='minseok0920#', db='pybo_db', charset='utf8')
    cur = con.cursor()
    sql = "SELECT end_date, title, content FROM calendar"

    cur.execute(sql)
    rows = cur.fetchall()
    today_date = datetime.today().date()
    schedule_list = []
    for end_date in rows:
        if 0 <= (end_date[0].date() - today_date).days <= 3:
            title = end_date[1]
            content = end_date[2]
            remain_days = (end_date[0].date() - today_date).days
            schedule_list.append((title, content, remain_days))

    if schedule_list:
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
        email_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                /* 링크 스타일을 여기에 정의하세요. */
                .link-style {{
                    text-decoration: none;
                    border: 1px solid #007bff;
                    padding: 5px 10px;
                    color: #007bff;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="card" style="border: 1px solid #000; background-color: #dedbd5;
            box-shadow: 3px 3px 5px 0 rgba(0,0,0,0.5); border-radius: 10px; padding: 10px;">
                <p>자세한 내용을 보기 위해서 아래의 링크를 클릭해주세요!</p>
                <div class="container" style="max-width: 50%; border: 1px solid #000; padding: 20px; margin: 10px;
                background-color: #f5f2eb;">
                    <h4>종료가 얼마 남지 않은 일정이 {len(schedule_list)}개 있습니다.</p>
                </div>
                <a href="{get_weather_data()}/calendar/show/">자세히보기</a>
            </div>
        </body>
        </html>
        """

        # 이메일 본문을 MIMEText로 설정
        message = MIMEMultipart()
        message.attach(MIMEText(email_content, 'html'))

        # 3. MIME 형태의 이메일 메세지 작성
        message["Subject"] = "일정 종료가 얼마 남지 않았습니다!"
        message["From"] = EMAIL_ADDR  # 보내는 사람의 이메일 계정
        message["To"] = 'dreampilot920@naver.com'

        # 4. 서버로 메일 보내기
        smtp.send_message(message)

        # 5. 메일을 보내면 서버와의 연결 끊기
        smtp.quit()

    else:
        pass
    con.close()


def write_weather_data(city):
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    city_name = city
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    try:
        response = requests.get(complete_url)
        url_path = os.path.join(BASE_DIR, f"pybo/static/statistic_data/weather_data_{city}.txt")
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_description = data['weather'][0]['description']

        # 데이터를 파일에 쓰는 코드
        with open(url_path, 'a') as f:
            f.write(f"{datetime.datetime.now().strftime('%H:%M')}, {round(temperature-273.15, 1)}, {humidity}, {weather_description}\n")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP 오류 발생: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"연결 오류 발생: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"요청 시간 초과: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"기타 오류 발생: {err}")
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}")
    else:
        print("날씨 데이터를 성공적으로 가져왔습니다.")


def get_weather_data():
    write_weather_data("Seoul")
    write_weather_data("Busan")
    write_weather_data("Daegu")
    write_weather_data("Daejeon")
    write_weather_data("Incheon")
    write_weather_data("Ulsan")
    write_weather_data("Gwangju")

