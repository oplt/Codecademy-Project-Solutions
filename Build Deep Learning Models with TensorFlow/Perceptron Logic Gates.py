#Perceptron Logic Gates

#In this project, we will use perceptrons to model the fundamental building blocks of computers — logic gates.

import seaborn as sns
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt
import numpy as np
from itertools import product

# Create a variable named data that is a list that contains the four possible inputs to an AND gate:

data = [[0,0], [0,1], [1,0], [1,1]]

# Create a variable named labels associated with each data point. The label will be the result of the AND gate given the input:

labels = [0, 0, 0, 1]

# plot these four points on a graph: 

plt.scatter([point[0] for point in data], [point[1] for point in data], c= labels)

# Create a Perceptron object named classifier. For now, set the parameter max_iter to 40:
classifier = Perceptron(max_iter = 40)

# Call the .fit() method using data and labels as parameter:

classifier.fit(data, labels)

# Call classifier‘s .score() method using data and labels as parameters. Print the results. This will print the accuracy of the model on the data points:

print(classifier.score(data, labels))

# Try calling classifier‘s .decision_function() method using [[0, 0], [1, 1], [0.5, 0.5]] as a parameter. Print the results:

print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]]))

#make a heat map that reveals the decision boundary:

x_values = np.linspace(0, 1, 100)
y_values = np.linspace(0, 1, 100)
point_grid = list(product(x_values, y_values))
distances = classifier.decision_function(point_grid)
abs_distances = [abs(pt) for pt in distances]
distances_matrix = np.reshape(abs_distances, (100,100))
print(classifier.score(data, labels))
print(classifier.decision_function([[0, 0], [1, 1], [0.5, 0.5]]))
heatmap = plt.pcolormesh(x_values, y_values, distances_matrix)
plt.colorbar(heatmap) 
plt.show()
















