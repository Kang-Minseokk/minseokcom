from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, SelectField, DateField, BooleanField, \
    FileField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수 입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])
    category = TextAreaField('category',  validators=[DataRequired('카테고리를 선택해주세요')])
    tag = TextAreaField('태그', validators=[DataRequired('태그는 최소 한개를 선택을 해야 합니다')])


class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])


class EmailForm(FlaskForm):
    email = TextAreaField('Email', validators=[DataRequired(), Email()])


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    profile_img = FileField('프로필 사진')
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField('이메일', [DataRequired(), Email()])
    subscribe_num = IntegerField('구독자 수')


class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])


class GoalForm(FlaskForm):
    title = TextAreaField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])
    describe = TextAreaField('설명')
    period = TextAreaField('기간', validators=[DataRequired()])
    done = BooleanField('완료')


class CalendarForm(FlaskForm):
    title = TextAreaField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])
    start_date = DateField('시작날짜', validators=[DataRequired()])
    end_date = DateField('종료날짜', validators=[DataRequired()])


class CategoryForm(FlaskForm):
    category = TextAreaField('카테고리', validators=[DataRequired()])


class StatisticForm(FlaskForm):
    title = TextAreaField('제목')
    labels = TextAreaField('가로축 값')
    data_value = TextAreaField('가로축 인덱스')
    stepsize = IntegerField('세로축 눈금간격')
    border_color = TextAreaField('그래프 색상')
    type = TextAreaField('그래프 형태')
    background_color = TextAreaField('그래프 색 채우기')
    border_width = IntegerField('그래프 두께')


class KakaoForm(FlaskForm):
    id = IntegerField('아이디')
    email = TextAreaField('이메일')
    profile_img = TextAreaField('프로필 사진')