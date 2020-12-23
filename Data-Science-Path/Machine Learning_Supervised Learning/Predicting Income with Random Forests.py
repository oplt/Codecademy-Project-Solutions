#In this project, we will be using a dataset containing census information from UCI’s Machine Learning Repository.
# By using this census data with a random forest, we will try to predict whether or not a person makes more than $50,000.

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

# load data
income_data =pd.read_csv("income.csv", header = 0, delimiter = ", ")

# look at one of the rows of the data
print(income_data.iloc[0])

# For this project, the labels are in the column called "income"
labels = income_data[["income"]]

# convert sex column into integer
income_data["sex-int"] = income_data["sex"].apply(lambda row: 0 if row == "Male" else 1)

# make a column where every row that contains "United-States" becomes a 0 and any other country becomes a 
income_data["country-int"] = income_data["native-country"].apply(lambda row: 0 if row == "United-States" else 1)

# Create a new variable named data
data = income_data[["age", "capital-gain", "capital-loss", "hours-per-week", "sex-int", "country-int"]]

# split our data and labels into a training set and a test set
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state = 1)

# create a classifier
forest = RandomForestClassifier(random_state= 1)

# fit the model
forest.fit(train_data, train_labels)

# find the accuracy
print(forest.score(test_data, test_labels))