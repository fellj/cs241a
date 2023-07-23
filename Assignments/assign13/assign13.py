import pandas as pd # Our data manipulation library
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods
import os # Used to change the directory to the right place

#basketball_players.csv - contains the stats for each player for a given season.
#basketball_master.csv - contains additional information about the players, such as biographical information, etc.


os.chdir("J:/John/Programming/Thonny/CS241/Assignments/assign13")

players = pd.read_csv("basketball_players.csv", low_memory = False)


# The "master" data (basketball_master.csv) has names, biographical information, etc.
master = pd.read_csv("basketball_master.csv")
#print(master)

# We can do a left join to "merge" these two datasets together
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")


## Part II: COME UP WITH SUPPORTING EVIDENCE

# Question 01. Some players score a lot of points
#              because they attempt a lot of shots.
#              Among players that have scored a lot
#              of points, are there some that are much
#              more efficient (points per attempt) than others?

# View Data
print(nba[["year", "useFirst", "lastName", "points", "ftAttempted"]])

# Remove entries where GP=0
nba = nba[nba.GP > 0]

# Only include those who make points above the median of all players
points_max   = nba.points.max()
points_median = nba.points.median()
points_mid   = points_max - ((points_max - points_median) / 2)
nba = nba[nba.points > points_mid]

# Create new dataset
nba_attempts = nba[["fgMade", "fgAttempted"]]


# Let's just remove any rows with fgAttempted=0
nba_attempts = nba_attempts[nba_attempts.fgAttempted > 0.0]

print(nba_attempts)

# Show Regression of shots made to shot attempts
sns.regplot(data=nba_attempts, x="fgMade", y="fgAttempted").set_title("Success Rate for Goal Attempts Among Highest Point Players")
plt.show()

# Question 02. It seems like some players may excel in one
#              statistical category, but produce very little
#              in other areas. Are there any players that are
#              exceptional across many categories?

# Create new ability datset
nba_overall_ability = nba[["playerID", "points", "steals", "blocks", "rebounds", "turnovers"]]

# Let's remove any rows with zero ability
nba_overall_ability = nba_overall_ability[nba_overall_ability.points > 0]
nba_overall_ability = nba_overall_ability[nba_overall_ability.steals > 0]
nba_overall_ability = nba_overall_ability[nba_overall_ability.blocks > 0]
nba_overall_ability = nba_overall_ability[nba_overall_ability.rebounds > 0]
nba_overall_ability = nba_overall_ability[nba_overall_ability.turnovers > 0]

print(nba_overall_ability)

# Group by player
nba_overall_ability_by_player = nba_overall_ability.groupby("playerID")["points","steals","blocks","rebounds","turnovers"].median()

print(nba_overall_ability_by_player)

# Show players having high stats in all categories in descending order
print(nba_overall_ability_by_player[["points", "steals","blocks","rebounds","turnovers"]].sort_values(["points", "steals","blocks","rebounds","turnovers"], ascending=False).head(10))


# Question 03. Much has been said about the rise of the
#              three-point shot in recent years. It seems
#              that players are shooting and making more
#              three-point shots than ever. Recognizing
#              that this dataset doesn't contain the very
#              most recent data, do you see a trend of more
#              three-point shots either across the league or
#              among certain groups of players? Is there a point
#              at which popularity increased dramatically?

# Create new dataset
nba_three_point_shots = nba[["threeAttempted","threeMade","year","tmID"]]

print(nba_three_point_shots)

# Remove years with zero three point attempts
nba_three_point_shots = nba_three_point_shots[nba_three_point_shots["threeAttempted"] > 0]

# Group by Year
nba_three_point_shots_by_yr = nba_three_point_shots.groupby(["year"])["threeAttempted"].median()

print(nba_three_point_shots_by_yr)

nba_three_point_shots_by_yr = nba_three_point_shots_by_yr.reset_index()

sns.regplot(data=nba_three_point_shots_by_yr, x="year", y="threeAttempted").set_title("Three Point Shot Trend")
plt.show()


## Part III: SHOW CREATIVITY

# Question 01: Many sports analysts argue about
#              which player is the GOAT
#              (the Greatest Of All Time). Based
#              on this data, who would you say is
#              the GOAT? Provide evidence to back
#              up your decision.

# See output from Part II Question 02.

# Question 02: The biographical data in this dataset
#              contains information about home towns,
#              home states, and home countries for
#              these players. Can you find anything
#              interesting about players who came from
#              a similar location?

# Create dataset
nba_bthState = nba[["birthState", "points", "steals", "blocks", "rebounds", "turnovers"]]

print(nba_bthState)


# Let's remove any rows with zero ability
nba_bthState = nba_bthState[nba_bthState.points > 0]
nba_bthState = nba_bthState[nba_bthState.steals > 0]
nba_bthState = nba_bthState[nba_bthState.blocks > 0]
nba_bthState = nba_bthState[nba_bthState.rebounds > 0]
nba_bthState = nba_bthState[nba_bthState.turnovers > 0]

nba_bthState = nba_bthState.reset_index()
sns.catplot(x="birthState", y="points", jitter=False, data=nba_bthState)
plt.show()
sns.catplot(x="birthState", y="steals", jitter=False, data=nba_bthState)
plt.show()
sns.catplot(x="birthState", y="blocks", jitter=False, data=nba_bthState)
plt.show()
sns.catplot(x="birthState", y="rebounds", jitter=False, data=nba_bthState)
plt.show()
sns.catplot(x="birthState", y="turnovers", jitter=False, data=nba_bthState)
plt.show()


# Question 03: Find something else in this dataset
#              that you consider interesting. Produce a graph
#              to communicate your insight.

# Create dataset
nba_height = nba[["blocks", "points", "height"]]

# Remove cases with zero points or blocks
nba_height = nba_height[nba_height.points > 0]
nba_height = nba_height[nba_height.blocks > 0]

print(nba_height)

sns.regplot(data=nba_height, x="height", y="points").set_title("Field Goal Rate in relation to Player Height")
plt.show()

sns.regplot(data=nba_height, x="height", y="blocks").set_title("Block Rate in relation to Player Height")
plt.show()




