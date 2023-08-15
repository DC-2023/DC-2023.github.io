#!/usr/bin/python3
import dash
#from dash import dcc, ctx
from dash import html

#dash.register_page(__name__)

layout = html.Div([
    html.Hr(style = {"color": "indigo"}),
    html.H2('!!!__ПРИВЕТ__!!!', style = {'color':'green'}),
    html.Hr(style = {"color": "indigo"}),
    ])
