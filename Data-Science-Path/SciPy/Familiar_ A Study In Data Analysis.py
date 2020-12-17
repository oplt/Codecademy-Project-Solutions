# Familiar: A Study In Data Analysis

# Hypothesis Testing

import familiar
vein_pack_lifespans= familiar.lifespans(package='vein')

# We’d like to find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy of 71 years
# Import the statistical test we would use to determine if a sample comes from a population that has a given mean from scipy.stats
from scipy.stats import ttest_1samp

#  use the 1-Sample T-Test to compare vein_pack_lifespans to the average life expectancy 71
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)

# check if the results are significant
print(vein_pack_lifespans.pvalue, "0.10f")

# If the test’s p-value is less than 0.05, print “The Vein Pack Is Proven To Make You Live Longer!”. 
# Otherwise print “The Vein Pack Is Probably Good For You Somehow!”
if vein_pack_lifespans.pvalue < 0.05
    print(“The Vein Pack Is Proven To Make You Live Longer!”) 
else:
    print(“The Vein Pack Is Probably Good For You Somehow!”)

# call the package
artery_pack_lifespans = familiar.lifespans(package='artery')

# Import the 2-Sample T-Test 
from scipy.stats import ttest_ind 

# run the 2-Sample test to compare the lifespans
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)

# If the p-value from our experiment is less than 0.05, print out “the Artery Package guarantees even stronger results!”. 
# Otherwise we should print out “the Artery Package is also a great product!”
if package_comparison_results.pvalue < 0.05
    print(“the Artery Package guarantees even stronger results!”) 
else:
    print(“the Artery Package is also a great product!”)

# load the iron_counts
iron_contingency_table = familiar.iron_counts_for_package()

#  Import the Chi-Squared test
from scipy.stats import chi2_contingency

# Run the Chi-Squared test on the iron_contingency_table
_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)

# evaluate the results
if iron_pvalue < 0.05
    print(“The Artery Package Is Proven To Make You Healthier!”) 
else:
    print(“While We Can’t Say The Artery Package Will Help You, I Bet It’s Nice!”)
