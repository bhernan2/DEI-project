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
            html.H5('The Diversity, Equity and Inclusion (DEI) Survey team created a survey to gather more information about your experience working at Foundation Communities. We researched two surveys: 1) Gallup Diversity and Inclusion and 2) Building Movement Project Race to Lead. We decided to merge questions from both surveys to create the FC DEI Survey. The Gallup survey questions are more focused on individual experience while the Building Movement Project survey is more focused on the racial leadership gap in nonprofit organizations. Both are leaders in collecting data about diversity, equity and inclusion in the workplace. Your responses were important to us and helped us learn more about the racial biases, discriminatory practices and unconscious prejudices that affect staff of color and those who belong to marginalized groups within the agency.', className='text-justify', ),                                                                                                                                              
            ]),
        ], fluid=True), 
    ]) 
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
        #dbc.Container([
            #html.Ul(id='my-list', children=[html.Li(i) for i in dei_list], className= 'mb-10 lead text-left'),  
            #])
           
])    

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
        #dbc.Container([
            #html.Ul(id='my-list', children=[html.Li(i) for i in dei_list], className= 'mb-10 lead text-left'),  
            #])
           
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

card_content = [
    #dbc.CardHeader("Descriptive Stats"),
    html.H4([
        dbc.CardHeader([
            ("My supervisor tries to understand my point of view."),
            html.Br(),
            html.Br(),
            ("At work I am treated with respect."),
            html.Br(),
            html.Br(),
        ], style={"display": "flex"}),
    ]),
    dbc.CardBody([
            html.H2("81%", className="card-title"),
            html.H5([
                'of all staff members agree + strongly agree.',
                ],className="card-text"),
            html.Br(),
            html.H2("88%", className="card-title"),
            html.H5([
                'of all staff survey particapnts agree + strongly agree.',
                ],className="card-text"),
        
        ]),
]
card_content1 = [
    #dbc.CardHeader("Descriptive Stats"),
    html.H4([
        dbc.CardHeader([
            ("My organization treasurese diverse opinions and ideas."),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
        ], style={"display": "flex"}),
    ]),
    dbc.CardBody([
            html.H2("34%", className="card-title"),
            html.H5([
                'of LGBTQ+ staff members either strongly disagree + disagree.',
                ],className="card-text"),
            html.Br(),
            html.H2("25%", className="card-title"),
            html.H5([
                'of employees who have been employeed between 1-10 years disagree + strongly disagree.',
                ],className="card-text"),
        
        ]),
]
card_content2 = [
    #dbc.CardHeader("Descriptive Stats"),
    html.H4([
        dbc.CardHeader("Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.")
    ],style={"display": "flex"}),
    dbc.CardBody([
            html.H2("54%", className="card-title"),
            html.H5(
                "of Black/African American identifying staff disagree + strongly disagree.",
                className="card-text",),
            html.Br(),
            html.H2("45%", className="card-title"),
            html.H5("of survey respndents who have worked at FC for one year disagree + strongly disagree with this statement.", className="card-text",),
        ]),
]
card_content3 = [
    html.H4([
        dbc.CardHeader(" I have the same opportunities for advancement as other team members with similar experience and performance levels.")
    ],style={"display": "flex"}),
    dbc.CardBody([
            html.H2("63%", className="card-title"),
            html.H5(
                "of Black/African American identifying staff disagree + strongly disagree.",
                className="card-text",),
            html.Br(),
            html.H2("27%", className="card-title"),
            html.H5(
                "of LGBTQ+ identigying staff disagree + strongly disagree.",
                className="card-text",),
        ]),
]
card_content4 = [
    html.H4([
        dbc.CardHeader([
            ("Diversity and inclusiveness issues are openly discussed at my organization."),
            html.Br(),
            html.Br(),
            ], style={"display": "flex"})
    ]),
    dbc.CardBody([
            # html.H2("100%", className="card-title"),
            # html.H5(
            #     "of Native American identifying staff disagree + strongly disagree."),
            html.Br(),
            html.H2("50%", className="card-title"),
            html.H5(
                "of Black/African American identifying staff disagree + strongly disagree.", 
                className="card-text",),
                
        ]),
]
card_content5 = [
    #dbc.CardHeader("Descriptive Stats"),
    dbc.CardBody([
            html.H2("No.1", className="card-title"),
            dbc.Button(html.Img(src="assets/icons8-survey-96.png"), id='popover-target1', color='warning', size='lg', block=True),
            dbc.Popover([
            dbc.PopoverHeader("135 responses"),
            dbc.PopoverBody("Address ways that racial inequity/systemic bias impact issues the organization works on and hold senior team members accountable for anti-racists actions.")
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
        dbc.Button(html.Img(src="assets/icons8-survey-96.png"), id='popover-target2', color='danger', size='lg', block=True),
        dbc.Popover([
            dbc.PopoverHeader("122 responses"),
            dbc.PopoverBody("Provide training for staff, leadership and board.")
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
        dbc.Button(html.Img(src="assets/icons8-survey-96.png"), id='popover-target3', color='info', size='lg', block=True),
        dbc.Popover([
            dbc.PopoverHeader("90 responses"),
            dbc.PopoverBody("Increase diverse representation on board and advisory committees.")
        ], 
        id="popover3",
        is_open=False,
        target="popover-target3",
        placement="bottom"
        )
        ]),
]
# card_content8 = [
#     #dbc.CardHeader("Descriptive Stats"),
#     dbc.CardBody([
#             html.H2("No. 4", className="card-title"),
#             html.H5(
#                 "Develop recruitment and hiring protocols and strategies that include implicit bias testing for managers and supervisors",
#                 className="card-text",),
#         ]),
# ]
descriptive_stats = dbc.Jumbotron([
    dbc.Container([
        html.Br(),
        dbc.Row([
            html.H3("Key findings", className='text-left', )
        ]), 
        html.Br(),
        dbc.Row([
            dbc.CardDeck([
                dbc.Col(
                    dbc.Card(card_content, color="light", inverse=True), style={"display": "flex"}, width=4),
                dbc.Col(
                    dbc.Card(card_content1, color="primary", inverse=True), style={"display": "flex"}, width=4),
                dbc.Col(
                    dbc.Card(card_content2, color="secondary", inverse=True), style={"display": "flex"}, width=4), 
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
    ], fluid=True),
])
key_findings1 = dbc.Jumbotron([
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
                            ],className="flip-card-back", color="warning", inverse=True, style={"display": "flex"},)
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
                            ], className="flip-card-front", color="light", inverse=True, style={"display": "flex"},),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("88%"),
                                html.P('of all staff survey particapnts'),
                                html.Br(),
                                html.H4('agree + strongly agree'),
                                html.Br(),
                                ]), 
                            ],className="flip-card-back", color="warning", inverse=True, style={"display": "flex"},)
                    ],className="flip-card-inner",),
            
                ],className="flip-card"),
            
            dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("My organization treasurese diverse opinions and ideas."),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                dbc.CardImg(src="/assets/icons8-learning-80.png", alt="Avatar", style={"width":"25%"}),
                                ]),
                            ], className="flip-card-front", color="light", inverse=True, style={"display": "flex"},),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("34%"), 
                                html.P('of LGBTQ+ and'),
                                html.Br(),
                                html.H4("25%"), 
                                html.P('employees who have been employeed between 1-10 years'),
                                html.H4('disagree + strongly disagree')
                                ]),
                            ],className="flip-card-back", color="warning", inverse=True, style={"display": "flex"},)
                    ],className="flip-card-inner",),
                ],className="flip-card"),
            
            dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                #dbc.CardImg(src="/assets/icons8-handshake-80.png", alt="Avatar", style={"width":"25%"}),
                                html.H4("Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance."),
                                dbc.CardImg(src="/assets/icons8-handshake-80.png", alt="Avatar", style={"width":"25%"}),
                                ]),
                            ], className="flip-card-front", color="light", inverse=True, style={"display": "flex"},),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("54%"), 
                                html.P('of Black/African American identifying staff and'),
                                html.Br(),
                                html.H4("45%"), 
                                html.P('of employees who have worked for one year'),
                                html.H4('disagree + strongly disagree'),
                                ]),
                            ],className="flip-card-back", color="warning", inverse=True, style={"display": "flex"},)
                    ],className="flip-card-inner",align="center"),
                ],className="flip-card", align="center"),
            dbc.Row([], align="center"),
            dbc.Row([], align="center"),
            dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                #dbc.CardImg(src="/assets/icons8-handshake-80.png", alt="Avatar", style={"width":"25%"}),
                                html.H4("I have the same opportunities for advancement as other team members with similar experience and performance levels"),
                                html.Br(),
                                dbc.CardImg(src="/assets/icons8-circled-up-right-80.png", alt="Avatar", style={"width":"25%"}),
                                ]),
                            ], className="flip-card-front", color="light", inverse=True, style={"display": "flex"},),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("63%"), 
                                html.P('of Black/African American identifying staff and'),
                                html.Br(),
                                html.H4("27%"), 
                                html.P('of LGBTQ+ employees'),
                                html.H4('disagree + strongly disagree'),
                                ]),
                            ],className="flip-card-back", color="warning", inverse=True, style={"display": "flex"},)
                    ],className="flip-card-inner",align="center"),
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
                            ], className="flip-card-front", color="light", inverse=True, style={"display": "flex"},),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("50%"), 
                                html.P('of Black/African American identifying staff'),
                                html.H4('disagree + strongly disagree'),
                                ]),
                            ],className="flip-card-back", color="warning", inverse=True, style={"display": "flex"},)
                    ],className="flip-card-inner",align="center"),
                ],className="flip-card", align="center"),

            ], className="cards", fluid=True),
])
priorities = dbc.Jumbotron([
    dbc.Container([
        html.Br(),
        dbc.Row([
            html.H3("Top 3 DEI efforts that FC staff would like to see prioritized", className='text-left', )
        ]), 
        html.Br(),       
        dbc.Row([
            dbc.Col(
                dbc.Card(card_content5, color="warning", inverse=True), width = 4),
            dbc.Col(
                dbc.Card(card_content6, color="danger", inverse=True),width = 4),
            dbc.Col(
                dbc.Card(card_content7, color="info", inverse=True),width = 4),
            # dbc.Col(
            #     dbc.Card(card_content8, color="light", inverse=True),style={"display": "flex"},width=3),
            ], align="center"), 
    ], fluid=True)
])
#dropdown row
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
           

