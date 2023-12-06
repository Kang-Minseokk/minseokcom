from flask import Blueprint, render_template, request, redirect, url_for


from pybo.forms import CalendarForm, CategoryForm
from pybo.functions import get_total_visit_count, get_yesterday_visit_count, get_total_posts_count, \
    get_today_visit_count
from pybo.models import Calendar, Category
from pybo import db
from datetime import datetime

from pybo.views.auth_views import power_login_required

bp = Blueprint('calendar', __name__, url_prefix="/calendar")


@bp.route('/show/')
@power_login_required
def show():
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    form_for_new_category = CategoryForm()
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)
    schedule_list = Calendar.query.all()
    schedule_data = []
    today_schedule_list = []
    today_date = datetime.today().date()
    for schedule in schedule_list:
        start_date = schedule.start_date.date()
        end_date = schedule.end_date.date()
        schedule_data.append({
            'id': schedule.id,
            'title': schedule.title,
            'content': schedule.content,
            'start_date': schedule.start_date.strftime("%Y-%m-%d"),
            'end_date': schedule.end_date.strftime("%Y-%m-%d 23:59:59")
        })
        if 0 <= (end_date - today_date).days <= 3:
            today_schedule_list.append(schedule)

    return render_template('calendar/calendar.html', schedule_list=schedule_list,
                           schedule_data=schedule_data, today_schedule_list=today_schedule_list, today_date=today_date,
                           form_for_new_category=form_for_new_category, category_list=category_list,
                           total_posts_count=total_posts_count, total_visit_count=total_visit_count,
                           yesterday_visit_count=yesterday_visit_count, today_visit_user_count=today_visit_user_count)


@bp.route('/list/')
def list():
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    schedule_list = Calendar.query.all()
    form_for_new_category = CategoryForm()
    return render_template('calendar/calendar_list.html', schedule_list=schedule_list,
                           form_for_new_category=form_for_new_category, total_posts_count=total_posts_count,
                           total_visit_count=total_visit_count, yesterday_visit_count=yesterday_visit_count,
                           today_visit_user_count=today_visit_user_count)


@bp.route('/create/', methods=['POST', 'GET'])
def create():
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    form = CalendarForm()
    form_for_new_category = CategoryForm()
    if request.method == 'POST':
        schedule = Calendar(
            title=form.title.data,
            content=form.content.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data
        )
        db.session.add(schedule)
        db.session.commit()
        return redirect(url_for('calendar.show'))

    return render_template('calendar/calendar_form.html', form=form, usage='create',
                           form_for_new_category=form_for_new_category, total_posts_count=total_posts_count,
                           total_visit_count=total_visit_count, yesterday_visit_count=yesterday_visit_count,
                           today_visit_user_count=today_visit_user_count)


@bp.route('/modify/<int:schedule_id>/', methods=['POST', 'GET'])
def modify(schedule_id):
    total_visit_count = get_total_visit_count()
    yesterday_visit_count = get_yesterday_visit_count()
    total_posts_count = get_total_posts_count()
    today_visit_user_count = get_today_visit_count()
    form_for_new_category = CategoryForm()
    schedule = Calendar.query.get_or_404(schedule_id)
    if request.method == 'POST':
        form = CalendarForm()
        schedule.title = form.title.data,
        schedule.content = form.content.data,
        schedule.start_date = form.start_date.data,
        schedule.end_date = form.end_date.data
        db.session.commit()
        return redirect(url_for('calendar.show'))
    else:
        schedule.start_date = schedule.start_date.date()
        schedule.end_date = schedule.end_date.date()
        form = CalendarForm(obj=schedule)

    return render_template('calendar/calendar_form.html', form=form, usage='modify',
                           form_for_new_category=form_for_new_category, total_posts_count=total_posts_count,
                           total_visit_count=total_visit_count, yesterday_visit_count=yesterday_visit_count,
                           today_visit_user_count=today_visit_user_count)