from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import CommentForm, CategoryForm
from pybo.functions import get_total_visit_count, get_yesterday_visit_count, get_total_posts_count, \
    get_today_visit_count
from pybo.models import Question, Comment, Answer
from pybo.views.auth_views import login_required

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/create/question/<int:question_id>', methods=('GET', 'POST'))
@login_required
def create_question(question_id):
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    form = CommentForm()
    form_for_new_category = CategoryForm()
    question = Question.query.get_or_404(question_id)
    if request.method == 'POST' and form.validate_on_submit():
        comment = Comment(user=g.user, content=form.content.data, create_date=datetime.now(), question=question)
        db.session.add(comment)
        db.session.commit()
        return redirect('{}#comment_{}'.format(
            url_for('question.detail', question_id=question_id), comment.id))

    return render_template('comment/comment_form.html', form=form,
                           form_for_new_category=form_for_new_category, today_visit_user_count=today_visit_user_count,
                           total_visit_count=total_visit_count, yesterday_visit_count=yesterday_visit_count,
                           total_posts_count=total_posts_count)


@bp.route('/modify/question/<int:comment_id>', methods=('GET', 'POST'))
@login_required
def modify_question(comment_id):
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    comment = Comment.query.get_or_404(comment_id)
    form_for_new_category = CategoryForm()
    if g.user != comment.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=comment.question.id))
    if request.method == 'POST':
        form = CommentForm()
        if form.validate_on_submit():
            form.populate_obj(comment)
            comment.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect('{}#comment_{}'.format(url_for(
                'question.detail', question_id=comment.question.id), comment.id))

    else:
        form = CommentForm(obj=comment)
    return render_template('comment/comment_form.html', form=form,
                           form_for_new_category=form_for_new_category, today_visit_user_count=today_visit_user_count,
                           total_visit_count=total_visit_count, yesterday_visit_count=yesterday_visit_count,
                           total_posts_count=total_posts_count)


@bp.route('/delete/question/<int:comment_id>')
@login_required
def delete_question(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    question_id = comment.question.id
    if g.user != comment.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))


@bp.route('/create/answer/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def create_answer(answer_id):
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    form = CommentForm()
    form_for_new_category = CategoryForm()
    answer = Answer.query.get_or_404(answer_id)
    if request.method == 'POST' and form.validate_on_submit():
        comment = Comment(user=g.user, content=form.content.data, create_date=datetime.now(), answer=answer)
        db.session.add(comment)
        db.session.commit()
        return redirect('{}#comment_{}'.format(url_for(
            'question.detail', question_id=answer.question.id), comment.id))

    return render_template('comment/comment_form.html', form=form, form_for_new_category=form_for_new_category,
                           today_visit_user_count=today_visit_user_count,
                           total_visit_count=total_visit_count, yesterday_visit_count=yesterday_visit_count,
                           total_posts_count=total_posts_count)


@bp.route('/modify/answer/<int:comment_id>', methods=('GET', 'POST'))
@login_required
def modify_answer(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    form_for_new_category = CategoryForm()
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    if g.user != comment.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=comment.answer.id))
    if request.method == 'POST':
        form = CommentForm()
        if form.validate_on_submit():
            form.populate_obj(comment)
            comment.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect('{}#comment_{}'.format(url_for(
                'question.detail', question_id=comment.answer.question.id), comment.id))

    else:
        form = CommentForm(obj=comment)
    return render_template('comment/comment_form.html', form=form, form_for_new_category=form_for_new_category,
                           today_visit_user_count=today_visit_user_count, total_visit_count=total_visit_count,
                           yesterday_visit_count=yesterday_visit_count, total_posts_count=total_posts_count)


@bp.route('/delete/answer/<int:comment_id>')
@login_required
def delete_answer(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    question_id = comment.answer.question.id
    if g.user != comment.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))