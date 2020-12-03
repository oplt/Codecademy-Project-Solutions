---
  title: "Page Visits Funnel"
output: html_notebook
---
# load packages
library(readr)
library(dplyr)
```

# load data
visits <- read_csv("visits.csv")
cart <- read_csv("cart.csv")
checkout <- read_csv("checkout.csv")
purchase <- read_csv("purchase.csv")
```

# inspect data frames
head(visits)
head(cart)
head(checkout)
head(purchase)
```

# define visits_cart here:
visits_cart <- visits %>% 
  left_join(cart)


# How long is the visits data frame?:
total_visits <- nrow(visits)

# How many of the timestamps are NA for the column cart_time:
visit_no_cart <- cart %>%
  filter(is.na(cart_time))

visit_no_cart
visit_no_cart_count <- nrow(visit_no_cart)
visit_no_cart_count

# calculate visit_no_cart_percent here:
visit_no_cart_percent <- visit_no_cart_count/total_visits
visit_no_cart_percent

# define cart_checkout here:
cart_checkout <- cart %>% 
  left_join(checkout)

# define total_carts here:
total_carts = nrow(cart)
total_carts

# define cart_no_checkout here:
cart_no_checkout <- cart_checkout %>% 
  filter(is.na(checkout_time))
cart_no_checkout

cart_no_checkout_count <- nrow(cart_no_checkout)
cart_no_checkout_count

# calculate cart_no_checkout_percent here:
cart_no_checkout_percent <- cart_no_checkout_count/total_carts
cart_no_checkout_percent

# define all_data here:
all_data <- visits_cart %>%
  left_join(cart_checkout)

head(all_data)

# define total_checkout here:
total_checkout <- nrow(checkout)
total_checkout

# define checkout_no_purchase here:
checkout_no_purchase <- purchase %>% 
  filter(is.na(purchase_time))
checkout_no_purchase

# calculate checkout_no_purchase_percent here:
checkout_no_purchase_percent <- checkout_no_purchase / total_checkout
checkout_no_purchase_percent

# update all_data with time_to_purchase column here:
all_data <- all_data %>%
  mutate(time_to_purchase = purchase_time - visit_time)


# inspect the updated all_data data frame here:

head(all_data)

# define time_to_purchase here:
time_to_purchase <- all_data %>%
  summarize(mean_time = mean(time_to_purchase, na.rm = TRUE))
time_to_purchase
