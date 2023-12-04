import os

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from config.default import BASE_DIR
from .auth_views import login_required
from .. import db
from ..forms import CategoryForm, StatisticForm
from ..models import Category, Statistic
from collections import Counter
import csv, requests

bp = Blueprint('statistic', __name__, url_prefix='/statistic')


@bp.route('/s_list/')
@login_required
def s_list():
    grp = request.args.get('grp', type=str, default=1)
    form_for_new_category = CategoryForm()
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)

    # Statistic 테이블에서 데이터 가져오기
    title_list = []
    statistic_list = Statistic.query.all()
    for name in statistic_list:
        title_list.append(name.title)

    if grp:
        statistic_query = Statistic.query.filter_by(id=grp).first()
        title = statistic_query.title
        labels = statistic_query.labels.strip('[]')
        data = statistic_query.data_value.strip('[]')
        stepsize = statistic_query.stepsize
        border_color = statistic_query.border_color
        type = statistic_query.type
        background_color = statistic_query.background_color
        border_width = statistic_query.border_width
    else:
        statistic_query = Statistic.query.filter_by(id=1).first()
        title = statistic_query.title
        labels = statistic_query.labels.strip('[]')
        data = statistic_query.data_value.strip('[]')
        stepsize = statistic_query.stepsize
        border_color = statistic_query.border_color
        type = statistic_query.type
        background_color = statistic_query.background_color
        border_width = statistic_query.border_width

    return render_template('statistic/statistic_list.html', form_for_new_category=form_for_new_category,
                           category_list=category_list, title=title, labels=labels, data=data, stepsize=stepsize,
                           border_color=border_color, type=type, title_list=title_list,
                           view_name='statistic.s_list', background_color=background_color, border_width=border_width)


@bp.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    form = StatisticForm()
    form_for_new_category = CategoryForm()
    category_list = []
    for selected_category in Category.query.all():
        category_list.append(selected_category.category)

    if request.method == 'POST':
        new_graph = Statistic(
            title=form.title.data,
            labels=form.labels.data,
            data_value=form.data_value.data,
            stepsize=form.stepsize.data,
            border_color=form.border_color.data,
            type=form.type.data,
            background_color=form.background_color.data,
            border_width=form.border_width.data
        )
        db.session.add(new_graph)
        db.session.commit()
        return redirect(url_for('statistic.s_list'))

    return render_template('statistic/statistic_form.html', category_list=category_list,
                           form_for_new_category=form_for_new_category, form=form, view_name='statistic.create')


