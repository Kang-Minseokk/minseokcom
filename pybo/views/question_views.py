import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Blueprint, render_template, request, url_for, g, flash, make_response
from sqlalchemy import func
from werkzeug.utils import redirect

from config import SMTP_SERVER, SMTP_PORT, EMAIL_ADDR, EMAIL_PASSWORD
from .. import db
from ..forms import QuestionForm, AnswerForm, CategoryForm
from ..models import Question, Answer, User, question_voter, Subscriber, Category, Statistic
from ..views.auth_views import login_required

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/data_science_list/<string:category>')
def ds_list(category):
    # 입력 파라미터
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    so = request.args.get('so', type=str, default='recent')
    form_for_new_category = CategoryForm()

    # 정렬
    if so == 'recommend':
        sub_query = db.session.query(question_voter.c.question_id, func.count('*').label('num_voter')) \
            .group_by(question_voter.c.question_id).subquery()
        question_list = Question.query.filter(Question.category == category) \
            .outerjoin(sub_query, Question.id == sub_query.c.question_id) \
            .order_by(sub_query.c.num_voter.desc(), Question.create_date.desc())
    elif so == 'popular':
        sub_query = db.session.query(Answer.question_id, func.count('*').label('num_answer')) \
            .group_by(Answer.question_id).subquery()
        question_list = Question.query.filter(Question.category == category) \
            .outerjoin(sub_query, Question.id == sub_query.c.question_id) \
            .filter(Question.category == category) \
            .order_by(sub_query.c.num_answer.desc(), Question.create_date.desc())
    else:  # recent
        question_list = Question.query.order_by(Question.create_date.desc()).filter(Question.category == category)
    # 태그 리스트 생성

    tag_list = question_list.with_entities(Question.tag).all()
    tag_list = list(set(tag_list))
    tag_list = [tag[0] for tag in tag_list]
    # 조회
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(Answer.question_id, Answer.content, User.username) \
            .join(User, Answer.user_id == User.id).subquery()
        question_list = question_list \
            .join(User) \
            .outerjoin(sub_query, sub_query.c.question_id == Question.id) \
            .filter(Question.subject.ilike(search) |  # 질문제목
                    Question.content.ilike(search) |  # 질문내용
                    User.username.ilike(search) |  # 질문작성자
                    sub_query.c.content.ilike(search) |  # 답변내용
                    sub_query.c.username.ilike(search)  # 답변작성자
                    ) \
            .distinct()

    # 페이징
    question_list = question_list.paginate(page=page, per_page=10, error_out=False)
    form=CategoryForm()
    # 카테고리 리스트 전달해주기
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)

    return render_template('question/question_list.html', question_list=question_list, page=page,
                            kw=kw, so=so, view_name='question.ds_list', tag_list=tag_list, category=category, form=form,
                            category_list=category_list, form_for_new_category=form_for_new_category)


@bp.route('/development_list/')
def d_list():
    # 입력 파라미터
    tag_list = Question.query.with_entities(Question.tag).all()
    tag_list = list(set(tag_list))
    tag_list = [tag[0] for tag in tag_list]

    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    so = request.args.get('so', type=str, default='recent')
    form_for_new_category = CategoryForm()

    question_list = Question.query.order_by(Question.create_date.desc()).filter(Question.category == 'Development')
    question_list = question_list.paginate(page=page, per_page=10, error_out=False)
    form = CategoryForm()
    # 카테고리 리스트 전달해주기
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)
    return render_template('question/development_list.html', question_list=question_list, page=page,
                           kw=kw, so=so, view_name='question.d_list', tag_list=tag_list, category='Development', form=form,
                           category_list=category_list, form_for_new_category=form_for_new_category)


@bp.route('/computer_science_list/')
def cs_list():
    # 입력 파라미터
    kw = request.args.get('kw', type=str, default='')
    form_for_new_category = CategoryForm()

    question_list = Question.query.order_by(Question.create_date.desc()).filter(
        Question.category == 'Computer Science')

    # 태그 리스트 생성
    tag_list = question_list.with_entities(Question.tag).all()
    tag_list = list(set(tag_list))
    tag_list = [tag[0] for tag in tag_list]
    # 조회
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(Answer.question_id, Answer.content, User.username) \
            .join(User, Answer.user_id == User.id).subquery()
        question_list = question_list \
            .join(User) \
            .outerjoin(sub_query, sub_query.c.question_id == Question.id) \
            .filter(Question.subject.ilike(search) |  # 질문제목
                    Question.content.ilike(search) |  # 질문내용
                    User.username.ilike(search) |  # 질문작성자
                    sub_query.c.content.ilike(search) |  # 답변내용
                    sub_query.c.username.ilike(search)  # 답변작성자
                    ) \
            .distinct()
    form = CategoryForm()
    # 카테고리 리스트 전달해주기
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)
    return render_template('question/computer_science_list.html', question_list=question_list,
                           kw=kw, view_name='question.cs_list', tag_list=tag_list, category='Computer Science', form=form,
                           category_list=category_list, form_for_new_category=form_for_new_category)


