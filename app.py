import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import sys

from page import DEI_title, FC_output,  about_, FC_stats #FC_dropdown_row, FC_demo_row


dei_title = DEI_title()
dei_stats = FC_stats()
dei_about = about_()
#dei_demo = FC_demo_row()
#dei_dropdown = FC_dropdown_row()
dei_output = FC_output()

#dei_wordcloud = FC_wordcloud()
#this is just to save
def Dashboard():
    layout = html.Div([
    dei_title,
    dei_stats,
    dei_about,
    #dei_demo,
    #dei_dropdown,
    dei_output,
    #dei_wordcloud
    ])
    return layout 

#to test if running uncomment below: 

app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=-2"}], external_stylesheets = [dbc.themes.SUPERHERO])

app.layout = Dashboard()
server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)
   

