import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#  load data frame
df = pd.read_csv("WorldCupMatches.csv")

# Inspect the DataFrame 
print(df.head())

# Create a new column in df named Total Goals, and set it equal to the sum of the columns Home Team Goals and Away Team Goals
df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"] 

# You are going to create a bar chart visualizing how many goals were scored each year the World Cup was held between 1930-2014.
# Set the style of your plot to be whitegrid . 
# This will add gridlines to the plot which will make it easier to read the visualization.
sns.set_style("whitegrid")

# set the context to be "poster" and arrange the font scale
# sns.set_context("name_of_context", font_scale=0.8) 

# Create a figure and axes for your plot
f, ax = plt.subplots(figsize=(12, 7))

# visualize the columns Year and Total Goals as a bar chart
ax = sns.barplot(x=df["Year"], y = df["Total Goals"])

# Render your bar chart
plt.show()

# Give your bar chart a meaningful title
ax.set_title("Average Goals per Year in World Cup")

# Load goals.csv
df_goals = pd.read_csv("Load goals.csv")

# Try setting the context of the plot to be notebook and the font_scale to be 1.25
sns.set_context("notebook", font_scale=1.25) 

# Create a figure for your second plot.
# Set the variables f, ax2 and instantiate a figure that is 12 inches wide and 7 inches tall
# set ax2 equal to a box plot with the color palette Spectral that visualizes the data in the DataFrame df_goals with the column year on the x-axis and goals on the y-axis
f, ax2 = plt.subplots(x="year", y = "goals, data = df_goals, palette = "Spectral", figsize=(12, 7))

# Give your box plot a title
ax.set_title(" Goals Visualization")

# render your box plot
plt.show()

