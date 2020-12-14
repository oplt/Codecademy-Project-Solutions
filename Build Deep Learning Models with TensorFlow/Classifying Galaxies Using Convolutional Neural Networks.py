# Image Classification

# Classifying Galaxies Using Convolutional Neural Networks

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.model_selection import train_test_split
from utils import load_galaxy_data

import app

# use load_galaxy_data() to load the compressed data files into the Codecademy learning environment
input_data, labels = load_galaxy_data()

# print the dimensions of the input_data and labels
print(input_data.shape) 
print(labels.shape)

# divide the data into training and validation data
x_train, x_valid, y_train, y_valid = train_test_split(input_data, labels, test_size=0.20, stratify=labels, shuffle=True, random_state=222)

# Define an ImageDataGenerator
data_generator = ImageDataGenerator(rescale=1./255)

# Create a training and validation data iterator 
training_iterator = data_generator.flow(x_train, y_train,batch_size=5)
validation_iterator = data_generator.flow(x_valid, y_valid, batch_size=5)

# build the model, starting with the input shape and output layer
model = tf.keras.Sequential()

#input layer
model.add(tf.keras.Input(shape=(128, 128, 3)))

#output layer
model.add(tf.keras.layers.Dense(4,activation="softmax"))

#  complete the model architecture with two convolutional layers, interspersed with max pooling layers, followed by two dense layers

model = tf.keras.Sequential()
model.add(tf.keras.Input(shape=(128, 128, 3)))
model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu")) 
model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(2, 2), strides=(2,2)))
model.add(tf.keras.layers.Conv2D(8, 3, strides=2, activation="relu")) 
model.add(tf.keras.layers.MaxPooling2D(
    pool_size=(2,2), strides=(2,2)))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(16, activation="relu"))
model.add(tf.keras.layers.Dense(4, activation="softmax"))

# compile the model with an optimizer, loss, and metrics
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.CategoricalCrossentropy(),
    metrics=[tf.keras.metrics.CategoricalAccuracy(),tf.keras.metrics.AUC()])

# check the number of parameters
model.summary()

# train the model
model.fit(
        training_iterator,
        steps_per_epoch=len(x_train)/5,
        epochs=8,
        validation_data=validation_iterator,
        validation_steps=len(x_valid)/5)

# visualize the results
from visualize import visualize_activations
visualize_activations(model,training_iterator)
visualize_activations(model,validation_iterator)