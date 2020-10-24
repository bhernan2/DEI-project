import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly

import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

from dashboard import Dashboard
from figures import FC_fig1, FC_fig2

dei = pd.read_csv("DEISurveyFinal.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

app.config.suppress_callback_exceptions = True

app.layout = Dashboard()

@app.callback(
    Output('figure1', 'figure'),
    [Input('dei-dropdown', 'value')]
)

def update_graph(item1):
    graph = FC_fig1()
    return graph

@app.callback(
    Output('figure2', 'figure'),
    [Input('dei-dropdown', 'value')]
)

def update_graph(item2):
    graph = FC_fig2()
    return graph

if __name__ == '__main__':
    app.run_server(debug=True)

