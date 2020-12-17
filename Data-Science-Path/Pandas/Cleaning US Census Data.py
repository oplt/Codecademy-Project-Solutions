# How to clean data with Python

# Cleaning US Census Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

# Using glob, loop through the census files available and load them into DataFrames. 
# Then, concatenate all of those DataFrames together into one DataFrame, called something like us_census
files = glob.glob("states*.csv")
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)
print(us_census.head())

# turn the Income column into a format that is ready for conversion into a numerical type
us_census["Income"] = us_census["Income"].replace('[\$,]', '', regex=True)
us_census["Income"] = pd.to_numeric(us_census.Income)
print(us_census.head())

# Look at the GenderPop column. 
# We are going to want to separate this into two columns, the Men column, and the Women column.
# Split the column into those two new columns using str.split and separating out those results
us_census["Men"] = us_census["GenderPop"].str.split("_").str[0]
us_census["Women"] = us_census["GenderPop"].str.split("_").str[1]
print(us_census.head())

# Convert both of the columns into numerical datatypes.
# There is still an M or an F character in each entry! We should remove those before we convert.
us_census["Men"] = us_census["Men"].replace("[M,]", "", regex=True)
us_census["Men"] = pd.to_numeric(us_census.Men)
us_census["Women"] = us_census["Women"].replace("[F,]", "", regex=True)
us_census["Women"] = pd.to_numeric(us_census.Women)
print(us_census.head())

# As an estimate for the nan values in the Women column, you could use the TotalPop of that state minus the Men for that state.
us_census = us_census.fillna(value={"Women": us_census["TotalPop"] - us_census["Men"]})

# drop duplicates
us_census = us_census.drop_duplicates()
print(us_census.head())
print(us_census.Women)

# Use matplotlib to make a scatterplot
plt.scatter(us_census["Women"], us_census["Income"], color=["red","green"])
plt.xlabel("Women")
plt.ylabel("Income")
plt.show()
plt.cla()

# clean the race columns and convert all to numeric
us_census["Hispanic"] = us_census["Hispanic"].replace("[%,]", "", regex=True)
us_census["Hispanic"] = pd.to_numeric(us_census.Hispanic)
us_census["White"] = us_census["White"].replace("[%,]", "", regex=True)
us_census["White"] = pd.to_numeric(us_census.White)
us_census["Black"] = us_census["Black"].replace("[%,]", "", regex=True)
us_census["Black"] = pd.to_numeric(us_census.Black)
us_census["Native"] = us_census["Native"].replace("[%,]", "", regex=True)
us_census["Native"] = pd.to_numeric(us_census.Native)
us_census["Asian"] = us_census["Asian"].replace("[%,]", "", regex=True)
us_census["Asian"] = pd.to_numeric(us_census.Asian)
us_census["Pacific"] = us_census["Pacific"].replace("[%,]", "", regex=True)
us_census["Pacific"] = pd.to_numeric(us_census.Pacific)

# fill the nan values in race columns
print(us_census.Hispanic.isna().value_counts())
print(us_census.White.isna().value_counts())
print(us_census.Black.isna().value_counts())
print(us_census.Native.isna().value_counts())
print(us_census.Asian.isna().value_counts())
print(us_census.Pacific.isna().value_counts())

us_census['Pacific'] = us_census['Pacific'].fillna(value = {100 - (us_census['Hispanic'] + us_census['Black'] + us_census['White'] + us_census['Native'] + us_census['Asian'])})

# make a histogram for each one
plt.hist(us_census.Hispanic)
plt.show()
plt.hist(us_census.White)
plt.show()
plt.hist(us_census.Black)
plt.show()
plt.hist(us_census.Native)
plt.show()
plt.hist(us_census.Asian)
plt.show()
plt.hist(us_census.Pacific)
plt.show()