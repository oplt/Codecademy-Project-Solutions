# In this project, we’ll use decision trees to try to predict the continent of flags based on several of these features.
# We’ll explore which features are the best to use and the best way to create your decision tree.

import codecademylib3_seaborn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

# load the data into a variable named flags
# We also want row 0 to be used as the header, so include the parameter header = 0
flags = pd.read_csv("flags.csv", header = 0)

# look at the names of the columns and the first few rows of the dataset
print(flags.columns)
print(flags.head())

#We’re eventually going to use create a decision tree to classify what Landmass a country is on.
# Create a variable named labels and set it equal to only the "Landmass" column from flags
labels = flags.Landmass

# Create a variable named data and set it equal to a DataFrame containing the following columns: 
# "Red", "Green", "Blue", "Gold", "White", "Black", "Orange"
data = flags[["Red", "Green", "Blue", "Gold", "White", "Black", "Orange"]]

# split data into a training set and test 
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state=1)

# create a classifier
tree = DecisionTreeClassifier(random_state = 1)

# Call tree‘s .fit() method 
tree.fit(train_data, train_labels)

# find the accuracy of the model
score = tree.score(test_data, test_labels)
print(score)

# Put your code that creates, trains, and tests the tree inside a for loop that has a variable named i that increases from 1 to 20.
# Inside your for loop, when you create tree, give it the parameter max_depth = i
# Rather than printing the score of each tree,  graph it

scores = []
for i in range(1, 20):
  tree = DecisionTreeClassifier(random_state = 1, max_depth = i)
  tree.fit(train_data, train_labels)
  score = tree.score(test_data, test_labels)
  scores.append(tree.score(test_data, test_labels))

plt.plot(range(1,20), scores)
plt.show()