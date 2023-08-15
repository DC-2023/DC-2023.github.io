#!/usr/bin/python3

import dash
import dash_bootstrap_components as dbc
from dash import dcc, ctx
from dash import html, callback
from dash.dependencies import Input, Output, State
from SOScar import truck, uzel
import time
import os
import json
import re


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
                stroka = (f'{val}')
                rez = re.sub('[\'\"\[\]]', '', stroka)
    else:
        rez.append("ДАННОЙ ОШИБКИ НЕТ В БАЗЕ!!! Проверьте правильность вводимых данных!")
        #rez.append(
            #html.H5("ДАННОЙ ОШИБКИ НЕТ В БАЗЕ!!! Проверьте правильность вводимых данных!", style = {'display': 'flex','align-items': 'center', 'justify-content': 'center', 'height': '100%','background': 'lightblue', 'font': 'sans-serif', 'color': 'indigo', 'padding': 10}
            #), align = 'center'
        #)
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

cabina = dbc.Row([
    dbc.Row([
        dbc.Col(html.P('')),
        dbc.Col(
            html.P(''),
            style = {'background': 'orange'},
            width = 2,
            align = "end",
        ),
        dbc.Col(html.P('')),
    ]),
    dbc.Row([
        dbc.Col(html.P('')),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dbc.Row(
                        dbc.Col(
                            html.P(), style = {'background': 'orange', 'color': 'black'}
                        )
                    ),
                    dbc.Row([
                        dbc.Col(
                            html.Hr(), style = {'background': 'white', 'color': 'black'}, width = 4, align = "end"
                        ),
                        dbc.Col(
                            dbc.Row([
                                dbc.Col(
                                    html.H5('Поиск ошибок', style = {'display': 'flex','align-items': 'center', 'justify-content': 'center', 'height': '100%','background': 'lightblue', 'font': 'sans-serif', 'color': 'indigo', 'padding': 10},
                                    ), align = 'center'
                                ),
                            ])
                        ),
                        dbc.Col(
                            html.Hr(), style = {'background': 'white', 'color': 'black'}, width = 4, align = "end"
                        ),
                    ], style = {'background': 'orange'}
                    ),
                    dbc.Row([
                        dbc.Col(
                           dbc.CardLink("Применение", href="#") 
                        ),
                    ]),
                ]), color="warning", outline=True
            ), width = 9, style = {'background': 'orange', 'padding': 10}, align = 'end'
        ),
        dbc.Col(html.P(''))
    ])
], align = "end")

# Создание надписей и полей
bort = dbc.Row(
    dbc.CardGroup([
        dbc.Card(
            dbc.CardBody([
                html.H6('Марка'),
                dcc.Dropdown(options = [{'label': m, 'value': m} for m in marka()],
                    id = 'dropdown',
                    value = 'DAF',
                    style = {'display':'inline-block', 'width': 110}
                )
            ], style = {'background':'lightblue', 'border': 0})
        ),
        dbc.Card(
            dbc.CardBody([
                html.H6('Модель'),
                dcc.Dropdown(
                    id = 'dropdown2',
                    value = 'XF105',
                    style={'display':'inline-block', 'width': 100}
                ),
            ], style = {'background':'lightblue'})
        ),
        dbc.Card(
            dbc.CardBody([
                html.H6('Объем'),
                dcc.Dropdown(
                    id = 'dropdown3',
                    style={'display':'inline-block', 'width': 80}
                ),
            ], style = {'background':'lightblue'})
        ),
        dbc.Card(
            dbc.CardBody([
                html.H6('Год'),
                dcc.Dropdown(
                    year,
                    id = 'dropdown4',
                    value = '2000',
                    style={'display':'inline-block', 'width': 80}
                ),
            ], style = {'background':'lightblue'})
        ),
        dbc.Card(
            dbc.CardBody([
                html.H6('Узел'),
                dcc.Dropdown(
                    #value = 'ALL',
                    id = 'dropdown5',
                    style={'display':'inline-block', 'width': 110}
                ),
            ], style = {'background':'lightblue'})
        ),
        dbc.Card(
            dbc.CardBody([
                html.H6('Код'),
                dcc.Dropdown(
                    code,
                    value = 'ALL',
                    id = 'dropdown6',
                    style={'display':'inline-block', 'width': 75}
                ),
            ], style = {'background':'lightblue'})
        ),
        dbc.Card(
            dbc.CardBody([
                html.H6('FMI'),
                dcc.Dropdown(
                    fmi,
                    value = 'ALL',
                    id = 'dropdown7',
                    style={'display':'inline-block', 'width': 75}
                ),
            ], style = {'background':'lightblue'})
        ),
    ], style = {'background':'orange', 'padding': 10}) 
)

