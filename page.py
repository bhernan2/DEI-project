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
            html.H4("Dashboard contributors: DeShan Allison, Bianca A. Hernandez, Michelle Le, Kenya Lewis, Stephanie Perrone, Julie Roebuck, Ebonie Trice, Mary Young and Tiffany Nicely-Williams")
            ]
            ,style={'textAlign': 'center'}
        )
    ]
)

about = dbc.Card([
    dbc.CardBody([
        html.H4(
            "The Diversity, Equity and Inclusion Committee created a survey to gather more information about your experience working at Foundation Communities. Your responses were important to us and helped us learn more about the racial biases, discriminatory practices and unconscious prejudices that affect staff of color and those who belong to marginalized groups within the agency. See below to explore survey results."
           ),
        

    ])
])

wordcloud_col = dbc.Card([
    dbc.CardBody([
        html.H3("Word Cloud Analysis", className='display-3 text-center'),
        dbc.Row([
            dbc.Col([
                dbc.Container([
                html.Img(src='assets/word_cloud3.png', style={'height':'75%', 'width':'75%'})
                ],style={'textAlign': 'center'})
            ]),
            dbc.Col([
                dbc.Container([
                    html.H4('Word cloud is a common technique used for visualizing frequent words in a text where the size of the text represents their frequency. The most frequent words in response to DEI Staff Survey question, "Other (please let us know what other efforts you would like to see prioritized) are shown in the Word Cloud on the left.')
                ])
            ])
        ])
    ])
])

def DEI_title():
    heading = title
    return heading

def about_():
    heading = about
    return heading 

def wordcloud():
    figure = wordcloud_col
    return figure 

