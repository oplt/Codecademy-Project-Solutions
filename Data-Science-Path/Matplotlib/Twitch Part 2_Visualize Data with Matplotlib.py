# In this part of the project, you will be taking your findings from the SQL queries and visualize them using Python and Matplotlib, in the forms of:
# - Bar Graph: Featured Games
# - Pie Chart: Stream Viewers’ Locations
# - Line Graph: Time Series Analysis
# The Twitch Science Team provided this practice dataset. 
# You can download the .csv files (800,000 rows) from GitHub.

import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

# use the plt.bar() to plot a bar graph using range(len(games)) and viewers as arguments 
# add a title, a legend, axis labels, ticks, tick labels (rotate if necessary)
plt.bar(range(len(games)), viewers, color = "green", label = "viewers")
plt.title("Game Viewers")
plt.legend(["Twitch"])
plt.xlabel("Games")
plt.ylabel ("Viewers")
plt.subplot().set_xticks(range(len(games)))
plt.subplot().set_xticklabels(games, rotation=90)
plt.show()
plt.clf()

# Pie Chart: League of Legends Viewers' Whereabouts
labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]
countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

# plot a pie chart
# Add the explode, shadows, percentages, and turn the pie 345 degrees, Configure the percentages’ placement
plt.pie(countries, explode=explode, colors=colors, shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)
plt.title("League of Legends Viewers' Whereabouts")
plt.legend(labels, loc="right")
plt.show()
plt.clf()


# Line Graph: Time Series Analysis

hour = range(24)
viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

# Plot a line graph.
# Don’t forget to throw in hour and viewers_hour.
# Then, add the title, the axis labels, legend, and ticks.
# Lastly, use plt.show() to visualize.
plt.plot(hour, viewers_hour)
plt.title("Time Series")
plt.xlabel("Hour")
plt.ylabel("Viewers")
plt.legend(['2015-01-01'])
ax = plt.subplot()
ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])
plt.show()

y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)
plt.show()