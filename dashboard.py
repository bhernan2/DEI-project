import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from page import DEI_title, FC_figures, about_, FC_stats #FC_wordcloud

title = DEI_title()
dei_figures = FC_figures()
dei_about = about_()
dei_stats = FC_stats()
#dei_wordcloud = FC_wordcloud()

def Dashboard():
    layout = html.Div([
    title,
    dei_stats,
    dei_about,
    dei_figures,
    #dei_wordcloud
    ])
    return layout 

#to test if running uncomment below: 
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SUPERHERO])
app.layout = Dashboard()
if __name__ == "__main__":
    app.run_server(debug=True)