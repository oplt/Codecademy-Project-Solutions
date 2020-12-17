# Traveling to Acadia

# In this project, you will use flower bloom data, and flight information to recommend the best time of year for someone to make a trip to Maine

# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Use Matplotlib to create a flights histogram
# Set the number of bins in your plot to 365 
# set the range of your histogram to (0, 365) 
# Add an x-label, y-label, and title
# set up the figure so it displays two plots at once.
plt.figure(1)
plt.subplot(211)
plt.hist(flights, range=(0, 365), bins=365,  edgecolor='black')
# plt.title("Weekday Frequency of Customers")
plt.ylabel("Count")

# Under plt.subplot(212), make a histogram that displays the number of flowers that begin to bloom each day of the year.
plt.subplot(212)
plt.hist(in_bloom, range=(0, 365), bins=365,  edgecolor='black')
plt.title("Flower Blooms and Flights by Day")
plt.ylabel("Bloom Count")
plt.xlabel("Day of the Year")

plt.tight_layout()
plt.show()

