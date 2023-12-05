import datetime
import json
import logging
import os.path
import re
import time

from flask import Blueprint, render_template, g, request, redirect, url_for, jsonify, session

from config.default import BASE_DIR
from ..forms import CategoryForm, KakaoForm
from ..functions import get_redirect_url, get_latest_post
from ..models import Question, DailyVisit, Category, question_voter, User, answer_voter, Answer, Kakao
from pybo import db
from collections import Counter


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/robots.txt')
def hello_pybo():
    robots = 'User-agent: * Allow: /'
    return robots


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/', methods=['POST', 'GET'])
def index():
    # 오늘 최초 접속한 클라이언트의 ip주소
    only_visit_user_ip = request.remote_addr
    question_list = get_latest_post(5)
    today_date = datetime.datetime.now().strftime('%Y-%m-%d')
    today_visit_user = DailyVisit.query.filter_by(date=today_date).first()
    form_for_new_category = CategoryForm()
    redirect_url = get_redirect_url()

    if request.method == 'POST' and form_for_new_category.validate_on_submit():
        category = Category(
            category=form_for_new_category.category.data
        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('main.index'))

    #어제 방문한 클라이언트의 수
    yesterday_visit_result = DailyVisit.query.all()[-2]
    yesterday_visit_count = yesterday_visit_result.only_visit_count

    # 테이블에 로그인을 완료한 사용자 추적하기
    if g.user:
        if today_visit_user:
            today_visit_user_list = json.loads(today_visit_user.visit_list)
            if g.user.id not in today_visit_user_list:
                today_visit_user_list.append(g.user.id)
                today_visit_user.visit_list = json.dumps(today_visit_user_list)
                today_visit_user.count = json.dumps(len(today_visit_user_list))
                db.session.commit()

    else:
        try:
            with open('/var/log/nginx/access.log', 'r') as log_file:
                for row in log_file:
                    ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')
                    # Use the pattern to search for the IP address in the log entry
                    match = ip_pattern.search(row)
                    ip_address = match.group(1)
                only_visit_user_list = json.loads(today_visit_user.only_visit_user_list)
                logging.debug(only_visit_user_list)
                if ip_address not in only_visit_user_list:
                    only_visit_user_list.append(ip_address)
                    today_visit_user.only_visit_user_list = json.dumps(only_visit_user_list)
                    today_visit_user.only_visit_count = json.dumps(len(only_visit_user_list))
                    db.session.commit()
                else:
                    pass
        except FileNotFoundError:
            print("File not found. Please check file path.")
        except Exception as e:
            print(f"An error occurred: {e}")

        if today_visit_user:
            only_visit_user_list = json.loads(today_visit_user.only_visit_user_list)

            if only_visit_user_ip not in only_visit_user_list:
                only_visit_user_list.append(only_visit_user_ip)
                today_visit_user.only_visit_list = json.dumps(only_visit_user_list)
                today_visit_user.only_visit_count = json.dumps(len(only_visit_user_list))
                db.session.commit()


    # 총 방문자 리스트
    total_visit_user = DailyVisit.query.all()
    total_visit_count = 0
    for day_visit in total_visit_user:
        day_visit_list = json.loads(day_visit.only_visit_user_list)
        day_visit_count = len(day_visit_list)
        total_visit_count += day_visit_count

    # 일별 방문자 리스트
    if DailyVisit.query.filter_by(date=today_date).first():
        pass
    else:
        today_visit = DailyVisit(
            date=today_date,
            visit_list="[]",
            count=0,
            only_visit_user_list="[]",
            only_visit_count=0
        )
        db.session.add(today_visit)
        db.session.commit()
    daily_count_list = reversed(DailyVisit.query.order_by(DailyVisit.id.desc()).limit(8).all())
    daily_visit_list = []
    for daily_count in daily_count_list:
        daily_visit_list.append(daily_count.count)
    daily_visit_list = str(daily_visit_list).strip('[]')

    # 총 포스트 개수
    total_posts_count = Question.query.count()

    # 카테고리 리스트 전달해주기
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)

    # 일별 게시글 개수 리스트 전달
    post_list = []
    for i in range(8):
        now = datetime.datetime.now()
        date = ((now - datetime.timedelta(days=7-i)).strftime("%Y-%m-%d"))
        count = 0
        for question in Question.query.all():
            if question.create_date.strftime("%Y-%m-%d") == date:
                count += 1
        post_list.append(count)
    post_list = str(post_list).strip('[]')

    # 질문 추천 점수 최신화
    question_vote = db.session.query(question_voter).all()
    question_voted_user_list = []
    for voter in question_vote:
        voted_question = Question.query.filter_by(id=voter.question_id).first()
        question_voted_user_list.append(voted_question.user_id)
    question_elements_counts = Counter(question_voted_user_list)
    for user_id, value in question_elements_counts.items():
        User.query.filter_by(id=user_id).first().score = value
        db.session.commit()

    answer_vote = db.session.query(answer_voter).all()
    answer_voted_user_list = []
    for voter in answer_vote:
        voted_answer = Answer.query.filter_by(id=voter.answer_id).first()
        answer_voted_user_list.append(voted_answer.user_id)
    answer_elements_counts = Counter(answer_voted_user_list)
    for user_id, value in answer_elements_counts.items():
        User.query.filter_by(id=user_id).first().score += value
        db.session.commit()

    # 게시물 점수 순위 (1~3위)
    top3_user = []
    top3_score = []
    top3_obj = User.query.order_by(User.score.desc()).limit(3).all()
    for user in top3_obj:
        top3_user.append(user.username)
        top3_score.append(user.score)
    first_user = top3_user[0]
    first_score = top3_score[0]
    second_user = top3_user[1]
    second_score = top3_score[1]
    third_user = top3_user[2]
    third_score = top3_score[2]

    with open(os.path.join(BASE_DIR, 'pybo/static/statistic_data/news_letter.txt'), 'r') as f:
        lines = f.readlines()
        news_list_link = lines[-2]
        news_list = lines[-1]

    return render_template('home.html', question_list=question_list, total_posts_count=total_posts_count,
                           today_visit_user_count=today_visit_user.only_visit_count, total_visit_count=total_visit_count,
                           daily_visit_list=daily_visit_list, category_list=category_list, form_for_new_category=form_for_new_category,
                           post_list=post_list, first_user=first_user, second_user=second_user, third_user=third_user,
                           first_score=first_score, second_score=second_score, third_score=third_score,
                           news_list=news_list, redirect_url=redirect_url, news_list_link=news_list_link,
                           only_visit_user_ip=only_visit_user_ip, yesterday_visit_count=yesterday_visit_count)

