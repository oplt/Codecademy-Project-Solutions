---
title: "ACLU Child Separations"
output: html_notebook
---
  
# load libraries
library(readr)
library(dplyr)


# load data
aclu <- read_csv('aclu_separations.csv')

# inspect data
head(aclu)
summary(aclu)


# select columns
aclu <- aclu %>%
  select(-addr)
head(aclu)

# view columns
colnames(aclu)

# rename columns

aclu <- aclu %>% 
  rename(city = program_city, 
         state = program_state, 
         number_children = n, 
         longitude = lon, 
         latitude = lat)

print(colnames(aclu))

# add column
border_latitude  <- 25.83
aclu <- aclu %>% 
  mutate(lat_change_border  = latitude -border_latitude)
head(aclu)

# latitude change
further_away <- aclu %>%
  filter(lat_change_border > 15) %>%
  arrange(desc(lat_change_border ))
  
further_away

# number of children
ordered_by_children <- aclu %>%
  arrange(desc(number_children))

head(ordered_by_children)

# state analysis

chosen_state <- 'CA'
chosen_state_separations <- aclu %>%
  filter(state == chosen_state)%>%
  arrange(desc(number_children))

chosen_state_separations











```