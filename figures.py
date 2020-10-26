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


def FC_fig2():
#At work, I feel comfortable being myself.  
#defining list_updatemenus
    list_updatemenus = [{'label': 'Total',
                     'method': 'update',
                     'args': [{'visible': [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'At work, I feel comfortable being myself.'}]},
                    {'label': 'Race',
                     'method': 'update',
                     'args': [{'visible': [False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'At work, I feel comfortable being myself.'}]},
                    {'label': 'Age',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'At work, I feel comfortable being myself.'}]},
                    {'label': 'Sexual Orientation',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False]}, {'title': 'At work, I feel comfortable being myself.'}]},
                   {'label': 'Tenure',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False]}, {'title': 'At work, I feel comfortable being myself.'}]},
                   {'label': 'Status',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True]}, {'title': 'At work, I feel comfortable being myself.'}]}
                   ]
#defining graph objects
    x_total = dei['At work, I feel comfortable being myself.  ']
    x_white = dei[dei['What is your race? ']=="White"]["At work, I feel comfortable being myself.  "]
    x_latinx = dei[dei['What is your race? ']=="Latino/Hispanic"]["At work, I feel comfortable being myself.  "]
    x_black = dei[dei['What is your race? ']=="Black/ African American"]["At work, I feel comfortable being myself.  "]
    x_two_plus = dei[dei['What is your race? ']=="Two or more Races"]["At work, I feel comfortable being myself.  "]
    x_asian = dei[dei['What is your race? ']=="Asian"]["At work, I feel comfortable being myself.  "]
    x_first_peoples = dei[dei['What is your race? ']=="Indian/ Native American"]["At work, I feel comfortable being myself.  "]
    x_age1 = dei[dei["What is your age?"]=="25-34"]["At work, I feel comfortable being myself.  "]
    x_age2 = dei[dei["What is your age?"]=="35-44"]["At work, I feel comfortable being myself.  "]
    x_age3 = dei[dei["What is your age?"]=="45-54"]["At work, I feel comfortable being myself.  "]
    x_age4 = dei[dei["What is your age?"]=="55-64"]["At work, I feel comfortable being myself.  "]
    x_age5 = dei[dei["What is your age?"]=="18-24"]["At work, I feel comfortable being myself.  "]
    x_age6 = dei[dei["What is your age?"]=="65-74"]["At work, I feel comfortable being myself.  "]
    x_straight = dei[dei["What is your sexual orientation?"]=="Straight"]["At work, I feel comfortable being myself.  "]
    x_lgbtq = dei[dei["What is your sexual orientation?"]=="LGBTQ+"]["At work, I feel comfortable being myself.  "]
    x_tenure1 = dei[dei["How long have you worked for FC?"]=="1-3 years"]["At work, I feel comfortable being myself.  "]
    x_tenure2 = dei[dei["How long have you worked for FC?"]=="3-5 years"]["At work, I feel comfortable being myself.  "]
    x_tenure3 = dei[dei["How long have you worked for FC?"]=="Less than a year"]["At work, I feel comfortable being myself.  "]
    x_tenure4 = dei[dei["How long have you worked for FC?"]=="5-10 years"]["At work, I feel comfortable being myself.  "]
    x_tenure5 = dei[dei["How long have you worked for FC?"]=="10+ years"]["At work, I feel comfortable being myself.  "]
    x_tenure6 = dei[dei["How long have you worked for FC?"]=="1 year"]["At work, I feel comfortable being myself.  "]
    x_status1 = dei[dei["What is your employment status?"]=="Full-time"]["At work, I feel comfortable being myself.  "]
    x_status2 = dei[dei["What is your employment status?"]=="Part-time"]["At work, I feel comfortable being myself.  "]
    x_status3 = dei[dei["What is your employment status?"]=="Seasonal"]["At work, I feel comfortable being myself.  "]
    x_status4 = dei[dei["What is your employment status?"]=="Part-time, Seasonal"]["At work, I feel comfortable being myself.  "]
