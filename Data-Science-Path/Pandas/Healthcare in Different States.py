# Healthcare in Different States

# In this project, we will use boxplots to investigate the way hospitals in different states across the United States charge their patients for medical procedures.

import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")

# print the first five rows of the dataset
print(healthcare.head())

# check all of the different diagnoses in our dataset
print(healthcare["DRG Definition"].unique())

# grab only the rows in the dataset that are about chest pain
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

# get every chest pain diagnosis in Alabama
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]

# find the average cost of those diagnoses
costs = alabama_chest_pain[' Average Covered Charges '].values

# make a boxplot of those values
# plt.boxplot(costs)
# plt.show()

# Let’s make a boxplot for every state

# Find all of the unique states from the dataset chest_pain and store it in a variable named states
states = chest_pain["Provider_State"].unique()
print(states)

# separate the dataset into a dataset for each state
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

# We’re about to draw 50 boxplots
plt.figure(figsize=(20,6))

# Draw the boxplot using datasets as the first parameter. 
# Add the second parameter labels = states to label your boxplots.
plt.figure(figsize=(20,6))
plt.boxplot(datasets, labels = states)
plt.show()