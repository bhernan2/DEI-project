import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

#from navbar import dash_navbar
from page import FC_logo, DEI_title, figures, about_


#nav = dash_navbar()

dei_logo = FC_logo()
title = DEI_title()
dei_figures = figures()
dei_about = about_()

def Dashboard():
    layout = html.Div([
    #nav, 
    #dei_logo,
    title,
    dei_about,
    dei_figures
    ])
    return layout 
#to test if running uncomment below: 
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.DARKLY])
app.layout = Dashboard()
if __name__ == "__main__":
    app.run_server(debug=True)