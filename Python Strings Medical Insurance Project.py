# Python Strings: Medical Insurance Project

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here

#1. Print medical_data:
print(medical_data)

#2. Replace all instances of # with $ and store the result in a variable called updated_medical_data:
updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

# 3. Create a variable called num_records and initialize it at 0:
num_records = 0

#4. write a for loop to iterate through the updated_medical_data string. Inside of the loop, add 1 to num_records when the current character is equal to $:
for i in updated_medical_data:
  if i == "$":
    num_records += 1

#5. print
print("There are " + str(num_records) + " medical records in the data.")

#6. splitting the string:
medical_data_split = updated_medical_data.split(";")
print(medical_data_split)

#7. define an empty list called medical_record:
medical_records = []

#8. iterate through medical_data_split and for each record, split the string after each comma (,) and append the split string to medical_records:
for record in medical_data_split:
  medical_records.append(record.split(','))
print(medical_records)

#9, 10,11,12. for loop:

medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:    
    record_clean.append(item.strip())  
  medical_records_clean.append(record_clean)

#13: 
print(medical_records_clean)

# 14:
for record in medical_records_clean:
  print(record[0])

# 15. names in uppercase: 
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])

#16. empty lists:
names = []
ages = []
bmis = []
insurance_costs = []

# 17. Append the name, age, BMI, and insurance cost from the current medical record in a for loop:
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

# 18. print the lists:
print("Names: " + str(names))
print("Ages: " + str(ages))
print("BMI: "  + str(bmis))
print("Insurance Costs: " + str(insurance_costs))

# 19, 20. use a for loop to iterate through bmis and add each bmi to total_bmi:
total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)

# 21. calculate and pring average_bmi:
average_bmi = total_bmi/len(bmis)
print("Average BMI: " + str(average_bmi))
