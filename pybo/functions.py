import datetime, re

from pybo import db
from pybo.models import LoginStatus


# 리다이렉트 url을 반환하는 함수
def get_redirect_url():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    redirect_url = os.environ.get('REDIRECT_URL')

    return redirect_url


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
