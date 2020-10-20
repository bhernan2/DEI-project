import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.offline as py
import plotly.tools as tls

dei = pd.read_csv("DEISurveyFinal.csv")

def FC_fig1():
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
            xanchor='right',
            yanchor= 'top',
            font=dict(
                size=25,
                color='#000000'
            )

        ),
        margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
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
            type = 'buttons', 
            bordercolor = "#3f3f3f",
            xanchor='right',
            yanchor='top')
        ]),
        barmode='stack',
        width=1400, 
        height=800,
        paper_bgcolor='#FFFFFF',
        plot_bgcolor='#FFFFFF')
    #defining layout and plotting
    fig = go.Figure(data,layout)
    #fig.add_layout_image(
        #dict(
            #source="/assets/foundcom-logo-ffce54.png",
            #xref="paper", yref="paper",
            #x=1, y=1.05,
            #sizex=0.1, sizey=0.1,
            #xanchor="right", yanchor="bottom"
        #)
    #)
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    return fig







