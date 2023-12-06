import datetime, re, os, requests
import json

from dotenv import load_dotenv
from flask import redirect

from config.default import BASE_DIR
from pybo import db
from pybo.models import LoginStatus, Question, DailyVisit


#최신 글 반환 함수
def get_latest_post(posts):
    question_list = Question.query.order_by(Question.create_date.desc()).limit(posts).all()
    return question_list

# 리다이렉트 url을 반환하는 함수
def get_redirect_url():
    load_dotenv()
    redirect_url = os.environ.get('REDIRECT_URL')
    return redirect_url


# 카카오 REST API키 가져오는 함수
def get_rest_api_kakao():
    load_dotenv()
    rest_api_key = os.environ.get('KAKAO_REST_API_KEY')
    return rest_api_key


def get_client_id_google():
    load_dotenv()
    google_client_id = os.environ.get('GOOGLE_CLIENT_ID')
    return google_client_id


def get_client_secret_google():
    load_dotenv()
    google_client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')
    return google_client_secret


# 로그인 시간 추적 함수
def login_time_management(user_id, platform):
    with open('/var/log/nginx/access.log', 'r') as log_file:
        for row in log_file:
            ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')
            # Use the pattern to search for the IP address in the log entry
            match = ip_pattern.search(row)
            ip_address = match.group(1)
    login_user = LoginStatus(user_id=user_id, login_time=datetime.datetime.now(), platform=platform,
                             ip_address=ip_address)
    db.session.add(login_user)
    db.session.commit()


# 카카오 접근 토큰 반환 함수
def get_access_token(code):
    TOKEN_URL = "https://kauth.kakao.com/oauth/token"
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': '462f43a92e08ad9b2279efee154c9229',
        'redirect_uri': f'{get_redirect_url()}/auth/after_login',
        'code': code
    }
    token_response = requests.post(TOKEN_URL, data=token_data)
    tokens = token_response.json()
    return tokens.get('access_token')


# 카카오 사용자 정보 반환 함수
def get_user_info(access_token):
    USER_INFO_URL = "https://kapi.kakao.com/v2/user/me"
    headers = {'Authorization': f'Bearer {access_token}'}

    user_info_response = requests.get(USER_INFO_URL, headers=headers)
    return user_info_response.json()


# 카카오 로그아웃 함수
def kakao_logout():
    url = f"https://kauth.kakao.com/oauth/logout?client_id={get_rest_api_kakao()}&logout_redirect_uri={get_redirect_url()}"
    # GET 요청을 보냅니다.
    response = requests.get(url)
    if response.status_code == 200:
        print('로그아웃 요청이 성공적으로 완료되었습니다.')

    else:
        print('로그아웃 요청이 실패했습니다.')


# 총 포스트 개수 반환 함수
def get_total_posts_count():
    total_posts_count = Question.query.count()

    return total_posts_count


# 총 방문자 수 반환 함수
def get_total_visit_count():
    total_visit_user = DailyVisit.query.all()
    total_visit_count = 0
    for day_visit in total_visit_user:
        day_visit_list = json.loads(day_visit.only_visit_user_list)
        day_visit_count = len(day_visit_list)
        total_visit_count += day_visit_count

    return total_visit_count


# 어제 방문자 수 반환 함수
def get_yesterday_visit_count():
    yesterday_visit_result = DailyVisit.query.all()[-2]
    yesterday_visit_count = yesterday_visit_result.only_visit_count

    return yesterday_visit_count


# 오늘 방문자 수 반환 함수
def get_today_visit_count():
    today_date = datetime.datetime.now().strftime('%Y-%m-%d')
    today_visit_count = DailyVisit.query.filter_by(date=today_date).first().only_visit_count

    return today_visit_count

