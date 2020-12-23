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

#title and survey info 
title = dbc.Jumbotron([
    dbc.Container([
        html.Img(src='assets/foundcom-logo-ffce54.png')
        ], style={'textAlign': 'center'}),
    dbc.Container([
            html.H1("FC DEI Survey Dashboard", className='display-3 text-center'),
            html.Br(),
            # html.H6("Contributors: DeShan Allison, Bianca A. Hernandez, Michelle Le, Kenya Lewis, Stephanie Perrone, Julie Roebuck, Ebonie Trice, Mary Young and Tiffany Nicely-Williams", className='lead text-center', ),
            html.Br(),
            html.Br(),
        dbc.Row([
            html.Br(),
            html.Br(),
            html.H5('The Diversity, Equity and Inclusion (DEI) Survey team created a survey to gather more information about your experience working at Foundation Communities. We researched two surveys: 1) Gallup Diversity and Inclusion and 2) Building Movement Project Race to Lead. We decided to merge questions from both surveys to create the FC DEI Survey. The Gallup survey questions are more focused on individual experience while the Building Movement Project survey is more focused on the racial leadership gap in nonprofit organizations. Both are leaders in collecting data about diversity, equity and inclusion in the workplace. Your responses were important to us and helped us learn more about the racial biases, discriminatory practices and unconscious prejudices that affect staff of color and those who belong to marginalized groups within the agency.', className='text-justify', ),                                                                                                                                              
            ]),
        ], fluid=True), 
    ])
#how to video jumbo
video = dbc.Jumbotron([
        dbc.Container([
            dbc.Row([
            html.H3("Dashboard how-to", className='text-left', ),
            ]),
            html.Br(),
            dbc.Row([
                html.H5("Space for video"),
                html.Video(title="Dashboard how-to", src="", width=4),  
            ]),
        ], fluid=True),       
    ])    

#big pic jumbo
big_picture = dbc.Jumbotron([
        dbc.Container([
            dbc.Row([
                html.H3("Big picture", className='text-left', ),   
            ]),
            html.Br(),
            dbc.Row([
                html.H5("Include big picture figure: interactive pie chart")
            ])
        ], fluid=True),      
    ])

# about jumbo
about = dbc.Jumbotron([
        dbc.Container([
            dbc.Row([
                html.H5("The subcommittee gathered on __/__/__ to develop the all staff survey, it was relased on __/__/__ and participants had X # of days to complete it. Survey participants were asked to rank individual experience questions from 1 to 5 (1 = strongly disagree, 2 = disagree, 3 = neutral, 4 = agree, 5 = strongly agree). The team investigated 1) how the distribution of demographics compared to the individual expierence question responses, 2) to see if there were any correlations between individual experience question responses and 3) designed a wordcloud to analyze an open ended question.", className='text-justify', ),   
            ]),
        ], fluid=True),
    ])

# top 3 priorities card definitions
card_content5 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("No.1", className="card-title"),
            dbc.Button(html.Img(src="assets/icons8-survey-80.png"), id='popover-target1', color='light', size='sm',),
            dbc.Popover([
            dbc.PopoverHeader("135 responses", className="pop-header"),
            dbc.PopoverBody("Address ways that racial inequity/systemic bias impact issues the organization works on and hold senior team members accountable for anti-racists actions.", className="pop-body")
        ], 
        id="popover1",
        is_open=False,
        target="popover-target1",
        placement="bottom"
        )
        ]),
] 
card_content6 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
        html.H2("No.2", className="card-title"),
        dbc.Button(html.Img(src="assets/icons8-survey-80.png"), id='popover-target2', color='light', size='sm',),
        dbc.Popover([
            dbc.PopoverHeader("122 responses", className="pop-header"),
            dbc.PopoverBody("Provide training for staff, leadership and board.", className="pop-body")
        ], 
        id="popover2",
        is_open=False,
        target="popover-target2",
        placement="bottom"
        )
        ]),
]
card_content7 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
        html.H2("No.3", className="card-title"),
        dbc.Button(html.Img(src="assets/icons8-survey-80.png"), id='popover-target3', color='light', size="sm",),
        dbc.Popover([
            dbc.PopoverHeader("90 responses", className="pop-header"),
            dbc.PopoverBody("Increase diverse representation on board and advisory committees.", className="pop-body")
        ], 
        id="popover3",
        is_open=False,
        target="popover-target3",
        placement="bottom"
        )
        ]),
]

