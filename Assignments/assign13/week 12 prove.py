import pandas as pd # Our data manipulation library
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods
import os # Used to change the directory to the right place

#basketball_players.csv - contains the stats for each player for a given season.
#basketball_master.csv - contains additional information about the players, such as biographical information, etc.


os.chdir("J:/Programming/Thonny/CS241/Assignments/assign13")

players = pd.read_csv("basketball_players.csv", low_memory = False)

#print(players.columns)

#############################################################################################################################
                                                                                                                           
#Calculate the mean and median number of points scored.                                                                    
                                                                                                                           
#mean points scored for season                                                                                              
mean = players["points"].mean()                                                                                             
print("Mean points: " + str((mean)))                                                                                       
                                                                                                                            
#median points scored for season                                                                                            
median = players["points"].median()                                                                                         
print("Median points: " + str(median))                                                                                      
##############################################################################################################################
#highest number of points recorded in a single season. Identify player who scored those points and the year they did so.
#print(players[["playerID", "year", "tmID", "points"]].sort_values("points", ascending=False).head(1))

# The "master" data (basketball_master.csv) has names, biographical information, etc.
master = pd.read_csv("basketball_master.csv")
#print(master)

# We can do a left join to "merge" these two datasets together
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")

#print(nba.columns)
print("Highest number of points recorded in a single season; Player & Year")
print(nba[["year", "useFirst", "lastName", "tmID", "points"]].sort_values("points", ascending=False).head(1))

#############################################################################################################################

nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
#print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]].sort_values("reboundsPerGame", ascending=False).head(10))

# Let's just remove any rows with GP=0
nba = nba[nba.GP > 0]

nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
#print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]].sort_values("reboundsPerGame", ascending=False).head(10))

#############################################################################################################################

#Produce a boxplot that shows the distribution of total points, total assists, and total rebounds
#(each of these three is a separate box plot, but they can be on the same scale and in the same graphic).

sns.boxplot(data=nba[["points", "assists", "rebounds"]])
# Show the current plot
plt.show()

##############################################################################################################################

#Produce a plot that shows how the number of points scored has changed over time by showing the median of points scored per year, over time.
#The x-axis is the year and the y-axis is the median number of points among all players for that year.

nba_grouped_year = nba[["points", "year"]].groupby("year").median()
print(nba_grouped_year)

#In order to plot this data, we need to change the index to be the year now, rather than the id that it was previously.
#Then we can plot it along with a linear regression line

nba_grouped_year = nba_grouped_year.reset_index()
#sns.regplot(data=nba_grouped_year, x="year", y="points")
#plt.show()

# Take out any years where points were not counted
nba_grouped_year = nba_grouped_year[nba_grouped_year["points"] > 0]

#let's also put a title on the plot.
sns.regplot(data=nba_grouped_year, x="year", y="points").set_title("Median Points per Year")
plt.show()

## Part II: COME UP WITH SUPPORTING EVIDENCE

# Question 01. Some players score a lot of points
#              because they attempt a lot of shots.
#              Among players that have scored a lot
#              of points, are there some that are much
#              more efficient (points per attempt) than others?

# View Data
print(nba[["year", "useFirst", "lastName", "points", "ftAttempted"]])

nba_grouped_year = nba[["points", "year", "lastName", "fgAttempted"]].groupby("lastName").median()
print(nba_grouped_year)

# Get Points Per Attempt
nba_grouped_year["pointPerAttempt"] = nba_grouped_year["points"] / nba_grouped_year["fgAttempted"]



# Show Regression
sns.regplot(data=nba, x="lastName", y="pointPerAttempt").set_title("Number of Shot Attempts")
plt.show()

sns.boxplot(data=nba_grouped_year[["lastName", "pointperAttempt"]])
# Show the current plot
plt.show()
