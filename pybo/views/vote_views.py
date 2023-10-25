from flask import Blueprint, url_for, flash, g
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import CategoryForm
from pybo.models import Question, Answer, question_voter
from pybo.views.auth_views import login_required

bp = Blueprint('vote', __name__, url_prefix='/vote')


@bp.route('/question/<int:question_id>/')
@login_required
def question(question_id):
    form_for_new_category = CategoryForm()
    _question = Question.query.get_or_404(question_id)
    if g.user == _question.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        voted_question_list = []
        voted_questions = db.session.query(question_voter).filter_by(user_id=g.user.id).all()
        for voted_question in voted_questions:
            voted_question_list.append(voted_question.question_id)
        if question_id not in voted_question_list:
            _question.voter.append(g.user)
            db.session.commit()
        else:
            flash('이미 추천했습니다.')

    return redirect(url_for('question.detail', question_id=question_id, form_for_new_category=form_for_new_category))


@bp.route('/answer/<int:answer_id>/')
@login_required
def answer(answer_id):
    form_for_new_category = CategoryForm()
    _answer = Answer.query.get_or_404(answer_id)
    if g.user == _answer.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        _answer.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=_answer.question.id, form_for_new_category=form_for_new_category))