@bp.route('/artificial_intelligence_list/<int:num>')
def ai_list(num):
    # 입력 파라미터
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    so = request.args.get('so', type=str, default='recent')
    form_for_new_category = CategoryForm()
    question_list = Question.query.filter(Question.category == 'Artificial Intelligence').order_by(
        Question.create_date.desc())

    # 조회
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(Answer.question_id, Answer.content, User.username) \
            .join(User, Answer.user_id == User.id).subquery()
        question_list = question_list \
            .join(User) \
            .outerjoin(sub_query, sub_query.c.question_id == Question.id) \
            .filter(Question.subject.ilike(search) |  # 질문제목
                    Question.content.ilike(search) |  # 질문내용
                    User.username.ilike(search) |  # 질문작성자
                    sub_query.c.content.ilike(search) |  # 답변내용
                    sub_query.c.username.ilike(search)  # 답변작성자
                    ) \
            .distinct()

    # 태그 리스트 생성
    tag_list = question_list.with_entities(Question.tag).all()
    tag_list = list(set(tag_list))
    tag_list = [tag[0] for tag in tag_list]
    # 페이징
    form = CategoryForm()
    # 카테고리 리스트 전달해주기
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)
    return render_template('question/ai_list.html', question_list=question_list, page=page,
                           kw=kw, so=so, view_name='question.ai_list', tag_list=tag_list,
                           category='Artificial Intelligence', num=num, form=form, category_list=category_list,
                           form_for_new_category=form_for_new_category)


@bp.route('/relaxation_list/<int:num>')
def r_list(num):
    # 입력 파라미터
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    so = request.args.get('so', type=str, default='recent')
    form_for_new_category = CategoryForm()

    # 정렬
    if so == 'recommend':
        sub_query = db.session.query(question_voter.c.question_id, func.count('*').label('num_voter')) \
            .group_by(question_voter.c.question_id).subquery()
        question_list = Question.query.filter(Question.category == 'Relaxation') \
            .outerjoin(sub_query, Question.id == sub_query.c.question_id) \
            .order_by(sub_query.c.num_voter.desc(), Question.create_date.desc())
    elif so == 'popular':
        sub_query = db.session.query(Answer.question_id, func.count('*').label('num_answer')) \
            .group_by(Answer.question_id).subquery()
        question_list = Question.query.filter(Question.category == 'Relaxation') \
            .outerjoin(sub_query, Question.id == sub_query.c.question_id) \
            .order_by(sub_query.c.num_answer.desc(), Question.create_date.desc())
    else:  # recent
        question_list = Question.query.filter(Question.category == 'Relaxation').order_by(Question.create_date.desc())

    # 조회
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(Answer.question_id, Answer.content, User.username) \
            .join(User, Answer.user_id == User.id).subquery()
        question_list = question_list \
            .join(User) \
            .outerjoin(sub_query, sub_query.c.question_id == Question.id) \
            .filter(Question.subject.ilike(search) |  # 질문제목
                    Question.content.ilike(search) |  # 질문내용
                    User.username.ilike(search) |  # 질문작성자
                    sub_query.c.content.ilike(search) |  # 답변내용
                    sub_query.c.username.ilike(search)  # 답변작성자
                    ) \
            .distinct()

    # 태그 리스트 생성
    tag_list = question_list.with_entities(Question.tag).all()
    tag_list = list(set(tag_list))
    tag_list = [tag[0] for tag in tag_list]
    form = CategoryForm()
    # 카테고리 리스트 전달해주기
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)
    return render_template('question/relaxation_list.html', question_list=question_list, page=page,
                           kw=kw, so=so, view_name='question.r_list', tag_list=tag_list, category='Relaxation', num=num,
                           form=form, category_list=category_list, form_for_new_category=form_for_new_category)


@bp.route('/communication_list/')
def c_list():
    # 입력 파라미터
    kw = request.args.get('kw', type=str, default='')
    form_for_new_category = CategoryForm()

    question_list = Question.query.filter(Question.category == 'Communication').order_by(
        Question.create_date.desc())
    tag_list = question_list.with_entities(Question.tag).all()
    tag_list = list(set(tag_list))
    tag_list = [tag[0] for tag in tag_list]
    list_count = question_list.count()
    # 조회
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(Answer.question_id, Answer.content, User.username) \
            .join(User, Answer.user_id == User.id).subquery()
        question_list = question_list \
            .join(User) \
            .outerjoin(sub_query, sub_query.c.question_id == Question.id) \
            .filter(Question.subject.ilike(search) |  # 질문제목
                    Question.content.ilike(search) |  # 질문내용
                    User.username.ilike(search) |  # 질문작성자
                    sub_query.c.content.ilike(search) |  # 답변내용
                    sub_query.c.username.ilike(search)  # 답변작성자
                    ) \
            .distinct()
    form = CategoryForm()
    # 카테고리 리스트 전달해주기
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)
    return render_template('question/communication_list.html', question_list=question_list, kw=kw,
                           view_name='question.c_list', tag_list=tag_list, category='Communication',
                           list_count=list_count, form=form, category_list=category_list,
                           form_for_new_category=form_for_new_category)


