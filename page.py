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
            html.H5('The Diversity, Equity and Inclusion (DEI) Survey team created a survey to gather more information about your experience working at Foundation Communities. We researched two surveys: 1) Gallup Diversity and Inclusion and 2) <a href="https://racetolead.org/the-survey/">Building Movement Project Race to Lead.</a> We decided to merge questions from both surveys to create the FC DEI Survey. The Gallup survey questions are more focused on individual experience while the Building Movement Project survey is more focused on the racial leadership gap in nonprofit organizations. Both are leaders in collecting data about diversity, equity and inclusion in the workplace. Your responses were important to us and helped us learn more about the racial biases, discriminatory practices and unconscious prejudices that affect staff of color and those who belong to marginalized groups within the agency.', className='text-justify', ),                                                                                                                                              
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
    html.H3([
        dbc.CardHeader([
            ("My organization treasurese diverse opinions and ideas."),
        ], style={"display": "flex"})
    ]),
    dbc.CardBody([
            html.H1("34%", className="card-title"),
            html.H4([
                'of LGBTQ+ staff members either strongly disagree or disagree.',
                ],className="card-text"),
            html.Br(),
            html.H1("25%", className="card-title"),
            html.H4([
                'of employees who have been employeed between 1-10 years disagree or strongly disagree.',
                ],className="card-text"),
        
        ]),
]
card_content2 = [
    #dbc.CardHeader("Descriptive Stats"),
    html.H3([
        dbc.CardHeader("Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.")
    ],style={"display": "flex"}),
    dbc.CardBody([
            html.H1("54%", className="card-title"),
            html.H4(
                "of Black/African American identifying staff disagree or strongly disagree.",
                className="card-text",),
        ]),
]
card_content3 = [
    html.H3([
        dbc.CardHeader(" I have the same opportunities for advancement as other team members similar experience and performance levels.")
    ],style={"display": "flex"}),
    dbc.CardBody([
            html.H1("65%", className="card-title"),
            html.H4(
                "of Black/African American identifying staff disagree or strongly disagree.",
                className="card-text",),
            html.Br(),
            html.H1("27%", className="card-title"),
            html.H4(
                "of LGBTQ+ identigying staff disagree or strongly disagree.",
                className="card-text",),
        ]),
]
card_content4 = [
    html.H3([
        dbc.CardHeader([
            ("Diversity and inclusiveness issues are openly discussed at my organization."),
            ], style={"display": "flex"})
    ]),
    dbc.CardBody([
            html.H1("100%", className="card-title"),
            html.H4(
                "of Native American identifying staff disagree or strongly disagree."),
            html.Br(),
            html.H1("50%", className="card-title"),
            html.H4(
                "of Black/African American identifying staff disagree or strongly disagree.", 
                className="card-text",),
                
        ]),
]
card_content5 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H1("No. 1", className="card-title"),
            html.H4(
                "Address ways that racial inequity/systemic bias impact issues the organization works on and hold senior team members accountable for anti-racists actions",
                className="card-text",),
        ]),
] 
card_content6 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H1("No. 2", className="card-title"),
            html.H4(
                "Increase diverse representation on board and advisory committees",
                className="card-text",),
        ]),
]
card_content7 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H1("No. 3", className="card-title"),
            html.H4(
                "Provide training for staff, leadership, and board",
                className="card-text",),
        ]),
]
card_content8 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H1("No. 4", className="card-title"),
            html.H4(
                "Develop recruitment and hiring protocols and strategies that include implicit bias testing for managers and supervisors",
                className="card-text",),
        ]),
]
descriptive_stats = dbc.Jumbotron([
    dbc.Container([
        html.Br(),
        dbc.Row([
            html.H2("Interesting findings", className='text-left', )
        ]), 
        html.Br(),
        dbc.Row([
            dbc.CardDeck([ 
                dbc.Col(
                    dbc.Card(card_content1, color="primary", inverse=True), style={"display": "flex"}, width=6),
                dbc.Col(
                    dbc.Card(card_content2, color="secondary", inverse=True), style={"display": "flex"}, width=6), 
            ]),
        ], className="mb-5"),
        dbc.Row([
            dbc.CardDeck([
            dbc.Col(
                dbc.Card(card_content3, color="dark", inverse=True), style={"display": "flex"}, width=6),
            dbc.Col(
                dbc.Card(card_content4, color="success", inverse=True), style={"display": "flex"}, width=6),
            ]),
            ], className="mb-5"), 
        dbc.Row([
            html.H2("DEI efforts that FC staff would like to see prioritized", className='text-left', )
        ]), 
        html.Br(),       
        dbc.Row([
            dbc.CardDeck([
            dbc.Col(
                dbc.Card(card_content5, color="warning", inverse=True),style={"display": "flex"},width=3),
            dbc.Col(
                dbc.Card(card_content6, color="danger", inverse=True),style={"display": "flex"},width=3),
            dbc.Col(
                dbc.Card(card_content7, color="info", inverse=True),style={"display": "flex"},width=3),
            dbc.Col(
                dbc.Card(card_content8, color="light", inverse=True),style={"display": "flex"},width=3),
            ]),
            ], className="mb-5"),
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
            html.H3("Individual experience X demographics", className='text-center', ),
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
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
            dbc.Col([
                html.H4('This is where we will add figure summary.'),
            ]),
        ],align="center"), 
        html.Br(), 
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig2(),
                    id='plot2', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
            dbc.Col([
                html.H5([
                    html.Li('77% of FC staff agree or strongly agree that they feel comforable being themselves at work.'),

                ]),
            ]),
        ],align="center"), 
        html.Br(), 
         dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig3(),
                    id='plot3', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
            dbc.Col([
                html.H4('This is where we will add figure summary.'),
            ]),
        ],align="center"), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig4(),
                    id='plot4', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 8, "order": 1}, "lg":4},),
            dbc.Col([
                html.H4('This is where we will add figure summary.'),
            ]),
        ],align="center"), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig5(),
                    id='plot5', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
            dbc.Col([
                html.H4('This is where we will add figure summary.'),
            ]),
        ],align="center"), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig6(),
                    id='plot6', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
            dbc.Col([
                html.H4('This is where we will add figure summary.'),
            ]),
        ],align="center"), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig7(),
                    id='plot7', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
            dbc.Col([
                html.H4('This is where we will add figure summary.'),
            ]),
        ],align="center"), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig8(),
                    id='plot8', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":6},),
            dbc.Col([
                html.P([
                    html.Ul([
                        html.Li('22% of total respondents strongly disagree or disagree, 25% are neutral and 53% agree and strongly agree.'),
                        html.Li('FC staff who identify as Latino/Hispanic, Black/African American and Native American strongly disagree or disagree (25, 33 and 50%, respectively).'),
                        html.Li('Younger (18-24) and older (65-74) staff generally agree or sttronly agree.'),
                        html.Li('Nearly 25% of staff in the 25-34 and 35-44 age ranges disagree or strongly disagree.')
                    ]),
                ]),
            ]),
            ],align="center"), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig9(),
                    id='plot9', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
            dbc.Col([
                html.H4('This is where we will add figure summary.'),
            ]),
        ],align="center"), 
        html.Br(), 
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig10(),
                    id='plot10', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
            dbc.Col([
                html.H4('This is where we will add figure summary.'),
            ]),
        ],align="center"), 
        html.Br(),
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    figure = FC_fig11(),
                    id='plot11', 
                    config={
                            'displayModeBar': False, 
                            'responsive': True, 
                            #'autosizable':True,
                            #'fillFrame':True 
                            },
                    style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'}),                      
            ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
            dbc.Col([
                html.H4('This is where we will add figure summary.'),
            ]),
        ],align="center"), 
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
