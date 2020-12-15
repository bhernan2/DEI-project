import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import sys

from page import DEI_title, about_, FC_stats, FC_prior, FC_video, FC_wordcloud, FC_big_pic, FC_dropdown_row 
from figures import FC_fig1, FC_fig2, FC_fig3, FC_fig4, FC_fig5, FC_fig6, FC_fig7, FC_fig8, FC_fig9, FC_fig10, FC_fig11

dei_title = DEI_title()
dei_stats = FC_stats()
dei_prior=FC_prior()
dei_about = about_()
dei_video = FC_video()
dei_big_pic = FC_big_pic()
dei_dropdown = FC_dropdown_row()
dei_wordcloud = FC_wordcloud()

#this is just to save
def Dashboard():
    layout = html.Div([
    dei_title,
    dei_about,
    dei_video,
    dei_big_pic,
    dei_stats,
    dei_prior,
    dei_wordcloud, 
    dei_dropdown,
    ])
    return layout 

#to test if running uncomment below: 

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SUPERHERO])

app.layout = Dashboard()
@app.callback(
    Output("popover1", "is_open"),
    [Input("popover-target1", "n_clicks")],
    [State("popover1", "is_open")],
)
def toggle_popover1(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("popover2", "is_open"),
    [Input("popover-target2", "n_clicks")],
    [State("popover2", "is_open")],
)
def toggle_popover2(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("popover3", "is_open"),
    [Input("popover-target3", "n_clicks")],
    [State("popover3", "is_open")],
)
def toggle_popover3(n, is_open):
    if n:
        return not is_open
    return is_open

# @app.callback(
#     Output("left-collapse", "is_open"),
#     [Input("left", "n_clicks")],
#     [State("left-collapse", "is_open")],
# )
# def toggle_left(n_left, is_open):
#     if n_left:
#         return not is_open
#     return is_open
# @app.callback(
#     Output("left-collapse2", "is_open"),
#     [Input("left2", "n_clicks")],
#     [State("left-collapse2", "is_open")],
# )
# def toggle_left2(n_left, is_open):
#     if n_left:
#         return not is_open
#     return is_open

# @app.callback(
#     Output("left-collapse3", "is_open"),
#     [Input("left3", "n_clicks")],
#     [State("left-collapse3", "is_open")],
# )
# def toggle_left3(n_left, is_open):
#     if n_left:
#         return not is_open
#     return is_open

@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('dei-dropdown', 'value')])
def update_plot(value):
    if value == "plot1-info":
        return html.Div([
            dbc.Container([
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
                        html.P([
                            html.Ul([
                                html.Li('The majority of all staff survey respondents agree + strongly agree that they are treated with respect at work and a similar trend is seen across race, age, sexual orientation and tenure.'),
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
    elif value == 'plot2-info':
        return html.Div([
            dbc.Container([
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
                        html.P([
                            html.Ul([
                                html.Li('The majority of all staff survey respondents agree + strongly agree that they feel comforable being themselves at work and a similar trend is seen across race, age, sexual orientation and tenure.'),
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
    elif value == 'plot3-info':
        return html.Div([
            dbc.Container([
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
                        html.P([
                            html.Ul([
                                html.Li('65% of all staff survey respondents agree + strongly agree that employees at FC are treated with respect and dignigty.'),
                                html.Li('However, 25% of staff survey respondents who identify as Black/African American disgaree + strongly disagree with this statement.'),
                                html.Li('75% of survey respondents within the 18-24 age range agree with this statement.'),
                                html.Li('Nearly half (46%) of survey respondents in the tenure category of 5-10 years employed are neutral to this statement.')
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
    elif value == "plot4-info":
        return html.Div([
            dbc.Container([
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
                        ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
                    dbc.Col([
                        html.P([
                            html.Ul([
                                html.Li('Nearly half of all staff survey respondents agree + strongly agree that diversity and inclusiveness are openly discussed'),
                                html.Li('83% of survey respondents in the 18-24 age range agree + strongly agree with this statement.'),
                                html.Li('31% of LGBTQ+ and 23% straight survey respondents disagree + strongly disagree with this statement.'),
                                html.Li('20% of White and 24% of Latinx/Hispanic survey respondents disagree + strongly disagree with this statement.')
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])

    elif value == "plot5-info":
        return html.Div([
            dbc.Container([
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
                        html.P([
                            html.Ul([
                                html.Li('Survey respondents in the 18-24 age range agree + strongly agree (83%) that everyone at this organization is treated fairy regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.'),
                                html.Li('71% of survey respondents who have worked af FC less than one year agree + strongly agree with this statement'),
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
    elif value == "plot6-info":
        return html.Div([
            dbc.Container([
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
                        html.P([
                            html.Ul([
                                html.Li('58%, 22% and 19% of all staff survey respndents either agree + strongly agree, are neutral, or disagree + strongly disgree that they have the same opportunities as other team members at FC with similar experience and performance levels, respectively.'),
                                html.Li('20%, 25%, 20% and 19% of employees who have worked at FC for one year, 1-3 years, 3-5 years and 5-10 years disagree + strongly disagree with this statement'),
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
    elif value == "plot7-info":
        return html.Div([
            dbc.Container([
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
                        html.P([
                            html.Ul([
                                html.Li('22% of employees who identify as Latinx disagree with this statement.'),
                                html.Li('38% of Black/African Americans neither agree nor disagree with this statement.'),
                                html.Li('75% of respondants aged 18-24 strongly agree with this statement whereas only 14% of employees within the age group 45-54 stronly agree.'),
                                html.Li('20% of employees with tenure of 3-5years strongly disagree with this statement compared to 50% of employees with less than one year of tenure who strongly agree with the statement.')
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
    elif value == "plot8-info":
        return html.Div([
            dbc.Container([
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
                        ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
                    dbc.Col([
                        html.P([
                            html.Ul([
                                html.Li('22% of total respondents strongly disagree or disagree, 25% are neutral and 53% agree and strongly agree.'),
                                html.Li('FC staff who identify as Latinx/Hispanic, Black/African American and Native American strongly disagree or disagree (25, 33 and 50%, respectively).'),
                                html.Li('Younger (18-24) and older (65-74) staff generally agree or sttronly agree.'),
                                html.Li('Nearly 25% of staff in the 25-34 and 35-44 age ranges disagree or strongly disagree.')
                    ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
    elif value == "plot9-info":
        return html.Div([
            dbc.Container([
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
                        html.P([
                            html.Ul([
                                html.Li('The majority of all staff survey respondents agree + strongly agree that their team members appreciate their contributions and a similar trend is seen across race, age, sexual orientation and tenure.'),
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
    elif value == "plot10-info":
        return html.Div([
            dbc.Container([
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
                        html.P([
                            html.Ul([
                                html.Li('81% of all staff survey respondents agree + strongly agree that their superviors try to understand their point of views and a similar trend is seen across race, age, sexual orientation and tenure.'),
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
    elif value == "plot11-info":
        return html.Div([
            dbc.Container([
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
                        html.P([
                            html.Ul([
                                html.Li('Over 60% of all staff survery respondents agree + strongle agree that their workplace is committed to building the strengths of each employee.'),
                                html.Li('38% of Black/African American respondents disagree + strongly disagree with this statement compared to 12% of White and Latinx respondents.'),
                                html.Li('23% of LGBTQ+ respondents disagree + strongly disagree with this statement compared to 14% of straight respondents.'),
                                html.Li('Over 50% of all tenure age ranges agree + strongly agree with this statement')
                            ]),
                        ]),
                    ]),
                ], align="center"),  
            ], fluid=True),
        ])
server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)
   
#
