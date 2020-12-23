# Honey Production
# As you may have already heard, the honeybees are in a precarious state right now. 
# You may have seen articles about the decline of the honeybee population for various reasons. 
# You want to investigate this decline and how the trends of the past predict the future for the honeybees.

import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

# get a sense of how this DataFrame is structured
print(df.head())

# get the mean of totalprod per year
prod_per_year = df.groupby('year').totalprod.mean().reset_index()

# Create a variable called X that is the column of years in this prod_per_year DataFrame.
# After creating X, we will need to reshape it to get it into the right format
X = prod_per_year ["year"]
X = X.values.reshape(-1, 1)

# Create a variable called y that is the totalprod column in the prod_per_year dataset
y = prod_per_year["totalprod"]

# plot y vs X as a scatterplot
plt.scatter(X, y)
plt.show()

# Create a linear regression model from scikit-learn and call it regr
regr = linear_model.LinearRegression()

# Fit the model to the data 
regr.fit(X,y)

#  print out the slope of the line (stored in a list called regr.coef_) and the intercept of the line (regr.intercept_)
print(regr.coef_[0])
print(regr.intercept_)

# Plot y_predict vs X as a line, on top of your scatterplot
y_predict = regr.predict(X)
plt.plot(X, y_predict)
plt.show()

# Let’s predict what the year 2050 may look like in terms of honey production.
# Our known dataset stops at the year 2013, so let’s create a NumPy array called X_future that is the range from 2013 to 2050. 
X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)

# Create a list called future_predict that is the y-values that your regr model would predict for the values of X_future
future_predict = regr.predict(X_future)

# Plot future_predict vs X_future on a different plot
plt.plot(X_future, future_predict)
plt.show()