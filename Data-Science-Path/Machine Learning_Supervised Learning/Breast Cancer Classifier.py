# In this project, we will be using several Python libraries to make a K-Nearest Neighbor classifier that is trained to predict whether a patient has breast cancer.
import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt

breast_cancer_data = load_breast_cancer()

# let’s take a look at the data
print(breast_cancer_data.data[0])
print(breast_cancer_data.feature_names)
print(breast_cancer_data.target)
print(breast_cancer_data.target_names)

# split the train data
training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)

# create a classifier
classifier = KNeighborsClassifier(n_neighbors = 3)

# Train your classifier using the fit function
classifier.fit(training_data, training_labels)

#  find how accurate it is
print(classifier.score(validation_data, validation_labels))

# create a for loop to choose the best fitting k:

accuracies = []
for k in range(1, 101):
    classifier = KNeighborsClassifier(n_neighbors = k)
    classifier.fit(training_data, training_labels)
    accuracies.append(classifier.score(validation_data, validation_labels))

# make a graph using matplotlib for the results of k values
k_list = range(1 ,101)
plt.plot(k_list, accuracies)
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.show()