@bp.route('/detail/<int:question_id>/')
@login_required
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    form_for_new_category = CategoryForm()
    question_content = question.content
    response = make_response(render_template('question/question_detail.html', question=question, form=form,
                                             question_content=(question_content), form_for_new_category=form_for_new_category))

    cookie_name = str(g.user.id)
    if request.cookies.get(cookie_name) is not None:
        cookies = request.cookies.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(question_id) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{question_id}')
            question.views += 1
            db.session.commit()
            return response
    else:
        response.set_cookie(cookie_name, str(question_id))
        question.views += 1
        db.session.commit()
        return response

    return render_template('question/question_detail.html', question=question, form=form,
                           question_content=(question_content), form_for_new_category=form_for_new_category)


@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = QuestionForm()
    form_for_new_category = CategoryForm()
    tag_list = Question.query.with_entities(Question.tag).all()
    tag_list = list(set(tag_list))
    tag_list = [tag[0] for tag in tag_list]
    subscriber_rows = Subscriber.query.filter_by(to_user_id=g.user.id).all()
    user_emails = [User.query.get_or_404(row.from_user_id).email for row in subscriber_rows]
    # 카테고리 리스트 전달해주기
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)

    if request.method == 'POST' and form.validate_on_submit():
        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now(),
            user=g.user,
            category=form.category.data,
            tag=form.tag.data
        )
        db.session.add(question)
        db.session.commit()

        # 1. SMTP 서버 연결
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

        # 2. SMTP 서버에 로그인
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
                <p>글을 확인하기 위해서 아래의 링크를 클릭해주세요!</p>
                <span>미리보기</span>
                <div class="container" style="max-width: 50%; border: 1px solid #000; padding: 20px; margin: 10px; 
                background-color: #f5f2eb;">
                    <p>Title: {question.subject}</p>
                    <p style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis">Content: {(question.content)}</p>
                </div>
                <a href="http://127.0.0.1:5000/question/detail/{question.id}/" class="link-style">글 읽으러 가기</a>
            </div>
        </body>
        </html>
        """

        # 구독자가 없는 경우를 대비
        if user_emails:
            # 이메일 본문을 MIMEText로 설정
            message = MIMEMultipart()
            message.attach(MIMEText(email_content, 'html'))

            # 3. MIME 형태의 이메일 메세지 작성
            message["Subject"] = f"{g.user.username}님의 새로운 글이 올라왔어요!"
            message["From"] = EMAIL_ADDR  # 보내는 사람의 이메일 계정
            message["To"] = ','.join(user_emails)

            # 4. 서버로 메일 보내기
            smtp.send_message(message)

            # 5. 메일을 보내면 서버와의 연결 끊기
            smtp.quit()

        else:
            pass
        return redirect(url_for('main.index'))

    return render_template('question/question_form.html', form=form, tag_list=tag_list,
                           category_list=category_list, form_for_new_category=form_for_new_category)


@bp.route('/modify/<int:question_id>', methods=('GET', 'POST'))
@login_required
def modify(question_id):
    form_for_new_category = CategoryForm()
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id, form_for_new_category=form_for_new_category))
    if request.method == 'POST':
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id, form_for_new_category=form_for_new_category))
    else:
        form = QuestionForm(obj=question)
    return render_template('question/question_form.html', form=form, form_for_new_category=form_for_new_category)


@bp.route('/delete/<int:question_id>')
@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id)
    form_for_new_category = CategoryForm()
    if g.user != question.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id, form_for_new_category=form_for_new_category))
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('main.index', form_for_new_category=form_for_new_category))


@bp.route('/tagged_list/<string:tag>/<string:category>')
@login_required
def tagged_list(tag, category):
    question_list = Question.query.filter(Question.tag == tag, Question.category == category)
    form_for_new_category = CategoryForm()
    page = request.args.get('page', type=int, default=1)
    question_list = question_list.paginate(page=page, per_page=10, error_out=False)
    return render_template('question/tagged_list.html', question_list=question_list, page=page, tag=tag,
                           category=category, view_name='question.tagged_list', form_for_new_category=form_for_new_category)


