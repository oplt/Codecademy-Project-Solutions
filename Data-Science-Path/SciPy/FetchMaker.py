# FetchMaker

# Hypothesis Testing

import numpy as np
import fetchmaker

# Get the tail lengths of all of the "rottweiler"s in the system, and store it in a variable called rottweiler_tl

#Get the tail lengths of all of the "rottweiler"s in the system
rottweiler_tl = get_tail_length("rottweiler")

# Print out the mean and the standard deviation of rottweiler_tl
print(np.mean(rottweiler_tl))
print(np.std(rottweiler_tl))

# Store the is_rescue values for "whippet"s in a variable called whippet_rescue
whippet_rescue = get_is_rescue("whippet")

# get the number of entries in whippet_rescue that are 1
num_whippet_rescues = np.count_nonzero(whippet_rescue)

# Get the number of samples
num_whippets = np.size(whippet_rescue)

# Use a binomial test to test the number of whippet rescues, num_whippet_rescues, against our expected percentage, 8%
from scipy.stats import binom_test 
print(binom_test(num_whippet_rescues, num_whippets, 0.8))

#Three of our most popular mid-sized dog breeds are whippets, terriers, and pitbulls. 
# Is there a significant difference in the average weights of these three dog breeds? 
# Perform a comparative numerical test to determine if there is a significant difference
from scipy.stats import f_oneway
w = fetchmaker.get_weight("whippet")
t = fetchmaker.get_weight("terrier")
p = fetchmaker.get_weight("pitbull")
print(f_oneway(w,t,p,).pvalue)

# perform another test to determine which of the pairs of these dog breeds differ from each other
from statsmodels.stats.multicomp import pairwise_tukeyhsd
values = np.concatenate([w,t,p])
labels = ["whippet"]*len(w) + ["terrier"]*len(t) +["pitbull"]*len(p)
print(pairwise_tukeyhsd(values, labels, .05))

# We want to see if "poodle"s and "shihtzu"s have significantly different color breakdowns.
# Get the poodle colors and store it in a variable called poodle_colors.
# Get the shih tzu colors and store it in a variable called shihtzu_colors
poodle_color = fetchmaker.get_color("poodle")
shihtzu_color = fetchmaker.get_color("shihtzu")

# build a Chi Square contingency table, called color_table
color_table = [
    [np.count_nonzero(poodle_color == "Black"), np.count_nonzero(shihtzu_color == "Black")],
    [np.count_nonzero(poodle_color == "Brown"), np.count_nonzero(shihtzu_color == "Brown")],
    [np.count_nonzero(poodle_color == "White"), np.count_nonzero(shihtzu_color == "White")],
    [np.count_nonzero(poodle_color == "Gold"), np.count_nonzero(shihtzu_color == "Gold")],
    [np.count_nonzero(poodle_color == "Grey"), np.count_nonzero(shihtzu_color == "Grey")],
 
]
print(color_table)

# Feed the color_table into SciPy’s Chi Square test, save the p-value and print it out
from scipy.stats import chi2_contingency
_, color_pval, _, _ = chi2_contingency(color_table)
print(color_pval)