import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import numpy as np

from datetime import datetime


word_heading = html.H2(children="Let us know what other efforts you'd like to see prioritized", className='lead text-center')
#word_title
#title and survey info 

title = dbc.Jumbotron(
    [
        dbc.Container(
            [
            html.Img(src='assets/foundcom-logo-ffce54.png'),
            html.H1("DEI Survey Results", className='display-3 text-center'),
            html.P(
            "The Diversity, Equity and Inclusion Committee created a survey to gather more information about your experience working at Foundation Communities. Your responses were important to us and helped us learn more about the racial biases, discriminatory practices and unconscious prejudices that affect staff of color and those who belong to marginalized groups within the agency. See below to explore survey results.",
            className='lead text-center')

            ]
            ,style={'textAlign': 'center'}
        )
    ]
)


wordcloud_col = dbc.Card([
    dbc.CardBody([
        dbc.Container([word_heading,
        html.Img(src='assets/word_cloud.png', style={'height':'75%', 'width':'75%'})
        ],style={'textAlign': 'center'})
    ])
])

def DEI_title():
    heading = title
    return heading

def wordcloud():
    figure = wordcloud_col
    return figure 

