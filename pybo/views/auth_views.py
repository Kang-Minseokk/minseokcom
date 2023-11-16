import datetime
import os
import re

import requests
from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
import functools
from sqlalchemy import desc

from pybo import db
from pybo.forms import UserCreateForm, UserLoginForm, EmailForm, CategoryForm
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
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            if not form.profile_img.data:
                user = User(username=form.username.data, password=generate_password_hash(form.password1.data),
                            email=form.email.data, profile_img='minsoek.png')
                db.session.add(user)
                db.session.commit()
            else:
                profile_img = form.profile_img.data
                filename = profile_img.filename
                profile_img.save(os.path.join('/Users/minseokkang/projects/myproject/pybo/static/image', filename))
                user = User(username=form.username.data, password=generate_password_hash(form.password1.data),
                            email=form.email.data, profile_img=filename)
                db.session.add(user)
                db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form, form_for_new_category=form_for_new_category)


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    form_for_new_category = CategoryForm()
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
            with open('/var/log/nginx/access.log', 'r') as log_file:
                for row in log_file:
                    ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')
                    # Use the pattern to search for the IP address in the log entry
                    match = ip_pattern.search(row)
                    ip_address = match.group(1)
            login_user = LoginStatus(user_id=user.id, login_time=datetime.datetime.now(), platform="main",
                                     ip_address=ip_address)
            db.session.add(login_user)
            db.session.commit()
            return redirect(url_for('main.index'))
        flash(error)

    return render_template('auth/login.html', form=form, form_for_new_category=form_for_new_category)


@bp.route('/kakao_login', methods=['GET', 'POST'])
def kakao_login():
    form_for_new_category = CategoryForm()

    if request.method == 'POST':
        data = request.get_json()
        already_kakao_user = User.query.filter((User.kakao == 1) & (User.email == data["kakaoEmail"])).first()
        # 이미 가입되어있는 사용자
        if already_kakao_user:
            session.clear()
            session['user_id'] = already_kakao_user.id
            login_user = LoginStatus(user_id=already_kakao_user.id, login_time=datetime.datetime.now(), platform="kakao")
            db.session.add(login_user)
            db.session.commit()
        else:
            user = User(username=data["kakaoName"], password="None", email=data["kakaoEmail"],
                        profile_img=data["kakaoImg"], kakao=1)
            db.session.add(user)
            db.session.commit()

        # 응답 반환
    return render_template('auth/login_progress.html', form_for_new_category=form_for_new_category)


@bp.route('/google_login', methods=['GET', 'POST'])
def google_login():
    form_for_new_category = CategoryForm()

    if request.method == 'POST':
        data = request.get_json()
        data = data['User']
        user_profile_img = data['photoURL']
        user_name = data['displayName']
        user_uid = data['uid']
        user_email = data['email']
        already_google_user = User.query.filter_by(email=user_email).first()
        if already_google_user:
            session.clear()
            session['user_id'] = already_google_user.id
            login_user = LoginStatus(user_id=already_google_user.id, login_time=datetime.datetime.now(),
                                     platform="google")
            db.session.add(login_user)
            db.session.commit()
        else:
            # 동명이인 발생하는 경우..
            if User.query.filter_by(username=user_name).first():
                user_name = user_name + str(len(User.query.filter_by(username=user_name).all()))
            else:
                pass
            user = User(username=user_name, password="Google", email=user_email, profile_img=user_profile_img, kakao=0)
            db.session.add(user)
            db.session.commit()

        # 응답 반환
    return render_template('auth/login_progress.html', form_for_new_category=form_for_new_category)


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



