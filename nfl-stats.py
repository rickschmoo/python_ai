import csv

# nfl-stats.py
"""
open the CSV file called "nfl_offsensive_stats.csv" 
and read in the data, print out the number of rows and columns
"""
# The code reads in the data from the CSV file and prints out the number of rows and columns in the data.
# The pandas library is used to read in the data and the shape attribute is used to get the number of rows and columns.
# The number of rows and columns is then printed out to the screen.
# import pandas as pd   # import the pandas library
# nfl_stats = pd.read_csv("nfl_offensive_stats.csv")  # read in the data
# rows, cols = nfl_stats.shape  # get the number of rows and columns
# print("There are", rows, "rows and", cols, "columns in the data")
# open the csv file
with open('nfl_offensive_stats.csv', 'r') as f:
    # read the csv data
    data = list(csv.reader(f))


"""
the 3rd column in data is player position, the fourth column
is the player, and the 8th column is the passing yards.
For each player whose position in column 3 is "QB",
determine the sum of yards from column 8
"""
# The code filters the data to only include rows where the player position is "QB" and then calculates the sum of passing yards for those players.
# The loc method is used to filter the data based on the player position column and then the passing yards column is summed.

# create a dictionary to hold the player name and passing yards
passing_yards = {}

# loop through the data
for row in data:
    # check if the player is a quarterback
    if row[2] == 'QB':
        # check if the player is already in the dictionary
        if row[3] in passing_yards:
            # add the passing yards to the existing value
            passing_yards[row[3]] += int(row[7])
        else:
            # add the player to the dictionary
            passing_yards[row[3]] = int(row[7])

"""
print the sum of the passing yards sorted by sum
of passing yards in descending order.
Do not include Tom Brady because he wins too much
"""
for player in sorted(passing_yards, key=passing_yards.get, reverse=True):
    if player != "Tom Brady":
        print(player, passing_yards[player])

