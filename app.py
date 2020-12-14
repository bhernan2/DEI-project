import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import sys

from page import DEI_title, FC_output,  about_, FC_stats, FC_prior, FC_video, FC_wordcloud, FC_big_pic, FC_dropdown_row #FC_graph1
from figures import FC_fig1, FC_fig2, FC_fig3, FC_fig4, FC_fig5, FC_fig6, FC_fig7, FC_fig8, FC_fig9, FC_fig10, FC_fig11

dei_title = DEI_title()
dei_stats = FC_stats()
dei_prior=FC_prior()
dei_about = about_()
dei_video = FC_video()
dei_big_pic = FC_big_pic()
dei_dropdown = FC_dropdown_row()
dei_output = FC_output()
dei_wordcloud = FC_wordcloud()
#dei_graph1 = FC_graph1()
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
    dei_output,
    dei_dropdown,
    #FC_graph1
    ])
    return layout 

#to test if running uncomment below: 

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SUPERHERO])

app.layout = Dashboard()
@app.callback(
    Output("left-collapse", "is_open"),
    [Input("left", "n_clicks")],
    [State("left-collapse", "is_open")],
)
def toggle_left(n_left, is_open):
    if n_left:
        return not is_open
    return is_open
@app.callback(
    Output("left-collapse2", "is_open"),
    [Input("left2", "n_clicks")],
    [State("left-collapse2", "is_open")],
)
def toggle_left2(n_left, is_open):
    if n_left:
        return not is_open
    return is_open

@app.callback(
    Output("left-collapse3", "is_open"),
    [Input("left3", "n_clicks")],
    [State("left-collapse3", "is_open")],
)
def toggle_left3(n_left, is_open):
    if n_left:
        return not is_open
    return is_open

@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('dei-dropdown', 'value')])
def update_plot1(value):
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
    

    



# @app.callback(Output('plot1', 'figure'),
#               Input('dei-dropdown', 'value'))
# def update_graph_a(value):
#     # prepare figure_a from value
#     return FC_fig1

# @app.callback(Output('plot2', 'figure'),
#               Input('dei-dropdown', 'value'))
# def update_graph_b(value):
#     # prepare figure_b from value
#     return FC_fig2

# @app.callback(Output('plot3', 'figure'),
#               Input('dei-dropdown', 'value'))
# def update_graph_c(value):
#     # prepare figure_c from value
#     return FC_fig4

server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)
   
#