# Заполнение полей
@callback(
    Output('dropdown2', 'options'),
    [Input('dropdown', 'value')])
def set_options(val):
    return model(val)

@callback(
    Output('dropdown3', 'options'),
    [Input('dropdown2', 'value')])
def set_value(val):
    return automob(val)

@callback(
    Output('dropdown5', 'options'),
    [Input('dropdown', 'value')])
def set_uzel(val):
    return modul(val)

@callback(
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
                msg = html.Div("ЗАПОЛНЕНЫ НЕ ВСЕ ПОЛЯ!!!", style={'padding': 10, 'color': 'red'})
                break
            else:
                msg = poisk(marka, uzel, code, fmi)
             
    return dbc.Row([
        html.Hr(),
        dbc.Col(html.P('')
        ),
        dbc.Col(
            html.H5(f'Выбран код ошибки: {st}',
                style = {'display': 'flex','align-items': 'center', 'justify-content': 'center', 'height': '100%','background': 'lightblue', 'font': 'sans-serif', 'color': 'red', 'padding': 10}
            ), width = 6, align = 'center'
        ),
        dbc.Col(html.P('')
        ),
    ]), msg
    
# Чекбокс для выбора ручного ввода кода ошибки поле ввода и кнопка расшифровки
chek = dbc.Row([
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                dbc.Col(
                    html.H5('Выберите ручной ввод кода ошибки',
                        style = {'display': 'flex','align-items': 'center','justify-content': 'center', 'height': '100%', 'padding': 10},
                    ),
                    style = {'background': 'lightblue', 'color': 'indigo'},
                ),
                html.Br(),
                html.Br(),
                dcc.Checklist(options=[
                    {'label': ' Ручной режим', 'value': 'Ручной'}
                ], style={ 'color': 'yellow',}),
            ]), color = "dark"
        )
    ),
    dbc.Col(
        html.Div([
            html.Br(),
            dbc.Row([
                dbc.Row(
                    dbc.Col(html.P(''),
                        align = 'end',
                        style = {'background': 'black', 'color': 'indigo'}, width = {"size": 2, "offset": 6}
                    )
                ),
                dbc.Row(
                    dbc.Col(html.P(''),
                        align = 'end',
                        style = {'background': 'black', 'color': 'indigo'}, width={"size": 6, "offset": 4}
                    )
                ),
                dbc.Row(
                    dbc.Col(html.P(''),
                        align = 'end',
                        style = {'background': 'black', 'color': 'indigo'}, width={"size": 10, "offset": 2}
                    )
                )
            ]),
            dbc.Row([
                dbc.Col(html.Div(''), style = {'background': 'black'}, width = 3),
                dbc.Col(
                    dbc.Input(
                        placeholder = "Введите код ошибки",
                        type = 'text',
                        style = {'font': 'sans-serif', 'background': 'black', 'color': 'yellow', 'padding': 10},
                    ), style = {'background': 'black', 'align': 'center'}, width = 7
                ),
                dbc.Col(html.Div(''), style = {'background': 'black'}, width = 2),
            ], style = {'background': 'black', 'align': 'center'}
            ),
            dbc.Row([
                dbc.Row(
                    dbc.Col(html.P(''),
                        align = 'start',
                        style = {'background': 'black', 'color': 'indigo'}, width={"size": 10, "offset": 2}
                    )
                ),
                dbc.Row(
                    dbc.Col(html.P(''),
                        align = 'start',
                        style = {'background': 'black', 'color': 'indigo'}, width={"size": 6, "offset": 4}
                    )
                ),
                dbc.Row(
                    dbc.Col(html.P(''),
                        align = 'start',
                        style = {'background': 'black', 'color': 'indigo'}, width={"size": 2, "offset": 6}
                    )
                ),
            ]),
        ])
    ),
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                dbc.Col(
                    html.H5('Заполните все поля и нажмите кнопку',
                        style = {'display': 'flex','align-items': 'center','justify-content': 'center', 'height': '100%', 'padding': 10},
                    ), style = {'background': 'lightblue', 'color': 'indigo'}
                ),
                dbc.Row([
                    dbc.Col(html.P('')),
                    dbc.Col([
                        html.Hr(style = {"color": "black"}),
                        dbc.Button("Расшифровать", id = 'button-example-1', color = "success")
                    ]) 
                ])
            ]), color = "dark"
        )
    )
], style = {"background": "light"})
    
