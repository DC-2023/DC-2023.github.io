#!/usr/bin/python3

import dash
import dash_bootstrap_components as dbc
from dash import dcc, ctx
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
#from Pages import onas, sos, grafiki, kontakt, magazin, razborka
from Pages import onas, sos, magazin

# Create the app
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

app.config.suppress_callback_exceptions = True

server = app.server

# Создание sidebara
sidebar = dbc.Row([
    dbc.Col([
        #dbc.Container([
            #html.Div([
                #html.H2("SOSCARS", style = {'textAlign':'left', "color": "white"}),
                #html.Label('online', style = {'textAlign':'center'}),
                #html.Hr(style = {"color": "white"}),
            #]),
        #]),
        dcc.Location(id="url", refresh=False),
        html.Div([
            html.H2("SOSCARS", style = {'textAlign':'left', "color": "white"}),
            #html.Label('online', style = {'textAlign':'center'}),
            html.Hr(style = {"color": "white"}),
            dbc.Nav(id = 'demo',  children = [          
                dbc.NavLink('О Проекте', href = '/Pages/onas', active = 'exact'),
                dbc.NavLink('Поиск Ошибок', href = '/Pages/sos', active = 'exact'),
                dbc.NavLink('Поиск СТО', href = '/Pages/sto', active = 'exact'),
                dbc.NavLink('Поиск Магазинов', href = '/Pages/magazin', active = 'exact'),
                dbc.NavLink('Поиск Разборок', href = '/Pages/razborka', active = 'exact'), 
                html.Div([
                    html.Br(),
                    html.H5("Дополнительно", style = {'textAlign':'left', "color": "white"}),
                    html.Hr(style = {"color": "white"}),
                ]),
                dbc.NavLink('Найти Заправку', href = '/Pages/zapravka', active = 'exact'),
                dbc.NavLink('Найти Кафе', href = '/Pages/kafe', active = 'exact'),
                dbc.NavLink('PDF_TO_MP3', href = '/Pages/pdf_to_mp3', active = 'exact'),
                dbc.NavLink('ГРАФИКИ', href = '/Pages/grafiki', active = 'exact'),
                dbc.NavLink('Литература', href = '/Pages/liter', active = 'exact'),
                html.Div([
                    html.Br(),
                    html.H5("О Нас", style = {'textAlign':'left', "color": "white"}),
                    html.Hr(style = {"color": "white"}),
                ]),
                dbc.NavLink('Контакты', href = '/Pages/kontakt', active = 'exact'),
            ], vertical = True, pills = True),
        ]),
    ], width = 2, className = 'sidebar'),
    dbc.Col(
        html.Div(children=[],
            id="page-content",  
            className = 'content',
        ), width={"size": 9, "offset": 2},
    ),
])


#content = html.Div(id="page-content", children=[], style={'display':'inline-block'})

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def pagecontent(pathname):

    if pathname == '/Pages/onas':
        return onas.layout
        
    if pathname == '/Pages/sos':
        return sos.layout
        
    if pathname == '/Pages/magazin':
        return magazin.layout

#app.layout = html.Div(children=[sidebar])
#app.layout = dbc.Container([sidebar, content])
app.layout = dbc.Container(sidebar, fluid = True)

if __name__ == '__main__':
   app.run_server(debug=True)
   