#key findings jumbo
key_findings1 = dbc.Jumbotron([
    html.Br(),
        dbc.Row([
            dbc.Col(width=1),
            dbc.Col(html.H3("Key findings",))
        ]), 
    html.Br(),
    dbc.Container([
            dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("My supervisor tries to understand my point of view."),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                dbc.CardImg(src="/assets/icons8-group-task-80.png", style={"width":"25%"}),
                                ])
                            ], className="flip-card-front", color="light", inverse=True, style={"display": "flex"}),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("81%"),
                                html.P('of all staff members'),
                                html.Br(),
                                html.H4('agree + strongly agree')
                                ]),
                            ],className="flip-card-back", color="warning", inverse=True,)
                    ],className="flip-card-inner",), 
                ],className="flip-card"),
            dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                #dbc.CardImg(src="/assets/icons8-handshake-80.png", alt="Avatar", style={"width":"25%"}),
                                html.H4("At work I am treated with respect."),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                dbc.CardImg(src="/assets/icons8-high-five-80.png", style={"width":"25%"}),

                                ]),
                            ], className="flip-card-front", color="light", inverse=True,),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("88%"),
                                html.P('of all staff survey particapnts'),
                                html.Br(),
                                html.H4('agree + strongly agree'),
                                html.Br(),
                                ]), 
                            ],className="flip-card-back", color="warning", inverse=True,)
                    ],className="flip-card-inner",),
            
                ],className="flip-card"),
            dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("My organization treasures diverse opinions and ideas."),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                dbc.CardImg(src="/assets/icons8-learning-80.png", alt="Avatar", style={"width":"25%"}),
                                ]),
                            ], className="flip-card-front", color="light", inverse=True,),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("34%"), 
                                html.P('of LGBTQ+ and'),
                                html.Br(),
                                html.H4("25%"), 
                                html.P('employees who have been employeed between 1-10 years'),
                                html.H4('disagree + strongly disagree')
                                ]),
                            ],className="flip-card-back", color="warning", inverse=True,)
                    ],className="flip-card-inner",),
                ],className="flip-card"),
            dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance."),
                                dbc.CardImg(src="/assets/icons8-handshake-80.png", alt="Avatar", style={"width":"25%"}),
                                ]),
                            ], className="flip-card-front", color="light", inverse=True,),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("54%"), 
                                html.P('of Black/African American identifying staff and'),
                                html.Br(),
                                html.H4("45%"), 
                                html.P('of employees who have worked for one year'),
                                html.H4('disagree + strongly disagree'),
                                ]),
                            ],className="flip-card-back", color="warning", inverse=True,)
                    ],className="flip-card-inner",align="center",),
                ],className="flip-card", align="center"),
            dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                #dbc.CardImg(src="/assets/icons8-handshake-80.png", alt="Avatar", style={"width":"25%"}),
                                html.H4("I have the same opportunities for advancement as other team members with similar experience and performance levels"),
                                html.Br(),
                                dbc.CardImg(src="/assets/icons8-circled-up-right-80.png", alt="Avatar", style={"width":"25%"}),
                                ]),
                            ], className="flip-card-front", color="light", inverse=True,),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("63%"), 
                                html.P('of Black/African American identifying staff and'),
                                html.Br(),
                                html.H4("27%"), 
                                html.P('of LGBTQ+ employees'),
                                html.H4('disagree + strongly disagree'),
                                ]),
                            ],className="flip-card-back", color="warning", inverse=True,)
                    ],className="flip-card-inner",align="center",),
                ],className="flip-card", align="center"),

            dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                #dbc.CardImg(src="/assets/icons8-handshake-80.png", alt="Avatar", style={"width":"25%"}),
                                html.H4("Diversity and inclusiveness are openly discussed at my organization"),
                                html.Br(),
                                html.Br(),
                                dbc.CardImg(src="/assets/icons8-meeting-room-80.png", alt="Avatar", style={"width":"25%"}),
                                ]),
                            ], className="flip-card-front", color="light", inverse=True,),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("50%"), 
                                html.P('of Black/African American identifying staff'),
                                html.H4('disagree + strongly disagree'),
                                ]),
                            ],className="flip-card-back", color="warning", inverse=True,)
                    ],className="flip-card-inner",align="center",),
                ],className="flip-card", align="center"),

            ], className="cards", fluid=True, style={'textAlign': 'center'}),
], fluid=True)

