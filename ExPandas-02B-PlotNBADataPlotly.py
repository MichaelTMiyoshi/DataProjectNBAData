# Michael T. Miyoshi
# 03/21/2020
# from (sorta) https://realpython.com/pandas-python-explore-dataset/
# extrapolation from the website and the plotly examples

import plotly
import plotly.graph_objs as go
import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")

# ought to work.  There is an x value ("year_id") and y value ["pts"].sum()
# they are in the pandas dataframe called nba and the specifics listed
# confusing.  stopping for the day.  03/19/2020
# 03/20/2020
#   Without the x in go.Scatter, the data plots, but only has 0, 10, 20, etc. as x
#   instead of decade markers
data = [go.Scatter(
#    x=nba[nba["fran_id"] == "Knicks"].groupby("year_id"),
    y=nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum()
)]

plotly.offline.plot(data, filename="timeSeriesNBANoYear.html")