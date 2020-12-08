# Museums and Nature Centers

# Intermediate Data visualization with R

library(dplyr)
library(ggplot2)
library(stringr)
library(tidyr)
library(plotrix)

# Load file as data frame
museums_df <- read.csv("museums.csv")

# Inspect data frame
head(museums_df)

# Create and print a bar plot called museum_type that maps Museum:
museum_type <- ggplot(museums_df, aes(x = Museum.Type)) + 
  geom_bar()
museum_type


#Add a scale_x_discrete() layer to customize our x axis, using the function scales::wrap_format(8) to reformat our labels:

museum_type <- ggplot(museums_df, aes(x = Museum.Type)) + 
  geom_bar() +
  scale_x_discrete(labels = scales::wrap_format(8))
museum_type

# Create and print bar plot by museum vs non-museum
museum_class <- ggplot(museums_df, aes(x = Is.Museum)) +
  geom_bar() +
  scale_x_discrete(labels = c( "TRUE" = "Museum", "FALSE" = "Non-Museum"))
museum_class

# Filter data frame to select states
museums_states <- museums_df %>%
  filter(State..Administrative.Location. %in% c("IL", "CA", "NY"))


# Create and print bar plot with facets
museums_states <- ggplot(museums_states, aes(x = Is.Museum)) +
  geom_bar() +
  scale_x_discrete(labels = c( "TRUE" = "Museum", "FALSE" = "Non-Museum")) +
  facet_grid(cols = vars(State..Administrative.Location.))
museums_states

#Convert Region.Code..AAM. to a factor (e.g. factor(Region.Code..AAM.)) so ggplot2 plots its levels as discrete rather than continuous values. Call this plot museum_stacked.:

museum_stacked <- ggplot(museums_df, aes(x = factor(Region.Code..AAM.), fill = Is.Museum)) +
  geom_bar() 
museum_stacked

# Use scale_x_discrete() to rename the numeric labels to text according to the following table:
museum_stacked <- ggplot(museums_df, aes(x = factor(Region.Code..AAM.), fill = Is.Museum)) +
  geom_bar() +
  scale_x_discrete(labels = c( "1" = "New England",
                               "2" = "Mid-Atlantic",
                               "3" = "Southeastern",
                               "4" = "Midwest",
                               "5" = "Montain Plains",
                               "6" = "Western")) +
  scale_fill_discrete(labels = c( "TRUE" = "Museum", "FALSE" = "Non-Museum"))
museum_stacked

#Apply the scales::percent_format() function to transform  y axis labels into percentage values:
museum_stacked <- ggplot(museums_df, aes(x = factor(Region.Code..AAM.), fill = Is.Museum)) +
  geom_bar(position = "fill") +
  scale_x_discrete(labels = c( "1" = "New England",
                               "2" = "Mid-Atlantic",
                               "3" = "Southeastern",
                               "4" = "Midwest",
                               "5" = "Montain Plains",
                               "6" = "Western")) +
  scale_fill_discrete(labels = c( "TRUE" = "Museum", "FALSE" = "Non-Museum"), ) +
  scale_y_continuous(labels = scales::percent_format())

museum_stacked

#Add labels:

museum_stacked <- ggplot(museums_df, aes(x = factor(Region.Code..AAM.), fill = Is.Museum)) +
  geom_bar(position = "fill") +
  scale_x_discrete(labels = c( "1" = "New England",
                               "2" = "Mid-Atlantic",
                               "3" = "Southeastern",
                               "4" = "Midwest",
                               "5" = "Montain Plains",
                               "6" = "Western")) +
  scale_fill_discrete(labels = c( "TRUE" = "Museum", "FALSE" = "Non-Museum"), ) +
  scale_y_continuous(labels = scales::percent_format()) +
  labs(title = "Museum Types by Region", x = "Region", y = "Percentage of Total", fill = "Type")

museum_stacked

# Create a new data frame called museums_revenue_df that retains only unique values of Legal.Name in museums_df. Additionally, filter this data frame to include only entities with Annual.Revenue greater than 0
museums_revenue_df <- museums_df %>%
  distinct(Legal.Name, .keep_all = TRUE) %>% 
  filter(Annual.Revenue > 0)

