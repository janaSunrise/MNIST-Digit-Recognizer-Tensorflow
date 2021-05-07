# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

# Get the reference to the dataset
mnist = keras.datasets.mnist

# Separate into Train and test sets
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Check the shapes
print("Train images", train_images.shape)
print("Test images", test_images.shape)

# Resize and preprocess the data
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

input_shape = (28, 28, 1)

# Convert into float for Keras API
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')

# Normalize the data
train_images, test_images = train_images / 255.0, test_images / 255.0

# Create the model!
model = keras.models.Sequential([
  keras.layers.Conv2D(28, kernel_size=(3,3), input_shape=input_shape),
  keras.layers.MaxPooling2D(pool_size=(2, 2)),
  keras.layers.Flatten(),
  keras.layers.Dense(128, activation="relu"),
  keras.layers.Dropout(0.2),
  keras.layers.Dense(10, activation="softmax")
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Initializing a callback, So the model doesn't train further, If there is no proper improvement in it. Within 4 epochs.
callback = keras.callbacks.EarlyStopping(monitor='loss', patience=3)

# We'll start the training process now, with 20 epochs.
model.fit(train_images, train_labels, epochs=20, callbacks=[callback])

# Time to evaluate the model's predictions.
model.evaluate(test_images, test_labels)

# Testing
image_index = 2853

plt.imshow(test_images[image_index].reshape(28, 28),cmap="gray")
predict = test_images[image_index].reshape(28,28)

pred = model.predict(test_images[image_index].reshape(1, 28, 28, 1))

print("Prediction", pred.argmax())

# Let's now save the model!
model.save("mnist_classifier.h5")

