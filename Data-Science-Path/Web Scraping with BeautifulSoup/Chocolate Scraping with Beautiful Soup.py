# WEB SCRAPING

# Chocolate Scraping with Beautiful Soup

import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# make a request to the site to get the raw HTML
webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")

# Create a BeautifulSoup object called soup to traverse this HTML
# Use "html.parser" as the parser
soup = BeautifulSoup(webpage.content, "html.parser")

# print out the soup object to explore the HTML
print(soup)

# Use a command on the soup object to get all of the tags that contain the ratings
ratings_data = soup.find_all(attrs={"class": "Rating"})

# Create an empty list called ratings
ratings = []

# Loop through the ratings tags and get the text contained in each one. 
# Add it to the ratings list.
# As you do this, convert the rating to a float
for rating in ratings_data[1:]:
  ratings.append(float(rating.get_text()))
print(ratings)

#  create a histogram of the ratings values
plt.hist(ratings)
plt.show()

# find all the tags on the webpage that contain the company names
company_data = soup.select(".Company")

# make an empty list to hold company names
companies = []

# Loop through the tags containing company names, and add the text from each tag to the list you just created
for company in company_data[1:]:
  companies.append(company.get_text())

# Create a DataFrame with a column “Company” corresponding to your companies list, and a column “Ratings” corresponding to your ratings list
dict = {"Company": companies, "Rating": ratings }
df = pd.DataFrame.from_dict(dict)
df.head()

# group your DataFrame by Company and take the average of the grouped ratings
# get the 10 highest rated chocolate companies. Print them out.
avg_ratings = df.groupby("Company").Rating.mean()
top_ten = avg_ratings.nlargest(10)
print(top_ten)

# create a list that contains all of the cocoa percentages
# Store each percent as an integer, after stripping off the % character
cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")
for cacao_percent in cocoa_percent_tags[1:]:
  percent = int(cacao_percent.get_text().strip('%'))
  cocoa_percents.append(percent)

# Add the cocoa percentages as a column called "CocoaPercentage" in the DataFrame that has companies and ratings in it
df["CocoaPercentage"] = cocoa_percents
df.head()

# Make a scatterplot of ratings (your_df.Rating) vs percentage of cocoa (your_df.CocoaPercentage)
plt.scatter(df.CocoaPercentage, df.Rating)
plt.show()

# ıs there any correlation here? 
# We can use some numpy commands to draw a line of best-fit over the scatterplot
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")