from .. import db
from ..forms import AnswerForm, CategoryForm
from pybo.models import Question, Answer
from datetime import datetime
from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect
from .auth_views import login_required
from ..functions import get_total_visit_count, get_yesterday_visit_count, get_total_posts_count, get_today_visit_count

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
@login_required
def create(question_id):
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    form = AnswerForm()
    form_for_new_category = CategoryForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)
        question.answer_set.append(answer)
        db.session.commit()
        return redirect('{}#answer_{}'.format(url_for(
            'question.detail', question_id=answer.question.id), answer.id))
    return render_template('question/question_detail.html', question=question, form=form,
                           form_for_new_category=form_for_new_category, total_visit_count=total_visit_count,
                           today_visit_user_count=today_visit_user_count, total_posts_count=total_posts_count,
                           yesterday_visit_count=yesterday_visit_count)


@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    form_for_new_category = CategoryForm()
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    if g.user != answer.user:
        flash('수정 권한이 없습니다')
        return redirect(url_for('question.detail', question_id=answer.question.id))
    if request.method == "POST":
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()
            db.session.commit()
            return redirect('{}#answer_{}'.format(url_for(
                'question.detail', question_id=answer.question.id), answer.id))

    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', answer=answer, form=form,
                           form_for_new_category=form_for_new_category, total_visit_count=total_visit_count,
                           today_visit_user_count=today_visit_user_count, yesterday_visit_count=yesterday_visit_count,
                           total_posts_count=total_posts_count)


@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if g.user != answer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))

