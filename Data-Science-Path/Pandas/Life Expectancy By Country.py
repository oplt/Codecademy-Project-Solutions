# Life Expectancy By Country

# In this project, we will investigate a dataset containing information about the average life expectancy in 158 different countries. We will specifically look at how a country’s economic success might impact the life expectancy in that area.

import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

# Check the first 5 rows of the dataset
print(data.head())

# isolate the column that contains the life expectancy
life_expectancy = data["Life Expectancy"]

# find the quartiles of life_expectancy
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])

# Plot the histogram 
#plt.hist(life_expectancy)
#plt.show()

# isolate the GDP column
gdp = data["GDP"]

# find the median GDP by using quantile function
median_gdp = np.quantile(gdp, 0.5)
print(median_gdp)

# grab all of the rows from our original dataset that have a GDP less than or equal to the median 
# Do the same for all of the rows that have a GDP higher than the median
low_gdp = data[data['GDP'] <= median_gdp]
high_gdp = data[data['GDP'] > median_gdp]

# Find the quartiles of the "Life Expectancy" column of low_gdp
low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25, 0.5, 0.75])

# Find the quartiles of the high GDP countries
high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25, 0.5, 0.75])


plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()