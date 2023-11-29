import datetime
import os
import firebase_admin
from firebase_admin import credentials
import requests
from flask import Blueprint, url_for, render_template, flash, request, session, g, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
import functools
from sqlalchemy import desc

from config.default import BASE_DIR
from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm, EmailForm, CategoryForm
from pybo.functions import get_redirect_url, login_time_management, get_rest_api_kakao, get_access_token, get_user_info, \
    kakao_logout
from pybo.models import User, Question, question_voter, Subscriber, LoginStatus
import random, string


bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view


def power_login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None or g.user.username != "강민석":
            flash("Special Access Required!!", "warning")
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    form_for_new_category = CategoryForm()
    redirect_url = get_redirect_url()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            if not form.profile_img.data:
                user = User(username=form.username.data, password=generate_password_hash(form.password1.data),
                            email=form.email.data, profile_img='minsoek.png', kakao=0)
                db.session.add(user)
                db.session.commit()
                session.clear()
                session['user_id'] = user.id
            else:
                profile_img = form.profile_img.data
                filename = profile_img.filename
                profile_img.save(os.path.join('/Users/minseokkang/projects/myproject/pybo/static/image', filename))
                user = User(username=form.username.data, password=generate_password_hash(form.password1.data),
                            email=form.email.data, profile_img=filename, kakao=0)
                db.session.add(user)
                db.session.commit()
                session.clear()
                session['user_id'] = user.id
                if os.path.exists('/var/log/nginx/access.log'):
                    login_time_management(user.id, "main")
                else:
                    pass
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form, form_for_new_category=form_for_new_category,
                           redirect_url=redirect_url)


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    form_for_new_category = CategoryForm()
    redirect_url = get_redirect_url()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            if os.path.exists('/var/log/nginx/access.log'):
                login_time_management(user.id, "main")
            else:
                pass
            return redirect(url_for('main.index'))
        flash(error)

    return render_template('auth/login.html', form=form, form_for_new_category=form_for_new_category,
                           redirect_url=redirect_url)


@bp.route('/kakao_login', methods=['GET'])
def kakao_login():
    redirect_uri = f"{get_redirect_url()}/auth/after_login"
    kakao_auth_url = f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={get_rest_api_kakao()}&redirect_uri={redirect_uri}&prompt=login"
    return redirect(kakao_auth_url)


@bp.route('/after_login', methods=['GET'])
def kakao_after_login():
    code = request.args.get('code')
    # 카카오 인증을 성공한 경우
    if code:
        access_token = get_access_token(code)
        kakao_user_info = get_user_info(access_token)
        name = kakao_user_info["properties"]["nickname"]
        email = kakao_user_info['kakao_account']['email']
        profile_img = kakao_user_info['properties']['profile_image']

        # 카카오 계정이 이미 있는 경우
        already_kakao_user = User.query.filter_by(username=name).first()
        if already_kakao_user:
            session.clear()
            session['user_id'] = already_kakao_user.id
            if os.path.exists('/var/log/nginx/access.log'):
                login_time_management(already_kakao_user.id, "kakao")
            else:
                pass
        else:
            # 동명이인 발생하는 경우
            if User.query.filter_by(username=name).first():
                name = name + str(len(User.query.filter_by(username=name).all()))
            else:
                pass
            user = User(username=name, password="Kakao_oauth", email=email, profile_img=profile_img, kakao=1)
            db.session.add(user)
            db.session.commit()

    return redirect(url_for('main.index'))


@bp.route('/google_login', methods=['GET'])
def google_login():
    return redirect('https://accounts.google.com/o/oauth2/v2/auth?client_id=515175817600-mhrgqiiri81dco8jdch7oheleu8l9qd8.apps.googleusercontent.com&redirect_uri=http://127.0.0.1:5000/auth/after_google_login&scope=https://www.googleapis.com/auth/userinfo.email%20https://www.googleapis.com/auth/userinfo.profile&response_type=code')


