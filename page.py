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

from figures import FC_fig1, FC_fig2, FC_fig3, FC_fig4, FC_fig5, FC_fig6, FC_fig7, FC_fig8, FC_fig9, FC_fig10, FC_fig11

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
            html.H1("FC DEI Survey Dashboard", className='display-3 text-center'),
            html.Br(),
            html.H6("Contributors: DeShan Allison, Bianca A. Hernandez, Michelle Le, Kenya Lewis, Stephanie Perrone, Julie Roebuck, Ebonie Trice, Mary Young and Tiffany Nicely-Williams", className='lead text-center', ),
            html.Br(),
            html.Br(),
        dbc.Row([
            html.Br(),
            html.Br(),
            html.H5("The Diversity, Equity and Inclusion (DEI) Survey team created a survey to gather more information about your experience working at Foundation Communities. We researched two surveys: 1) Gallup Diversity and Inclusion and 2) Building Movement Project Race to Lead. We decided to merge questions from both surveys to create the FC DEI Survey. The Gallup survey questions are more focused on individual experience while the Building Movement Project survey is more focused on the racial leadership gap in nonprofit organizations. Both are leaders in collecting data about diversity, equity and inclusion in the workplace. Your responses were important to us and helped us learn more about the racial biases, discriminatory practices and unconscious prejudices that affect staff of color and those who belong to marginalized groups within the agency.", className='text-justify', ),                                                                                                                                              
            
            ]),
        ], fluid=True), 
    ])     

about = dbc.Jumbotron([
        dbc.Container([
            dbc.Row([
                
                html.H5("The subcommittee gathered on __/__/__ to develop the all staff survey, it was relased on __/__/__ and participants had X # of days to complete it. Survey participants were asked to rank individual experience questions from 1 to 5 (1 = strongly disagree, 2 = disagree, 3 = neutral, 4 = agree, 5 = strongly agree). The team investigated 1) how the distribution of demographics compared to the individual expierence question responses, 2) to see if there were any correlations between individual experience question responses and 3) designed a wordcloud to analyze an open ended question.", className='text-justify', ),  
                      
            ]),
        ], fluid=True),
        #dbc.Container([
            #html.Ul(id='my-list', children=[html.Li(i) for i in dei_list], className= 'mb-10 lead text-left'),  
            #])
           
])

