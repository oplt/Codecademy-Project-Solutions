# Classification Project
#In this project, a dataset from Kaggle will be used to predict the survival of patients with heart failure from serum creatinine and ejection fraction, and other factors such as age, anemia, diabetes, and so on.

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from sklearn.metrics import classification_report
from tensorflow.keras.utils import to_categorical
import numpy as np

# Loading the data

# load the data from heart_failure.csv:
data = pd.read_csv("heart_failure.csv")

# print all the columns and their types
print(data.info())

# Print the distribution of the death_event 
print('Classes and number of values in the dataset',Counter(data['death_event']))

# Extract the label column death_event and assign the result to a variable called y
y = data["death_event"]

# Extract the features columns ['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time']
x = data[['age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction','high_blood_pressure','platelets','serum_creatinine','serum_sodium','sex','smoking','time']]

# Data preprocessing

# convert the categorical features in the DataFrame instance x to one-hot encoding vectors 
x  = pd.get_dummies(x)

# split the data into training features, test features, training labels, and test labels
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

# Initialize a ColumnTransformer object
ct = ColumnTransformer([("numeric", StandardScaler(), ['age','creatinine_phosphokinase','ejection_fraction','platelets','serum_creatinine','serum_sodium','time'])])

# train the scaler instance ct on the training data
X_train = ct.fit_transform(X_train)

# test data instance X_test using the trained scaler ct
X_test = ct.transform(X_test)

# initialize an instance of LabelEncoder
le = LabelEncoder()

#  fit the encoder instance le to the training labels Y_train
Y_train = le.fit_transform(Y_train.astype(str))

# encode the test labels
Y_test = le.transform(Y_test.astype(str))

# transform the encoded training labels Y_train into a binary vector
Y_train = to_categorical(Y_train)

# transform the encoded test labels Y_test into a binary vector
Y_test = to_categorical(Y_test)

# Initialize a model
model = Sequential()

# Create an input layer and add it to the model
model.add(InputLayer(input_shape=(X_train.shape[1],)))

# Create a hidden layer with relu activation function and 12 hidden neurons, and add it to the model
model.add(Dense(64, activation='relu'))

# Create an output layer instance with a softmax activation function (because of classification) with the number of neurons corresponding to the number of classes in the dataset.
model.add(Dense(2, activation='softmax'))

# compile the model instance model using the categorical_crossentropy loss, adam optimizer and accuracy as metrics.
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train and evaluate the model

# fit the model  to the training data  and training labels . Set the number of epochs to 100 and the batch size parameter to 16.
model.fit(X_train, Y_train, epochs = 100, batch_size = 16, verbose=1)

# evaluate the trained model 
loss, acc = model.evaluate(X_test, Y_test, verbose=0)
print("Loss", loss, "Accuracy:", acc)

# get the predictions for the test data 
y_estimate = model.predict(X_test, verbose=0)

# select the indices of the true classes for each label encoding
y_estimate = np.argmax(y_estimate, axis=1)
y_true = np.argmax(Y_test, axis=1)

# Print additional metrics, such as F1-score
print(classification_report(y_true, y_estimate))








