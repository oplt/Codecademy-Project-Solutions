import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load the data:
dataset  = pd.read_csv('life_expectancy.csv')

# Observe the data by printing the first five entries:
print(dataset.head())

# Drop the Country column : 
dataset = dataset.drop(["Country"], axis = 1)

# Labels are contained in the “Life expectancy” column. It’s the final column in the DataFrame. Create a new variable called labels. Use iloc indexing to assign the final column of dataset to it.:
labels = dataset.iloc[:, -1]

# Features span from the first column to the last column (not including it, since it’s a label column in our dataset). Create a new variable called features:
features = dataset.iloc[:, 0:-1]

# conver categorical columns into numerical columns:
features = pd.get_dummies(features)

# Split your data into training set and test sets: 
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state=23)

# standardize/normalize  numerical features: 
numerical_features = features.select_dtypes(include=['float64', 'int64'])
numerical_columns = numerical_features.columns
ct = ColumnTransformer([("only numeric", StandardScaler(), numerical_columns)], remainder='passthrough')

# Fit your instance ct of ColumnTransformer to the training data and at the same time transform it by using the ColumnTransformer.fit_transform() method. Assign the result to a variable called features_train_scaled:
features_train_scaled = ct.fit_transform(features_train)

#ransform your test data instance features_test using the trained ColumnTransformer instance ct. Assign the result to a variable called features_test_scaled:
features_test_scaled  = ct.transform(features_test)

# Create an instance of my_model:
my_model = Sequential()

# Create the input layer
input = InputLayer(input_shape = (features.shape[1], ))

# Add the input layer:
my_model.add(input)

# Add one hidden layer:
my_model.add(Dense(64, activation = "relu"))

# Add an output layer: 
my_model.add(Dense(1))

# Print the summary of the model: 
print(my_model.summary())

# Create an instance of the Adam optimizer with the learning rate equal to 0.01
opt = Adam(learning_rate = 0.01)

# compile the model:
my_model.compile(loss = 'mse', metrics = ['mae'], optimizer = opt)

# Train tje model
my_model.fit(features_train_scaled, labels_train, epochs = 50, batch_size = 1, verbose = 1)

# evaluate the trained model 
res_mse, res_mae = my_model.evaluate(features_test_scaled, labels_test, verbose = 0)

# Print the final loss (RMSE) and final metric (MAE)
print(res_mse, res_mae)



