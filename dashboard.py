import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from page import DEI_title, FC_demo_row, FC_dropdown_row, FC_output,  about_, FC_stats

dei_title = DEI_title()
dei_stats = FC_stats()
dei_about = about_()
dei_demo = FC_demo_row()
dei_dropdown = FC_dropdown_row()
dei_output = FC_output()

#dei_wordcloud = FC_wordcloud()

def Dashboard():
    layout = html.Div([
    dei_title,
    dei_stats,
    dei_about,
    dei_demo,
    dei_dropdown,
    dei_output,
    #dei_wordcloud
    ])
    return layout 

#to test if running uncomment below: 
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.SUPERHERO])
app.layout = Dashboard()
if __name__ == "__main__":
    app.run_server(debug=True)