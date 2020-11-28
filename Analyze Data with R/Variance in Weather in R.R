---
  title: "Standard Deviation"
output: html_notebook
---
  ```{r message=FALSE, warning=FALSE, error=TRUE}
library(readr)
library(dplyr)
```

```{r error=TRUE}
load("project.Rda")
```

```{r error=TRUE}
# Change these variables to be the standard deviation of each dataset.
# Inspect Data
head(london_data)
nrow(london_data)

#Create a variable named temp and set it equal to the TemperatureC column of london_data :
temp <- london_data$TemperatureC

#find the average temperature in London in 2015:
average_temp <- mean(temp)

# Variance and SD for the year
temperature_var <- variance(temp)
temperature_standard_deviation <- sd(temp)
#Inspect once again
tail(london_data)

# Get monthly temperature average
june <- london_data %>%
  filter(month == "06")

july <- london_data %>%
  filter(month == "07")

# Analyze by month
print(mean(june$TemperatureC))
print(mean(july$TemperatureC))

print(sd(june$TemperatureC))
print(sd(july$TemperatureC))

# Analyze for every month:
monthly_stats <- london_data %>%
  group_by(month) %>%
  summarize(mean = mean(TemperatureC),
            standard_deviation = sd(TemperatureC))

monthly_stats

```