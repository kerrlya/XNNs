# function for viewing opinion distributions

import plotly.express as px
import pandas as pd

def view_hist(df, x_axis, color, nbins = 300):
    """
    General histogram generating function data. Can choose dataframe and name of column that creates the x_axis.
    NOTE: do not set log_x to True, it doesn't work with this function.
        INPUTS: df (pandas dataframe), x_axis (string, name of column you want to plot), color (str, column that determines 
                colors of overlaying histogram), log_x (bool, make x-axis log), log_y (bool, make y-axis log).
        RETURNS: None
    """

    fig = px.histogram(df, x_axis, color, marginal="violin", # can be `box`, `violin`
                         hover_data=df.columns, nbins = nbins, log_y = False, log_x=False)
    fig.update_layout(barmode='overlay')
    
    # Reduce opacity to see both histograms
    fig.update_traces(opacity=0.5)
    fig.show()


# display distribution of scored tweets from related dataset
# df_related = pd.read_csv("L2reg_scored_SurgeAItweets.csv")

# view_hist(df_related,"score","Category")


# display distribution of scored tweets from unrelated dataset
df_related = pd.read_csv("L2reg_scored_COVIDtweets.csv")

view_hist(df_related,"score",None)