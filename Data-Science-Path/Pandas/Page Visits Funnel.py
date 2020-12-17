# Multiple tables in Pandas

# Page Visits Funnel

import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

# Inspect the DataFrames using print and head
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# Combine visits and cart using a left merge
visits_cart = pd.merge(visits, cart, how='left')
print(visits_cart)

# How many of the timestamps are null for the column cart_time
null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])

# What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
print(float(null_cart_times/len(visits_cart)))

# Repeat the left merge for cart and checkout and count null values. 
# What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout = pd.merge(cart, checkout, how='left')
print(cart_checkout)

print(float(len(cart_checkout[cart_checkout.checkout_time.isnull()])/len(cart_checkout)))

# Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data.
# Examine the result using print and head.
all_data = visits.merge(cart, how="left").merge(checkout, how="left").merge(purchase, how="left")
print(all_data.head())

# What percentage of users proceeded to checkout, but did not purchase a t-shirt?
checkout_purchase = pd.merge(checkout, purchase, how ="left")
checkout_purchase_rows = len(checkout_purchase)
null_purchase_times = len(checkout_purchase[checkout_purchase.purchase_times.isnull()])
print(float(null_purchase_timces/checkout_purchase_rows))

# Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.time_to_purchase)

# Calculate the average time to purchase 
print(all_data.time_to_purchase.mean())