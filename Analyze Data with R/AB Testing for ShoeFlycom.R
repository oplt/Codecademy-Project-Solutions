
# A/B Testing for ShoeFly.com

title: "Aggregates in R"
output: html_notebook

# load packages
library(readr)
library(dplyr)

# load ad clicks data
ad_clicks <- read_csv("ad_clicks.csv")

# inspect ad_clicks here:
head(ad_clicks)

# define views_by_utm here:
views_by_utm <- ad_clicks %>%
  group_by(utm_source)%>%
  summarize(count = n())
views_by_utm 

# define clicks_by_utm here:
clicks_by_utm <- ad_clicks %>%
  group_by(utm_source, ad_clicked) %>%
  summarize(count = n())

clicks_by_utm

# define percentage_by_utm here:
percentage_by_utm <- clicks_by_utm %>%
  group_by(utm_source) %>%
  mutate(percentage = count/sum(count))
filter(ad_clicked == TRUE)

# define experiment_split here:
experiment_split <- ad_clicks %>%
  group_by(experimental_group) %>%
  summarize(count = n())
experiment_split

# define clicks_by_experiment here:
clicks_by_experiment <- ad_clicks %>%
  group_by(experimental_group, ad_clicked) %>%
  summarize(count = n())
clicks_by_experiment

# define a_clicks data framehere:
a_clicks <- ad_clicks %>%
  filter(experimental_group == ("A"))
a_clicks


# define b_clicks data frame here:
b_clicks <- ad_clicks %>%
  filter(experimental_group == ("B"))

b_clicks


# define a_clicks_by_day here:
a_clicks_by_day <- a_clicks %>%
  group_by(day, ad_clicked) %>%
  summarize(count = n())

# define b_clicks_by_day here:
b_clicks_by_day <- b_clicks %>%
  group_by(day, ad_clicked) %>%
  summarize(count = n())

# define a_percentage_by_day here:

a_percentage_by_day <- a_clicks_by_day %>%
  group_by(day) %>%
  mutate(percentage = count/sum(count))
filter(ad_clicked == TRUE)
# define b_percentage_by_day here:

b_percentage_by_day <- b_clicks_by_day %>%
  group_by(day) %>%
  mutate(percentage = count/sum(count))
filter(ad_clicked == TRUE)
