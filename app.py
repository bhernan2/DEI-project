import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import sys

from page import DEI_title, about_, FC_prior, FC_video, FC_wordcloud, FC_dropdown_row, FC_key_findings, FC_contributors
from figures import FC_fig1, FC_fig2, FC_fig3, FC_fig4, FC_fig5, FC_fig6, FC_fig7, FC_fig8, FC_fig9, FC_fig10, FC_fig11

dei_title = DEI_title()
dei_prior=FC_prior()
dei_key_findings=FC_key_findings()
dei_about = about_()
dei_video = FC_video()
dei_dropdown = FC_dropdown_row()
dei_wordcloud = FC_wordcloud()
dei_contributors = FC_contributors()

#this is just to save
def Dashboard():
    layout = html.Div([
    dei_title,
    dei_about,
    dei_video,
    dei_key_findings,
    dei_prior,
    dei_wordcloud, 
    dei_dropdown,
    dei_contributors
    ])
    return layout 

#to test if running uncomment below: 

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SUPERHERO])

app.layout = Dashboard()
#top priorities popover callbacks
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

#video modal callback
@app.callback(
    Output("video-centered", "is_open"),
    [Input("video-open", "n_clicks"), Input("video-close", "n_clicks")],
    [State("video-centered", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#wordcloud modal callback
@app.callback(
    Output("modal-centered", "is_open"),
    [Input("open-centered", "n_clicks"), Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

#dashboard contributors modal callbacks
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
@app.callback(
    Output("modal2", "is_open"),
    [Input("open2", "n_clicks"), Input("close2", "n_clicks")],
    [State("modal2", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
@app.callback(
    Output("modal3", "is_open"),
    [Input("open3", "n_clicks"), Input("close3", "n_clicks")],
    [State("modal3", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
@app.callback(
    Output("modal4", "is_open"),
    [Input("open4", "n_clicks"), Input("close4", "n_clicks")],
    [State("modal4", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
@app.callback(
    Output("modal5", "is_open"),
    [Input("open5", "n_clicks"), Input("close5", "n_clicks")],
    [State("modal5", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
@app.callback(
    Output("modal6", "is_open"),
    [Input("open6", "n_clicks"), Input("close6", "n_clicks")],
    [State("modal6", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
@app.callback(
    Output("modal7", "is_open"),
    [Input("open7", "n_clicks"), Input("close7", "n_clicks")],
    [State("modal7", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
# @app.callback(
#     Output("modal8", "is_open"),
#     [Input("open8", "n_clicks"), Input("close8", "n_clicks")],
#     [State("modal8", "is_open")],
# )
# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open

#dropdown figures callbacks
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('86% agree + strongly agree'),
                                html.Li('6% disagree + strongly disagree'),
                                html.Li('8% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('21% of Black/African American identifying staff'),
                                html.Li('10% of staff between the ages 35 - 44'),
                                html.Li('10% of staff employed 3-5 years'),
                                html.Li('8% of LatinX identifying staff'),
                                html.Li('8% of staff between the ages 55 - 64'),
                                
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 4.33'),
                                html.Li('No gallup comparison'),
                            ]),
                        ]),
                    ], align="baseline"),
                ]),
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
                        ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4}),
                    dbc.Col([
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('77% agree + strongly agree'),
                                html.Li('8% disagree + strongly disagree'),
                                html.Li('15% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('21% of Black/African American identifying staff'),
                                html.Li('13% of staff who have been employed for 3-5 years'),
                                html.Li('12% of staff between the ages 35 - 44'),
                                html.Li('10% of staff between the ages 45 - 54'),
                                html.Li('9% of LatinX identifying staff'),
                                html.Li('9% of staff who have been employed for one year'),
                                
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 4.10'),
                                html.Li('FC ranks in the 50th percentile when compared to Gallup data.'),
                            ]),
                        ]),
                    ], align='baseline'),
                ],),  
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('60% agree + strongly agree'),
                                html.Li('10% disagree + strongly disagree'),
                                html.Li('24% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('25% of Black/African American identifying staff'),
                                html.Li('17% of staff between the ages 18 - 24'),
                                html.Li('17% of staff who have been employed for one year'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 3.86'),
                                html.Li('FC ranks in the 25th percentile when compared to Gallup data.'),
                            ]),
                        ]),
                        
                    ],align="baseline"),
                ],),  
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('47% agree + strongly agree'),
                                html.Li('25% disagree + strongly disagree'),
                                html.Li('28% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('100% of Native American identifying staff'),
                                html.Li('50% of Black/African American identifying staff'),
                                html.Li('36% of staff who have been employed for one year'),
                                html.Li('36% of staff who have been employed for one year'),
                                html.Li('33% of non-binary identifying staff'),
                                html.Li('31% of of LGBTQ+ identifying staff'),
                                html.Li('30% of staff between the ages 35 - 44'),
                                html.Li('13% of staff who have been employed for 5-10 years'),
                                
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 3.40'),
                                html.Li('No gallup comparison'),
                            ]),
                        ]),
                        
                    ],align="baseline"),
                ],),  
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('50% agree + strongly agree'),
                                html.Li('23% disagree + strongly disagree'),
                                html.Li('27% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('53% of Black/African American identifying staff'),
                                html.Li('45% of staff who have been employed for one year'),
                                html.Li('32% of staff who have been employed for 1-3 years'),
                                html.Li('26% of of LGBTQ+ identifying staff'),
                                html.Li('26% of staff between the ages 35 - 44'),
                                html.Li('24% of staff between the ages 45 - 54'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 3.53'),
                                html.Li('FC ranks in the 25th percentile when compared to Gallup data.'),
                            ]),
                        ]),
                    ], align="baseline"),
                ],),  
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('58% agree + strongly agree'),
                                html.Li('19% disagree + strongly disagree'),
                                html.Li('22% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('63% of Black/African American identifying staff'),
                                html.Li('50% of Native American identifying staff'),
                                html.Li('33% of seasonal staff'),
                                html.Li('33% of non-binary identifying staff'),
                                html.Li('27% of of LGBTQ+ identifying staff'),
                                html.Li('27% of staff between the ages 55 - 64'),
                                html.Li('25% of staff who have been employed for 1-3 years'),
                                html.Li('24% of staff between the ages 35 - 44'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 3.63'),
                                html.Li('No gallup comparison'),
                            ]),
                        ]),
                    ], align="baseline"),
                ], ),  
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('55% agree + strongly agree'),
                                html.Li('26% disagree + strongly disagree'),
                                html.Li('19% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('41% of Black/African American identifying staff'),
                                html.Li('32% of LatinX identifying staff'),
                                html.Li('32% of staff who have been employed for 1-3 years'),
                                html.Li('31% of LGBTQ+ identifying staff'),
                                html.Li('30% of staff who have been employed for 3-5 years'),
                                html.Li('29% of full time staff'),
                                html.Li('29% of female identifying staff'),     
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 3.48'),
                                html.Li('No gallup comparison'),
                            ]),
                        ]),
                    ], align="baseline"),
                ], ),  
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('55% agree + strongly agree'),
                                html.Li('21% disagree + strongly disagree'),
                                html.Li('24% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('50% of Native American identifying staff'),
                                html.Li('34% of Black/African American identifying staff'),
                                html.Li('27% of staff who have been employed for 1-3 years'),
                                html.Li('34% of LGBTQ+ identifying staff'),
                                html.Li('26% of staff who have been employed for 3-5 years'),
                                html.Li('24% of staff who have been employed for 5-10 years'),
                                html.Li('24% of full time staff'),
                                html.Li('24% of staff between the ages 35 - 44'),
                                html.Li('23% of staff between the ages 25 - 34'),
                                html.Li('23% of female identifying staff'),     
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 3.53'),
                                html.Li('FC ranks in the 25th percentile when compared to Gallup data.'),
                            ]),
                        ]),
                    ], align="baseline"),
                ], ),  
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('85% agree + strongly agree'),
                                html.Li('3% disagree + strongly disagree'),
                                html.Li('12% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('10% of staff who have been employed for 10+ years'),
                                html.Li('8% of staff between the ages 55 - 64'),
                                html.Li('4% of Black/African American identifying staff'),
                                html.Li('4% of staff between the ages 35 - 44'),
                                html.Li('4% of staff who have been employed for 1-3 years'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 4.31'),
                                html.Li('FC ranks in the 75th percentile when compared to Gallup data.'),
                            ]),
                        ]),
                    ],  align="baseline"),
                ],),  
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('81% agree + strongly agree'),
                                html.Li('9% disagree + strongly disagree'),
                                html.Li('12% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('50% of Native American identifying staff'),
                                html.Li('33% of seasonal staff'),
                                html.Li('16% of staff between the ages 55 - 64'),
                                html.Li('13% of Black/African American identifying staff'), 
                                html.Li('11% of staff who have been employed for 1-3 years'), 
                                html.Li('10% of staff who have been employed for 3-5 years'),     
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 4.23'),
                                html.Li('No Gallup comparison.'),
                            ]),
                        ]),
                    ], align="baseline"),
                ], ),  
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
                        html.H5('Total % across demographic categories:'),
                        html.P([
                            html.Ul([
                                html.Li('63% agree + strongly agree'),
                                html.Li('15% disagree + strongly disagree'),
                                html.Li('22% neither agree or disagree'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Disagree + strongly disagree by specific identities:'),
                        html.P([
                            html.Ul([
                                html.Li('50% of Native American identifying staff'),
                                html.Li('38% of Black/African American identifying staff'),
                                html.Li('33% of non-binary identifying staff'),
                                html.Li('27% of staff who have been employed for 1-3 years'),
                                html.Li('24% of staff between the ages 55 - 64'),
                                html.Li('23% of LGBTQ+ identifying staff'),
                                html.Li('20% of staff who have been employed for 3-5 years'), 
                                html.Li('19% of male identifying staff'), 
                                html.Li('18% of staff between the ages 45 - 54'),
                            ]),
                        ]),
                        html.Br(),
                        html.H5('Rank mean average & Gallup comparison:'),
                        html.P([
                            html.Ul([
                                html.Li('Avg - 3.75'),
                                html.Li('No Gallup comparison.'),
                            ]),
                        ]),
                    ], align="baseline"),
                ],),  
            ], fluid=True),
        ])
server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)

#removed closing parantheses above 