# Отображение загрузки
load = dcc.Loading([
    html.Div(
        id = "loading-demo",
        style = {'color': 'indigo', 'padding': 10}
    )
])

# Форма вывода описание ошибки
out = dbc.Row(
    dbc.CardGroup([
        dbc.Card(
            dbc.CardBody([
                dbc.Col(
                    html.H5('ОПИСАНИЕ: ', style = {'display': 'flex','align-items': 'center', 'justify-content': 'center', 'height': '100%','background': 'lightblue', 'font': 'sans-serif', 'color': 'green', 'padding': 10}
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        html.H5(id = 'out', style = {'display': 'flex','align-items': 'center', 'justify-content': 'center', 'height': '100%','background': 'lightblue', 'font': 'sans-serif', 'color': 'indigo', 'padding': 10}
                        )
                    )
                )
            ]), color = "warning", outline = True
        ),
        dbc.Card(
            dbc.CardBody([
                dbc.Col(
                    html.H5('ПРИЧИНА: ', style = {'display': 'flex','align-items': 'center', 'justify-content': 'center', 'height': '100%','background': 'lightblue', 'font': 'sans-serif', 'color': 'green', 'padding': 10}
                    )
                ),
                dbc.Row(
                    dbc.Col(
                        html.H5(id = 'pricina', style = {'display': 'flex','align-items': 'center', 'justify-content': 'center', 'height': '100%','background': 'lightblue', 'font': 'sans-serif', 'color': 'indigo', 'padding': 10}
                        )
                    )
                )
            ]), color = "warning", outline = True
        ),
    ], style = {'background':'orange'})
)

autobot = dbc.Row([
    dbc.Col(
        html.Hr(), style = {'background': 'lightblue', 'color': 'black'}, width = 3, align = "end"
    ),
    dbc.Col(
        dbc.Row([
            dbc.Col(
                html.H4('AUTOBOT', style = {'display': 'flex','align-items': 'center', 'justify-content': 'center', 'height': '100%','background': 'lightblue', 'font': 'sans-serif', 'color': 'indigo', 'padding': 10},
                ), align = 'center'
            ),
        ])
    ),
    dbc.Col(
        html.Hr(), style = {'background': 'lightblue', 'color': 'black'}, width = 3, align = "end"
    ),
], style = {'background': 'orange'})

# Прорисовка фар
fary = dbc.Row([
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                dbc.CardGroup([
                    dbc.Card(
                        dbc.CardBody([
                            html.P(''),
                        ]),
                        color = "warning"
                    ),
                    dbc.Card(
                        dbc.CardBody([
                            html.P(''),
                        ]),
                        color = "danger"
                    ),
                    dbc.Card(
                        dbc.CardBody([
                            html.P(''),
                        ]),
                        color = "light"
                    ),
                    dbc.Card(
                        dbc.CardBody([
                            html.P(''),
                        ]),
                        color = "danger"
                    ),
                ])
            ], style = {'background': 'black'})
        ), width = {"size": 3, "order": "first"}
    ),
    dbc.Col(html.P("")),
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                dbc.CardGroup([
                    dbc.Card(
                        dbc.CardBody([
                            html.P(''),
                        ]),
                        color = "danger"
                    ),
                    dbc.Card(
                        dbc.CardBody([
                            html.P(''),
                        ]),
                        color = "light"
                    ),
                    dbc.Card(
                        dbc.CardBody([
                            html.P(''),
                        ]),
                        color = "danger"
                    ),
                    dbc.Card(
                        dbc.CardBody([
                            html.P(''),
                        ]),
                        color = "warning"
                    ),
                ])
            ], style = {'background': 'black'})
        ), width = {"size": 3, "order": "last"}
    ),
], style = {'background': 'black'})

# Прорисовка шин
chiny = dbc.Row([
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.P('')
            ], style = {'background': 'black'}
            ), #style = {'width': '280px'}
        ), width = {"size": 2, "order": "first"}
    ),
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.P('')
            ], style = {'background': 'black'}
            ), #style = {'width': '280px'}
        ), width = {"size": 2}
    ),
    dbc.Col(html.P("")),
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.P('')
            ], style = {'background': 'black'}
            ), #style = {'width': '280px'}
        ), width = {"size": 2}
    ),
    dbc.Col(
        dbc.Card(
            dbc.CardBody([
                html.P('')
            ], style = {'background': 'black'}
            ), #style = {'width': '280px'}
        ), width = {"size": 2, "order": "last"}
    ),
], justify = "around")

layout = dbc.Container([
    cabina,
    bort,
    autobot,
    fary,
    chek,
    chiny,
    load, out], fluid = True)
   
