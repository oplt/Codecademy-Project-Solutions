
# PYTHON SYNTAX: MEDICAL INSURANCE PROJECT


# 1) Initial variables:

age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# 2) Insurance cost formula:

insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# 3) Print the string:

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# 4) Add 4 to "age" variable:

age += 4

# 5) New insurance cost variable:

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

# 6) Difference between the insurance cost variables:

change_in_insurance_cost = new_insurance_cost - insurance_cost

# 7) Print the difference through concatenating strings and using str() method:

print("The Change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# 8) Set age to 28 and add 3.1 to  bmi variable:

age = 28
bmi += 3.1

# 9) Rewrite the insurance cost formula, calculate the difference and print the string:

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 1250 
change_cost_bmi = new_insurance_cost - insurance_cost
print("The change in estimated isnurance cost after increasing BMI by 3.1 is " + str(change_cost_bmi) + " dollars.")

# 10) Reassign  bmi variable  to 26.2 and sex to 1 :

bmi = 26.2
sex = 1

# 11) Rewrite the insurance cost formula, calculate the difference and print the string:
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 1250 
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is " + str(change_cost_sex) + " dollars") 

