import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
#!pip install squarify
#plt.style.use('fivethirtyeight')
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.tools as tls
import pygsheets
#%matplotlib inline
from wordcloud import WordCloud, STOPWORDS

#connect to google sheets
gc = pygsheets.authorize()
#choose which sheet to open
sh = gc.open('Diversity Equity & Inclusion Survey (Responses)')
#get the sheet we want to look at. In our case only one sheet called it wk1 of responses
wk1 = sh.sheet1
#create a dataframe
dei=pd.DataFrame(wk1.get_all_records())

def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off")

#generate word cloud for open ended question
wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='black', colormap='Set2', collocations=False, stopwords=STOPWORDS).generate(dei["Other (please let us know what other efforts you'd like to see prioritized)"].str.cat())
plot_cloud(wordcloud)

def dei_word_cloud():
    fig = wordcloud 
    return fig