#defining data
    data=[
        go.Histogram(x=x_total,name='   ',opacity = .75),
        go.Histogram(x=x_white,name='White',opacity = .75),
        go.Histogram(x=x_latinx,name='Latino/Hispanic',opacity = .75),
        go.Histogram(x=x_black,name='Black/African American',opacity = .75),
        go.Histogram(x=x_two_plus,name='Two or more Races',opacity = .75),
        go.Histogram(x=x_asian,name='Asian',opacity = .5),
        go.Histogram(x=x_first_peoples,name='Indian/Native American',opacity = .75),
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
            text='At work, I feel comfortable being myself.',
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


def FC_fig3():
    #Employees in my organization are treated with respect and dignity.  
    #defining list_updatemenus
    #defining list_updatemenus
    list_updatemenus = [{'label': 'Total',
                     'method': 'update',
                     'args': [{'visible': [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Employees in my organization are treated with respect and dignity.'}]},
                    {'label': 'Race',
                     'method': 'update',
                     'args': [{'visible': [False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Employees in my organization are treated with respect and dignity.'}]},
                    {'label': 'Age',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Employees in my organization are treated with respect and dignity.'}]},
                    {'label': 'Sexual Orientation',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Employees in my organization are treated with respect and dignity.'}]},
                   {'label': 'Tenure',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False]}, {'title': 'Employees in my organization are treated with respect and dignity.'}]},
                   {'label': 'Status',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True]}, {'title': 'Employees in my organization are treated with respect and dignity.'}]}
                   ]
    #defining graph objects
    x_total = dei["Employees in my organization are treated with respect and dignity.  "]
    x_white = dei[dei['What is your race? ']=="White"]["Employees in my organization are treated with respect and dignity.  "]
    x_latinx = dei[dei['What is your race? ']=="Latino/Hispanic"]["Employees in my organization are treated with respect and dignity.  "]
    x_black = dei[dei['What is your race? ']=="Black/ African American"]["Employees in my organization are treated with respect and dignity.  "]
    x_two_plus = dei[dei['What is your race? ']=="Two or more Races"]["Employees in my organization are treated with respect and dignity.  "]
    x_asian = dei[dei['What is your race? ']=="Asian"]["Employees in my organization are treated with respect and dignity.  "]
    x_first_peoples = dei[dei['What is your race? ']=="Indian/ Native American"]["Employees in my organization are treated with respect and dignity.  "]
    x_age1 = dei[dei["What is your age?"]=="25-34"]["Employees in my organization are treated with respect and dignity.  "]
    x_age2 = dei[dei["What is your age?"]=="35-44"]["Employees in my organization are treated with respect and dignity.  "]
    x_age3 = dei[dei["What is your age?"]=="45-54"]["Employees in my organization are treated with respect and dignity.  "]
    x_age4 = dei[dei["What is your age?"]=="55-64"]["Employees in my organization are treated with respect and dignity.  "]
    x_age5 = dei[dei["What is your age?"]=="18-24"]["Employees in my organization are treated with respect and dignity.  "]
    x_age6 = dei[dei["What is your age?"]=="65-74"]["Employees in my organization are treated with respect and dignity.  "]
    x_straight = dei[dei["What is your sexual orientation?"]=="Straight"]["Employees in my organization are treated with respect and dignity.  "]
    x_lgbtq = dei[dei["What is your sexual orientation?"]=="LGBTQ+"]["Employees in my organization are treated with respect and dignity.  "]
    x_tenure1 = dei[dei["How long have you worked for FC?"]=="1-3 years"]["Employees in my organization are treated with respect and dignity.  "]
    x_tenure2 = dei[dei["How long have you worked for FC?"]=="3-5 years"]["Employees in my organization are treated with respect and dignity.  "]
    x_tenure3 = dei[dei["How long have you worked for FC?"]=="Less than a year"]["Employees in my organization are treated with respect and dignity.  "]
    x_tenure4 = dei[dei["How long have you worked for FC?"]=="5-10 years"]["Employees in my organization are treated with respect and dignity.  "]
    x_tenure5 = dei[dei["How long have you worked for FC?"]=="10+ years"]["Employees in my organization are treated with respect and dignity.  "]
    x_tenure6 = dei[dei["How long have you worked for FC?"]=="1 year"]["Employees in my organization are treated with respect and dignity.  "]
    x_status1 = dei[dei["What is your employment status?"]=="Full-time"]["Employees in my organization are treated with respect and dignity.  "]
    x_status2 = dei[dei["What is your employment status?"]=="Part-time"]["Employees in my organization are treated with respect and dignity.  "]
    x_status3 = dei[dei["What is your employment status?"]=="Seasonal"]["Employees in my organization are treated with respect and dignity.  "]
    x_status4 = dei[dei["What is your employment status?"]=="Part-time, Seasonal"]["Employees in my organization are treated with respect and dignity.  "]

    #defining data
    data=[
        go.Histogram(x=x_total,name='   ',opacity = .75),
        go.Histogram(x=x_white,name='White',opacity = .75),
        go.Histogram(x=x_latinx,name='Latino/Hispanic',opacity = .75),
        go.Histogram(x=x_black,name='Black/African American',opacity = .75),
        go.Histogram(x=x_two_plus,name='Two or more Races',opacity = .75),
        go.Histogram(x=x_asian,name='Asian',opacity = .5),
        go.Histogram(x=x_first_peoples,name='Indian/Native American',opacity = .75),
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
            text='Employees in my organization are treated with respect and dignity.',
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


def FC_fig4():
    list_updatemenus = [{'label': 'Total',
                     'method': 'update',
                     'args': [{'visible': [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Employees in my organization are treated with respect and dignity.'}]},
                    {'label': 'Race',
                     'method': 'update',
                     'args': [{'visible': [False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Diversity and Inclusiveness issues are openly discussed.'}]},
                    {'label': 'Age',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Diversity and Inclusiveness issues are openly discussed.'}]},
                    {'label': 'Sexual Orientation',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Diversity and Inclusiveness issues are openly discussed.'}]},
                   {'label': 'Tenure',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False]}, {'title': 'Diversity and Inclusiveness issues are openly discussed.  '}]},
                   {'label': 'Status',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True]}, {'title': 'Diversity and Inclusiveness issues are openly discussed.  '}]}
                   ]
    #defining graph objects
    x_total = dei["Diversity and Inclusiveness issues are openly discussed.  "]
    x_white = dei[dei['What is your race? ']=="White"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_latinx = dei[dei['What is your race? ']=="Latino/Hispanic"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_black = dei[dei['What is your race? ']=="Black/ African American"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_two_plus = dei[dei['What is your race? ']=="Two or more Races"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_asian = dei[dei['What is your race? ']=="Asian"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_first_peoples = dei[dei['What is your race? ']=="Indian/ Native American"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_age1 = dei[dei["What is your age?"]=="25-34"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_age2 = dei[dei["What is your age?"]=="35-44"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_age3 = dei[dei["What is your age?"]=="45-54"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_age4 = dei[dei["What is your age?"]=="55-64"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_age5 = dei[dei["What is your age?"]=="18-24"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_age6 = dei[dei["What is your age?"]=="65-74"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_straight = dei[dei["What is your sexual orientation?"]=="Straight"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_lgbtq = dei[dei["What is your sexual orientation?"]=="LGBTQ+"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_tenure1 = dei[dei["How long have you worked for FC?"]=="1-3 years"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_tenure2 = dei[dei["How long have you worked for FC?"]=="3-5 years"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_tenure3 = dei[dei["How long have you worked for FC?"]=="Less than a year"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_tenure4 = dei[dei["How long have you worked for FC?"]=="5-10 years"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_tenure5 = dei[dei["How long have you worked for FC?"]=="10+ years"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_tenure6 = dei[dei["How long have you worked for FC?"]=="1 year"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_status1 = dei[dei["What is your employment status?"]=="Full-time"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_status2 = dei[dei["What is your employment status?"]=="Part-time"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_status3 = dei[dei["What is your employment status?"]=="Seasonal"]["Diversity and Inclusiveness issues are openly discussed.  "]
    x_status4 = dei[dei["What is your employment status?"]=="Part-time, Seasonal"]["Diversity and Inclusiveness issues are openly discussed.  "]
#defining data
    data=[
        go.Histogram(x=x_total,name='   ',opacity = .75),
        go.Histogram(x=x_white,name='White',opacity = .75),
        go.Histogram(x=x_latinx,name='Latino/Hispanic',opacity = .75),
        go.Histogram(x=x_black,name='Black/African American',opacity = .75),
        go.Histogram(x=x_two_plus,name='Two or more Races',opacity = .75),
        go.Histogram(x=x_asian,name='Asian',opacity = .5),
        go.Histogram(x=x_first_peoples,name='Indian/Native American',opacity = .75),
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
            text='Diversity and Inclusiveness issues are openly discussed.',
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

def FC_fig5():
    list_updatemenus = [{'label': 'Total',
                     'method': 'update',
                     'args': [{'visible': [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.'}]},
                    {'label': 'Race',
                     'method': 'update',
                     'args': [{'visible': [False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.'}]},
                    {'label': 'Age',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.'}]},
                    {'label': 'Sexual Orientation',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False]}, {'title': 'Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.'}]},
                   {'label': 'Tenure',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, False, False, False, False]}, {'title': 'Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  '}]},
                   {'label': 'Status',
                     'method': 'update',
                     'args': [{'visible': [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True]}, {'title': 'Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  '}]}
                   ]
    #defining graph objects
    x_total = dei["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_white = dei[dei['What is your race? ']=="White"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_latinx = dei[dei['What is your race? ']=="Latino/Hispanic"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_black = dei[dei['What is your race? ']=="Black/ African American"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_two_plus = dei[dei['What is your race? ']=="Two or more Races"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_asian = dei[dei['What is your race? ']=="Asian"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_first_peoples = dei[dei['What is your race? ']=="Indian/ Native American"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_age1 = dei[dei["What is your age?"]=="25-34"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_age2 = dei[dei["What is your age?"]=="35-44"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_age3 = dei[dei["What is your age?"]=="45-54"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_age4 = dei[dei["What is your age?"]=="55-64"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_age5 = dei[dei["What is your age?"]=="18-24"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_age6 = dei[dei["What is your age?"]=="65-74"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_straight = dei[dei["What is your sexual orientation?"]=="Straight"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_lgbtq = dei[dei["What is your sexual orientation?"]=="LGBTQ+"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_tenure1 = dei[dei["How long have you worked for FC?"]=="1-3 years"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_tenure2 = dei[dei["How long have you worked for FC?"]=="3-5 years"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_tenure3 = dei[dei["How long have you worked for FC?"]=="Less than a year"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_tenure4 = dei[dei["How long have you worked for FC?"]=="5-10 years"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_tenure5 = dei[dei["How long have you worked for FC?"]=="10+ years"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_tenure6 = dei[dei["How long have you worked for FC?"]=="1 year"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_status1 = dei[dei["What is your employment status?"]=="Full-time"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_status2 = dei[dei["What is your employment status?"]=="Part-time"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_status3 = dei[dei["What is your employment status?"]=="Seasonal"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    x_status4 = dei[dei["What is your employment status?"]=="Part-time, Seasonal"]["Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.  "]
    #defining data
    data=[
        go.Histogram(x=x_total,name='   ',opacity = .75),
        go.Histogram(x=x_white,name='White',opacity = .75),
        go.Histogram(x=x_latinx,name='Latino/Hispanic',opacity = .75),
        go.Histogram(x=x_black,name='Black/African American',opacity = .75),
        go.Histogram(x=x_two_plus,name='Two or more Races',opacity = .75),
        go.Histogram(x=x_asian,name='Asian',opacity = .5),
        go.Histogram(x=x_first_peoples,name='Indian/Native American',opacity = .75),
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
    #defining layout
    layout=go.Layout(
        title=dict(
            text='Everyone at this organization is treated fairly regardless of ethnic background, race, gender, age, disability, or other differences not related to job performance.',
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

    #def FC_fig6():


