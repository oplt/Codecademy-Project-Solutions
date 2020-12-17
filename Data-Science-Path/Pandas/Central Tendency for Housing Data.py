# Central Tendency for Housing Data

# In this project, you will find the mean, median, and mode cost of one-bedroom apartments in three of the five New York City boroughs: Brooklyn, Manhattan, and Queens.

import numpy as np
import pandas as pd
from scipy import stats

# Read in housing data
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

# check the data 
print(brooklyn_one_bed)
print(manhattan_one_bed)
print(queens_one_bed)
 
print(brooklyn_price)
print(manhattan_price)
print(queens_price)

# Find the average value of one-bedroom apartments in Brooklyn and save the value to brooklyn_mean
brooklyn_mean = np.average(brooklyn_one_bed)

# Find the average value of one-bedroom apartments in Manhattan and save the value to manhattan_mean
manhattan_mean = np.average(manhattan_one_bed)

# Find the average value of one-bedroom apartments in Queens and save the value to queens_mean
queens_mean = np.average(queens_one_bed)

# Find the median value of one-bedroom apartments in Brooklyn and save the value to brooklyn_median
brooklyn_median = np.median(brooklyn_one_bed)

# Find the median value of one-bedroom apartments in Manhattan and save the value to manhattan_median.
manhattan_median = np.median(manhattan_one_bed)

# Find the median value of one-bedroom apartments in Queens and save the value to queens_median
queens_median = np.median(queens_one_bed)

# Find the mode value of one-bedroom apartments in Brooklyn and save the value to brooklyn_mode.
brooklyn_mode = stats.mode(brooklyn_one_bed)

# Find the mode value of one-bedroom apartments in Manhattan and save the value to manhattan_mode.
manhattan_mode = stats.mode(manhattan_one_bed)

# Find the mode value of one-bedroom apartments in Queens and save the value to queens_mode.
queens_mode = stats.mode(queens_one_bed)






