import random

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

# See a grid of the images
plt.figure(figsize=(10, 10))

for i in range(25):
    plt.subplot(5, 5, i + 1)

    plt.xticks([])
    plt.yticks([])
    plt.grid(False)

    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(train_labels[i])

plt.show()

# Resize and preprocess the data
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

input_shape = (28, 28, 1)

# Convert into float for Keras API
train_images = train_images.astype("float32")
test_images = test_images.astype("float32")

# Normalize the data
train_images, test_images = train_images / 255.0, test_images / 255.0

# Validation set
validation_samples = 10000

# Create validation sets and use rest for the training
x_val = train_images[-validation_samples:]
y_val = train_labels[-validation_samples:]

train_images = train_images[:-validation_samples]
train_labels = train_labels[:-validation_samples]

# Create the model!
model = keras.models.Sequential([
    keras.layers.Conv2D(
    	32, kernel_size=(3, 3), input_shape=input_shape, activation="relu"
	),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Dropout(0.2),

    keras.layers.Conv2D(64, (3, 3), activation="relu"),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Dropout(0.2),

    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation="softmax"),
])

# Compile the model
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# Initializing a callback, So the model doesn't train further, If there is no proper improvement in it. Within 3 epochs.
callback = keras.callbacks.EarlyStopping(monitor="loss", patience=3)

# We'll start the training process now, with 20 epochs.
model.fit(
    train_images,
    train_labels,
    epochs=20,
    callbacks=[callback],
    validation_data=(x_val, y_val),
)

# Time to evaluate the model's predictions.
model.evaluate(test_images, test_labels)

# Great, we got 98% + Of accuracy! Let's test on a random digit.
image_index = random.randint(0, 10000)

plt.imshow(test_images[image_index].reshape(28, 28), cmap="gray")
predict = test_images[image_index].reshape(28, 28)

pred = model.predict(test_images[image_index].reshape(1, 28, 28, 1))

print("Prediction", pred.argmax())

# Let's now save the model!
model.save("mnist_classifier.h5")