#top 3 priorities jumbo
priorities = dbc.Jumbotron([
    dbc.Container([
        html.Br(),
        dbc.Row([
            dbc.Col(width=1),
            html.H3("Top DEI efforts that FC staff would like to see prioritized", className='text-left', )
        ], justify="left"), 
        html.Br(),       
        dbc.Row([

            dbc.Col(
                dbc.Card(card_content5, color="light", inverse=True), width=3),
            
            dbc.Col(
                dbc.Card(card_content6, color="light", inverse=True), width=3),
            dbc.Col(
                dbc.Card(card_content7, color="light", inverse=True), width=3),
            ], justify="center"), 
    ], fluid=True, style={'textAlign': 'center'}),
])

#dropdown jumbo
dropdown_row = html.Div([
    dbc.Jumbotron([
    dbc.Container([
            dbc.Row([
                html.Br(),
                html.H3("Demographics X individual experience", className='text-center', ),
                html.Br(),
        ]),
            dbc.Row([
                html.P('*Total of totals shows when app first downloads. Select a category (total responses, race, age, etc.) to further explore the data.'),
            ]),
            dbc.Row([
                html.P('*All figures are interactive! Hover over bars to see individual exerience ranking counts or select individual subcategories from the legend.'),
            ]),
                html.Br(),
            dbc.Row([
                dbc.Col([
                dcc.Dropdown(
                    id='dei-dropdown', 
                    clearable=False,
                    style={'backgroundColor': '#cdd3dc', 'color':'black', 'width': '100%'},
                    options=[
                        {'label': 'At work, I am treated with respect.', 'value': 'plot1-info'},
                        {'label': 'At work, I feel comfortable being myself.', 'value': 'plot2-info'},
                        {'label': 'Employees in my organization are treated with respect and dignity.', 'value': 'plot3-info'},
                        {'label': 'Diversity and inclusiveness issues are openly discussed.', 'value': 'plot4-info'},
                        {'label': 'Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.', 'value': 'plot5-info'},
                        {'label': 'I have the same opportunities for advancement as other team members at my organization with similar experience and performance levels.', 'value': 'plot6-info'},
                        {'label': 'If I raised a concern about ethics and integrity, I am confident my employer would do what is right.', 'value': 'plot7-info'},
                        {'label': 'My organization treasures diverse opinions and ideas.', 'value': 'plot8-info'},
                        {'label': 'My team members appreciate my contributions.', 'value': 'plot9-info'},
                        {'label': 'My supervisor tries to understand my point of view.', 'value': 'plot10-info'},
                        {'label': 'My workplace is committed to building the strengths of each employee.', 'value': 'plot11-info'},        
                        ],
                    placeholder='Select a question'
                )
                ]),
            ], className="mb-5"),
            dbc.Row(id='dd-output-container'),
            html.Br(),
        ], fluid=True),
    ]),
])

