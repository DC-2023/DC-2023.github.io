#!/usr/bin/python3

import dash
from dash import dcc, ctx
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import truck
import uzel
import time
import os
import json
import re


# Create the app
app = dash.Dash(__name__)

# Load dataset using Plotly
tips = px.data.tips()

fig = px.scatter(tips, x="total_bill", y="tip") # Create a scatterplot

title = html.H1("!!!Привет, Вован!!!")

# Поиск кода ошибки в базе
def poisk(marka_, uzel_, code_, fmi_):
    if fmi_ == 'ALL':
        kod = f'{uzel_} ' + f'{code_} ' + f'{marka_}'
    else:
        kod = f'{uzel_} ' + f'{code_}-' + f'{fmi_} ' + f'{marka_}'
    
    file = f'{marka_}/FAIL_CODE/{uzel_}/{kod}.json'
    
    rez = []
    if os.path.exists(f'{marka_}/FAIL_CODE/{uzel_}/{kod}.json'):
        with open (file) as f:
            js = json.load(f)
            for val in js.values():
                v = 'Описание ошибки: '
                stroka = (f'{v}===> {val}')
                rez = re.sub('[\'\"\[\]]', '', stroka)
    else:
        rez.append("Данной ошибки нет в базе. Проверьте правильность вводимых данных")
    #name, __ = os.path.splitext(filename)
    #from os.path import basename, splitext
    #name, ext = splitext(basename("C:/Users/111/some_video.mp4"))
    return rez
    
# Извлечение марок авто
def marka():
    #with open ('truck.json') as f:
        #tr = f.load()
    tr = truck.truck
    marka = []
    for t in tr:
        for mar in t.keys():
            marka.append(mar)
    return marka

# Извлечение модели относительно марки
auto = []
def model(car):
    #with open ('truck.json') as f:
        #tr = f.load()
    tr = truck.truck
    md = []
    for t in tr:
        for marka, mod in t.items():      
            if marka == car:
                for m in mod:
                    for mdl, ltr in m.items():
                        md.append(mdl)
                        auto.append(ltr)
    return md

# Извлечение объема относительно модели
def automob(au):
    #with open ('truck.json') as f:
        #tr = f.load()
    tr = truck.truck
    obiem = []
    for t in tr:
        for model in t.values():
            for mod in model:
                for m, l in mod.items():
                    if m == au:
                        for litr in l: # Удаление скобок
                            obiem.append(litr)
    return obiem

# Извлечение узла относительно модели
def modul(mod):
    #with open ('uzel.json') as f:
        #md = f.load()
    md = uzel.uzel
    m = []
    for uz in md:
        for k, v in uz.items():
            if k == mod:
                for u in v:
                    m.append(u)
    return m

year = [i for i in range(1995, 2024)]
code = [i for i in range(0, 4001)]
code.insert(0, 'ALL')
fmi = [i for i in range(0, 100)]
fmi.insert(0, 'ALL')

col = html.Div([
    dcc.Dropdown(options = [{'label': m, 'value': m} for m in marka()], 
        id = 'dropdown', 
        value = 'MAN',
        style = {'display':'inline-block', 'padding': 10, 'width': 150}),
    dcc.Dropdown(
        id = 'dropdown2',
        value = 'TGA',
        style={'display':'inline-block','padding': 10,'width': 100}),
    dcc.Dropdown(
        id = 'dropdown3',
        style={'display':'inline-block','padding': 10,'width': 90}),
    dcc.Dropdown(year, value = '2000', id = 'dropdown4',
        style={'display':'inline-block','padding': 10,'width': 70}),
    dcc.Dropdown( 
        id = 'dropdown5',
        style={'display':'inline-block','padding': 10,'width': 150}),
    dcc.Dropdown(code, id = 'dropdown6',
        style={'display':'inline-block','padding': 10,'width': 75}),
    dcc.Dropdown(fmi, value = 'ALL', id = 'dropdown7',
        style={'display':'inline-block','padding': 10,'width': 55})       
  ]
)

# Заполнение полей
@app.callback(
    Output('dropdown2', 'options'),
    [Input('dropdown', 'value')])
def set_options(val):
    return model(val)

@app.callback(
    Output('dropdown3', 'options'),
    [Input('dropdown2', 'value')])
def set_value(val):
    return automob(val)

@app.callback(
    Output('dropdown5', 'options'),
    [Input('dropdown', 'value')])
def set_uzel(val):
    return modul(val)
  
# Кнопка и реакция на нажатие
buttom = html.Div([html.Div(
        'Выберите все данные автомобиля и нажмите расшифровать', style={'display':'inline-block','color': 'blue','padding': 10,'fontSize': 16}),
        html.Label('=========>', style={'display':'inline-block','padding': 10,'color': 'red'}),
        html.Button('Расшифровать', id='button-example-1',style={'color': 'green','padding': 10, 'display':'inline-block','fontSize': 16})
])

@app.callback(
    [Output('loading-demo', 'children'),
    Output('out', 'children')],
    [Input('button-example-1', 'n_clicks'),
    State('dropdown', 'value'),
    State('dropdown5', 'value'),
    Input('dropdown6', 'value'),
    State('dropdown7', 'value')]
)
def displayClick(n, marka, uzel, code, fmi):
    time.sleep(2)
    msg = ''
    if fmi == 'ALL':
        st = f'{marka} {uzel} {code}'
    else:
        st = f'{marka} {uzel} {code}-{fmi}'
        
    if "button-example-1" == ctx.triggered_id:
        # Проверка на пустые поля
        for pole in [uzel, code]:
            if pole == None:
                msg = "Заполнены не все поля!!!"
                break
            else:
                msg = poisk(marka, uzel, code, fmi)
             
    return f'Выбрана ошибка: {st}', msg
    
# Метки над полями 
text_div = html.Div([
    html.Label("Марка", style={'color': 'indigo', 'display':'inline-block','padding': 10, 'width': 150}),    
    html.Label("Модель", style={'color': 'indigo','display':'inline-block','padding': 10,'width': 100}),
    html.Label("Объём", style={'color': 'indigo','display':'inline-block','padding': 10,'width': 90}),
    html.Label("Год", style={'color': 'indigo','display':'inline-block','padding': 10,'width': 70}),
    html.Label("Узел ошибки", style={'color': 'indigo','display':'inline-block','padding': 10,'width': 150}),
    html.Label("Код", style={'color': 'indigo','display':'inline-block','padding': 10,'width': 75}),
    html.Label("FMI", style={'color': 'indigo','display':'inline-block','padding': 10,'width': 50})
])

# Форма вывода описание ошибки
out = html.Div([
    html.Form('Здесь будет текст', id = 'out', style={'display':'inline-block','color': 'indigo','fontSize': 17, 'padding': 10})
])

load = dcc.Loading([html.Div(id="loading-demo", style={'color': 'indigo','display':'inline-block','padding': 10})])

graph_to_display = dcc.Graph(id="scatter", figure=fig)

# Выполнение программы
app.layout = html.Div(children=[title, text_div, col, buttom, load, out])

if __name__ == '__main__':
   app.run_server(debug=True) # Run the Dash app
