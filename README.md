# DataProjectNBAData
Data project example for Python.
Uses skills developed from website: https://realpython.com/pandas-python-explore-dataset/

file: ExPandas-01-DownloadNBAData.py
Downloads csv file from website: https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv
Saves the file as nba_all_elo.csv

file: ExPandas-02A-PlotNBAData.py
Puts the csv data into a Pandas DataFrame and outputs the data using MatPlotLib
Saves the file as NBAmplib.png

file: ExPandas-02B-PlotNBADataPlotly.py
Puts the csv data into a Pandas DataFrame and outputs the data using Plotly
Saves the file as timeSeriesNBANoYear.html
This iteration of the plotting does not display the year but rather integers starting at 0 on the x-axis

file: DataProjNBAStats.py
This file is a larger project that takes the skills from the tutorial website and codes the Python Console commands
into one file.  There are options to display different parts of the file.  And lastly, an option to display the 
data (Knicks' points every year) as a line graph. This  graph is stored as an html file.
Saves the file as timeSeriesNicksNBA.html

The main lesson learned from this project was that you need to understand your data.
You can download the data.  You can display the rows, columns, and even cells of the
data, but you need to be able to truly understand what the data is telling you to be
able to give it meaning to somebody else.  And that is when and where the coding comes in.
(By the way, you can open your data in a spreadsheet to look at it closely.)

This project also has all the introductory fundamentals of Python:
  Output
  Input
  Variables
  Branching
  Looping
  (no functions)

It also obviously includes working with a few different modules (Pandas, MatPlotLib, Plotly, NumPy) 
that help to organize and visualize data.  Which was the main goal of the project.
