# Variance in Weather

# Print the first few rows of the dataset
print(london_data.head())

# print rows 100 through 199
print(london_data.iloc[100:200])

# look at how many data points we have
print(len(london_data))

# get the "TemperatureC" column
Temp = london_data["TemperatureC"]

# find the average temperature in London in 2015
average_temp = np.average("Temp")

# Calculate and print the variance of the temperature column
temperature_var = np.var(temp)
print(temperature_var))

# Calculate the standard deviation of the temperature column
temperature_sd = np.std(temp)
print(temperature_std))

# get the temperature from the rows where "month" is 6
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]

# Create a variable named july that contains all of the data points from July
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]

# Calculate and print the mean temperature in London for both June and July
print(np.mean(june))
print(np.mean(july))

# Calculate and print the standard deviation of temperature in London for both June and July
print(np.std(june))
print(np.std(july))

# calculate and print the mean and standard deviation of every month

If you want to quickly see the mean and standard deviation of every month, use this block of code.

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n"