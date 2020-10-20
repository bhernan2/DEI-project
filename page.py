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

from figures import FC_fig1

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

title = dbc.Jumbotron([
    dbc.Container([
        html.Img(src='assets/foundcom-logo-ffce54.png')
    ], style={'textAlign': 'center'}),
    dbc.Container([
            html.H1("DEI Survey Dashboard", className='display-3 text-center'),
            html.Br(),
            html.H4("Dashboard contributors: DeShan Allison, Bianca A. Hernandez, Michelle Le, Kenya Lewis, Stephanie Perrone, Julie Roebuck, Ebonie Trice, Mary Young and Tiffany Nicely-Williams", className='text-center'),
            html.Br(),
            html.Br(),
            dbc.Row([
                        html.Br(),
                        html.Br(),
                        html.H3("The Diversity, Equity and Inclusion (DEI) Survey team created a survey to gather more information about your experience working at Foundation Communities. We researched both Gallup Diversity and Inclusion and Building Movement Project Race to Lead surveys and decided to merge them together to make up the FC DEI survey. The Gallup survey questions are more focused on individual experience while the Building Movement Project survey is more focused on the racial leadership gap in nonprofit organizations. Both are leaders in collecting data about diversity, equity and inclusion in the workplace. Your responses were important to us and helped us learn more about the racial biases, discriminatory practices and unconscious prejudices that affect staff of color and those who belong to marginalized groups within the agency.", className='mb-75'),                                                                                                                                            
                    ]), 
    ], style={'textAlign': 'justify'})    
])
about = dbc.Jumbotron([
        dbc.Container([
            html.H3("The subcommittee gathered on __/__/__ to develop the all staff survey and it was relased on __/__/__. Participants had X # of days to complete the survey. The team investigated 1) how the distribution of demographics compared to the DEI specific responses, 2) to see if there were any correlations between DEI related question responses and 3) design a wordcloud to address the open ended question mentioned earlier.", className='text-justify'),
        ]),
        #dbc.Container([
            #html.Ul(id='my-list', children=[html.Li(i) for i in dei_list], className= 'mb-10 lead text-left'),  
            #])
           
])

#descriptive stats cards 
card_content1 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("Card title", className="card-title"),
            html.H3(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content2 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("Card title", className="card-title"),
            html.H3(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content3 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("Card title", className="card-title"),
            html.H3(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content4 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("Card title", className="card-title"),
            html.H3(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content5 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("Card title", className="card-title"),
            html.H3(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content6 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("Card title", className="card-title"),
            html.H3(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content7 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("Card title", className="card-title"),
            html.H3(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content8 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("Card title", className="card-title"),
            html.H3(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
descriptive_stats = html.Div([
            dbc.Row([
                dbc.Col(
                    dbc.Card(card_content1, color="primary", inverse=True)),
                dbc.Col(
                    dbc.Card(card_content2, color="secondary", inverse=True)), 
                dbc.Col(
                    dbc.Card(card_content3, color="success", inverse=True)),
                dbc.Col(
                    dbc.Card(card_content4, color="dark", inverse=True)),
            ], className="mb-5"),
            
            dbc.Row([
                dbc.Col(
                    dbc.Card(card_content5, color="warning", inverse=True)),
                dbc.Col(
                    dbc.Card(card_content6, color="danger", inverse=True)),
                dbc.Col(
                    dbc.Card(card_content7, color="info", inverse=True)),
                dbc.Col(
                    dbc.Card(card_content8, color="light", inverse=True))
                ], className="mb-5")          
            ])
#figures row
figures_col = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Container([
                dbc.DropdownMenu( 
                    label="Compare DEI related questions to demographics",
                    bs_size="lg",
                    className="m-2 'text-justify",
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
                        ]
                    )
                    ], 'text-align', className='text-center'),
       dcc.Graph(
                id='fig1-viz',
                figure=FC_fig1(),
                className='container', style={'maxWidth': '1200px'}
                ),  
        ]),
        html.Br(),      
    ])
])

wordcloud = dbc.Jumbotron([
    dbc.Container([
                    html.Img(src='assets/final_word_cloud.png', style={'height': '100%','width': '100%'}, className='image-center')
                ])
            ])
                

def DEI_title():
    heading = title
    return heading

def about_():
    heading = about
    return heading 
#def FC_introduction():
    #heading = introduction
    #return heading 

def FC_stats():
    heading = descriptive_stats
    return heading 

def FC_figures():
    figure = figures_col
    return figure 

def FC_wordcloud():
    heading = wordcloud
    return heading 