#descriptive stats cards 
card_content1 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H3("Card title", className="card-title"),
            html.H4(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content2 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H3("Card title", className="card-title"),
            html.H4(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content3 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H3("Card title", className="card-title"),
            html.H4(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content4 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H3("Card title", className="card-title"),
            html.H4(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content5 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H3("Card title", className="card-title"),
            html.H4(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
] 
card_content6 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H3("Card title", className="card-title"),
            html.H4(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content7 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H3("Card title", className="card-title"),
            html.H4(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
card_content8 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H3("Card title", className="card-title"),
            html.H4(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]),
]
descriptive_stats = dbc.Jumbotron([
    dbc.Container([
        html.Br(),
        dbc.Row([
            html.H3("Interesting findings", className='text-left', )
        ], ), 
        html.Br(),
        dbc.Row([  
            dbc.Col(
                dbc.Card(card_content1, color="primary", inverse=True)),
            dbc.Col(
                dbc.Card(card_content2, color="secondary", inverse=True)), 
            dbc.Col(
                dbc.Card(card_content3, color="success", inverse=True)),
            dbc.Col(
                dbc.Card(card_content4, color="dark", inverse=True)),
            ], className="mb-5", ),        
        dbc.Row([
            dbc.Col(
                dbc.Card(card_content5, color="warning", inverse=True)),
            dbc.Col(
                dbc.Card(card_content6, color="danger", inverse=True)),
            dbc.Col(
                dbc.Card(card_content7, color="info", inverse=True)),
            dbc.Col(
                dbc.Card(card_content8, color="light", inverse=True)),
            ], className="mb-5", ),
    ], fluid=True),
])
#figures row
demo_row = html.Div([
    html.Br(),
    dbc.Row([
        
        html.H3("Personal experience X demographics", className='lead text-center', ), 
          
            ]),
    html.Br()
    
])
#dropdown row


dropdown_row = html.Div([
    dbc.Row([
        dbc.Container([
            dcc.Dropdown(
            id='dei-dropdown', 
            value = 'item1',
            style={'backgroundColor': '#cdd3dc', 'maxWidth': '1460px'},
            options=[
                ({"label":"At work I am treated with respect.", "value":"item1"}),
                ({"label":"At work, I feel comfortable being myself.", "value":'item2'}),
                #dbc.DropdownMenuItem("Diversity and inclusiveness issues are openly discussed.", id='item3'),
                #dbc.DropdownMenuItem("Employees in my organization are treated with respect and dignity", id='item4'),
                #dbc.DropdownMenuItem("Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.", id='item5'),
                #dbc.DropdownMenuItem("I have the same opportunities for advancement as other team members at my organization with similar experience and performance levels.", id='item6'),
                #dbc.DropdownMenuItem("If I raised a concern about ethics and integrity, I am confident my employer would do what is right.", id='item7'),
                #dbc.DropdownMenuItem("My organization treasures diverse opinions and ideas.", id='item8'),
                #dbc.DropdownMenuItem("My team members appreciate my contributions.", id='item9'),
                #dbc.DropdownMenuItem("My supervisor tries to understand my point of view.", id='item10'),
                #dbc.DropdownMenuItem("My workplace is committed to building the strengths of each employee.", id='item11')
                    ]
                )

        ], className="mb-5"),
         
        
    ])
])

#output row
output_row=dbc.Jumbotron([
    dbc.Container([
        dbc.Row([
            html.Br(),
            html.H3("Individual experience X demographics", className='text-left', ),
            html.Br(),
        ]),
    html.Br(), 
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig1(),
                    id='plot1', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            }
                        ),
                                    
            ],
            align="start",
            style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'},  
            width={"sm": 12, "md": {"size": 4, "order": 1}, "lg":4},
            ),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.'),
                html.Br(),
                html.H4('Finding 1'),
                html.H4('Finding 2'),
                html.H4('Finding 3'),
                html.H4('Finding 4'),
            ],
            align="end",  
            width={"sm": 12, "md": {"size": 4, "order":1}, "lg":4},
            ),
        
        html.Br(),
        ]), 
        html.Br(), 
         dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig2(),
                    id='plot2', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            'autosizable':True,
                            'fillFrame':True 
                            }
                        )    
            ], 
                className='mb-8', 
                width={"sm": 12, "md": {"size": 6, "order": 2}, "lg": 4}),
            dbc.Col(width=1),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
            ], 
                align="center",
                className='mb-4', 
                width={"sm": 12, "md": {"size": 6, "order": 2}, "lg": 4}
            ),
            html.Br(),
        ]),  
        html.Br(), 
         dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig3(),
                    id='plot3', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            'autosizable':True,
                            'fillFrame':True 
                            }
                        )    
            ], width={"sm": 12, "md": {"size": 6, "order": 2}, "lg": 4}),
            dbc.Col(width=1),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
            ], className='text-left', width={"sm": 12, "md": {"size": 5, "order": 1}, "lg": 2}),
            html.Br(),
        ]), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                figure = FC_fig4(),
                id='plot4', 
                config={'displayModeBar': False}),
            ],md=8),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
                ],md=4),
            html.Br(),
        ],className='text-left'), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                figure = FC_fig5(),
                id='plot5', 
                config={'displayModeBar': False}),
            ],md=8),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
                ],md=4),
            html.Br(),
        ],className='text-left'), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                figure = FC_fig6(),
                id='plot6', 
                config={'displayModeBar': False}),
            ],md=8),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
                ],md=4),
            html.Br(),
        ],className='text-left'), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                figure = FC_fig7(),
                id='plot7', 
                config={'displayModeBar': False}),
            ],md=8),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
                ],md=4),
            html.Br(),
        ],className='text-left'), 
        html.Br(),  
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                figure = FC_fig8(),
                id='plot8', 
                config={'displayModeBar': False}),
            ],md=8),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
                ],md=4),
            html.Br(),
        ],className='text-left'), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                figure = FC_fig9(),
                id='plot9', 
                config={'displayModeBar': False}),
            ],md=8),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
                ],md=4),
            html.Br(),
        ],className='text-left'), 
        html.Br(), 
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                figure = FC_fig10(),
                id='plot10', 
                config={'displayModeBar': False}),
            ],md=8),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
                ],md=4),
            html.Br(),
        ],className='text-left'), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                figure = FC_fig11(),
                id='plot11', 
                config={'displayModeBar': False}),
            ],md=8),
            dbc.Col([
                html.H4('This is where we will add figure summaries focusing on what stood out.')
                ],md=4),
            html.Br(),
        ],className='text-left'), 
        html.Br(),      
    ], fluid=True), 
])            
            
wordcloud = dbc.Jumbotron([
    dbc.Container([
                    html.Img(
                        src='assets/final_word_cloud.png', 
                        style={'height': '100%','width': '100%'}, 
                        className='image-center')
                ])
            ])
                

def DEI_title():
    heading = title
    return heading

def about_():
    heading = about
    return heading 

def FC_stats():
    cards = descriptive_stats
    return cards 

def FC_demo_row():
    heading = demo_row
    return heading
def FC_dropdown_row():
    heading = dropdown_row
    return heading 

def FC_output():
    heading = output_row
    return heading

def FC_wordcloud():
    heading = wordcloud
    return heading 
