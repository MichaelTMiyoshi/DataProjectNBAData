# Michael T. Miyoshi
# 03/21/2020
# from (sorta) https://realpython.com/pandas-python-explore-dataset/
# uses matplotlib to plot data

import matplotlib.pyplot as plt
import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")

plt.plot(nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum())
plt.savefig("NBAmplib.png")
plt.show()