@bp.route('/after_google_login', methods=['GET'])
def google_after_login():
    code = request.args.get('code')
    if code:
        CLIENT_ID = '515175817600-mhrgqiiri81dco8jdch7oheleu8l9qd8.apps.googleusercontent.com'
        CLIENT_SECRET = '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'
        REDIRECT_URI = 'http://127.0.0.1:5000/auth/after_google_login'
        GOOGLE_TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token'
        GOOGLE_USERINFO_ENDPOINT = 'https://www.googleapis.com/oauth2/v2/userinfo'

        # 액세스 토큰 요청
        token_response = requests.post(
            GOOGLE_TOKEN_ENDPOINT,
            data={
                'code': code,
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'redirect_uri': REDIRECT_URI,
                'grant_type': 'authorization_code',
            }
        ).json()
        # 액세스 토큰에서 사용자 정보 가져오기
        access_token = token_response.get('access_token')
        user_info_response = requests.get(
            GOOGLE_USERINFO_ENDPOINT,
            headers={'Authorization': f'Bearer {access_token}'}
        ).json()

        name = user_info_response['name']
        email = user_info_response['email']
        profile_img = user_info_response['picture']

        already_google_user = User.query.filter_by(email=email).first()
        if already_google_user:
            session.clear()
            session['user_id'] = already_google_user.id
            if os.path.exists('/var/log/nginx/access.log'):
                login_time_management(already_google_user, 'Google')
            else:
                pass
        else:
            if User.query.filter_by(username=name).first():
                name = name + str(len(User.query.filter_by(username=name).all()))
            else:
                pass
            user = User(
                username=name,
                password="Google",
                email=email,
                profile_img=profile_img,
                kakao=0
            )
            db.session.add(user)
            db.session.commit()
    return redirect(url_for('main.index'))


@bp.route('/forgot/', methods=('GET', 'POST'))
def forgot():
    form = EmailForm()
    form_for_new_category = CategoryForm()
    error = None
    if request.method == 'POST' and form.validate_on_submit():
        mail = User.query.filter_by(email=form.email.data).first()
        if not mail:
            error = "이메일을 확인해주세요"
            flash(error)
        if error is None:
            session.clear()
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                # 순서가 중요하다! : 임시 비밀번호 생성 -> 임시 비밀번호 flash해주기 -> 임시비밀번호 hash함수 적용
                # -> db에 commit해줌으로서 데이터 수정 및 저장
                # 나중에 password random generatot를 만들도록 하자.
                lowercase_letters = ''.join(random.choices(string.ascii_lowercase, k=4))
                digits = ''.join(random.choices(string.digits, k=4))
                generated_password = lowercase_letters + digits
                user.password = generated_password
                flash(f"Your temporary password is: {user.password}")
                user.password = generate_password_hash(user.password)
                db.session.commit()

    return render_template('auth/forgot.html', form=form, form_for_new_category=form_for_new_category)


@bp.route('/logout/')
def logout():
    if g.user.kakao == '1':
        kakao_logout()
    logout_user = LoginStatus.query.filter_by(user_id=g.user.id).order_by(desc(LoginStatus.login_time)).first()
    logout_user.logout_time = datetime.datetime.now()
    db.session.commit()
    session.clear()
    return redirect(url_for('main.index'))


@bp.route('/user_info/<int:user_id>/')
@login_required
def user_info(user_id):
    form_for_new_category = CategoryForm()
    page = request.args.get('page', type=int, default=1)
    user_question_list = Question.query.filter(Question.user_id == user_id).order_by(Question.create_date.desc())
    user_question_num = user_question_list.count()
    user_question_list = user_question_list.paginate(page=page, per_page=10, error_out=False)
    user = User.query.get_or_404(user_id)
    user_name = user.username
    user_total_recommend = db.session.query(question_voter).filter(question_voter.c.user_id == user_id).count()
    profile_img_path = User.query.get_or_404(user_id).profile_img
    user_subscribe_num = user.subscribe_num
    return render_template('auth/user_information.html', to_user_id=user_id,
                           user_question_list=user_question_list, user_name=user_name,
                           user_question_num=user_question_num, user_total_recommend=user_total_recommend,
                           profile_img_path=profile_img_path, user_subscribe_num=user_subscribe_num,
                           form_for_new_category=form_for_new_category)


@bp.route('/subscribe/<int:to_user_id>/<int:from_user_id>/', methods=('GET', 'POST'))
@login_required
def subscribe(from_user_id, to_user_id):
    user = User.query.get_or_404(to_user_id)
    if request.method == 'POST':
        existing_subscription = Subscriber.query.filter_by(
            from_user_id=from_user_id,
            to_user_id=to_user_id
        ).first()
        if from_user_id == to_user_id:
            flash('본인을 구독할 수 없습니다!')
        else:
            if not existing_subscription:
                user.subscribe_num += 1
                subscribe_status = Subscriber(
                    from_user_id=from_user_id,
                    to_user_id=to_user_id
                )
                db.session.add(subscribe_status)
                db.session.commit()
                return redirect(url_for('auth.user_info', user_id=to_user_id))
            else:
                flash('이미 구독을 하셨습니다!')
    return redirect(url_for('auth.user_info', user_id=to_user_id))


@bp.route('/friends/')
@login_required
def friends():
    form_for_new_category = CategoryForm()
    return render_template('auth/friends.html', form_for_new_category=form_for_new_category)