# collapse1 = html.Div(
#     [
#         dbc.Button(
#             "At work I feel comfortable being myself.", size="lg", color="primary", id="left", className="mr-1"
#         ),
#         dbc.Row(
#             [
#                 dbc.Col(
#                     dbc.Collapse(
#                         dbc.Card("FC response rank avg compared to Gallup responses.", body=True),
#                         id="left-collapse",
#                     )
#                 ),
#             ],
#             className="mt-3",
#         ),
#     ]
# )
# collapse2 = html.Div([
#         dbc.Button(
#             "Employees in my organization are treated with respect and dignity.", size="lg", color="primary", id="left2", className="mr-1"),
#         dbc.Row([
#                 dbc.Col(
#                     dbc.Collapse(
#                         dbc.Card("FC response rank avg compared to Gallup responses.", body=True),
#                         id="left-collapse2",)
#                 ),
#                 ],className="mt-3",),
#     ])
# collapse3 = html.Div([
#         dbc.Button(
#             "Everyone at this organization is treated fairly.", size="lg", color="primary", id="left3", className="mr-1"),
#         dbc.Row([
#                 dbc.Col(
#                     dbc.Collapse(
#                         dbc.Card("FC response rank avg compared to Gallup responses.", body=True),
#                         id="left-collapse3",)
#                 ),
#                 ],className="mt-3",),
#     ])


wordcloud = dbc.Jumbotron([
    dbc.Container([
        dbc.Row([
            html.H3("Other efforts you'd like to see prioritized", className='text-left', ),
        ]), 
        html.Br(),
        dbc.Row([
            dbc.Col(width=2),
            dbc.Col([
                dbc.Card([
                    dbc.CardImg(src='assets/word_cloud7.png'),
                    dbc.CardBody([
                        html.H4("Wordcloud", className="card-title"),
                        html.P("A word cloud is a collection of words depicted in different sizes. The bigger and bolder the word appears, the more often it is mentioned within a given text and the more important it is. This is an ideal way to pull the most pertinent parts of textual data and helps users compare and contrast pieces of text.")   
                        ])
                    ]),
                ], width=8),
                dbc.Col(width=2),
            # dbc.Col([
            #     dbc.Row([
            #         html.H3("FC DEI response scores compared to Gallup response scores"),
            #     ]),
            #     html.Br(),
            #     dbc.Row([collapse1]),
            #     html.Br(),
            #     dbc.Row([collapse2]),
            #     html.Br(),
            #     dbc.Row([collapse3])        
            #     ], width=6)
            ], align='center')       
            ], fluid=True),
        ])

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