@bp.route('/live_chart')
@login_required
def live_chart():
    form_for_new_category = CategoryForm()
    seoul_time_list, seoul_temperature_list, seoul_humidity_list, seoul_description_list = [], [], [], []
    url_path = os.path.join(BASE_DIR, "pybo/static/statistic_data/weather_data_Seoul.txt")
    with open(url_path, 'r') as f:
        weather_data = f.read()
        weather_data = weather_data.split('\n')
    for data in weather_data[-11:-1]:
        data = data.split(',')
        current_time = data[0]
        temperature = data[1]
        humidity = data[2]
        weather_description = data[3]
        seoul_time_list.append(current_time)
        seoul_temperature_list.append(temperature)
        seoul_humidity_list.append(humidity)
        seoul_description_list.append(weather_description)

    busan_time_list, busan_temperature_list, busan_humidity_list, busan_description_list = [], [], [], []
    url_path = os.path.join(BASE_DIR, "pybo/static/statistic_data/weather_data_Busan.txt")
    with open(url_path, 'r') as f:
        weather_data = f.read()
        weather_data = weather_data.split('\n')
    for data in weather_data[-11:-1]:
        data = data.split(',')
        current_time = data[0]
        temperature = data[1]
        humidity = data[2]
        weather_description = data[3]
        busan_time_list.append(current_time)
        busan_temperature_list.append(temperature)
        busan_humidity_list.append(humidity)
        busan_description_list.append(weather_description)

    daegu_time_list, daegu_temperature_list, daegu_humidity_list, daegu_description_list = [], [], [], []
    url_path = os.path.join(BASE_DIR, "pybo/static/statistic_data/weather_data_Daegu.txt")
    with open(url_path, 'r') as f:
        weather_data = f.read()
        weather_data = weather_data.split('\n')
    for data in weather_data[-11:-1]:
        data = data.split(',')
        current_time = data[0]
        temperature = data[1]
        humidity = data[2]
        weather_description = data[3]
        daegu_time_list.append(current_time)
        daegu_temperature_list.append(temperature)
        daegu_humidity_list.append(humidity)
        daegu_description_list.append(weather_description)

    daejeon_time_list, daejeon_temperature_list, daejeon_humidity_list, daejeon_description_list = [], [], [], []
    url_path = os.path.join(BASE_DIR, "pybo/static/statistic_data/weather_data_Daejeon.txt")
    with open(url_path, 'r') as f:
        weather_data = f.read()
        weather_data = weather_data.split('\n')
    for data in weather_data[-11:-1]:
        data = data.split(',')
        current_time = data[0]
        temperature = data[1]
        humidity = data[2]
        weather_description = data[3]
        daejeon_time_list.append(current_time)
        daejeon_temperature_list.append(temperature)
        daejeon_humidity_list.append(humidity)
        daejeon_description_list.append(weather_description)

    ulsan_time_list, ulsan_temperature_list, ulsan_humidity_list, ulsan_description_list = [], [], [], []
    url_path = os.path.join(BASE_DIR, "pybo/static/statistic_data/weather_data_Ulsan.txt")
    with open(url_path, 'r') as f:
        weather_data = f.read()
        weather_data = weather_data.split('\n')
    for data in weather_data[-11:-1]:
        data = data.split(',')
        current_time = data[0]
        temperature = data[1]
        humidity = data[2]
        weather_description = data[3]
        ulsan_time_list.append(current_time)
        ulsan_temperature_list.append(temperature)
        ulsan_humidity_list.append(humidity)
        ulsan_description_list.append(weather_description)

    incheon_time_list, incheon_temperature_list, incheon_humidity_list, incheon_description_list = [], [], [], []
    url_path = os.path.join(BASE_DIR, "pybo/static/statistic_data/weather_data_Incheon.txt")
    with open(url_path, 'r') as f:
        weather_data = f.read()
        weather_data = weather_data.split('\n')
    for data in weather_data[-11:-1]:
        data = data.split(',')
        current_time = data[0]
        temperature = data[1]
        humidity = data[2]
        weather_description = data[3]
        incheon_time_list.append(current_time)
        incheon_temperature_list.append(temperature)
        incheon_humidity_list.append(humidity)
        incheon_description_list.append(weather_description)

    return render_template('statistic/live_chart_list.html', form_for_new_category=form_for_new_category,
                           seoul_temperature_list=str(seoul_temperature_list).strip('[]'),
                           seoul_humidity_list=str(seoul_humidity_list).strip('[]'),
                           seoul_description_list=str(seoul_description_list).strip('[]'),
                           seoul_time_list=str(seoul_time_list).strip('[]'),
                           busan_temperature_list=str(busan_temperature_list).strip('[]'),
                           busan_humidity_list=str(busan_humidity_list).strip('[]'),
                           busan_description_list=str(busan_description_list).strip('[]'),
                           busan_time_list=str(busan_time_list).strip('[]'),
                           daegu_temperature_list=str(daegu_temperature_list).strip('[]'),
                           daegu_humidity_list=str(daegu_humidity_list).strip('[]'),
                           daegu_description_list=str(daegu_description_list).strip('[]'),
                           daegu_time_list=str(daegu_time_list).strip('[]'),
                           daejeon_temperature_list=str(daejeon_temperature_list).strip('[]'),
                           daejeon_humidity_list=str(daejeon_humidity_list).strip('[]'),
                           daejeon_description_list=str(daejeon_description_list).strip('[]'),
                           daejeon_time_list=str(daejeon_time_list).strip('[]'),
                           ulsan_temperature_list=str(ulsan_temperature_list).strip('[]'),
                           ulsan_humidity_list=str(ulsan_humidity_list).strip('[]'),
                           ulsan_description_list=str(ulsan_description_list).strip('[]'),
                           ulsan_time_list=str(ulsan_time_list).strip('[]'),
                           incheon_temperature_list=str(incheon_temperature_list).strip('[]'),
                           incheon_humidity_list=str(incheon_humidity_list).strip('[]'),
                           incheon_description_list=str(incheon_description_list).strip('[]'),
                           incheon_time_list=str(incheon_time_list).strip('[]')
                           )
