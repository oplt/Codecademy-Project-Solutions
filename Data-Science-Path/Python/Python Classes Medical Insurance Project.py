# PYTHON FUNDAMENTALS
# Python Classes: Medical Insurance Project

# 1. Add more paremeters:
class Patient:
    def __init__(self, name, age, sex, bmi, num_of_children, smoker):
        self.name = name
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker
    # 3. define estimated_insurance_cost() constructor:
    def estimated_insurance_cost(self):
        estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
        # 4. Add a print statement:
        print(self.name + "'s estimated insurance cost is " + str(estimated_cost) + " dollars.")
    # 5. create an update_age() method: 
    def update_age(self, new_age):
        self.age = new_age
        #7. Call the estimated_insurance_cost() method in update_age():
        self.estimated_insurance_cost()
    #8. define a new method called update_num_children():
    def update_num_children(self, new_num_children):
        self.num_of_children = new_num_children
        # 6. Add a print statement :
        print(self.name + " is now " + str(self.age) + " years old.")
        # 9, 10. Add in a print statement that clarifies the information that is being updated:
        if self.num_of_children == 1:
              print(self.name + " has " + str(self.num_of_children) + " child.")
        else:
            print(self.name + " has " + str(self.num_of_chilrden) + " children.")
        # 11. call our estimated_insurance_cost() method at the end:
        self.estimated_insurance_cost()
    
    # 12. create one last method that uses a dictionary to store a patient’s information in one convenient variable:
    def patient_profile(self):
        patient_information = {}
        patient_information["Name"] = self.name
        patient_information["Age"] = self.age
        patient_information["Sex"] = self.sex
        patient_information["BMI"] = self.bmi
        patient_information["Number of Children"] = self.num_of_children
        patient_information["Smoker"] = self.smoker
        return patient_information
# 12. Create an instance variable outside of our class called patient1:
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
patient1.update_age(26)
patient1.update_num_children(1)
# 13. Test the final method using patient1 :
print(patient1.patient_profile())