#wordlcoud jumbo
wordcloud = dbc.Jumbotron([
    dbc.Container([
        html.Br(),
        dbc.Row([
            dbc.Col(width=1),
            html.H3("Other efforts staff would like to see prioritized",)
        ], justify="left"), 
        html.Br(),
        dbc.Row([
            dbc.Col(width=2),
            dbc.Col([
                dbc.Card([ 
                    dbc.CardBody([
                        html.H5("A word cloud is a collection of words depicted in different sizes. The bigger and bolder the word appears, the more often it is mentioned within a given text and the more important it is. This is an ideal way to pull the most pertinent parts of textual data and helps users compare and contrast pieces of text. Click open to see our wordcloud analysis for the open ended question of the survey."),
                        dbc.Button(html.Img(src="assets/icons8-open-sign-80.png"), id='open-centered', color='light', size='md',),
                        ]),
                    ], color="light"),
                    ], width=8),
            dbc.Col(width=2),     
        dbc.Row([
            dbc.Modal([
                dbc.ModalHeader("Wordcloud"),
                dbc.ModalBody([
                    dbc.Card([
                    dbc.CardImg(src='assets/word_cloud7.png'),
                    dbc.CardBody([
                        ]),
                    ]),
                ]),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-centered", className="ml-auto", size="lg")
                ),
            ],
            id="modal-centered",
            centered=True,
            size="xl",
            ),
        ]),
        ], justify="center"),     
    ], fluid=True, style={'textAlign': 'center'}),
])

contributors = dbc.Jumbotron([
    dbc.Container([
        html.Br(),
        dbc.Row(html.H5("Meet the dashboard contributors")),
        html.Br(),
        dbc.Row([
            dbc.Col([
                dbc.Button(
                    html.Img(src="assets/IMG_2474.png", id="open", className="circle-img",style={"width":"25%", "height":"25%"}), size="sm"),
                dbc.Modal([
                    dbc.ModalHeader("Boris Antonio Hernandez"),
                    dbc.Card([
                        dbc.CardImg(src="assets/IMG_2474.png"),
                        dbc.CardBody([
                            html.H5("Boris brings joy and happiness to everyone he encounters! He loves to play catch and is an exceptional retriever. He's been by his mama's side for 11 years and absolutely loves that she's working from home the last several months.", ),
                        ],style={'justify': 'center'}),
                    ]),
                    dbc.ModalFooter([
                        dbc.Button("Close", id="close", className="ml-auto", size="lg")
                    ]),
                    ],
                    id="modal",
                    centered=True,
                    size="lg",
                    ),

            ], className="circle"),

            # dbc.Col(html.Img(src="assets/IMG_2474.png", className="circle-img"),),
            # dbc.Col(html.Img(src="assets/IMG_2474.png", className="circle-img"),),
            # dbc.Col(html.Img(src="assets/IMG_2474.png", className="circle-img"),),
            # dbc.Col(html.Img(src="assets/IMG_2474.png", className="circle-img"),),
            # dbc.Col(html.Img(src="assets/IMG_2474.png", className="circle-img"),),
            # dbc.Col(html.Img(src="assets/IMG_2474.png", className="circle-img"),),
            # dbc.Col(html.Img(src="assets/IMG_2474.png", className="circle-img"),),
            # dbc.Col(html.Img(src="assets/IMG_2474.png", className="circle-img"),),
            ], className="circles")
                      
        ],fluid=True, style={'textAlign': 'center'}),
    ],)


def DEI_title():
    heading = title
    return heading

def about_():
    heading = about
    return heading 

def FC_video():
    heading = video
    return heading 
def FC_big_pic():
    heading = big_picture
    return heading 

def FC_stats():
    cards = descriptive_stats
    return cards 
def FC_key_findings():
    flipcards = key_findings1
    return flipcards

def FC_prior():
    heading = priorities
    return heading

def FC_dropdown_row():
    heading = dropdown_row
    return heading 

def FC_wordcloud():
    heading = wordcloud
    return heading 
def FC_contributors():
    heading = contributors
    return heading 
