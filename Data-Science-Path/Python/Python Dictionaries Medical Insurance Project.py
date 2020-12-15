#Python Dictionaries: Medical Insurance Project

#1. empty dictionary:
medical_costs = {}

#2. adding the key-value pairs::
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

#3. Update the dictionary:
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

#4 Print medical_costs:
print(medical_costs)

#5. Update the dictionary and print:
medical_costs["Vinay"] = 3325.0
print(medical_costs)

#6. iterate through for loop:
total_cost = 0
for cost in medical_costs.values():
  total_cost += cost

#7. calculate average cost and print:
average_cost = total_cost/len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))

#8. Create lists of names and ages:
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

#9. Zip these two lists in a list:
zipped_ages = list(zip(names, ages))

#10. 
names_to_ages = {key:value for key, value in zipped_ages}
print(names_to_ages)

#11. Get the value of the key via get() funchtion and print:
marina_age = names_to_ages.get("Marina", None)
print("Marina's age is " + str(marina_age))

#12. Initiate an empty dictionary:
medical_records = {}

#13. Add "Marina" to medical_records as a key:
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

#14. Add the other individuals to the dictionary:
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

#15. Print medical_records:
print(medical_records)

#16. Print out Connie’s insurance cost:
print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")

#17. Remove Vinay from medical_records:
medical_records.pop("Vinay")

#18. Use a for loop to iterate through the items of medical_records:
for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance_cost"]))