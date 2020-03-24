# Michael T. Miyoshi
# 03/23/2020
# from (mostly) https://realpython.com/pandas-python-explore-dataset/
# extrapolation from the website and the plotly examples
# See comments at the end of the code.  Kept it there because it relates to option V.

import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
nba = pd.read_csv("nba_all_elo.csv")

# want an interactive project where the user can see the data and plot the data
pd.set_option("display.max.columns", None)  # so the user can see all 23 columns
pd.set_option("display.precision", 2)       # so user only sees 2 decimals of precision

print("Check out the NBA data!")

done = False
while not done:
    print("\nChoose what you would like to see:")
    print("\tA. First 5 lines of the database")
    print("\tB. Last n lines of the database")
    print("\tC. All the Column info")
    print("\tD. A column of info")
    print("\tE. Basic statistics of the numeric data")
    print("\tF. Basic statistics of other data")
    print("\tG. See how often values occur in a column")
    print("\tH. Sum of all the Boston Celtics points in the data set")  # aggregate fns
    print("\tI. Total points per franchise")        # groupby()
    print("\tJ. Spurs wins and losses since: ")
    print("\tK. ")
    print("\tL. Where did the Lakers play?")
    print("\tV. Visualize some data")
    print("\tQ. Quit\n")
    reply = input().upper()
    if reply == "Q" or reply == "X":
        print("Thanks for playing...")
        done = True
    elif reply == "A":
        print(nba.head())
    elif reply == "B":
        n = int(input("How many rows?  "))
        print(nba.tail(n))
    elif reply == "C":
        print(nba.info())
    elif reply == "D":
        print(nba.info())
        col = input("Which column?  (Match exact name not column number):  ")
        print(nba[col])
    elif reply == "E":
        print(nba.describe())
    elif reply == "F":
        print(nba.describe(include=np.object))
    elif reply == "G":
        print("\n\nTEAM IDs:")
        print(nba["team_id"].value_counts())
        print("\n\nFranchise IDs:")
        print(nba["fran_id"].value_counts())
    elif reply == "L":  # out of order, because L stands for Lakers (exercise came after G)
        print("\nWhich Lakers?\n")
        print(nba.loc[nba["fran_id"] == "Lakers", "team_id"].value_counts())
        print("\nMinneapolis Lakers")
        print(nba.loc[nba["team_id"] == "MNL", "date_game"].min())
        print(nba.loc[nba["team_id"] == "MNL", "date_game"].max())
        print(nba.loc[nba["team_id"] == "MNL", "date_game"].agg(("min", "max")))
        print("\nLos Angeles Lakers")
        print(nba.loc[nba["team_id"] == "LAL", "date_game"].agg(("min", "max")))
    elif reply == "H":  # B was already taken
        print("\nBoston Celtics\nTotal points scored: ", end="")
        print(nba.loc[nba["team_id"] == "BOS", "pts"].sum())
        print("Points as home team: ", end="")
        print(nba.loc[(nba["team_id"] == "BOS") & (nba["_iscopy"] == 0), "pts"].sum())
        print("Points as away team: ", end="")
        print(nba.loc[(nba["opp_id"] == "BOS") & (nba["_iscopy"] == 0), "opp_pts"].sum())
    elif reply == "I":  # I know the alpha order is off now, but it will be okay after L
        print("Points scored by franchise:")
        print(nba.groupby("fran_id", sort=False)["pts"].sum())
    elif reply == "J":
        year = int(input("Pick a year: "))
        print(nba[(nba["fran_id"] == "Spurs") & (year < nba["year_id"])].groupby(["year_id", "game_result"])["game_id"].count())
    elif reply == "K":
        print()
    elif reply == "V":
        print("Getting data ready to visualize...")
        # ought to work.  There is an x value ("year_id") and y value ["pts"].sum()
        # they are in the pandas dataframe called nba and the specifics listed
        # confusing.  stopping for the day.  03/19/2020
        # data = [go.Scatter(
        #    x=nba[nba["fran_id"] == "Knicks" & ("year_id")],
        #    y=nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum()
        # )]
        grouped = nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum()
        # print(grouped)
        # print(grouped.index)
        # print(grouped.values)
        data = [go.Scatter(
            # grouped,
            x = grouped.index,
            y = grouped.values
        )]

        plotly.offline.plot(data, filename="timeSeriesNicksNBA.html")

# Option V. Visualize some data
# Could not get the x-axis correct when just using the commented section above
# below where it says "ought to work."  Tried several things for the x values.
# The problem lies in the fact that the Pandas DataFrame is aggregating data.
# This means that the aggregate data does not have a unique year for each
# set of points.  Rather, the sum of the points for a year will have a specific
# year, but that year does not point to just one row of data.
# The solution ended up being simple.  Create a new series.  The Pandas series
# created is called grouped.  This series has specific years (year_id) as its indices
# and point totals for the values.  The problem then, was that the Pandas series
# is not the same as a Pandas DataFrame.  At least I did not make it so.  I had to
# investigate what a Pandas series was and how to access its indices (keys) and values.
# This investigation led to the code in option V.

# There are surely many more nuances to using plotly and pandas together.
# Option V. is just the start.

# And no.  At this point in time, I do not plan on putting in option K.
# Or any of the options between L and V for that matter.
#           Michael T. Miyoshi...
#           03/23/2020