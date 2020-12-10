import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import sys

from page import DEI_title, FC_output,  about_, FC_stats, FC_prior, FC_video, FC_wordcloud #FC_dropdown_row, FC_demo_row


dei_title = DEI_title()
dei_stats = FC_stats()
dei_prior=FC_prior()
dei_about = about_()
dei_video = FC_video()
#dei_demo = FC_demo_row()
#dei_dropdown = FC_dropdown_row()
dei_output = FC_output()
dei_wordcloud = FC_wordcloud()
#this is just to save
def Dashboard():
    layout = html.Div([
    dei_title,
    dei_about,
    dei_video,
    dei_stats,
    dei_prior,
    dei_wordcloud, 
    dei_output
    #dei_demo,
    #dei_dropdown,
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

server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)
   