# Filter for only small museums
museums_small_df <- museums_revenue_df %>% 
  filter(Annual.Revenue < 1000000)

# Filter for only large museums
museums_large_df <- museums_revenue_df %>% 
  filter(Annual.Revenue >= 1000000)


# Create a histogram called revenue_histogram using museums_small_df with Annual.Revenue mapped to the x axis. Experiment with different binwidth values to see what works best for our data, considering that our x axis variable ranges from 0 to $1,000,000.

revenue_histogram <- ggplot(museums_small_df, aes(x = Annual.Revenue)) +
  geom_histogram(binwidth = 25000)
revenue_histogram

# Add a scale_x_continuous() layer applying the function scales::dollar_format() to x axis labels. dollar_format() is a function from the scales library included in ggplot2 that adds dollar signs and commas to monetary data.

revenue_histogram +
  scale_x_continuous(labels = scales::dollar_format())


# Create a boxplot called revenue_boxplot using museums_large_df, mapping Region.Code..AAM. to the x axis and Annual.Revenue to the y axis

revenue_boxplot  <- ggplot(museums_large_df, aes(x = factor(Region.Code..AAM.), y = Annual.Revenue)) +
  geom_boxplot() +
  scale_x_discrete(labels = c( "1" = "New England",
                               "2" = "Mid-Atlantic",
                               "3" = "Southeastern",
                               "4" = "Midwest",
                               "5" = "Montain Plains",
                               "6" = "Western"))
revenue_boxplot


# Add a coord_cartesian() layer setting ylim to c(1e9, 3e10) telling the plot to zoom in on the y axis range between $1,000,000,000 and $30,000,000,000. 

revenue_boxplot  <- revenue_boxplot +
  coord_cartesian(ylim = c(1e9, 3e10))
revenue_boxplot

# reformat  y axis as billions of dollars.

revenue_boxplot +
  scale_y_continuous(labels = function(x) paste0("$", x/1e9, "B"))

# Use stat = "summary" and fun = "mean" to calculate and display the mean revenue by region. Apply the appropriate x and y axis label transformations to make labels more clear.:

revenue_barplot <- ggplot(museums_revenue_df, aes(x = factor(Region.Code..AAM.), y = Annual.Revenue)) +
  geom_bar(stat = "summary", fun = "mean") +
  scale_x_discrete(labels = c( "1" = "New England",
                               "2" = "Mid-Atlantic",
                               "3" = "Southeastern",
                               "4" = "Midwest",
                               "5" = "Montain Plains",
                               "6" = "Western")) +
  scale_y_continuous(labels = function(x) paste0("$", x/1e6, "M"))
revenue_barplot

# add labels:

revenue_barplot +
  labs(title = "Mean Annual Revenue by Region", x = "Region", y = "Mean Annual Revenue")

# Add error bars to our mean revenue by geography bar plot using the geom_errorbar() layer. Call this new plot revenue_errorbar

museums_error_df <- museums_revenue_df %>%
  group_by(Region.Code..AAM.) %>%
  summarize(
    Mean.Revenue = mean(Annual.Revenue), 
    Mean.SE = std.error(Annual.Revenue)) %>%
  mutate(
    SE.Min = Mean.Revenue - Mean.SE, 
    SE.Max = Mean.Revenue + Mean.SE)

revenue_errorbar <- ggplot(museums_error_df, aes(x = factor(Region.Code..AAM.), y = Mean.Revenue)) +
  geom_bar(stat = "identity") +
  scale_x_discrete(labels = c( "1" = "New England",
                               "2" = "Mid-Atlantic",
                               "3" = "Southeastern",
                               "4" = "Midwest",
                               "5" = "Montain Plains",
                               "6" = "Western")) +
  scale_y_continuous(labels = function(x) paste0("$", x/1e6, "M")) +
  labs(title = "Mean Annual Revenue by Region", x = "Region", y = "Mean Annual Revenue") +
  geom_errorbar(aes(ymin = SE.Min, ymax = SE.Max), width = 0.2)
revenue_errorbar

































































































