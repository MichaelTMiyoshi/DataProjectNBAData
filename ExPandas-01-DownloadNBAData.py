# Michael T. Miyoshi
# 03/20/2020
# from https://realpython.com/pandas-python-explore-dataset/
# this just downloads the data (CSV) from a website to a file.

import requests
download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status()     # check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")