from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from .. import db
from ..forms import CategoryForm, StatisticForm
from ..models import Category, Statistic
from collections import Counter
import csv, requests

bp = Blueprint('statistic', __name__, url_prefix='/statistic')


@bp.route('/s_list/')
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


@bp.route('/live_chart/')
def live_chart():
    form_for_new_category = CategoryForm()
    data = list()
    csv_file = open("/Users/minseokkang/projects/myproject/pybo/static/statistic_data/salaries.csv", 'r', encoding='utf-8-sig')
    rea = csv.reader(csv_file)
    for case in rea:
        data.append(case)

    data_scientist_salary_2023 = []
    data_engineer_salary_2023 = []
    data_analyst_salary_2023 = []
    data_scientist_salary_2022 = []
    data_engineer_salary_2022 = []
    data_analyst_salary_2022 = []
    data_scientist_salary_2021 = []
    data_engineer_salary_2021 = []
    data_analyst_salary_2021 = []
    data_scientist_salary_2020 = []
    data_engineer_salary_2020 = []
    data_analyst_salary_2020 = []
    for row in data:
        if row[0] == '2023':
            if row[3] == 'Data Scientist':
                data_scientist_salary_2023.append(row[6])
            elif row[3] == 'Data Engineer':
                data_engineer_salary_2023.append(row[6])
            elif row[3] == 'Data Analyst':
                data_analyst_salary_2023.append(row[6])
        if row[0] == '2022':
            if row[3] == 'Data Scientist':
                data_scientist_salary_2022.append(row[6])
            elif row[3] == 'Data Engineer':
                data_engineer_salary_2022.append(row[6])
            elif row[3] == 'Data Analyst':
                data_analyst_salary_2022.append(row[6])
        if row[0] == '2021':
            if row[3] == 'Data Scientist':
                data_scientist_salary_2021.append(row[6])
            elif row[3] == 'Data Engineer':
                data_engineer_salary_2021.append(row[6])
            elif row[3] == 'Data Analyst':
                data_analyst_salary_2021.append(row[6])
        if row[0] == '2020':
            if row[3] == 'Data Scientist':
                data_scientist_salary_2020.append(row[6])
            elif row[3] == 'Data Engineer':
                data_engineer_salary_2020.append(row[6])
            elif row[3] == 'Data Analyst':
                data_analyst_salary_2020.append(row[6])







    time_list, temperature_list, humidity_list, description_list = [], [], [], []
    with open('/Users/minseokkang/projects/myproject/pybo/static/statistic_data/weather_data.txt', 'r') as f:
        weather_data = f.read()
        weather_data = weather_data.split('\n')
    for data in weather_data[-25:-1]:
        data = data.split(',')
        current_time = data[0]
        temperature = data[1]
        humidity = data[2]
        weather_description = data[3]
        time_list.append(current_time)
        temperature_list.append(temperature)
        humidity_list.append(humidity)
        description_list.append(weather_description)

    return render_template('statistic/live_chart_list.html', form_for_new_category=form_for_new_category,
                           temperature_list=str(temperature_list).strip('[]'), humidity_list=str(humidity_list).strip('[]'),
                           description_list=str(description_list).strip('[]'), time_list=str(time_list).strip('[]'))