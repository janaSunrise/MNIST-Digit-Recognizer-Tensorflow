import tensorflow as tf

model = tf.keras.models.load_model("models/model.h5")


def predict(grid):
    normalized_digit = grid.reshape((1, 28, 28, 1))
    normalized_digit = normalized_digit.astype('float32') / 255.0
    prediction_array = model.predict([normalized_digit])

    return prediction_array.argmax(), prediction_array
