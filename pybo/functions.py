import datetime, re, os, requests
from dotenv import load_dotenv
from flask import redirect

from config.default import BASE_DIR
from pybo import db
from pybo.models import LoginStatus


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


