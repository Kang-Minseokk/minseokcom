from datetime import datetime

from flask import Blueprint, render_template, request, url_for, escape
from werkzeug.utils import redirect

from .. import db
from ..forms import GoalForm, CategoryForm
from ..models import Goal
from ..views.auth_views import power_login_required

bp = Blueprint('goal', __name__, url_prefix='/goal')


@bp.route('/list/')
@power_login_required
def list():
    form_for_new_category = CategoryForm()
    goal_list = Goal.query.order_by(Goal.id.desc())
    month_goal_list = goal_list.filter(Goal.period == 'month')
    year_goal_list = goal_list.filter(Goal.period == 'year')
    book_goal_list = goal_list.filter(Goal.period == 'book')
    achieved_goal_list = goal_list.filter(Goal.done == True)
    achieved_month_goal = achieved_goal_list.filter(Goal.period == 'month')
    achieved_year_goal = achieved_goal_list.filter(Goal.period == 'year')
    achieved_book_goal = achieved_goal_list.filter(Goal.period == 'book')
    return render_template('goal/goal_list.html', datetime=datetime, month_goal_list=month_goal_list,
                           year_goal_list=year_goal_list, book_goal_list=book_goal_list,
                           achieved_goal_list=achieved_goal_list, achieved_month_goal=achieved_month_goal,
                           achieved_year_goal=achieved_year_goal, achieved_book_goal=achieved_book_goal,
                           form_for_new_category=form_for_new_category)


@bp.route('/create/', methods=('POST', 'GET'))
@power_login_required
def create():
    form = GoalForm()
    form_for_new_category = CategoryForm()
    if request.method == 'POST' and form.validate_on_submit():
        goal = Goal(
            title=form.title.data,
            content=form.content.data,
            period=form.period.data
        )
        db.session.add(goal)
        db.session.commit()
        return redirect(url_for('goal.list'))
    return render_template('goal/goal_form.html', form=form, form_for_new_category=form_for_new_category)


@bp.route('/detail/<int:goal_id>/', methods=('POST', 'GET'))
@power_login_required
def detail(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    form_for_new_category = CategoryForm()
    if request.method == 'POST':
        return redirect(url_for('goal.list', form_for_new_category=form_for_new_category))

    return render_template('goal/goal_detail.html', goal=goal, form_for_new_category=form_for_new_category)


@bp.route('/done/<int:goal_id>/')
@power_login_required
def done(goal_id):
    form_for_new_category = CategoryForm()
    goal = Goal.query.get_or_404(goal_id)
    goal.done = True
    db.session.commit()
    return redirect(url_for('goal.list', goal_id=goal_id, form_for_new_category=form_for_new_category))


@bp.route('/delete/<int:goal_id>/')
@power_login_required
def delete(goal_id):
    form_for_new_category = CategoryForm()
    goal = Goal.query.get_or_404(goal_id)
    db.session.delete(goal)
    db.session.commit()

    return redirect(url_for('goal.list', form_for_new_category=form_for_new_category))


@bp.route('/divided_list/<int:num>')
@power_login_required
def divided_list(num):
    form_for_new_category = CategoryForm()
    page = request.args.get('page', type=int, default=1)
    if num == 1:
        goal_list = Goal.query.filter(Goal.period == 'month', Goal.done==False).paginate(page=page, per_page=5,
                                                                                         error_out=False)
    elif num == 2:
        goal_list = Goal.query.filter(Goal.period == 'year', Goal.done==False).paginate(page=page, per_page=5,
                                                                                        error_out=False)
    elif num == 3:
        goal_list = Goal.query.filter(Goal.period == 'book', Goal.done==False).paginate(page=page, per_page=5,
                                                                                        error_out=False)
    else:
        goal_list = Goal.query.filter(Goal.done==True).paginate(page=page, per_page=5, error_out=False)

    return render_template('goal/goal_divided_list.html', goal_list=goal_list, num=num,
                           form_for_new_category=form_for_new_category)


@bp.route('/modify/<int:goal_id>/', methods=('GET', 'POST'))
@power_login_required
def modify(goal_id):
    goal = Goal.query.get_or_404(goal_id)
    form = GoalForm()
    form_for_new_category = CategoryForm()
    if request.method == 'GET':
        form.title.data = goal.title
        form.content.data = goal.content
        form.period.data = goal.period

    if request.method == 'POST':
        goal.title = form.title.data,
        goal.content = form.content.data,
        goal.period = form.period.data
        db.session.commit()
        return redirect(url_for('goal.detail', goal_id=goal.id))

    return render_template('goal/goal_form.html', form=form, goal=goal, form_for_new_category=form_for_new_category)
