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

dei_list = ['At work I am treated with respect.', 
            'At work, I feel comfortable being myself.', 
            'Diversity and inclusiveness issues are openly discussed.', 
            'Employees in my organization are treated with respect and dignity.', 
            'Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.',
            'I have the same opportunities for advancement as other team members at my organization with similar experience and performance levels.',
            'If I raised a concern about ethics and integrity, I am confident my employer would do what is right.',
            'My organization treasures diverse opinions and ideas.',
            'My team members appreciate my contributions.',
            'My supervisor tries to understand my point of view.',
            'My workplace is committed to building the strengths of each employee.']

word_heading = html.H2(children="Let us know what other efforts you'd like to see prioritized", className='lead text-center')
#word_title
#title and survey info 

logo = dbc.Card([
    dbc.CardBody([
        dbc.Row([html.Img(src='assets/foundcom-logo-ffce54.png', className='image-center'),
        ])
    ])
])

title = dbc.Jumbotron([
    dbc.Container([
        html.Img(src='assets/foundcom-logo-ffce54.png')
    ], style={'textAlign': 'center'}),
    dbc.Container([
            html.H1("DEI Survey Dashboard", className='display-3 text-center'),
            html.Br(),
            html.H4("Dashboard contributors: DeShan Allison, Bianca A. Hernandez, Michelle Le, Kenya Lewis, Stephanie Perrone, Julie Roebuck, Ebonie Trice, Mary Young and Tiffany Nicely-Williams", className='text-center'),
            html.Br(),
            html.H3("The Diversity, Equity and Inclusion (DEI) Survey Subcommittee created a survey to gather more information about your experience working at Foundation Communities. Your responses were important to us and helped us learn more about the racial biases, discriminatory practices and unconscious prejudices that affect staff of color and those who belong to marginalized groups within the agency.", className='text-justify')
            ])
    ])

about = dbc.Card([
    dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    html.H3("About the survey and its process"), 
                    html.H4("The DEI Survey Subcommitee gathered on __/__/__ to develop an all staff survey. It was relased on __/__/__ and participants had X # of days to complete the survey. The questions selected for the survey included general demographics (race, age, sexual orientation, tenure, etc.) and DEI specific questions (listed on the right). The DEI Survey Subcommitee wanted to answer the following questions:"),
                    html.H4("1) How does the distribution of demographics (race, age, sexual orientation, tenure and status) compare to the DEI specific responses?"),
                    html.H4("2) ")
                    
            ]),
                dbc.Col([
                    html.Ul(id='my-list', children=[html.Li(i) for i in dei_list], className= 'mb-10 lead text-left'),
                ])   
        ])
    ])
], color= "secondary", inverse=True)


figures_col = dbc.Card([
    dbc.CardBody([
        #html.H3("Explore results", className='display-3 text-left'),
        dbc.Row([
            dbc.Col([
                dbc.Container([
                    dbc.DropdownMenu( 
                        label="Explore the results",
                        bs_size="lg",
                        className="m-1",
                        children=[
                            dbc.DropdownMenuItem("At work I am treated with respect."),
                            dbc.DropdownMenuItem("At work, I feel comfortable being myself."),
                            dbc.DropdownMenuItem("Diversity and inclusiveness issues are openly discussed."),
                            dbc.DropdownMenuItem("Employees in my organization are treated with respect and dignity"),
                            dbc.DropdownMenuItem("Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance."),
                            dbc.DropdownMenuItem("I have the same opportunities for advancement as other team members at my organization with similar experience and performance levels."),
                            dbc.DropdownMenuItem("If I raised a concern about ethics and integrity, I am confident my employer would do what is right."),
                            dbc.DropdownMenuItem("My organization treasures diverse opinions and ideas."),
                            dbc.DropdownMenuItem("My team members appreciate my contributions."),
                            dbc.DropdownMenuItem("My supervisor tries to understand my point of view."),
                            dbc.DropdownMenuItem("My workplace is committed to building the strengths of each employee.")

    ],
)

                ],)
            ]),
            dbc.Col([
                dbc.Container([
                    #html.H4('Word cloud is a common technique used for visualizing frequent words in a text where the size of the text represents their frequency. The most frequent words in response to DEI Staff Survey question, "Other (please let us know what other efforts you would like to see prioritized) are shown in the Word Cloud on the left.')
                ])
            ])
        ])
    ])
])

def FC_logo():
    heading = logo
    return heading 

def DEI_title():
    heading = title
    return heading

def about_():
    heading = about
    return heading 

def figures():
    figure = figures_col
    return figure 

