from dash.dependencies import Input, Output
import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import data
import pandas as pd
from pathlib import *

sum_offline_un = data.university_costs() + data.offline_costs()
sum_online_un = data.university_costs() + data.online_costs()

#результыты для оффлайн университета
result = pd.DataFrame({
    'student_count' : [i for i in range(100)],
    'cost_of_study' : [0.0]*100,
})
for i in range(100):
    result['cost_of_study'][i] = sum_offline_un / i
result.to_csv(Path.cwd() / 'assets' / 'result.csv')

#результаты для онлайн обучения
result2 = pd.DataFrame({
    'student_count' : [i for i in range(100)],
    'cost_of_study' : [0.0]*100,
})
for i in range(100):
    result2['cost_of_study'][i] = sum_online_un / i
result2.to_csv(Path.cwd() / 'assets' / 'result2.csv')

fig = px.bar(data.salary, x = 'worker', y = ['salary', 'bonus'], labels = 'salary')
fig2 = px.bar(data.plan_learn, x = 'semestr', y = 'coach_count', color = 'semestr')
fig3 = px.line(result, x = 'student_count', y = 'cost_of_study')
fig4 = px.line(result2, x = 'student_count', y = 'cost_of_study')

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Затраты на университет и стоимость образования'),
    html.Div([
        html.H2('Зарплаты сотрудников'),
        dcc.Graph(figure = fig),
    ]),
    html.Div([
        html.H2('Необходимое количество преподавателей на каждый семестр'),
        dcc.Graph(figure = fig2),
    ]),
    html.Div([
        html.H2('Стоимость оффлайн обучения за 4 года'),
        dcc.Graph(figure = fig3),
    ]),
    html.Div([
        html.H2('Стоимость онлайн обучения за 4 года'),
        dcc.Graph(figure = fig4),
    ]),
])

app.run_server(debug=False)