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

def create_graph():
    #defining list_updatemenus
    list_updatemenus = [
        {'label': 'Total',
        'method': 'update',
        'args': [{'visible': [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'At work, I am treated with respect.'}]},
        {'label': 'Race',
        'method': 'update',
        'args': [{'visible': [False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'At work, I am treated with respect.'}]},
        {'label': 'Age',
        'method': 'update',
        'args': [{'visible': [False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'At work, I am treated with respect.'}]},
        {'label': 'Sexual Orientation',
        'method': 'update',
        'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False]}, {'title': 'At work, I am treated with respect.'}]},
        {'label': 'Tenure',
        'method': 'update',
        'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False]}, {'title': 'At work, I am treated with respect.'}]},
        {'label': 'Status',
        'method': 'update',
        'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True]}, {'title': 'At work, I am treated with respect.'}]}
                   ]
    #defining graph objects
    x_total = dei['At work, I am treated with respect.  ']
    x_white = dei[dei['What is your race? ']=="White"]["At work, I am treated with respect.  "]
    x_latinx = dei[dei['What is your race? ']=="Latino/Hispanic"]["At work, I am treated with respect.  "]
    x_black = dei[dei['What is your race? ']=="Black/ African American"]["At work, I am treated with respect.  "]
    x_two_plus = dei[dei['What is your race? ']=="Two or more Races"]["At work, I am treated with respect.  "]
    x_asian = dei[dei['What is your race? ']=="Asian"]["At work, I am treated with respect.  "]
    x_first_peoples = dei[dei['What is your race? ']=="Indian/ Native American"]["At work, I am treated with respect.  "]
    x_age1 = dei[dei["What is your age?"]=="25-34"]["At work, I am treated with respect.  "]
    x_age2 = dei[dei["What is your age?"]=="35-44"]["At work, I am treated with respect.  "]
    x_age3 = dei[dei["What is your age?"]=="45-54"]["At work, I am treated with respect.  "]
    x_age4 = dei[dei["What is your age?"]=="55-64"]["At work, I am treated with respect.  "]
    x_age5 = dei[dei["What is your age?"]=="18-24"]["At work, I am treated with respect.  "]
    x_age6 = dei[dei["What is your age?"]=="65-74"]["At work, I am treated with respect.  "]
    x_straight = dei[dei["What is your sexual orientation?"]=="Straight"]["At work, I am treated with respect.  "]
    x_lgbtq = dei[dei["What is your sexual orientation?"]=="LGBTQ+"]["At work, I am treated with respect.  "]
    x_tenure1 = dei[dei["How long have you worked for FC?"]=="1-3 years"]["At work, I am treated with respect.  "]
    x_tenure2 = dei[dei["How long have you worked for FC?"]=="3-5 years"]["At work, I am treated with respect.  "]
    x_tenure3 = dei[dei["How long have you worked for FC?"]=="Less than a year"]["At work, I am treated with respect.  "]
    x_tenure4 = dei[dei["How long have you worked for FC?"]=="5-10 years"]["At work, I am treated with respect.  "]
    x_tenure5 = dei[dei["How long have you worked for FC?"]=="10+ years"]["At work, I am treated with respect.  "]
    x_tenure6 = dei[dei["How long have you worked for FC?"]=="1 year"]["At work, I am treated with respect.  "]
    x_status1 = dei[dei["What is your employment status?"]=="Full-time"]["At work, I am treated with respect.  "]
    x_status2 = dei[dei["What is your employment status?"]=="Part-time"]["At work, I am treated with respect.  "]
    x_status3 = dei[dei["What is your employment status?"]=="Seasonal"]["At work, I am treated with respect.  "]
    x_status4 = dei[dei["What is your employment status?"]=="Part-time, Seasonal"]["At work, I am treated with respect.  "]
    #defining data
    data=[
        go.Histogram(x=x_total,name='   ',opacity = .75),
        go.Histogram(x=x_white,name='White',opacity = .75),
        go.Histogram(x=x_latinx,name='Latino/Hispanic',opacity = .75),
        go.Histogram(x=x_black,name='Black/African American',opacity = .75),
        go.Histogram(x=x_two_plus,name='Two or more Races',opacity = .75),
        go.Histogram(x=x_asian,name='Asian',opacity = .75),
        go.Histogram(x=x_first_peoples,name='Indian/Native American',opacity = .5),
        go.Histogram(x=x_age1,name='25-34', opacity = .75),
        go.Histogram(x=x_age2,name='35-44',opacity = .75),
        go.Histogram(x=x_age3,name='45-54',opacity = .75),
        go.Histogram(x=x_age4,name='55-64',opacity = .75),
        go.Histogram(x=x_age5,name='18-24',opacity = .75),
        go.Histogram(x=x_age6,name='65-74',opacity = .75),
        go.Histogram(x=x_straight,name='Straight',opacity = .75),
        go.Histogram(x=x_lgbtq,name='LGBTQ+',opacity = .75),
        go.Histogram(x=x_tenure1,name='1-3 years',opacity = .75),
        go.Histogram(x=x_tenure2,name='3-5 years',opacity = .75),
        go.Histogram(x=x_tenure3,name='< than a year',opacity = .75),
        go.Histogram(x=x_tenure4,name='5-10 years',opacity = .75),
        go.Histogram(x=x_tenure5,name='10+ years',opacity = .75),
        go.Histogram(x=x_tenure6,name='1 year',opacity = .75),
        go.Histogram(x=x_status1,name='Full-time',opacity = .75),
        go.Histogram(x=x_status2,name='Part-time',opacity = .75),
        go.Histogram(x=x_status2,name='Seasonal',opacity = .75),
        go.Histogram(x=x_status2,name='Part-time, Seasonal',opacity = .75) 
     ]

    #defining layout
    layout=go.Layout(
        title=dict(
            text='At work, I am treated with respect.',
            x=0.5,
            y=0.95,
            xanchor='center',
            yanchor= 'top',
            font=dict(
                size=25,
                color='#000000'
            )

        ),
        margin=dict(
            l=200,
            r=200,
            b=150,
            t=150,
            pad=4
        ),
        font=dict(
            size=18,
            color='#000000',
        ), 
        legend=dict(
        # Adjust click behavior
        itemclick="toggleothers",
        itemdoubleclick="toggle",
        ),  
        updatemenus=list([dict(
            buttons= list_updatemenus, 
            active=3,
            x = 0.2,
            y = -0.2,
            type = 'buttons', 
            bordercolor = "#000000",
            xanchor='left',
            yanchor='bottom',
            direction='left',
            pad=dict(
                l=10,
                r=10,
                t=10,
                b=10)
                )
        ]),
        barmode='stack',
        width=1440, 
        height=800,
        paper_bgcolor='#cdd3dc',
        plot_bgcolor='#cdd3dc')
    
    #defining layout and plotting
    fig = go.Figure(data,layout)
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    return fig

    


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

app.config.suppress_callback_exceptions = True

app.layout = Dashboard()

@app.callback(
    Output('plot', 'figure'),
    [Input('dei-dropdown', 'value')]
)

def update_figure(item1):
     if item1 == None:
        item1 = 'Type'
        trace = [
        go.Histogram(x=x_total,name='   ',opacity = .5),
        go.Histogram(x=x_white,name='White',opacity = .5),
        go.Histogram(x=x_latinx,name='Latino/Hispanic',opacity = .5),
        go.Histogram(x=x_black,name='Black/African American',opacity = .5),
        go.Histogram(x=x_two_plus,name='Two or more Races',opacity = .5),
        go.Histogram(x=x_asian,name='Asian',opacity = .5),
        go.Histogram(x=x_first_peoples,name='Indian/Native American',opacity = .5),
        go.Histogram(x=x_age1,name='25-34', opacity = .5),
        go.Histogram(x=x_age2,name='35-44',opacity = .5),
        go.Histogram(x=x_age3,name='45-54',opacity = .5),
        go.Histogram(x=x_age4,name='55-64',opacity = .5),
        go.Histogram(x=x_age5,name='18-24',opacity = .5),
        go.Histogram(x=x_age6,name='65-74',opacity = .5),
        go.Histogram(x=x_straight,name='Straight',opacity = .5),
        go.Histogram(x=x_lgbtq,name='LGBTQ+',opacity = .5),
        go.Histogram(x=x_tenure1,name='1-3 years',opacity = .5),
        go.Histogram(x=x_tenure2,name='3-5 years',opacity = .5),
        go.Histogram(x=x_tenure3,name='< than a year',opacity = .5),
        go.Histogram(x=x_tenure4,name='5-10 years',opacity = .5),
        go.Histogram(x=x_tenure5,name='10+ years',opacity = .5),
        go.Histogram(x=x_tenure6,name='1 year',opacity = .5),
        go.Histogram(x=x_status1,name='Full-time',opacity = .5),
        go.Histogram(x=x_status2,name='Part-time',opacity = .5),
        go.Histogram(x=x_status2,name='Seasonal',opacity = .5),
        go.Histogram(x=x_status2,name='Part-time, Seasonal',opacity = .5)
     
     ]
#defining layout
    
    else:
        trace = go.Histogram(x=df2[selected_feature1],
                         marker=dict(color='rgb(0, 0, 100)'))

    return {
        'data': [trace],
        'layout': go.Layout(title=f'Metrics considered: {item1.title()}',
                            colorway=["#EF963B", "#EF533B"], hovermode="closest",
                            xaxis={'title': "Distribution", 
                                   'titlefont': {'color': 'black', 'size': 14},
                                   'tickfont': {'size': 14, 'color': 'black'}},
                            yaxis={'title': "Frequency", 
                                   'titlefont': {'color': 'black', 'size': 14, },
                                   'tickfont': {'color': 'black'}})}
        

if __name__ == '__main__':
    app.run_server(debug=True)

