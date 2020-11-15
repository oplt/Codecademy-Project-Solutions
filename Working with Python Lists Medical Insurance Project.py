# Working with Python Lists Medical Insurance Project

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here

#Append a new individual, "Priscilla", to names, and her insurance cost, 8320.0, to insurance_costs:
names.append("Priscilla")
insurance_costs.append(8320.0)

# use zip() function to combine insurance_costs and names in a new variable called medical_records:
medical_records = list(zip(insurance_costs, names))
print(medical_records )

# Create a variable called num_medical_records that stores the length of medical_records.
num_medical_records = len(medical_records)
print(num_medical_records )

# Select the first medical record in medical_records, and save it to a variable called first_medical_record.
first_medical_record = medical_records[0]
print("Here is the first medical record:" + str(first_medical_record))

# Sort medical_records and print out:
medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

# Save the three cheapest insurance costs in a list called cheapest_three:
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

# Save the three most expensive insurance costs in a list called cheapest_three:
priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

# Save the number of occurrences of “Paul” in the names list to a new variable called occurrences_paul:
occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records.")

